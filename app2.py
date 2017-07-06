from flask import Flask

app = Flask(__name__)
stores = [ # need to store stores in list of dicts
    {'name': 'My wonderful store',
           'items': [
               {
               'name': 'My Item',
               'price': 15.99
           }
               ]
     }

          ]
# From servers perspective

# POST  - used to receive data
# GET - used to send data back only

# Endpoints
# POST /store data:  {name:}


# by default @app.route is for GET requests, need to specify POST
@app.route('/store', methods=['POST'])
def create_store():
    pass
# GET /store/<string:name>


# <string:name> is special flask syntax http://localhost:5000/store/some_name
@app.route('/store/<string:name>')
def get_store(name):  # method parameter must match value of string key
    pass
# GET /store


@app.route('/store')
def get_stores():
    pass
# POST /store/<string:name>/item {name:, price:}


# http://localhost:5000/store/some_name
@app.route('/store/<string:name>', methods=['POST'])
def create_item_in_store(name):
    pass
# GET /store/<string:name>/item


@app.route('/store/<string:name/item')
def get_item_in_store(name):
    pass
