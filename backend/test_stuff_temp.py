import requests
import uuid
import pandas as pd


class TestSurprise:
    token = ''
    conversation_id = ''

    def __init__(self):
        self.token = self.get_token()
        self.conversation_id = str(uuid.uuid4())

    def call_SBB_api(self, start_location, suitable_destinations):
        """
        Call SBB Api to get offer for activity-based filtered cities within time & duration boundaries
        """

        # get id & name of start location
        self.query_location(start_location, self.token, self.conversation_id)

        for dest in suitable_destinations:
            # get id & name of destination
            self.query_location(dest, self.token, self.conversation_id)

        return []

    @staticmethod
    def get_token():
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

    @staticmethod
    def query_location(location, token, conversation_id):
        url = "https://b2p-int.api.sbb.ch/api/locations"

        querystring = {"name": location}
        headers = {
            'Authorization': "Bearer {}".format(token),
            'Cache-Control': "no-cache",
            'Accept': "application/json",
            'Accept-Language': "en",
            'X-Contract-Id': "HAC222P",
            'X-Conversation-Id': conversation_id,
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

    def dump_locations(self):
        csv_path = 'eventscrape/events.csv'
        df_locations = pd.read_csv(csv_path)
        df_locations['dest_id'], df_locations['dest_name'] = zip(*df_locations.apply(self.test_apply, axis=1))

        df_locations.to_csv('eventscrape/events_enriched.csv', index=False)

        print('finished')

    enrich_id = 1

    def test_apply(self, row):
        activity_loc = row.loc['loc_name']
        # get id & name of destination
        location_id, location_name = self.query_location(activity_loc, self.token, self.conversation_id)
        print('{}/596'.format(self.enrich_id))
        self.enrich_id += 1
        return location_id, location_name


# __get_token()
# __call_SBB_api('Luzern', ['Bern'])
ts = TestSurprise()
ts.dump_locations()
