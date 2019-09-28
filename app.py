from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS
import sqlite3
import surpriseGenerator

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
          "date": "2019-10-25",
          "budget": "low",
          "start_location": "Winterthur",
          "preferences": {"hiking":5,"culture":3,"concert":8,"sports":4},
          "people":1
        }
        """
        body = request.get_json()
        surprise = surpriseGenerator.Suprise(
            body['date'],
            body['budget'],
            body['start_location'],
            body['preferences'],
            body['people'])
        offers = surprise.get_offers()
        # TODO do something with token
        return offers, 201


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
