from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
stores = [ # need to store stores in list of dicts
    {'name': 'My Wonderful Store',
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
#template for js testing

@app.route('/')
def home():
    return render_template('index.html')

# POST /store data:  {name:}
# by default @app.route is for GET requests, need to specify POST
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json() # this is the request that is made to the endpoint '/store'
    # browser will send store name
    new_store = {
        'name':request_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)
# GET /store/<string:name>
# <string:name> is special flask syntax http://localhost:5000/store/some_name
@app.route('/store/<string:name>')
def get_store(name):  # method parameter must match value of string key
    # Iterate voer stores
    # if the store name matches, return it
    # if none match, return an error message
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
        else:
            return jsonify({'error':'no store found'})

# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores}) #converts the stores dictionary to JSON
    #stores is a list not a dicitonary so we make it a value for the key 'stores'

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST']) # http://localhost:5000/store/some_name
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price':request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items':store['items']})
    return jsonify({'error': 'store not found'})

app.run(port=5000)
