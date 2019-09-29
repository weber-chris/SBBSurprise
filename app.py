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
        body = request.get_json()

        surprise = surpriseGenerator.Surprise(
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


api.add_resource(SBBSurprise, '/')

