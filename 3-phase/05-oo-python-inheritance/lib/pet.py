#!/usr/bin/env python3
import ipdb

class Pet:

    all_pets = []

    def __init__(self,name, age, breed, temperament, is_cool=True):
        self.name = name
        self.age = age
        self.breed = breed
        self.temperament = temperament
        self.is_cool = is_cool
        Pet.add_pet(self)
 
    """ 
        ! Defining Properties
        Read and Write Attributes

        Getter and Setter Methods
        - Getter => method to RETREIVE a given Attr
        - Setter => Method to overwrite/udpate a given attr
     
        Private(ish) Attributes in Python
        => self._attribute
        - Private variables are technically NOT private in PYthon, but withthe underscore, it tells the devs that they shouldn't
    """

    def get_name(self):
        print("getting name")
        return self._name
    
    def set_name(self, new_name):
        if (type(new_name) == str) and (len(new_name) > 0):
            self._name = new_name
        else:
            print("BAD STRING BOTY")
    
    name = property(get_name, set_name)

    @property
    def age(self):
        print("getting age")
        return self._age
    
    @age.setter
    def age(self, new_age):
        if (type(new_age) == int) and (new_age > 0):
            self._age = new_age
        else:
            print("BAD AGE BOTY")


    def say_hello(self):
        print("jelllo")

    def print_pet_details(self):
        print(f'''
            name:{self.name}
            age:{self.age}
            breed:{self.breed}
            temperament:{self.temperament}
        ''')

    def print_self(self):
        print(self)

    # ! CLASS METHODS
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
        return sum(age_list)
    
    @classmethod
    def average_age(cls):
        return cls.total_age() / cls.count_pets()
    
    @classmethod
    def show_certain_breed(cls, search_breed):
        # return [ pet for pet in cls.all_pets if pet.breed == search_breed ]
        matching = []
        for pet in cls.all_pets:
            if pet.breed == search_breed:
                matching.append(pet)
        return matching
        
        


    