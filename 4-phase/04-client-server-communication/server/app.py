#!/usr/bin/env python3
# 📚 Review With Students:
#   CORS
# Set up:
#   cd into server and run the following in Terminal
#   export FLASK_APP=app.py
#   export FLASK_RUN_PORT=5000
#   flask db init
#   flask db revision --autogenerate -m'Create tables'
#   flask db upgrade
#   python seed.py
#   cd into client and run `npm`
# Running React Together
# Two terminals or...
# Verify that gunicorn and honcho have been added to the pipenv
#   Create Procfile.dev in root
#   in Procfile.dev add:
#   web: PORT=3000 npm start --prefix client
#   api: gunicorn -b 127.0.0.1:5000 --chdir ./server app:app
# In Terminal, cd into root and run:
#   `honcho start -f Procfile.dev`

from flask import Flask, request, make_response, abort
from flask_migrate import Migrate

from flask_restful import Api, Resource
from werkzeug.exceptions import NotFound
from flask_cors import CORS 

# 5.✅ Import CORS from flask_cors, invoke it and pass it app
#   5.1Start up the server / client and navigate to client/src/App.js

from models import db, Production, CrewMember

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db, render_as_batch=True)
db.init_app(app)

api = Api(app)

class Productions(Resource):
    def get(self):
        production_list = [p.to_dict() for p in Production.query.all()]
        return make_response(production_list, 200)

    def post(self):
        form_json = request.get_json()
        # 4.✅ Add a try except, try to create a new production. If a ValueError is raised call abort with a 422 and pass it the validation errors.
        new_production = Production(
            title=form_json['title'],
            genre=form_json['genre'],
            budget=int(form_json['budget']),
            image=form_json['image'],
            director=form_json['director'],
            description=form_json['description']
        )

        db.session.add(new_production)
        db.session.commit()

        return make_response(new_production.to_dict(), 201)


api.add_resource(Productions, '/productions')


class ProductionByID(Resource):
    def get(self, id):
        production = Production.query.filter_by(id=id).first()
        if not production:
            raise NotFound

        return make_response(production.to_dict(), 200)

    def patch(self, id):
        production = Production.query.filter_by(id=id).first()
        if not production:
            raise NotFound

        form_json = request.get_json()
        for attr in form_json:
            if attr == "ongoing":
                production.ongoing = bool(form_json[attr])
            elif attr == "budget":
                production.budget = int(form_json[attr])
            else:
                setattr(production, attr, form_json[attr])

        db.session.add(production)
        db.session.commit()

        return make_response(production.to_dict(), 200)

    def delete(self, id):
        production = Production.query.filter_by(id=id).first()
        if not production:
            raise NotFound
        db.session.delete(production)
        db.session.commit()

        return make_response('', 204)


api.add_resource(ProductionByID, '/productions/<int:id>')


@app.errorhandler(NotFound)
def handle_not_found(e):
    return make_response(
        "Not Found: Sorry the resource you are looking for does not exist",
        404
    )


# To run the file as a script
# if __name__ == '__main__':
#     app.run(port=5000, debug=True)
