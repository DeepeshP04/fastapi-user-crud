## FastAPI CRUD with Neon PostgreSQL

This project is a CRUD (Create, Read, Update, Delete) application built with FastAPI and PostgreSQL. The application performs CRUD operations on a User resource and uses asyncpg for asynchronous database interaction. The database is hosted on Neon Serverless Postgres.

### Features

* CRUD Operations: Create, Read, Update, and Delete user records.

* Asynchronous Database Queries: asyncpg for async database connections and queries.

* FastAPI: RESTful API framework for creating API endpoints.

* Pydantic Validation: Data validation using Pydantic models.

### Setup

1. Clone the repository 

Clone the repository to your local machine:
git clone https://github.com/DeepeshP04/fastapi-user-crud.git

2. Create and activate virtual environment

python -m venv venv 
venv/Scripts/activate

3. Install dependencies

pip install -r requirements.txt

4. Setup the database

Create a .env file in the project root and add your database credentials: 
DATABASE_URL=postgresql://[user]:[password]@[neon_hostname]/[dbname]?sslmode=require (if using neon serveless postgres) 
DATABASE_URL=postgresql://username:password@hostname:port/database_name

5. Run the application

To run the FastAPI server, use uvicorn: 
uvicorn app.main:app --reload 

This will start the application on http://127.0.0.1:8000.

6. Test the API with Postman 

* GET /users: Returns a list of all users.

* GET /users/{id}: Returns a user with the specified ID.

* POST /users: Creates a new user.

* PUT /users/{id}: Updates a user with the specified ID.

* DELETE /users/{id}: Deletes a user with the specified ID.

You can also test these apis on http://127.0.0.1:8000/docs.