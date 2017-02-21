from flask import Flask

app = Flask(__name__)
from app import views

#The above script creates the appliation object (of class Flask)
#and then imports the views module.  Do not confuse app the variable
#which gets assigned the Flask instance with app the package from which
#we import the views module
