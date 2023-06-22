# Stretch Goal: Include Association with Owner

# Pet Attributes: 
# name: TEXT 
# species: TEXT
# breed: TEXT 
# temperament: TEXT

# Stretch Goal
# owner_id: INTEGER

""" 
    The `sqlite3` module!


 """
import ipdb 
import sqlite3 # We import the sqlite3 module
# included in the base python packages

# create the CONNECTION to our database
CONN = sqlite3.connect('lib/resources.db')

# The cursor, gives us the ability to EXECUTE our SQL Query strings as queries on the db
CURSOR = CONN.cursor()

class Pet:
    
    # Class variable for all pets
    all = []

    # ✅ 1. Add "__init__" with "name", "species", "breed", "temperament", and "id" (Default: None) Attributes
    def __init__(self, name, species, breed, temperament, owner_id, id=None):
        self.name = name
        self.species = species
        self.breed = breed
        self.temperament = temperament
        self.owner_id = owner_id
        self.id = id

    def __repr__(self):
        return str(self.__dict__)

    # ✅ 2. Add "create_table" Class Method to Create "pets" Table If Doesn't Already Exist
    @classmethod
    def create_table(cls):
        # 1st! Create the base sql query as a string
        create_table_sql = """
            CREATE TABLE IF NOT EXISTS pets (
                id INTEGER PRIMARY KEY,
                name TEXT,
                species TEXT,
                breed   TEXT,
                temperament INT,
                owner_id INT
            )"""
        # 2nd EXECUTE the query using the CURSOR
        CURSOR.execute(create_table_sql)
        print("creating table...")

    # ✅ 3. Add "drop_table" Class Method to Drop "pets" Table If Exists
    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS pets"
        CURSOR.execute(sql)
        print("Dropped table...")

    # ✅ 4. Add "save" Instance Method to Persist New "pet" Instances to DB
        # 4a. Create a new Pet Instance, 
        # 4b. pet_instance.save() => saves the instance to our database
    def save(self):
        sql = """
            INSERT INTO pets (name, species, breed, temperament, owner_id)
            VALUES (?, ?, ?, ?, ?)"""
        # the question marks in the query act as variables/arguments for when we execute the query
        # Order DOES matter
        # the Second argument on the execute is all the parameters to fill in the question marks as a tuple
        parameters = (self.name, self.species, self.breed, self.temperament, self.owner_id)
        CURSOR.execute(sql, parameters)
        CONN.commit()
        self.id = CURSOR.lastrowid
        print(self)

    # ✅ 5. Add "create" Class Method to Initialize and Save New "pet" Instances to DB
    @classmethod
    def create(cls, name, species, breed, temperament, owner_id, id=None):
        new_pet = Pet(name, species, breed, temperament, owner_id)
        new_pet.save()
        return new_pet


    # ✅ 6. Add "new_from_db" Class Method to Retrieve Newest "pet" Instance w/ Attributes From DB
    @classmethod
    def new_instance_from_db(cls, row):
        # for when our db is already active, but we closed our python application
        # aka, the definition of persistance...
        return cls(
            name=row[1],
            species=row[2],
            breed=row[3],
            temperament=row[4],
            owner_id=row[5],
            id=row[0],
        )


    # ✅ 7. Add "get_all" Class Method to Retrieve All "pet" Instances From DB
    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM pets"
        response = CURSOR.execute(sql)
        # Inorder to SEE any data from the SELECTor, .fetchall Or .fetchone, to return a list of tuples(rows)
        all_pets_list = response.fetchall()
        # we want to return a mapped list of all the rows as instances
        return [ Pet.new_instance_from_db(row) for row in all_pets_list]


    # ✅ 8. Add "find_by_name" Class Method to Retrieve "pet" Instance by "name" Attribute From DB
        # If No "pet" Found, return "None"
    @classmethod
    def find_by_name(cls, search):
        sql = """
            SELECT * FROM pets
            WHERE name = ?
        """
        # the second arg of parameters, still has to be a tuple even if there is only `1` arg
        response = CURSOR.execute(sql, (search,))
        row = response.fetchone()
        return Pet.new_instance_from_db(row) if row else None

    # ✅ 9. Add "find_by_id" Class Method to Retrieve "pet" Instance by "id" Attribute From DB
        # If No "pet" Found, return "None"
    @classmethod
    def find_by_id(cls, search_id):
        sql = "SELECT * FROM pets WHERE id = ?"
        row = CURSOR.execute(sql, (search_id,)).fetchone()
        return Pet.new_instance_from_db(row) if row else None

    # ✅ 10. Add "find_or_create_by" Class Method to:
    @classmethod
    def find_or_create_by(cls, name, species, breed, temperament, owner_id):
        find_sql = """
            SELECT * FROM pets
            WHERE (name, species, breed, temperament, owner_id) = (?, ?, ?, ?, ?)"""
        found_row = CURSOR.execute(find_sql, (name, species, breed, temperament, owner_id)).fetchone()
        if found_row:
            #  Find and Retrieve "pet" Instance w/ All Attributes
            return Pet.new_instance_from_db(found_row)
        else:
            # If No "pet" Found, Create New "pet" Instance w/ All Attributes
            new_pet = Pet.create(name, species, breed, temperament, owner_id)
            return new_pet


    # ✅ 11. Add "update" Class Method to Find "pet" Instance by "id" and Update All Attributes
    def update(self, name, species, breed, temperament, owner_id):
        sql = """
            UPDATE pets
            SET name = ?,
                species = ?,
                breed = ?,
                temperament = ?,
                owner_id = ?
            WHERE id = ?"""
        parameters = (name, species, breed, temperament, owner_id, self.id)
        CURSOR.execute(sql, parameters)
        CONN.commit()
        # then update all the self.attr to the new instance attributes

    # ✅ 12. DELETE
    def delete_from_db(self):
        sql = "DELETE FROM pets WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()