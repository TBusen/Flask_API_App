#The views are the handlers that respond to requests from web browsers or other clients.
#In Flask handlers are written as Python functions. Each view function is mapped to one or more request URLs.

from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

# This view returns a string to be displayed on the client's browser

#The two route decorators above the funciton create the mappings from URLS '/'
#and '/index' to this funciton
