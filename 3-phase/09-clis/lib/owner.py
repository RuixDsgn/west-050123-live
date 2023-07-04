from ipdb import set_trace
import sqlite3

CONN = sqlite3.connect('lib/resources.db')
CURSOR = CONN.cursor()

class Owner:
    
    def __init__(self, name, phone, email, address, id=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.id = id

    def __repr__(self):
        return str(self.__dict__)

    @classmethod
    def create_table(cls):
        create_table_sql = """
            CREATE TABLE IF NOT EXISTS owners (
                id INTEGER PRIMARY KEY,
                name TEXT,
                phone TEXT,
                email   TEXT,
                address TEXT
            )"""
        CURSOR.execute(create_table_sql)
        print("creating table...")

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS owners"
        CURSOR.execute(sql)
        print("Dropped table...")

    def save(self):
        sql = """
            INSERT INTO owners (name, phone, email, address)
            VALUES (?, ?, ?, ?)"""
        parameters = (self.name, self.phone, self.email, self.address)
        CURSOR.execute(sql, parameters)
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, phone, email, address, id=None):
        new_pet = cls(name, phone, email, address)
        new_pet.save()
        return new_pet

    @classmethod
    def new_instance_from_db(cls, row):
        return cls(
            name=row[1],
            phone=row[2],
            email=row[3],
            address=row[4],
            id=row[0],
        )

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM owners"
        response = CURSOR.execute(sql)
        all_owners_list = response.fetchall()
        return [ cls.new_instance_from_db(row) for row in all_owners_list]


    @classmethod
    def find_by_name(cls, search):
        sql = """
            SELECT * FROM owners
            WHERE name = ?"""
        response = CURSOR.execute(sql, (search,))
        row = response.fetchone()
        return cls.new_instance_from_db(row) if row else None

    @classmethod
    def find_by_id(cls, search_id):
        sql = "SELECT * FROM owners WHERE id = ?"
        row = CURSOR.execute(sql, (search_id,)).fetchone()
        return cls.new_instance_from_db(row) if row else None

    @classmethod
    def find_or_create_by(cls, name, phone, email, address):
        find_sql = """
            SELECT * FROM owners
            WHERE (name, phone, email, address) = (?, ?, ?, ?)"""
        found_row = CURSOR.execute(find_sql, (name, phone, email, address)).fetchone()
        if found_row:
            return cls.new_instance_from_db(found_row)
        else:
            new_pet = cls.create(name, phone, email, address)
            return new_pet

    def update(self, name, phone, email, address):
        sql = """
            UPDATE owners
            SET name = ?,
                species = ?,
                breed = ?,
                temperament = ?
            WHERE id = ?"""
        parameters = (name, phone, email, address, self.id)
        CURSOR.execute(sql, parameters)
        CONN.commit()

    def delete_from_db(self):
        sql = "DELETE FROM owners WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    def pets(self):
        from pet import Pet
        sql = "SELECT * from pets WHERE pets.owner_id = ?"
        my_pets = CURSOR.execute(sql, (self.id,)).fetchall()
        return [Pet.new_instance_from_db(pet) for pet in my_pets]
