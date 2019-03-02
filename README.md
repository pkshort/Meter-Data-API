# Meter-Data-API
Meter Data API using Flask and SQLite as the backend.

## Getting Started
Make sure to have Python 3.7 installed and running on your local machine, once the version matches you're going to want to install SQLite 3. Once SQLite is installed the database can be built using the two .csv files in the root directory of the project.

### Creating the database
From the root directory of your local project open a SQLite3 shell and you'll dump the .csv files into a database.

	$ sqlite3 metrics.db
	> .mode csv meter
	> .import meters.csv meter
	> .mode csv meter_data
	> .import meter_data.csv meter_data

### Installing dependencies
In a command prompt use pip to install the dependencies used. (pip or pip3 commands will both work)

	$ pip install flask
	$ pip install flask-restful
	$ pip install sqlalchemy
	
## Running the application
Run the application with:

	$ python3 Meters.py

Now the API is running on localhost port 5000.
Access the meters page at http://localhost:5000/meters/

Each meter will have a clickable link to their .json formatted data associated to each specific meter.

*The dummy data used only has four meter entries, ids 1-4, with three seperate data entries associated with each meter.

## Built With

* [Python](https://www.python.org/downloads/release/python-370/) - Programming language
* [Flask](http://flask.pocoo.org/docs/1.0/) - Micro web framework
* [SQLAlchemy](https://www.sqlalchemy.org/) - Database Toolkit for Python
