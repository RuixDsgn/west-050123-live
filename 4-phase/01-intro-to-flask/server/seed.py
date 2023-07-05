#!/usr/bin/env python3
# 📚 Review With Students:
    # Seeding 
# 5. ✅ Imports
    # app from app
    # db and Production from models
from app import app
from models import db, Production

# 7. ✅ Create application context `with app.app_context():`
    # Info on application context: https://flask.palletsprojects.com/en/1.1.x/appcontext/
with app.app_context():

# 8.✅ Create a query to delete all existing records from Production    
    print("Deleting Tables...")
    # In ORMland
    # Create a classmethod that drops the table or deletes all rows
    # Production.drop_table() or Production.delete_all() ish
    # sql = "DROP TABLE ", CURSOR.execute(sql)
    Production.query.delete()

# 9.✅ Create some seeds for production and commit them to the database. 

    # In ORMLand, how to create an entry to the db?
    # .save or .create
    # sql = "INSERT INTO table, values", CURSOR.execute(sql, params), CONN.commit()
    productions = []

    p1 = Production(title="Hamilton", genre="Historical Rap", budget=4.0, image="image1.png", director="Lin Manuel Miranda", description="Hamiltion", ongoing=True, runtime=180)
    productions.append(p1)
    # db.session.add(p1)
    
    p2 = Production(title="MacBeth", genre="Old", budget=4.0, image="image2.png", director="Shakespeare", description="lady", ongoing=False, runtime=120)
    # db.session.add(p2)
    productions.append(p2)
    
    p3 = Production(title="Cats", genre="Cat", budget=4.0, image="image3.png", director="Andrew Lloyd Weber", description="Cat", ongoing=False, runtime=120)
    productions.append(p3)

    db.session.add_all([p1,p2,p3])
    # db.session.add_all(productions)

    db.session.commit()

    print("Productions Seeded..")
    for p in productions:
        print(f'{p.id}: {p.title}')

# 10.✅ Run in terminal:
    # `python seed.py`
# 11.✅ run `flask shell` in the terminal 
    # from app import app
    # from models import Production
    # Check the seeds by querying Production
# 12.✅ Navigate back to app.py  
    
    