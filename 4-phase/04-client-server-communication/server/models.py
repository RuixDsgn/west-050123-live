# 📚 Review With Students:
    # Validations and Invalid Data

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
# 1.✅ Import validates from sqlalchemy.orm

db = SQLAlchemy()

class Production(db.Model, SerializerMixin):
    __tablename__ = 'productions'

    id = db.Column(db.Integer, primary_key=True)

# 2.✅ Add Constraints to the Columns     

    title = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    budget = db.Column(db.Float)
    image = db.Column(db.String)
    director = db.Column(db.String)
    description = db.Column(db.String)
    ongoing = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Production.crew_members =  CrewMember.query.filter_by(production_id = self.id).all()
    # Add the relationship between our Production -> CrewMember
    # crew_members = db.relationship("CrewMember", backref="production", lazy=True)
        
    serialize_rules = ('-updated_at', '-created_at')

# 3.✅ Use the "validates" decorator to create a validations
    # @validates("image")
    # def validates_image(self, key, image_path):
    #     if ".jpg" not in image_path:
    #         raise ValueError("Image file must be a .jpg")
    #     return image_path
    
    @validates("budget")
    def validates_budget(self, key, budget):
        if budget in range(5000, 1000000):
            return budget
        raise ValueError("Budget has to be greater than 5000, but less than 1 million")

  
# 4.✅ navigate to app.py
    def __repr__(self):
        return f'<Production Title:{self.title}, Genre:{self.genre}, Budget:{self.budget}, Image:{self.image}, Director:{self.director},ongoing:{self.ongoing}>'

# Add CrewMember model for the has_many association
    # name: string
    # role: string
    # production_id: int, foriegn_key
    # timestamps

class CrewMember(db.Model, SerializerMixin):
    __tablename__ = 'crew_members'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    role = db.Column(db.String)
    # production_id = db.Column(db.Integer, db.ForeignKey('productions.id'))
    production_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    # CrewMember.production => Production.query.filter_by(id = self.production_id).first()

    def __repr__(self):
        return f'<CrewMember Name:{self.name}, Role:{self.role}'
        # return f'<CrewMember Name:{self.name}, Role:{self.role}, ProductionTitle: {self.production.title}'

