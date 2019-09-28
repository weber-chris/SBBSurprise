import requests
import uuid


def __call_SBB_api(start_location, suitable_destinations):
    """
    Call SBB Api to get offer for activity-based filtered cities within time & duration boundaries
    """

    token = __get_token()
    conversation_id = str(uuid.uuid4())

    # get id & name of start location
    __query_location(start_location, token, conversation_id)

    for dest in suitable_destinations:
        # get id & name of destination
        __query_location(dest, token, conversation_id)

    return []


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


def __query_location(location, token, conversation_id):
    url = "https://b2p-int.api.sbb.ch/api/locations"

    querystring = {"name": location}
    headers = {
        'Authorization': "Bearer {}".format(token),
        'Cache-Control': "no-cache",
        'Accept': "application/json",
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

    print (location_id)
    return location_id, location_name

# __get_token()
__call_SBB_api('Luzern', ['Bern'])
