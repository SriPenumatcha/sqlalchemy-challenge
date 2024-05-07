# Import the dependencies.
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

#################################################
# Database Setup
#################################################

# Create engine using the `hawaii.sqlite` database file
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# Declare a Base using `automap_base()`
Base = automap_base()
# Use the Base class to reflect the database tables
Base.prepare(engine, reflect=True)

# Assign the measurement class to a variable called `Measurement` and
Measurement = Base.classes.measurement

# the station class to a variable called `Station`
Station = Base.classes.station

# Create a session
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)


#################################################
# Flask Routes
#################################################


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start_date<br/>"
        f"/api/v1.0/start_date/end_date"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the JSON representation of your dictionary."""
    session = Session(engine)
    # Query precipitation data for the last year
    most_recent_date = session.query(func.max(Measurement.date)).scalar()
    most_recent_date = datetime.strptime(most_recent_date, '%Y-%m-%d')
    one_year_ago = most_recent_date - timedelta(days=365)

    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= one_year_ago).all()
    # Close session
    session.close()
    # Convert the query results to a dictionary
    precipitation_data = {date: prcp for date, prcp in results}

    return jsonify(precipitation_data)


@app.route("/api/v1.0/stations")
def stations():
    """Return a JSON list of stations from the dataset."""
    session = Session(engine)

    # Query stations
    results = session.query(Station.station).all()

    # Close session
    session.close()

    # Convert list of tuples into normal list
    stations_list = [station for station, in results]

    return jsonify(stations_list)


@app.route("/api/v1.0/tobs")
def tobs():
    """Return a JSON list of Temperature Observations (tobs) for the previous year.""" 
    
    session = Session(engine)
 
    # Calculate the date one year ago from today
    most_recent_date = session.query(func.max(Measurement.date)).scalar()
    most_recent_date = datetime.strptime(most_recent_date, '%Y-%m-%d')
    one_year_ago = most_recent_date - timedelta(days=365)

  

    # Query the most active station
    most_active_station = session.query(Measurement.station).\
        group_by(Measurement.station).\
        order_by(func.count().desc()).first()

    if most_active_station:
        most_active_station_id = most_active_station[0]

        # Query temperature observations for the most active station for the last year
        results = session.query(Measurement.date, Measurement.tobs).\
            filter(Measurement.station == most_active_station_id).\
            filter(Measurement.date >= one_year_ago).all()

        # Close session
        session.close()

        # Convert the query results to a list of dictionaries
        tobs_data = [{"Date": date, "Temperature": tobs} for date, tobs in results]

        return jsonify(tobs_data)
    else:
        return jsonify({"error": "No data available for the most active station in the last year."})


@app.route("/api/v1.0/<start>")
def temp_start(start):
    """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start date."""
    session = Session(engine)

    # Query temperature data for given start date
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all()
    # Close session
    session.close()

    # Convert the query results to a dictionary
    temp_data = {
        "Minimum Temperature": results[0][0],
        "Average Temperature": results[0][1],
        "Maximum Temperature": results[0][2]
    }

    return jsonify(temp_data)


@app.route("/api/v1.0/<start>/<end>")
def temp_start_end(start, end):
    """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start-end range."""
    session = Session(engine)

    # Query temperature data for given start and end date range
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    # Close session
    session.close()

    # Convert the query results to a dictionary
    temp_data = {
        "Minimum Temperature": results[0][0],
        "Average Temperature": results[0][1],
        "Maximum Temperature": results[0][2]
    }

    return jsonify(temp_data)


if __name__ == '__main__':
    app.run(debug=True)
