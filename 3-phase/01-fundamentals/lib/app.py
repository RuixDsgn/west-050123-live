#!/usr/bin/env python3

# 📚 Review With Students:
    # Python environment set up
	# Python debugging tools 
	# Python datatypes 

# 🚨 To enable ipdb debugging, first import "ipdb"
import ipdb
import requests


print("HELLO WORLS")

# ? String Interpolation JS
# `${variable} is good`
name = "carla"
print(f'Her name is: {name}!')

# 1. ✅ Create a condition to check a pet's mood

    # Note => Feel free to set your own values for "pet_mood" to view various outputs.
# const func = () => {}

# def function_name(any, args):
#   INDENTATION NEEDS TO BE THERE
#   my code
#   return of things

def check_mood(mood):
    # If "pet_mood" is "Hungry!", "Rose needs to be fed."
    # If "pet_mood" is "Rowdy!", "Rose needs a walk."
    # In all other cases, "Rose is all good."
    # ? if (pet_mood === "HUngry!") {console.log("Rose needs to be feed")}
    # ? else if (pet_mood === Rowdy!") {console.log("Rose needs walk")}
    # ? else {last thing}

    # no "1" approx Number1
    # ONLY EXACT COMPARISONS IN PYTHON
    if mood == "Hungry!":
        print("Rose needs to be feed")
    elif mood == "Rowdy!":
        print("Rose needs a walk")
    else:
        print("Rose is all gucci")


pet_mood = "Hungry!"
check_mood(pet_mood)
check_mood("Rowdy!")
check_mood("asfghsdghkhksdghjksdfsdfghjkgjksdf")

pet_name = "Rose"

# 2. ✅ Create a ternary operator using "pet_mood" as a condition:
    # If pet_food is "Hungry!" => "Rose needs to be fed."
    # In all other cases => "Rose is all good."


def check_mood_ternary(mood, pet_name):
    # ? pet_mood === "Hungry!" ? "Rose be feed" : "All good"
    # if mood == "Hungry!":
    #     print("Rose needs to be feed")
    # else: 
    #     print("Rose is all gucci")

    # `return_if_true` if `conditional` else `return_if_false`
    output = f"{pet_name} needs to be feed" if mood == "Hungry!" else f"{pet_name} is all gucci"
    print(output)

check_mood_ternary("Hungry!", "Chauncy")

# 3. ✅ Create a function (say_hello) that returns the string "Hello, world!"
    # Test invocation of "say_hello" in ipdb using "say_hello()"
    # say_hello() => "Hello, world!"

def say_hello():
    # ? debugger
    # import ipdb
    ipdb.set_trace()

# def say_goodbye():
#     ipdb.set_trace()

# say_hello()
# say_goodbye()

# 4. ✅ Create a function (pet_greeting) that will return a string with interpolated pet's name
    # Test invocation of "pet_greeting" in ipdb using "pet_greeting()"
    # pet_greeting("Rose") => "Rose says hello!"
    # pet_greeting("Spot") => "Spot says hello!"

def pet_greeting(pet_name):
    print(f'{pet_name} says hello')


# 5. ✅ Move conditional logic from Deliverable 1 into a function (pet_status) so that we may use it with different pets / moods
    # Test invocation of "pet_status" in ipdb using "pet_status(pet_name, pet_mood)"
    # pet_status("Rose", "Hungry!") => "Rose needs to be fed."
    # pet_greeting("Spot", "Rowdy!") => "Spot needs a walk."
    # pet_greeting("Bud", "Relaxed") => "Bud is all good."
    
    # Take a moment to note that "pet_name" and "pet_mood" parameters are within Local Scope and take priority over "pet_name" and "pet_mood"
    # in Global Scope.

# 6. ✅ Create a function (pet_birthday) that will increment a pet's age up by 1. Use try / except to handle errors. 
    # If our function is given an incorrect datatype, it should handle the TypeError exception and alert the user
    # pet_birthday(10) => "Happy Birthday! Your pet is now 11."
    # pet_birthday("oops") => "Type Error Occurred"

    # Note => To view more common Python exceptions, visit https://docs.python.org/3/library/exceptions.html

def pet_birthday(age):
    # increase age by 1
    try:
        # new_age = age + 1
        new_age = bad_age + 1
        print(f'Happy Birthday! Your pet is {new_age}')
    except TypeError:
        print("There's a Type Error?")
    except NameError:
        print("Wrong name foo")
    except:
        print("else error....")

# Main Errors we will be dealing with:
#   TypeError
#   NameError
#   IndexError
#   ModuleNotFoundError
#   AssertionError
#   SyntaxError
#   ...etc

pet_birthday("5")
pet_greeting("chauncy")


# 🚨 To create an ipdb breakpoint, comment / uncomment line below:
# ipdb.set_trace()

print("DONE!")
