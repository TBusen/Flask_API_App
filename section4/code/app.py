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
        item = next(list(filter(lambda x: x['name'] == name, items)),None) # cleaned up for loop returns first returned value
        return {'item':item}, 200 if item else 400

    def post(self, name):
        if next(list(filter(lambda x: x['name'] == name, items)),None): # if name matches and it's not None
            # we don't want to create a value since it has to be unique return 400 for bad request
            return {'message': "An item with name '{}' already exists".format(name)}, 400

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
