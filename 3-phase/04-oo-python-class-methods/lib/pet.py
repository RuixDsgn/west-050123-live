#!/usr/bin/env python3
# Class Attributes and Methods 

""" 
    Warm Up Questions!

    1. What is `self`?
        - self referential variable
            - What am I? 
    chauncy = Pet(args_for_chauncy)
        => self in the __init__ => newly created instance
    chauncy.print_pet_details()
        => self in this method => the instance that we are calling the method on

    2. How can you define a default attribute for a class?
        - def __init(self, default_att="Hi")
 """

""" 
    ! Class Variables and Class Methods!

    What are Class methods?
    - Methods that are called ON the WHOLE CLASS
    - Pet.count_all_pet()

    What are Instance methods?
    - relative to this specific instance
    - a method that is callled on the instance
    - instance.instance_method()

 """
import ipdb

class Pet:

    # Class Variables
    cool_thing = "HI"
    all_pets = []
    # # pet_count = 0
    # # age_list = []
    # DOn't need those because.......
    # pet_count => len(all_pets)
    # age_list => .map => [ pet.age for pet in all_pets ]
    # !!! SINGLE SOURCE OF TRUTH
    #   - Keeps your data consitant
    #   - Helps debugging your db/backend
    #   - DOn't have to do extra work on all the aggregate metadata
    #   - Reduces the amount of Memory needed to store data

    def __init__(self,name, age, breed, temperament, is_cool=True):
        self.name = name
        self.age = age
        self.breed = breed
        self.temperament = temperament
        self.is_cool = is_cool
        Pet.add_pet(self)
 
    
    # 6✅. Create a class method increase_pets that will increment total_pets
        # replace Pet.total_pets += 1 in __init__ with increase_pets()

    def print_pet_details(self):
        print(f'''
            name:{self.name}
            age:{self.age}
            breed:{self.breed}
            temperament:{self.temperament}
        ''')

    def print_self(self):
        print(self)

    # CLASS METHODS

    # count all pets
    # show all pets
    # show total age of pets
    # avg age
    # show all of a certain breed

    # !PYTHON DECORATORS
    @classmethod
    def test_class_method(cls):
        print(cls == Pet)

    @classmethod
    def add_pet(cls, new_pet):
        cls.all_pets.append(new_pet)

    @classmethod
    def count_pets(cls):
        return len(Pet.all_pets)
    
    @classmethod
    def print_all_pets(cls):
        for pet in cls.all_pets:
            pet.print_pet_details()

    @classmethod
    def total_age(cls):
        age_list = [pet.age for pet in cls.all_pets]
        # total = 0
        # for age in age_list:
        #     total += age
        # return total
        return sum(age_list)
    
    @classmethod
    def average_age(cls):
        return cls.total_age() / cls.count_pets()
    
    @classmethod
    def show_certain_breed(cls, search_breed):
        return [ pet for pet in cls.all_pets if pet.breed == search_breed ]
        matching = []
        for pet in cls.all_pets:
            if pet.breed == search_breed:
                matching.append(pet)
        return matching
        
        


    