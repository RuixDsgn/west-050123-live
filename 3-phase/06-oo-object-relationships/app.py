# Our Run File

import ipdb
from lib.pet import *
from lib.owner import *

"""
  ! Warmup Questions!

  1. Define Object Inheritance?
  - Passing down the `properties` to a `child` class
  1a. What is the Syntax for inheriting
    - class Child(Parent):
    - def __init__(self, properites_of_parent, extra, props, here)
      - super().__init__(properites_of_parent)
      - self.extra = extra....

  Examples:
                  Animal
    Canine            Feline   Insects Equine
    German Shepard    Orange    ...
    Husky             Calico
    Beardie           Tabby   

  2. How to define a class method?
  - @classmethod
    - @ => decorator => the function/method defined below will have the decorators extra props
  
  3. What are the 2 ways to define Properties
    3.1 => property func
      def getter, def setter
      value = property(geter, setter, deleter)
    3.2 => @property decorator
      @property
      def value(self)
        self._other_thing

      @value.setter
      def value(self, new)
  3.3 What's the benefits of using these properties?
  - Give restriction to defining attributes
  - unforunately, python doesn't technically have private variables, but we use the underscore to tell devs that it's "private"
  # - self._value = "something bad"
 """



""" 
  ! OBJECT RELATIONSHIPS

  Objects that are related by any type of relationship

  One - Many
  Parent HAS_MANY Children
  Child BELONGS_TO a PARENT

  Examples:
    Owner has many Pets / Pet belongs_to an Owner
    Computer has_many Parts / Part belongs_to a Computer
    Console has_many Games 
    Waiter has_many Tables / Table belongs_to a Waiter
    Table has_many Order / Order belongs_to a Table
    Human has_many Organs / Organ belongs_to a Human

  Many - Many

  Once your Parent  adds more than 1 relationship, then it is now a Many to Many

  Parent has_many Children
  Children has-many Parents

  Examples:
    Book(Academic Text) has_many Authors / Author has_many Books
    Developer has_many Apps / App has_many Devs
    Owner has_many Pets / Pet has_many Owner


  Important that we DEFINE the relationships early (before you start coding) because they are VERRRRY difficult to change later in the process

  One - One
  Functions the same as a one-many just returning one thing instead
    
"""

phil = Owner("Phil", "MRY")
carla = Owner("Carla", "SF")

chauncy = Pet("Chauncy", 11, "mutt", "sleepy", phil)
pepper = Pet("Pepper", 11, "Yorkie Mix", "Feisty", carla)
simon = Pet("Simon", 90, "Maltese", "Timid", carla)

# Carla => pepper / simon
#  pepper.owner => carla
#   carla.pets => [pepper, simon]
# Phil => chauncy
#   chauncy.owner => phil
#   phil.pets     => [chauncy]

# owner.pets => return a list of ALL the Pet instances that related to this Owner
# pet.owner => return the Owner instance related to this Pet

# ! First SQL/Database way
#  create id's for each class and assign the owner_id as an attr on the Pet class

# ! Second Instance Way
# When we create the Pet instance, we assign the WHOLE OWNER INSTANCE AS AN ATTR ON Pet

# carla.pets()

ipdb.set_trace()