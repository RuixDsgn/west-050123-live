# Sequence Types

""" 
    ? Data Structures in JS
    1. Numbers
    2. Boolean
    3. Strings
    4. Undefined
    5. Null
    6. Objects
    6.5 Arrays

    
    * Data Structures in Python
    1. Numbers:
        int =>      Whole Numbers           => 1
        float =>    Decimal                 => 1.0
        complex =>  Imaginary Nums etc...
    2. Strings
        the same as js...
    3. Objects
        dict(ionary) => Key/Value pairs
            => { "key": "value" }
    4. Boolean
        bool => True / False
    5. Undefined/Null
        => None
    6. Arrays (Sequences)
        list()
            => order / changeable
            => ["first", "second"]
            => list()
        tuple()
            => ordered / unchangeable
            => ("first", "second")
            => ("first",) # Have to have trailing comma on single element tuple
        range()
            => starting value incrementing up to a end point at your interval
            => range(startVal, endVal, steps)
            => [startVal:endValue]
        set()
            => unordered / unchangeable / no dups
            => {"first", "second"}

        const arr = new Array(10)
 """
#Note: use print() to execute the examples. Comment out examples after they've been demoed.

import ipdb
import os

# Creating Lists (ARRAYS)
#1. ✅ Create a list of X pet names
pet_names = ['Rose', 'Meow Meow Beans', 'Mr.Legumes', 'Luke', 'Lea', 'Princess Grace', 'Spot', 'Tom', 'Mini', 'Paul', "Chauncy", "Cosmo", "Poppy", "Betty"]

# Reading Information From Lists
#2. ✅ Return the first pet name 
print(pet_names[0])
#2a. ✅ Return the last pet name 
print(pet_names[-1])

#3. ✅ Return all pet names beginning from the 3rd index
# print(pet_names[3:14])
print(pet_names[3:len(pet_names)])
print(pet_names[3:])


#4. ✅ Return all pet names before the 3rd index
print(pet_names[0:3])
print(pet_names[:3])

#5. ✅  Return all pet names beginning from the 3rd index and up to the 7th
print(pet_names[3:8])

# For using a RANGE, the starting number is INCLUSIVE
# The ending number is EXCLUSIVE
#   (start, end]
# ? JS Equivalent is .slice() / .splice()

#6. ✅ Find the index of "Cosmo"
# ? JS ? pet_names.findIndex(name => name === "Cosmo")
print(pet_names.index("Cosmo"))
# pet_names.index("bad name") => ValueError


#7. ✅ Reverse the original list
pet_names.reverse() # IS DESTRUCTIVE
print(pet_names)


#8. ✅ Return the frequency of 1
freq = [1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
# ? JS filter out only one's return length
# ? JS for loop count if element is 1
print(freq.count(1))


# Updating Lists
#9. ✅ Change the first element to all uppercase 
pet_names[0] = pet_names[0].upper()
print(pet_names)

# ? .push => .append
#10. ✅ Append a new name to the list
pet_names.append("Tymon")

# ? .splice()
#11. ✅ Add a new name at a specific index
pet_names.insert(3, "Louis")


#12. ✅ Add two lists together 
pet_names_2 = ["Carla", "Layne", "Joseph"]
both_lists = pet_names + pet_names_2

# ? .pop()
#13. ✅ Remove the final element from the list
print(pet_names.pop())

# ? .splice(index, -1)
#14. ✅ Remove element by specific index
print(pet_names.pop(3))

#15. ✅ Remove a specific element ("Tom")
pet_names.remove("Tom")
# pet_names.remove("Tom") => ValueError not in List

# 15a. Delete in a range
del(pet_names[3:8])


#16. ✅ Remove all pet names from the list
pet_names.clear()


#Tuple 
# 📚 Review With Students:
    # Mutable, Immutable, Changeable, Unchangeable

#17. ✅ Create a Tuple of pet 10 ages 
pet_ages = (6,7,9,4,6,8,20,7,6,7,8,3,6)


#18. ✅ Print the first pet age
print(pet_ages[0])


# Testing Changeability 
#19. ✅ Attempt to remove an element with ".pop" (should error)
# pet_ages.pop() *** AttributeError: 'tuple' object has no attribute 'pop'

#20. ✅ Attempt to change the first element (should error)
# pet_ages[0] = 500000 *** TypeError: 'tuple' object does not support item assignment

# Tuple Methods
#21. ✅ Return the frequency of a given element
print(pet_ages.count(7))

#22. ✅ Return the index of a given element 
print(pet_ages.index(20))

#23. ✅ Create a Range 
#Note:  Ranges are primarily used in loops
# Range from 0 - 100
range_1 = range(0,100)
range_2 = range(0,100, 5)
print(range_1)
print([*range_1])
print(range_2)
print([*range_2])

# Demo Sets (Stretch Goal)
#24. ✅ Create a set of 3 pet foods
pet_foods = {"purina", "chicken", "steak", "steak"}
print(pet_foods)

os.system("clear")

# ? OBJECTS!
# Demo Dictionaries 
# Creating 
#25. ✅  Create a dictionary of pet information with the keys "name", "age" and "breed"
rose_info = {'name':'rose','age':11,'breed':'domestic long'}


#26. ✅  Use dict to create a dictionary of pet information with the keys "name", "age" and "breed"
pet_info_spot = dict(name='Spot', age=25, breed='boxer')


# Reading
#27. ✅ Print the pet attribute of "name" using bracket notation
print(rose_info["name"])
# print(rose_info["name2"]) => KeyError


#28. ✅ Print the pet attribute of "age" using ".get"
#Note: ".get" is preferred over bracket notation in most cases because it will return "None" instead of an error
print(rose_info.get("age"))
print(rose_info.get("agegksfjadfghjkadsfghjkads"))


# Updating 
#29. ✅ Update the pets age to 12
rose_info['age'] = 12

#30. ✅ Update the pets age to 26, change their breed to mutt
rose_info.update({'age': 26, 'breed': 'mutt'})
# rose_info.update({'age2': 26, 'breed': 'mutt'}) => adds new key/value


# Deleting
#30. ✅ Delete a pets age using the "del" keyword 
# del(rose_info['age'])

#31. ✅ Delete the pets age using ".pop"
# rose_info.pop("age") => will return the value of the key deleted

#32. ✅ Delete the last item in the pet dictionary using "popitem()"
rose_info.popitem() 
# => return a tuple of (key, value)

ipdb.set_trace()
