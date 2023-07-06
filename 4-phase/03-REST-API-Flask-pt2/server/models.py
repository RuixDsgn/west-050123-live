
from flask_sqlalchemy import SQLAlchemy
# 6. ✅ Import `SerializerMixin` from `sqlalchemy_serializer`
from sqlalchemy_serializer import SerializerMixin
# a serializer is just a pass through method that FORMATS our data

db = SQLAlchemy()

# 7. ✅ Pass `SerializerMixin` to `Productions`
class Production(db.Model, SerializerMixin):
    __tablename__ = 'productions'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    genre = db.Column(db.String)
    budget = db.Column(db.Float)
    image = db.Column(db.String)
    director = db.Column(db.String)
    description = db.Column(db.String)
    ongoing = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # 7.1 ✅ Create a serialize rule that will help add our `crew_members` to the response and remove created_at and updated_at.
        #7.2 Demo serialize_only by only allowing title to be included in the response
        #    once done remove or comment the serialize_only line. 

    # takes a tuple of all the columns to show
    # serialize_only = ('title', 'genre')
    # takes a tuple of all the columns to omit
    serialize_rules = ('-created_at', '-updated_at')

    def __repr__(self):
        return f'<Production Title:{self.title}, Genre:{self.genre}, Budget:{self.budget}, Image:{self.image}, Director:{self.director},ongoing:{self.ongoing}>'


 # 9. ✅ Navigate back to `app.py` for further steps.
#  Stretch Add the CrewMember relationship