import pandas as pd
import requests
import uuid
import operator
from datetime import datetime


class Suprise:
    all_categories = ['SBB_lh_games_fun', 'SBB_lh_adventure_panorama_trips', 'SBB_lh_nature_sights_of_interest',
                      'SBB_lh_zoo_animal_parks', 'SBB_lh_bike_ebike', 'SBB_lh_wellness_relaxation', 'SBB_lh_hiking',
                      'SBB_lh_art_culture_museums', 'SBB_lh_concerts_musicals_festivals', 'SBB_lh_markets_shopping',
                      'SBB_lh_short_trips_in_switzerland', 'SBB_lh_city_trips']

    def __init__(self, startLocation, departureDate, departureTime, returnTime, budget, personCountFull,
                 personCountHalf, preferences):
        """
        :param date: date when surprise should take place
        :param budget: low/mid/high/None
        :param max_duration: how long can the trip be (i.e. max_radius) in minutes
        :param start_location: starting city
        :param preferences: dictionary for activity types with score
        :param people: how many people will participate
        """
        if startLocation == 'Current Location':
            self.startLocation = 'Zurich HB'
        else:
            self.startLocation = startLocation

        if departureTime == 'early':
            self.departure_timestamp = '06:00'
        else:
            self.departure_timestamp = '09:00'
        if returnTime == 'early':
            self.return_timestamp = '16:00'
        else:
            self.return_timestamp = '20:00'
        self.trip_date = departureDate[:10]
        # self.departure_datetime = datetime.strptime('{}{}'.format(departureDate[:10], dep_timestamp), '%Y-%m-%d%H:%M')
        # self.departureDate = departureDate
        # self.departureTime = departureTime
        # self.returnTime = returnTime
        # self.return_datetime = datetime.strptime('{}{}'.format(departureDate[:10], ret_timestamp), '%Y-%m-%d%H:%M')

        self.budget = budget
        self.personCountFull = personCountFull
        self.personCountHalf = personCountHalf
        self.preferences = preferences
        if self.budget == 'low':
            self.budget_CHF = 20
        elif self.budget == 'mid':
            self.budget_CHF = 40
        else:
            self.budget_CHF = 9999

        self.token = self.__get_token()
        self.conversation_id = str(uuid.uuid4())
        self.max_duration = 180  # minutes
        self.min_duration = 30  # minutes

        self.destinations = []

    @staticmethod
    def __get_token():
        url = "https://sso-int.sbb.ch/auth/realms/SBB_Public/protocol/openid-connect/token"
        client_id = '22ebc2be'
        client_secret = '2c820784f3e28837959abc43120989ca'
        payload = "grant_type=client_credentials&client_id={}&client_secret={}".format(client_id, client_secret)
        headers = {
            'User-Agent': "PostmanRuntime/7.17.1",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Host': "sso-int.sbb.ch",
            'Content-Type': "application/x-www-form-urlencoded",
        }

        response = requests.request("POST", url, data=payload, headers=headers)
        json_response = response.json()
        return json_response['access_token']

    def get_offers(self):
        """
        Gets list of possible destinations with respective possible activities and suitability score
        """
        self.__get_all_destinations()
        suitable_offers = self.__get_suitable_offers()
        scored_offers = self.__score_suitable_offers(suitable_offers)
        return scored_offers

    def __get_all_destinations(self):
        """
        Get all destinations with their hints and activities
        """
        csv_path = 'backend/eventscrape/events_enriched_cleaned.csv'
        df_locations = pd.read_csv(csv_path)
        self.destinations = df_locations[['dest_id', 'dest_name', 'category', 'title']]

    def __get_suitable_offers(self):
        """
        Get all cities that have offers
        """
        suitable_destinations = self.destinations[self.destinations['category'].isin(self.preferences)]

        offers = self.__call_SBB_api(suitable_destinations)
        return offers

    def __call_SBB_api(self, suitable_destinations):
        """
        Call SBB Api to get offer for activity-based filtered cities within time & duration boundaries
        """
        # get id & name of start location
        start_id, start_name = self.__query_location(self.startLocation)
        saver_trips = []
        for id, dest in suitable_destinations.iterrows():
            if len(saver_trips) > 1:
                break
            if start_id != dest['dest_id']:
                query_trip_result = self.__query_trip(start_id, dest['dest_id'])
                if query_trip_result:
                    trip_id, start_time, duration = query_trip_result[0], query_trip_result[1], query_trip_result[2]
                    super_destination = self.__query_price(trip_id)
                    if super_destination:
                        dest = Destination(dest['dest_id'], super_destination[0], super_destination[1], start_time,
                                           duration, self.startLocation)
                        saver_trips.append(dest)
                        print('Dest_Id: {}, Price: {}, Normal: {}, Start: {}'.format(dest.dest_id, dest.price_saver,
                                                                                     dest.price_normal,
                                                                                     dest.start_time))

        print(saver_trips)
        return saver_trips

    def __query_location(self, location):
        url = "https://b2p-int.api.sbb.ch/api/locations"

        querystring = {"name": location}
        headers = {
            'Authorization': "Bearer {}".format(self.token),
            'Cache-Control': "no-cache",
            'Accept': "application/json",
            'Accept-Language': "en",
            'X-Contract-Id': "HAC222P",
            'X-Conversation-Id': self.conversation_id,
            'Host': "b2p-int.api.sbb.ch",
            'Accept-Encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        json_response = response.json()
        location_name = json_response[0]['name']
        location_id = json_response[0]['id']

        return location_id, location_name

    def __query_trip(self, from_id, to_id):
        url = "https://b2p-int.api.sbb.ch/api/trips"

        querystring = {"arrivalDeparture": "ED", "date": self.trip_date, "destinationId": to_id,
                       "originId": from_id, "time": self.departure_timestamp}

        headers = {
            'Authorization': "Bearer {}".format(self.token),
            'Cache-Control': "no-cache",
            'Accept': "application/json",
            'X-Contract-Id': "HAC222P",
            'X-Conversation-Id': self.conversation_id,
            'Host': "b2p-int.api.sbb.ch",
            'Accept-Encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        json_response = response.json()
        if len(json_response) > 0:
            trip_id = json_response[0]['tripId']
            start_time = json_response[0]['segments'][0]['stops'][0]['departureDateTime']
            end_time = json_response[0]['segments'][-1]['stops'][-1]['arrivalDateTime']
            start_datetime = datetime.strptime(start_time[:19], '%Y-%m-%dT%H:%M:%S')
            end_datetime = datetime.strptime(end_time[:19], '%Y-%m-%dT%H:%M:%S')
            duration = (end_datetime - start_datetime).seconds
            if self.max_duration * 60 > duration > self.min_duration * 60:
                return trip_id, start_time, duration

    def __query_price(self, trip_id):
        url = "https://b2p-int.api.sbb.ch/api/trip-offers"

        querystring = {"passengers": "paxa;42;half-fare",
                       "tripId": trip_id}

        headers = {
            'Authorization': "Bearer {}".format(self.token),
            'Cache-Control': "no-cache",
            'Accept': "application/json",
            'Accept-Language': "en",
            'X-Contract-Id': "HAC222P",
            'X-Conversation-Id': self.conversation_id,
            'Host': "b2p-int.api.sbb.ch",
            'Accept-Encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        json_response = response.json()
        # find if one with productID 4004 (super saver)
        super_saver = next((item for item in json_response if item['offers'][0]['productId'] == 4004), None)

        # find one with productID 125 (point-to-point)
        point_to_point = next((item for item in json_response if item['offers'][0]['productId'] == 125), None)
        if super_saver and point_to_point:
            if super_saver['totalPrice'] <= self.budget_CHF * 100:
                return super_saver['totalPrice'], point_to_point['totalPrice']
        # print('price: {}, super-saver: {}'.format(price,super_saver))

    def __score_suitable_offers(self, suitable_offers):
        """
        Give a suitability score, weighted based on activity-preferences and price
        """
        # filter for non-existent prices
        suitable_offers = [x for x in suitable_offers if not x.price_saver == -1]

        for destination in suitable_offers:
            full_dest = self.destinations[self.destinations['dest_id'] == destination.dest_id]
            destination.dest_name = full_dest['dest_name'].iloc[0]
            destination.activities = [{x[0]: x[1]} for x in full_dest[['title', 'category']].values]
            # destination.activities = full_dest[['title', 'category']].to_string()
            # change score based on price
            if self.budget == 'low':
                destination.score += destination.price_saver * .1
            elif self.budget == 'mid':
                destination.score += destination.price_saver * 0.075
            else:
                destination.score += destination.price_saver * .05

        return sorted(suitable_offers, key=operator.attrgetter('score'))


class Destination:
    dest_id = None
    price_saver = -1
    price_normal = -1
    duration = -1
    start_time = None

    score = 0
    activities = None
    dest_name = None
    start_name = None

    def __init__(self, dest_id, price_saver, price_normal, start_time, duration, start_name):
        self.dest_id = dest_id
        self.price_saver = price_saver
        self.price_normal = price_normal
        self.start_time = start_time
        self.duration = duration
        self.start_name = start_name
