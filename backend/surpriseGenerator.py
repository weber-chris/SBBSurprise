import pandas as pd
import requests
import uuid
import operator


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
        self.startLocation = startLocation
        self.departureDate = departureDate
        self.departureTime = departureTime
        self.returnTime = returnTime
        self.budget = budget
        self.personCountFull = personCountFull
        self.personCountHalf = personCountHalf
        self.preferences = preferences

        self.token = self.__get_token()
        self.conversation_id = str(uuid.uuid4())

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
        destinations = self.__get_all_destinations()
        suitable_offers = self.__get_suitable_offers(destinations)
        scored_offers = self.__score_suitable_offers(suitable_offers)
        return scored_offers

    def __get_all_destinations(self):
        """
        Get all destinations with their hints and activities
        """
        csv_path = 'backend/eventscrape/events_enriched_cleaned.csv'
        df_locations = pd.read_csv(csv_path)
        # TODO read from DB/CSV
        return df_locations[['dest_id', 'dest_name', 'category', 'title']]

    def __get_suitable_offers(self, destinations):
        """
        Get all cities that have offers
        """
        suitable_destinations = destinations[destinations['category'].isin(self.preferences)]

        offers = self.__call_SBB_api(suitable_destinations)
        # TODO filter offers based on duration and cost
        suitable_offers = self.__filter_offers(offers)
        return []

    # def __get_suitable_destinations(self, destinations):
    #     """
    #     Get all destinations that match preferences
    #     """
    #     suitable_destinations = destinations[destinations['category'].isin(self.preferences)]
    #     # TODO merge activities & cities
    #     # should we already kick out some destinations here?
    #     return []

    def __call_SBB_api(self, suitable_destinations):
        """
        Call SBB Api to get offer for activity-based filtered cities within time & duration boundaries
        """
        # get id & name of start location
        start_id, start_name = self.__query_location(self.startLocation)
        saver_trips = []
        for id, dest in suitable_destinations.iterrows():
            if len(saver_trips) > 5:
                break
            if start_id != dest['dest_id']:
                query_trip_result = self.__query_trip(start_id, dest['dest_id'])
                if query_trip_result:
                    trip_id, start_time = query_trip_result[0], query_trip_result[1]
                    super_destination = self.__query_price(trip_id)
                    if super_destination:
                        dest = Destination(dest['dest_id'], super_destination[0], super_destination[1], start_time)
                        saver_trips.append(dest)

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

        querystring = {"arrivalDeparture": "ED", "date": "2019-11-27", "destinationId": to_id,
                       "originId": from_id, "time": "10:22"}

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
            return trip_id, start_time

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
            return super_saver['totalPrice'], point_to_point['totalPrice']
        # print('price: {}, super-saver: {}'.format(price,super_saver))

    def __filter_offers(self, offers):
        """
        Drop all offers that are against price/duration constraint
        """
        # TODO drop unsuitable offers
        return []

    def __score_suitable_offers(self, suitable_offers):
        """
        Give a suitability score, weighted based on activity-preferences and price
        """
        # TODO calculate weighted score that predicts, how much a user "likes" the destination

        # check that score adds up to 1.0!
        price_relevance = 1.0

        if self.budget == 'no':
            self.budget == 'hi'

        # filter for non-existent prices
        suitable_offers = [x for x in suitable_offers if not x.price == -1]

        for destination in suitable_offers:
            if self.budget == 'low':
                if destination.price < 20:
                    destination.score += 100 * price_relevance
                elif destination.price < 50:
                    destination.score += 50 * price_relevance
            elif self.budget == 'mid':
                if destination.price < 20:
                    destination.score += 50 * price_relevance
                elif destination.price < 50:
                    destination.score += 100 * price_relevance
            elif self.budget == 'hi':
                if destination.price < 20:
                    destination.score += 10 * price_relevance
                elif destination.price < 50:
                    destination.score += 50 * price_relevance
                else:
                    destination.score += 100 * price_relevance

        return sorted(suitable_offers, key=operator.attrgetter('score'))


class Destination:
    dest_id = None
    price_saver = -1
    price_normal = -1
    start_time = None

    score = -1
    activities = None

    def __init__(self, dest_id, price_saver, price_normal, start_time):
        self.dest_id = dest_id
        self.price_saver = price_saver
        self.price_normal = price_normal
        self.start_time = start_time
