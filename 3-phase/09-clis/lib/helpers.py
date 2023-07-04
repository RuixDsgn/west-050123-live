from ipdb import set_trace
from pet import Pet
from owner import Owner

# The helper file is where we will define all of our functions
def main_menu():
    # Print the menu options
    menu_options = ('1', '2', '3', 'X')
    print(f'''
          1. See all Pets
          2. See all Owners
          3. Add An Owner
          X. To Exit
          ''')
    # after we show to menu, we need to collect the user input
    first_input = input("Select an Option from the list: ")
    if first_input in menu_options:
      print(f'You ve selected {first_input}')

      if first_input == "1":
        #  see all the pets
        # print_all_pets()
        print_pet_list(Pet.get_all())
        main_menu()
      elif first_input == "2":
        #  see allthe owners
        print_all_owners()
        # Once we show all the owners, give the user the option to see all the pets RELATED to a specific owner by id
        owner_id_input = input("Select an id for the owner you'd like to see the pets of, or X to go back to main menu")
        found_owner = Owner.find_by_id(int(owner_id_input))
        if found_owner:
            pet_list = found_owner.pets()
            if pet_list:
              print_pet_list(found_owner.pets())
            else:
              print("You don't have any pets yet!")
        main_menu()

      elif first_input == "3":
        # Add an Owner to the Database
        name_input = input("What's your name?\t")
        phone_input = input("What's your phone number?\t")
        email_input = input("What's your email address?\t")
        address_input = input("What's your address?\t")

        print(f'{name_input}\t{phone_input}\t{email_input}\t{address_input}\t')
        # confirm_input = input("Is this info correct?")
        # Make sure that when you are adding data to the DB, you validate the data
        new_owner = Owner.create(name_input, phone_input, email_input, address_input)
        print(f"Congrats! New Owner Created!")
        display_owner(new_owner)
        main_menu()
      elif first_input == 'X':
          print("Good bye...")



    else:
      print("BAD OPTION")
      main_menu()
        




def testo_functiono():
    print("Testo")

def print_all_pets():
    all_pets = Pet.get_all()
    for pet in all_pets:
      #  display one pet
      print(f'''
            name => {pet.name}
            species => {pet.species}
            breed => {pet.breed}
            temperament => {pet.temperament}
            owner => {pet.owner().name}
            ''')

def print_all_owners():
    all_owners = Owner.get_all()
    for owner in all_owners:
        display_owner(owner)

def display_owner(owner):
      print(f'''
            id => {owner.id}
            name => {owner.name}
            phone => {owner.phone}
            email => {owner.email}
            address => {owner.address}
            ''')
   

def print_pet_list(pet_list):
    for pet in pet_list:
      #  display one pet
      print(f'''
            name => {pet.name}
            species => {pet.species}
            breed => {pet.breed}
            temperament => {pet.temperament}
            owner => {pet.owner().name}
            ''')
