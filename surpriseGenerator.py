class Suprise:
    def __init__(self, date, budget,  start_location, preferences, people):
        """
        :param date: date when surprise should take place
        :param budget: low/mid/high/None
        :param max_duration: how long can the trip be (i.e. max_radius) in minutes
        :param start_location: starting city
        :param preferences: dictionary for activity types with score
        :param people: how many people will participate
        """
        self.date = date
        self.budget = budget
        self.max_duration = 180 # max time for one way in train
        self.start_location = start_location
        self.preferences = preferences
        self.people = people

    def get_offers(self):
        """
        Gets list of possible destinations with respective possible activities and suitability score
        """
        activities = self.__get_all_activities()
        destinations = self.__get_all_destinations()
        suitable_offers = self.__get_suitable_offers(activities, destinations)
        scored_offers = self.__score_suitable_offers(suitable_offers)
        return scored_offers

    def __get_all_activities(self):
        """
        Get all activities with their labels and cities
        """
        # TODO read from DB/CSV
        return []

    def __get_all_destinations(self):
        """
        Get all destinations with their hints
        """
        # TODO read from DB/CSV
        return []

    def __get_suitable_offers(self, activities, destinations):
        """
        Get all cities that match offers
        """
        # TODO filter activities based on preferences
        suitable_destinations = self.__get_suitable_destinations(activities, destinations)
        # TODO call SBB API for all destinations
        offers = self.__call_SBB_api(suitable_destinations)
        # TODO filter offers based on duration and cost
        suitable_offers = self.__filter_offers(offers)
        return []

    def __get_suitable_destinations(self, activities, destinations):
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
        return []


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
