from flask import Flask, request
from flask_restful import Resource, Api
# resources are things our api can return, create, etc...

app = Flask(__name__)

api = Api(app) # allows us to add resources to app/api

# the api works with resources and every resource has to be a class

items = []

class Item(Resource): # student class inherets from the Resource class
    # essentially Student is a copy of Resource but we can change things
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'item':None}, 404

    def post(self, name):
        request_data = request.get_json()
        item = {'name':name, 'price': request_data['price']}
        items.append(item)
        return item, 201

class Itemlist(Resource):
    def get(self):
        return {'items':items}, 201

#the class Student is now going to be accessible via the api
api.add_resource(Item, '/item/<string:name>')  # http://localhost:5000/student/Rolf
api.add_resource(Itemlist, '/items')

app.run(port=5000, debug=True)
