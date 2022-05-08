from flask import Flask
from flask_restful import Resource,Api
from flask_jwt import JWT,jwt_required
from security import authenticate,identity
from resources.registeruser import User_Register
from resources.thing import Item,ItemList
import pyodbc


app=Flask(__name__)
api=Api(app)
app.secret_key='Potat'
app.env='developement'

jwt=JWT(app,authenticate,identity)

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(User_Register,'/register')


app.run(port=5010)
