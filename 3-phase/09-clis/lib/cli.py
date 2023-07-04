from ipdb import set_trace
from os import system
from owner import Owner
from pet import Pet
from helpers import *

if __name__ == "__main__":
    system("clear")
    print('''
        __________        __   _________                       __   
        \______   \ _____/  |_/   _____/ _____  _____ ________/  |_ 
        |     ___// __ \   __\_____  \ /     \ \__  \ \_  __ \   __\ 
        |    |   \  ___/|  | /        \  Y Y  \ / __ \|  | \/|  |  
        |____|    \___  >__|/_______  /__|_|   (____  /__|   |__|  
                      \/            \/      \/     \/             
    ''')
    print("Hello! Welcome to the Petsmart CLI!")

    # CLI Actions:
    #   See all the Pets in DB
    #   See all the Owners in DB
    #   See all the Pets of a given Owner
    #   add an Pet to our Owner
    #   Update a pet
    #   Add a new Owner

    # ! The CLI file is the main run file
    # Invoking the functions needed to start the app

        
    main_menu()
