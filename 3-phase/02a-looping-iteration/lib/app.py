# Demo Loops 
import ipdb
from os import system


""" 
    ? JS
    Types of Loops:
        for 
            => for (let i = 0; i < 10; i++) { something }
            => for..in  => for objects
            => for..of => still arrays
        while
        until

    exArr = [1,2,3,4,5]
    arrLength = exArr.length

    Array Iteration Methods
    .forEach
        console.log(arr.forEach(num => num + 1)) 
        => undefined
    .filter
        => returns array of arrLength OR LESS with the true conditions
    .map
        => returns copy of the array with any changes from the cbFunc
    .find
        => returns the FIRST ELEMENT that satisfies the condition


 """

system("clear")

pet_info = [
    {
        'name':'chauncy',
        'age':11,
        'breed': 'mutt',
    }, 
    {
        'name':'cosmo',
        'age':25,
        'breed': 'beardie',
    },
    {
        'name':'Meow Meow Beans',
        'age':2,
        'breed': 'domestic long-haired',
    },    
    {
        'name':'chauncy',
        'age':2,
        'breed': 'domestic long-haired',
    }
    ]
    
# for <enumerable> in <sequence>:
#   do thing

#33. ✅ Loop through a range of 10 and print every number within the range
# print(1)
# print(2)
# ..
# [*range(0,10)] just for us cool devs

# for num in range(10):
#     print(num)

#34. ✅ Loop through a range between 50 and 60 that iterates by 2 and print every number
# for num in range(50,60,2):
#     print(num)

#35. ✅ Loop through the "pet_info" list and print every dictionary
# for pet in pet_info:
#     print(pet)


#36. ✅ Create a function that takes a list as an argument 
    # The function should use a "for" loop to loop through the list and print every item 
    # Invoke the function and pass it "pet_names" as an argument

def print_list(lst):
    for item in lst:
        print(item)

print_list(pet_info)
print_list([1,2,3,4])

#37. ✅ Create a function that takes a list as an argument. (simple example) 
    # The function should define a counter and set it to 0
    # Create a "while" loop 
        # The loop will continue as long as the counter is less than the length of the list
        # Every loop should increase the count by 1
    # Return the counter 
def my_counter(lst):
    counter = 0
    while (counter < len(lst)):
        print(counter)
        counter += 1
    return counter

# print(f'Output: {my_counter([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])}')

#38. ✅ Create a function that updates the age of a given pet
        # The function should take a list of "dict"s, "name" and "age" as parameters 
        # Create am index variable and set it to 0
        # Create a while loop 
            # The loop will continue so long as the list does not contain a name matching the "name" param and the index is less then the length of the list
            # Every list will increase the index by 1
        # If the dict containing a matching name is found, update the item's age with the new age 
            # Otherwise, return 'pet not found'

def updates_age(pet_list, name, new_age):
    for pet in pet_list:
        print(pet['name'])
        if pet["name"] == name:
            pet.update({"age": new_age})
    return pet_list

print(updates_age(pet_info, "Meow Meow Beans", 4567893))
print(pet_info)

# arr = [1,2,3,4]
# map like 
# ? arr.map(x => x + 1) => [2,3,4,5]
""" 
const rawMap = arr => {
    let newArr = [] OR let newArr = new Array(arr.length)
    for (let i = 0; i < arr.length; i++ ) {
        new_value = x.toUpperCase()
        newArr.push(new_value) OR newArr[i] = new_value
    }
    return newArr
}
 """
#39. ✅ Use list comprehension to return a list containing every pet name from "pet_info" changed to uppercase
def py_map(lst):
    new_list = []
    for info in lst:
        upper_name = info["name"].upper()
        new_list.append(upper_name)
    return new_list
print(py_map(pet_info))

pet_upper = [pet["name"].upper() for pet in pet_info]
inc_by_1 = [ x + 1 for x in range(10)]
print(pet_upper)
print(inc_by_1)
print(pet_info)

""" 
const rawFind = arr => {
    for (let i = 0; i < arr.length; i++ ) {
        if (some condition) {
            return this element 
        }
    }
}
 """

# find like
#40. ✅ Use list comprehension to find a pet named spot
def py_find(lst):
    for info in lst:
        if info["name"] == "chauncy":
            return info
    return f"Not Found"

print(py_find(pet_info))
find_chauncy = [ pet for pet in pet_info if pet["name"] == "chauncy" ][0]
print(find_chauncy)

""" 
const rawFilter = arr => {
    let newArr = []
    for (let i = 0; i < arr.length; i++ ) {
        if (condition) {
            newArr.push(element)
        }
    }
}
 """
# filter like
#41. ✅ Use list comprehension to find all of the pets under 3 years old
def py_filter(lst):
    new_list = list()
    for info in lst:
        if info["name"] == "chauncy":
            new_list.append(info)
    return new_list
print(py_filter(pet_info))
find_chauncies = [ pet for pet in pet_info if pet["name"] == "chauncy" ]
print(find_chauncies)


#43. ✅ Create a generator expression matching the filter above. Compare and contrast the generator to the list comprehension. 
