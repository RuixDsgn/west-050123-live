from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

db = SQLAlchemy()


class Production(db.Model, SerializerMixin):
    __tablename__ = 'productions'

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    budget = db.Column(db.Float)
    image = db.Column(db.String)
    director = db.Column(db.String)
    description = db.Column(db.String)
    ongoing = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    cast_members = db.relationship(
        "CastMember", backref="production")

    serialize_rules = ("-cast_members.production",'-updated_at', '-created_at')

    @validates("image")
    def validates_image(self, key, image_path):
        if ".jpg" not in image_path:
            raise ValueError("Image file must be a .jpg")
        return image_path

    @validates("budget")
    def validates_budget(self, key, budget):
        if budget in range(5000, 1000000):
            return budget
        raise ValueError(
            "Budget has to be greater than 5000, but less than 1 million")

    def __repr__(self):
        return f'<Production Title:{self.title}, Genre:{self.genre}, Budget:{self.budget}, Image:{self.image}, Director:{self.director},ongoing:{self.ongoing}>'


class CastMember(db.Model, SerializerMixin):
    __tablename__ = 'cast_members'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    role = db.Column(db.String)
    production_id = db.Column(db.Integer, db.ForeignKey('productions.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'<CastMember Name:{self.name}, Role:{self.role}'
        # return f'<CastMember Name:{self.name}, Role:{self.role}, ProductionTitle: {self.production.title}'
