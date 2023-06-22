#!/usr/bin/env python3

# from owner import Owner, CONN, CURSOR
from lib.pet import Pet, CONN, CURSOR

""" 
  Warm up Questions!

  1. What is Object Inheritance?
  - When a child/sub class recieves all the properties of their super/parent class
  
  1a. How do we initialize a sub-class?
  - def __init__(self, Stuff...)
    super().__init__(all, the parent, attributes)
    self.child = attributes

  2. What are some reasons for SQL/Databases?
  - Relationships between tables
    - Foreign Keys on the belongs_to relationship
  - Perform CRUD ops
  - Manage queries
  - Data will persist

  3. What are some SQL Keywords/Queries?
  - Reads
    - SELECT (all is *) FROM table
    - JOIN other_table ON some condition(will mostly be the relationship
      - The Join will return a new combine table
    - WHERE (comparision)

  - Create
    - INSERT INTO table (columns) VALUES (the values)
  - UPDATE
    - UPDATE table SET = "new value" WHERE (finding the row)
      - For changes on one particular instance/row
    - ALTER table ()
      - For fundmental changes to the table/database
  - DELETE
    - DROP TABLE IF EXISTS table

"""

""" 
  Object Relational Mapping (ORMs)

  - Convert Database records into instance of our classes
    - Our `pets` table will have an associated class Pet
  - Just a principle, ORMs can (and have) been made in every language
    - JS => Sequelize
    - Ruby => ActiveRecord
  - Why???
    - Sending Raw SQL queries as strings, can get tidieous
    - Devs wrote their own class/instance methods to communicate with the db
    - Turns 'SELECT * FROM pets;' into Pet.all_pets()
    - Makes our code REUSEABLE and DRY

 """



Pet.drop_table()

Pet.create_table()

chauncy = Pet("Chauncy", "Canine", "Mutt", 7, 1)
print(chauncy)
chauncy.save()
cosmo = Pet.create("Cosmo", "Dog", "Breadie", 6, 2)

# Pet.get_all()
print(Pet.find_or_create_by("Chauncy", "Canine", "Mutt", 7, 1))
print(Pet.find_or_create_by("Pepper", "Canine", "Mutt", 7, 1))


import ipdb; ipdb.set_trace()