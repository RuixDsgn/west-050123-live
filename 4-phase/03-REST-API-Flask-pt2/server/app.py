#!/usr/bin/env python3
# 📚 Review With Students:
    # API Fundamentals
    # MVC Architecture and Patterns / Best Practices
    # RESTful Routing
    # There are 7 RESTful routes
    #   If we are dealing with the Backend only routes, there's only 5 need
    # | HTTP Verb 	|       Path       	| Description        	| REST Route    | 
    # |-----------	|:----------------:	|--------------------	|------------   |
    # | GET         |/productions   	|  READ all Prods     	| INDEX         |
    # | GET         |/productions/:id   |  READ ONE Prod     	| SHOW          |
    # | POST        |/productions       |  CREATE ONE Prod     	| CREATE        |
    # | PATCH/PUT   |/productions/:id   |  UPDATE ONE Prod     	| UPDATE        |
    # | DELETE      |/productions/:id   |  DELETE ONE Prod     	| DELETE/DESTROY|

    # The last 2 RESTful routes may exist on REACT
    # | GET         |/productions/new   |   DISPLAY NEW FORM    | NEW           |
    # | GET         |/path/:id/edit     |   DISPLAY EDIT FORM   | EDIT           |
    

# Set Up:
    # In Terminal, `cd` into `server` and run the following:
        # export FLASK_APP=app.py
        # export FLASK_RUN_PORT=5000
        # flask db init
        # flask db revision --autogenerate -m 'Create tables' 
        # flask db upgrade 
        # python seed.py

from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource

# 1. ✅ Import `Api` and `Resource` from `flask_restful`
    # ❓ What do these two classes do at a higher level? 

from models import db, Production

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Note: `app.json.compact = False` configures JSON responses to print on indented lines
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

# 2. ✅ Initialize the Api
    # `api = Api(app)`
api = Api(app)

class Productions(Resource):

    def get(self):
        all_prods = [ prod.to_dict() for prod in Production.query.all()]
        return make_response(all_prods, 200)
    
    def post(self):
        new_prod = Production(
            title=request.form["title"],
            genre=request.form["genre"],
            budget=int(request.form["budget"]),
            director=request.form["director"],
            description=request.form["description"],
            ongoing=True if request.form["ongoing"] == 'true' else False,
        )
        db.session.add(new_prod)
        db.session.commit()
        return make_response(new_prod.to_dict(), 201)


api.add_resource(Productions, "/productions")

class ProductionByID(Resource):

    def get(self, prod_id):
        found_prod = Production.query.filter_by(id=prod_id).first()
        # This will either return the Prod Instance or NONE
        if found_prod:
            return make_response(found_prod.to_dict(), 200)
        else:
            return make_response({"error": f'Production of id {prod_id} not found'}, 404)
        
    def update(self, prod_id):
        pass

    def delete(self, prod_id):
        pass

api.add_resource(ProductionByID, "/productions/<int:prod_id>")
