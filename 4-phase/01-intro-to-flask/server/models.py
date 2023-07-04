# 📚 Review With Students:
    # Review models
    # Review MVC
#SQLAlchemy import
from flask_sqlalchemy import SQLAlchemy

# 📚 Review With Students:
    # What SQLAlchemy() is replacing from SQLAlchemy/ORMs in phase 3
     
db = SQLAlchemy()
# Initalizes our database to link up with SQLAlchemy
# This would be the CONN = sqlite.connection(db)

# 1. ✅ Create a Production Model
	# tablename = 'Productions'
	# Columns:
        # title: string, genre: string, budget:float, image:string,director: string, description:string, ongoing:boolean, created_at:date time, updated_at: date time 

# Table called production
# Before, we'd have to define all the SQL query methods
# Each model will Inherit from the SQLA Model
class Production(db.Model):

    # Previously, we'd need to make an __init__ method and a Class.create_table() method
    # def __init__(self, title, genre, budget, image, director, desc, )
    # @classmethod
    # def create_table(cls):
    #     sql = """
    #         CREATE TABLE IF NOT EXISTS productions (
    #             id INTEGER PRIMARY KEY
    #         )"""
    #     CURSOR.execute(sql)

    __tablename__ = "productions"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    genre = db.Column(db.String)
    budget = db.Column(db.Float)
    image = db.Column(db.String)
    director = db.Column(db.String)
    description = db.Column(db.String)
    ongoing = db.Column(db.Boolean)
    runtime = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

# 2. ✅ navigate to app.py
