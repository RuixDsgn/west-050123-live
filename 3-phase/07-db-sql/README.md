## 4. SQL & Databases
### SWBAT

- [ ] Explain why we use databases
- [ ] Explain what SQL is and why we use it
- [ ] Explain the difference between a database, server, and API
- [ ] Explain the difference between rows and columns in a table
- [ ] Explain the difference between a foreign key and primary key
- [ ] Explain what a join table is
- [ ] Explain what it means to seed a database
- [ ] Observe using SQL to communicate with a database
- [ ] Explain what an ORM is and why we use Active Record


# Intro to Databases

## Putting Things in Context.

Databases allow us to store and perform CRUD actions on data outside of our code before allowing our changes persist to the next session.

## ORM Analogy

![ORM Analogy](https://res.cloudinary.com/dnocv6uwb/image/upload/v1651161995/Flatiron%20Slideshow%20images/analogy.drawio.svg)

## Where We're Headed

![The Pattern](https://raw.githubusercontent.com/learn-co-students/phase3-lecture-repo-template/04_begin_intro_to_databases/04_intro_to_databases/demo/object-method-sql-query-return.drawio.svg?token=GHSAT0AAAAAABS54V3M5DXF4WXV6T3OUTPUYTJ6M6A)


## The Flow

At the end of the phase, we'll be building out an API that will sit between our React app and our database:

- React App
- Fetch to API
- API interacts with database and sends response back to Browser
- Resolved promise from fetch leads to change in state
- React updates the DOM

### Key Features:

- Add persistence
  - A Read (SELECT) operation to retrieve persisted pets
  - A Create (INSERT INTO) operation to persist new pets
  - An Update (UPDATE) operation to update a persisted pet
  - An Delete (DELETE) operation to delete a persisted pet

Install [DB Browser for SQLite](https://sqlitebrowser.org/)

WSL [Using SQLite with VS Code Extension](https://www.youtube.com/watch?v=bKixKfb1J1o)
  - Right click DB and select "Open database"
  - In SQLite Explorer, right click the Database and select "New query"
  - Write the query, highlight the query, click right and select "Run query"


