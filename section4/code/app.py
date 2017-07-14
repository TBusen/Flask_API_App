from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity # our functions we wrote

# resources are things our api can return, create, etc...

app = Flask(__name__)
app.secret_key = 'travis'
api = Api(app) # allows us to add resources to app/api

jwt = JWT(app, authenticate, identity) #json web token for authentication
# jwt object uses app with other functions together to allow users

# how it works #

#JWT creates a new endpoint /auth, when we call this we send it a username and password
# JWT takes the username and password and passes it to the authenticate function
# find the correct user object.  compare its password to what we received.  if correct we return the user.

# this becomes the identity

# the /auth endpoint returns the jwt token.  it doesn't do anything on it's own but we can send it to the next request

# when the next call happens it sends it to the identity function to get the userid and then gets the correct user_id

# if this works then the user is authenticated



# the api works with resources and every resource has to be a class

items = []

class Item(Resource):
    parser = reqparse.RequestParser() # this puts restrictions / criteria on what we are updating
    parser.add_argument('price', # this checks the payload for what we want parsed and updated
                        type=float,
                        required=True,
                        help="This field cannot be left blank!")

    # student class inherets from the Resource class
    # essentially Student is a copy of Resource but we can change things
    @jwt_required() # we have to authentiate before the get request
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items),None) # cleaned up for loop returns first returned value
        return {'item':item}, 200 if item else 400

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items),None): # if name matches and it's not None
            # we don't want to create a value since it has to be unique return 400 for bad request
            return {'message': "An item with name '{}' already exists".format(name)}, 400

        request_data = Item.parser.parse_args()
        item = {'name':name, 'price': request_data['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    def put(self, name):
        #data = request.get_json() # no longer use with payload
        data = Item.parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

class Itemlist(Resource):
    def get(self):
        return {'items':items}, 201

#the class Student is now going to be accessible via the api
api.add_resource(Item, '/item/<string:name>')  # http://localhost:5000/student/Rolf
api.add_resource(Itemlist, '/items')

app.run(port=5000, debug=True)
