import pandas as pd
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
        Get all cities that match offers
        """
        print(destinations.to_string())
        # TODO filter activities based on preferences
        suitable_destinations = self.__get_suitable_destinations(destinations)
        # TODO call SBB API for all destinations
        offers = self.__call_SBB_api(suitable_destinations)
        # TODO filter offers based on duration and cost
        suitable_offers = self.__filter_offers(offers)
        return []

    def __get_suitable_destinations(self, destinations):
        """
        Get all destinations that match preferences
        """

        # TODO merge activities & cities
        # should we already kick out some destinations here?
        return []

    def __call_SBB_api(self, suitable_destinations):
        """
        Call SBB Api to get offer for activity-based filtered cities within time & duration boundaries
        """
        # TODO call api for each destination
        return []

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
        
        #check that score adds up to 1.0!
        price_relevance = 1.0

        if self.budget == 'no':
            self.budget == 'hi'

        #filter for non-existent prices
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
