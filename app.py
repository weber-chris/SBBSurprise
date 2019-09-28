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
            departureTime: "early", //early oder late  -> vorschlag early= abfahrt zwischen 6 und 8, late zwischen 8 und 10
            returnTime: "late", //early oder late -> vorschlag early= ruckkinft zwischen 4pm und 6pm, late zwischen 8pm und 10pm
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
            "start_time": o.start_time,
            "duration": o.duration,
            "score": o.score,
            "activities": o.activities
        } for o in offers], 201
        # return jsonify(offers), 201
        # return json.dumps([offer.__dict__ for offer in offers]), 201


api.add_resource(SBBSurprise, '/')

# TODOS = {
#     'todo1': {'task': 'build an API'},
#     'todo2': {'task': '?????'},
#     'todo3': {'task': 'profit!'},
# }
#
#
# def abort_if_todo_doesnt_exist(todo_id):
#     if todo_id not in TODOS:
#         abort(404, message="Todo {} doesn't exist".format(todo_id))
#
#
# parser = reqparse.RequestParser()
# parser.add_argument('task')
#
# db_name = '../sqlite/db1.db'
# table_name = 'todos1'
#
#
# # Todo
# # shows a single todo item and lets you delete a todo item
# class Todo(Resource):
#     def get(self, todo_id):
#         with sqlite3.connect(db_name) as con:
#             cur = con.cursor()
#             cur.execute("select task from {} where id = 'todo{}';".format(table_name, todo_id))
#             con.commit()
#             res = cur.fetchone()
#             if res is None:
#                 abort(404, message="Todo {} doesn't exist".format(todo_id))
#             return res
#
#     def delete(self, todo_id):
#         with sqlite3.connect(db_name) as con:
#             cur = con.cursor()
#             cur.execute("DELETE from {} where id = 'todo{}';".format(table_name, todo_id))
#             con.commit()
#         return '', 204
#
# # TodoList
# # shows a list of all todos, and lets you POST to add new tasks
# class TodoList(Resource):
#     def get(self):
#         with sqlite3.connect(db_name) as con:
#             cur = con.cursor()
#             cur.execute("select * from {};".format(table_name))
#             con.commit()
#             data = cur.fetchall()
#         return data
#
#     def post(self):
#         args = parser.parse_args()
#         todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
#         todo_id = 'todo%i' % todo_id
#
#         with sqlite3.connect(db_name) as con:
#             cur = con.cursor()
#             cur.execute("insert into {} values('{}','{}');".format(table_name, todo_id, args['task']))
#             con.commit()
#
#         return {'task': args['task']}, 201
#
#
# ##
# ## Actually setup the Api resource routing here
# ##
# api.add_resource(TodoList, '/todos')
# api.add_resource(Todo, '/todos/<todo_id>')
#
# if __name__ == '__main__':
#     app.run(debug=True)
