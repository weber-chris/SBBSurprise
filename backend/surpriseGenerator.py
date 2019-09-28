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

        # TODO call SBB API for all destinations
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
        print(start_id)
        # TODO call api for each destination
        for id, dest in suitable_destinations.iterrows():
            # trip_id = self.__query_trip(start_id, dest['dest_id'])
            # TODO query price for each trip
            trip_id = self.__query_trip(start_id, dest['dest_id'])

            break
        return []

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
        trip_id = json_response[0]['tripId']
        return trip_id

    def __query_price(self):
        pass

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
    name = None
    hints = None
    activities = None
    price = -1
    score = -1
    start_time = None

    def __init__(self, name, hints):
        self.name = name
        self.hints = hints
