import sqlite3
from flask import Flask, request
from sqlalchemy import create_engine
from flask_restful import Resource, Api
from json import dumps

e = create_engine('sqlite:///metrics.db')
app = Flask(__name__)
api = Api(app)
#app.config["DEBUG"] = True


class Meters(Resource):
    def get(self):
        #connecting to database
        conn = e.connect()
        #query and return json data
        query = conn.execute("select * from meter")
        return {'Meters:': [i[0] for i in query.cursor.fetchall()]}

class MeterData(Resource):
    def get(self):
        #connecting to database
        conn = e.connect()
        
api.add_resource(Meters, '/meters')

if __name__ == '__main__':
    app.run()
