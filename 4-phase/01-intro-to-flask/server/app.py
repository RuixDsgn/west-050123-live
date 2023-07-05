#!/usr/bin/env python3

# 📚 Review With Students:
    # Request-Response Cycle
    # Web Servers and WSGI/Werkzeug

""" 
    Request-Response Cycle

    - Client sending a HTTP requests to a server
    - Server Responds in a given way
        - Browser can ONLY DO GET REQUESTS

    MVC Design Principal

    Models
        - Server Side
        - database/columns/models.py
            - In p3, these were are lib/classes/dog.py.. 
            - In flask, all the tables/classes/models get defined in one models.py file
        - For this phase, this is the SQLAlchemy/ORM
        - How the Object is structured
            - Any attributes, functions, methods, etc..
        - Mostly for defining our database and schema

    Views
        - In a full(ish) stack Flask only app, the Flask app can render HTML and the view
        - In our tech stack, the views are rendered by React
        - Views are on the Client Side 

    Controllers
        - Routes that controller the models/views
        - Define routes that interact with our models
        - Can be any of the HTTP action routes
        - ReactRouter
            - Controls our FrontEnd Views
        - Flask
            - Controls our models, and serves up JSON for the client

    
    React/Flask Stack
    Models -> Flask-SQLAlchemy
    Views -> React
    Controllers -> ReactRouter / Flask

    FullStack JS
    Models -> Node.js, SQL, some JS ORM (Sequelize)
    Views ->  React 
    Controllers -> ReactRouter / Express.js

    React/Rails(Ruby)
    Models -> Ruby, ActiveRecord
    Views -> React
    Controllers -> ReactRouter / Rails

    
    ! Web Servers
    - localhost:port, ip 127.0.0.1:port
    - An active Computer/terminal, that responds to remote clients
        - json-server
        - External APIs
        - Apache 
        - React
        - Flask
        - Live Server/LiveShare

 """

# 1. ✅ Navigate to `models.py`

# 2. ✅ Set Up Imports
	# `Flask` from `flask`
	# `Migrate` from `flask_migrate`
	# db and `Production` from `models`
from ipdb import set_trace
from flask import Flask, request
from flask_migrate import Migrate
from models import db, Production

# 3. ✅ Initialize the App
    # Add `app = Flask(__name__)`
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# set_trace()
    
    # Set the migrations with `migrate = Migrate(app, db)`
migrate = Migrate(app, db)
db.init_app(app)
    
    # Finally, initialize the application with `db.init_app(app)`

 # 4. ✅ Migrate 
	# `cd` into the `server` folder
	
    # Run in Terminal
		# export FLASK_APP=app.py
		# export FLASK_RUN_PORT=5555
        # printenv FLASK_APP FLASK_RUN_PORT # to check 
		# flask db init
        # Next Migrate our database
		    # flask db revision --autogenerate -m 'Create tables productions'
		    # flask db migrate 'Create tables productions'
		# flask db upgrade
		# flask db downgrade

    # Review the database to verify your table has migrated correctly

# 5. ✅ Navigate to `seed.rb`

# 12. ✅ Routes

@app.route("/hello")
def index():
    return "<h2>Hello World</h2>"

# 13. ✅ Run the server with `flask run` and verify your route in the browser at `http://localhost:5000/`

# 14. ✅ Create a dynamic route
# in the decorator, define our path-variable with <type:varname>
# the dynamic route defaults to str
@app.route('/productions/<string:title>')
def production(title):
    print(f'{str(type(title))}')
    return f'<h1>{title}</h1>'


# 15.✅ Update the route to find a `production` by its `title` and send it to our browser
    
    # Before continuing, import `jsonify` and `make_response` from Flask at the top of the file.
    
    # 📚 Review With Students: status codes
        # `make_response` will allow us to make a response object with the response body and status code
        # `jsonify` will convert our query into JSON

    # `@app.route('/productions/<string:title>')
    # def production(title):
    #     production = Production.query.filter(Production.title == title).first()
    #     production_response = {
    #         "title":production.title,
    #         "genre":production.genre,
    #         "director": production.director
    #         }
    #     response = make_response(
    #         jsonify(production_response),
    #         200
    #     )`    

# 16.✅ View the path and host with request context
@app.route("/context")
def context():
    return f'<h1>Path {request.path}, Host: {request.host} </h1>'

# 17.✅ Use the before_request request hook, what this hook does is up to you. You could hit a breakpoint, print something to server console or anything else you can think of.
@app.before_request
def runs_before():
    print("THIS IS RUNNING BEFORE")

# @app.after_request()
# def runs_after():
#     print("THIS IS RUNNING AFTER>>>>")

# Note: If you'd like to run the application as a script instead of using `flask run`, uncomment the line below 
# and run `python app.py`

if __name__ == '__main__':
    app.run(port=5555, debug=True)
