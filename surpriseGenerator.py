class Suprise:
    def __init__(self):
        pass

    def get_suitable_offers(self, date, budget, max_duration, location, preferences, turned_down_offers):
        """
        Get requested surprise constraints, return list of possible destinations with respective possible activities,
        ordered by suitability  score
        possible acitivi
        :param date: date when surprise should take place
        :param budget: low/mid/high/None
        :param max_duration: how long can the trip be (i.e. max_radius) in minutes
        :param location: starting city
        :param preferences: dictionary for activity types with score
        :param turned_down_offers: list of destinations to exclude (because of reroll)
        :return:
            {city_1 :
                {score:int,
                trip_data:
                    {price:double,
                    start_time:DateTime,
                    hints:[..]}
                activities:
                    {activity_1:score, activity_2:score, ...}
                },
            city_2: ...}
        """
        suitable_cities = self.__get_suitable_cities(preferences, turned_down_offers)


    def __get_activities(self):
        """
        Get all possible activities per city
        :return: [city_1: [{activity_1: [labels_1, label_2..],{activity_2:..},
                  city_2: ..]
        """
        return []

    def __get_suitable_cities(self, preferences, turned_down_offers):
        """
        Get all cities that match offers, rated with a suitability score
        :param preferences: dictionary for activity types with score
        :param turned_down_offers: list of destinations to exclude (because of reroll)
        :return: [city_1: {score:double, [{activity_1: [labels_1, label_2..],{activity_2:..}},
                  city_2: ..]
        """
        return []

    def __suitable_offers_from_api(self, suitable_cities):
        """
        Get offer for suitable cities within time & duration boundaries
        :param suitable_cities:
        :return:
        """
        pass