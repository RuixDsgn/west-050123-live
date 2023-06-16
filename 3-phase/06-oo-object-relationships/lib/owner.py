
class Owner():
    
    all_owners = []
    
    def __init__(self, name, location):
        self.name = name
        self.location = location
        Owner.all_owners.append(self)

    def get_name(self):
        return self._name

    def set_name(self, name):
        if type(name) == str:
            self._name = name
        else:
            raise ValueError
      
    name = property(get_name, set_name)

    @property
    def location(self):
      return self._location
    
    @location.setter
    def location(self, location):
        if type(location) == str:
            self._location = location
        else:
            raise ValueError

    def __repr__(self):
        return f'''name: {self.name}, location: {self.location}'''
    
    @property
    def pets(self):
        import ipdb
        from lib.pet import Pet
        return [ pet for pet in Pet.all_pets if pet.owner == self]
        # owner_pets = []
        # for pet in Pet.all_pets:
        #     if pet.owner == self:
        #         owner_pets.append(pet)
        # return owner_pets

    def average_age_of_my_pets(self):
        age_list = [ pet.age for pet in self.pets]
        return sum(age_list) / len(age_list)