from ipdb import set_trace
from faker import Faker
from owner import Owner
from pet import Pet, CONN, CURSOR

if __name__ == "__main__":  
  print("Seeding 🌱...")
  fake = Faker()

  # Drop all the tables, so we start fresh
  Owner.drop_table()
  Pet.drop_table()

  # Recreate the Tables
  Owner.create_table()
  Pet.create_table()

  # Create our initial Testing instances with associations
  #   Start by creating the Parent/Has_many relationship
  #     For this example, Owners first Then Pets
  #  Owner has_many Pets
  print("Creating Owners...")
  o1 = Owner("Tymon", fake.phone_number(), fake.email(), fake.address())
  o2 = Owner("Ethan", fake.phone_number(), fake.email(), fake.address())
  o3 = Owner(fake.name(), fake.phone_number(), fake.email(), fake.address())
  
  o1.save()
  o2.save()
  o3.save()

  print("Creating Pets...")
  p1 = Pet.create("Thor", "Cat", "Orange", 6, o1.id) # the id will `probably` be 1, but we need to make sure it's the id of o1
  p2 = Pet.create("Loki", "Goat", "Highlands", 9, o2.id)
  p3 = Pet.create("Odin", "Crow", "Black", 1, o2.id)

  # Create any fake data to thicken our testing data

  print("done!")
