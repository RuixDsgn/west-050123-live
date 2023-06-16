# Create a subclass of Pet called Dog
import ipdb
from lib.pet import Pet

class Dog(Pet):
    
    all_dogs = []
    
    def __init__(self, name, age, breed, temperament, fixed, health):
      # self.name = name
      # self.breed = breed
      # self.age = age
      # self.temperament = temperament
      super().__init__(name, age, breed, temperament)
      self.fixed = fixed
      self.health = health
      
      Dog.all_dogs.append(self)

    @property
    def fixed(self):
       print("Getting Fixed")
       return self._fixed
    
    @fixed.setter
    def fixed(self, new_fixed):
       if type(new_fixed) == bool:
          self._fixed = new_fixed
       else:
          print("nah bruh")
    
    def print_pet_details(self):
      super().print_pet_details()
      print(f'''
            Fixed? {"Yup" if self.fixed else "Nah"}
            Health: {self.health}
            ''')