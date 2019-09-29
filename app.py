from flask import Flask, request, jsonify
from flask_restful import reqparse, Api, Resource
from flask_cors import CORS
from backend import surpriseGenerator
import json

app = Flask(__name__)
api = Api(app)
cors = CORS(app)

parser = reqparse.RequestParser()


class SBBSurprise(Resource):
    def get(self):
        return 'SBBSurprise APP HackZurich2019'

    def post(self):
        """
        {
            startLocation: "Current Location", //bahnhofsname
            departureDate: new Date(), //json datum "2014-01-01T23:28:56.782Z"
            departureTime: "early", //early oder late  -> vorschlag early= abfahrt ab 6 , late ab 9
            returnTime: "late", //early oder late -> vorschlag early= rückfahrt ab 4pm und 6pm, late ab 8pm
            budget: "no", // low, mid, hi, no, low < 20, mid < 50, hi < 9999, no = hi
            personCountFull: 1, // 0-9
            personCountHalf: 0 // 0-9
            preferences: [pref1, pref2] //list of f
        }

        example for postman:
{
"startLocation": "Zurich HB",
"departureDate": "2014-01-01T23:28:56.782Z",
"departureTime": "early",
"returnTime": "late",
"budget": "mid",
"personCountFull": 1,
"personCountHalf": 0,
"preferences": ["SBB_lh_games_fun", "SBB_lh_adventure_panorama_trips", "SBB_lh_zoo_animal_parks"]
}
        """
        body = request.get_json()

        surprise = surpriseGenerator.Suprise(
            body['startLocation'],
            body['departureDate'],
            body['departureTime'],
            body['returnTime'],
            body['budget'],
            body['personCountFull'],
            body['personCountHalf'],
            body['preferences'])
        offers = surprise.get_offers()
        return [{
            "start_name": o.start_name,
            "dest_name": o.dest_name,
            "price_saver": o.price_saver,
            "price_normal": o.price_normal,
            "start_time_go": o.start_time_go,
            "start_time_return": o.start_time_return,
            "duration_go": o.duration_go,
            "duration_return": o.duration_return,
            "score": o.score,
            "activities": o.activities
        } for o in offers], 201
        # return jsonify(offers), 201
        # return json.dumps([offer.__dict__ for offer in offers]), 201


api.add_resource(SBBSurprise, '/')

