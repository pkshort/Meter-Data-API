import sqlite3
from flask import Flask, request, render_template
from sqlalchemy import create_engine
from flask_restful import Resource, Api
import json

e = create_engine('sqlite:///metrics.db')
app = Flask(__name__)
api = Api(app)

app.config["DEBUG"] = True

@app.route('/meters')
def get():
    #connecting to database
    conn = e.connect()
    #query and return json data
    query = conn.execute("select * from meter")

    html_data = []

    for row in query:
        html_data.append([row['id'], row['label']])

    return render_template("meters.html", query=html_data)

@app.route('/meters/<int:meter_id>')
def get_data(meter_id):
    #connecting to database
    conn = e.connect()

    tempDict = {}
    #query and return json data
    query = conn.execute("SELECT * FROM meter_data WHERE meter_id={} ORDER BY timestamp DESC".format(meter_id))
    output = query.cursor.fetchall()
    for row in output:
        tempDict.update({row[0]: {"meter_id":row[1],"timestamp":row[2],"value":row[3]}})
    return json.dumps(tempDict)


if __name__ == '__main__':
    app.run()
