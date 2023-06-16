#!/usr/bin/env python3
import ipdb
from lib.owner import *

class Pet:

    all_pets = []

    def __init__(self,name, age, breed, temperament, owner, is_cool=True):
        self.name = name
        self.age = age
        self.breed = breed
        self.temperament = temperament
        self.is_cool = is_cool
        self.owner = owner
        Pet.add_pet(self)

    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        if (type(new_name) == str) and (len(new_name) > 0):
            self._name = new_name
        else:
            print("BAD STRING BOTY")
    
    name = property(get_name, set_name)

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if (type(new_age) == int) and (new_age > 0):
            self._age = new_age
        else:
            print("BAD AGE BOTY")

    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, owner):
        if type(owner) == Owner:
            self._owner = owner
        else:
            raise AttributeError("namh....")

    def print_pet_details(self):
        print(f'''
            name:{self.name}
            age:{self.age}
            breed:{self.breed}
            temperament:{self.temperament}
        ''')

    def __repr__(self):
        return f'''name: {self.name}, age: {self.age}, breed: {self.breed}, temperament: {self.temperament}, is_cool: {self.is_cool}, owner: [{self.owner}]'''
    
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
        
        


    