from flask import Flask

app = Flask(__name__) #create an object of flask

@app.route('/') # this decorator tells the app the starting point
def home(): # all decorators need a method to follow, can call it whatever you want
    # has to return a response to the browser
    return "Hello, world!"
    # when we access our endpoint in our browser we should see hello world

app.run(port=5000) # tell the app to start and on what port to listen
