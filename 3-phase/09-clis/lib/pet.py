from ipdb import set_trace
import sqlite3 

CONN = sqlite3.connect('lib/resources.db')
CURSOR = CONN.cursor()

class Pet:
    
    def __init__(self, name, species, breed, temperament, owner_id, id=None):
        self.name = name
        self.species = species
        self.breed = breed
        self.temperament = temperament
        self.owner_id = owner_id
        self.id = id

    def __repr__(self):
        return str(self.__dict__)

    @classmethod
    def create_table(cls):
        create_table_sql = """
            CREATE TABLE IF NOT EXISTS pets (
                id INTEGER PRIMARY KEY,
                name TEXT,
                species TEXT,
                breed   TEXT,
                temperament INT,
                owner_id INT
            )"""
        CURSOR.execute(create_table_sql)
        print("creating table...")

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS pets"
        CURSOR.execute(sql)
        print("Dropped table...")

    def save(self):
        sql = """
            INSERT INTO pets (name, species, breed, temperament, owner_id)
            VALUES (?, ?, ?, ?, ?)"""
        parameters = (self.name, self.species, self.breed, self.temperament, self.owner_id)
        CURSOR.execute(sql, parameters)
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, species, breed, temperament, owner_id, id=None):
        new_pet = Pet(name, species, breed, temperament, owner_id)
        new_pet.save()
        return new_pet

    @classmethod
    def new_instance_from_db(cls, row):
        return cls(
            name=row[1],
            species=row[2],
            breed=row[3],
            temperament=row[4],
            owner_id=row[5],
            id=row[0],
        )

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM pets"
        response = CURSOR.execute(sql)
        all_pets_list = response.fetchall()
        return [ Pet.new_instance_from_db(row) for row in all_pets_list]


    @classmethod
    def find_by_name(cls, search):
        sql = """
            SELECT * FROM pets
            WHERE name = ?"""
        response = CURSOR.execute(sql, (search,))
        row = response.fetchone()
        return Pet.new_instance_from_db(row) if row else None

    @classmethod
    def find_by_id(cls, search_id):
        sql = "SELECT * FROM pets WHERE id = ?"
        row = CURSOR.execute(sql, (search_id,)).fetchone()
        return Pet.new_instance_from_db(row) if row else None

    @classmethod
    def find_or_create_by(cls, name, species, breed, temperament, owner_id):
        find_sql = """
            SELECT * FROM pets
            WHERE (name, species, breed, temperament, owner_id) = (?, ?, ?, ?, ?)"""
        found_row = CURSOR.execute(find_sql, (name, species, breed, temperament, owner_id)).fetchone()
        if found_row:
            return Pet.new_instance_from_db(found_row)
        else:
            new_pet = Pet.create(name, species, breed, temperament, owner_id)
            return new_pet

    def update(self, name, species, breed, temperament, owner_id):
        sql = """
            UPDATE pets
            SET name = ?,
                species = ?,
                breed = ?,
                temperament = ?,
                owner_id = ?
            WHERE id = ?"""
        parameters = (
            name if name else self.name, 
            species if species else self.species, 
            breed if breed else self.breed, 
            temperament if temperament else self.temperament, 
            owner_id if owner_id else self.owner_id, 
            self.id)
        CURSOR.execute(sql, parameters)
        CONN.commit()

    def delete_from_db(self):
        sql = "DELETE FROM pets WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    def owner(self):  
        from owner import Owner
        sql = 'SELECT * FROM owners WHERE owners.id = ?'
        my_owner = CURSOR.execute(sql, (self.owner_id,)).fetchone()
        return Owner.new_instance_from_db(my_owner)
