#!/usr/bin/env python3

""" 
  Warmup Questions!

  1. What's the differences between the types of Sequences(arrayish)
    - List
      => Changeable, Ordered
        => .append, .pop
      => Syntax: [] OR list()
    - Tuple
      => Unchangeable, Ordered
        => Can only READ from tuple
      => Syntax: () or tuple()
    - Set
      => Unchangeable, Unordered
      => Syntax: {} or set()

  2. What are the ways to get values out of a dict()?
    => Bracket Notation
      - dict["key"] => value
      - dict["bad_key"] returns KeyError
      - CAN UPDATE THE key/value 
        - dict["key"] = "new_value"
    => Get Notation
      - dict.get("key") => value
      - dict.get("bad_key") returns None
      - CAN'T UPDATE key/value
        - dict.get("key") = "new_value" => Syntax Error
 """

""" 
  What is Object Orientation (OOP)?

  - Thinking like objects as part of our data. 
  - Use our data to Emulate real life
  - Programming Principals that focus on data/datastructures
  - creating Classes of 'real life' things and building methods (actions) that that class can do

  Classes:
  - Create a Blueprint for what the obejct is, as well as all the methods that this class can perform
  - Initialized with certain attributes

  Examples
  - Coffee Maker
    - Initalized with these attributes
      - make, model, size, etc...
      - methods
        - make coffee, clean thing, boil water
  - Toaster
    - type, size, color, material
    = methods
      - make toast, clean, cook chicken

    
 """

# Demonstrate classes 
# 1. ✅ Create a Pet class
# 2. ✅ Instantiate a few pet instance 
    # Compare the pet instances to demonstrate they are not the same object
    # Note: add 'pass' to the pet class 
import ipdb

class Pet:
    # pass
# 3. ✅ Demonstrate __init__ 
    # Add arguments to instances  
    # use dot notation to access their attributes 
    # update attributes with new values 

  def __init__(self, name, age, breed, temperament, is_cool=True):
    # in the init method, the `self` refers to the newly created INSTANCE of the Pet class
    self.name = name
    self.age = age
    self.breed = breed
    self.temperament = temperament
    self.is_cool = is_cool
    self.other_thing = "IDK?"
    print(self)

# 4.✅ Demonstrate instance methods by creating a print_pet_details function that will print the pet attributes
#     Review the self keyword 
#     Invoke the print_pet_details on an instance 
#           -> 
            # name:rose
            # age:11
            # breed:domestic longhair
            # temperament:sweet
            # image_url:rose.jpg
  
  # ! INSTANCE METHODS!
  # Methods that is call ON an instance 
  # without the (self) => *** TypeError: print_details() takes 0 positional arguments but 1 was given
  def print_details(self):
    # chauncy.name or cosmo.name or INSTANCE_VARIABLE.name
    print(f'Name => {self.name}')
    print(f'Age => {self.age}')
    print(f'Temp => {self.temperament}')
    # ipdb.set_trace()


  def high_five(self):
    print(f'{self.name} gives you a high five!')

  def play_fetch(self):
    print(f'{self.name} go Fetch!')
    self.temperament = "Happy"

  def take_a_nap(self):
    print(f'taking a nap')
    self.temperament = "sleepy"

  def go_back_in_time(self):
    self.age -= 1
    print(f'Happy Un-Birthday {self.name}, you are now {self.age}!')

  def change_temperament(self, new_temp):
    self.temperament = new_temp
    self.high_five()
    self.print_details()

  def tell_other_pet_i_said_hi(self, other_pet_instance):
    print(f'Hi, {other_pet_instance.name}! It\'s ya boi, {self.name}')


# Demonstrate instances 
    # Different Instances are Different Objects
# Demonstrate __init__
# Demonstrate instance method
# Demonstrate the self keyword 
# Stretch Goals
# Demonstrate object properties

# Instances 

# Run in ipdb session
# rose == cookie
#   False

#Read Attributes 
# rose.name -> rose
# rose.age -> 11

#Update
# rose.age -> 11
# rose.age = 12
# rose.age -> 12
