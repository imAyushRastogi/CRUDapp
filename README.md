# CRUDapp README
## Overview
CRUDapp is a RESTful API built with Django that provides basic CRUD (Create, Read, Update, Delete) operations for users, products, and tasks.

## API Endpoints
### Users
#### GET /api/users/
Retrieve a list of all users
* Response: JSON array of user objects
* Example: `[{"id": 1, "name": "John Doe", "email": "johndoe@example.com"}, ...]`

#### GET /api/users/:id
Retrieve a single user by ID
* Response: JSON user object
* Example: `{"id": 1, "name": "John Doe", "email": "johndoe@example.com"}`

#### POST /api/users/
Create a new user
* Request: JSON user object
* Example: `{"name": "Jane Doe", "email": "janedoe@example.com"}`
* Response: JSON user object with ID
* Example: `{"id": 2, "name": "Jane Doe", "email": "janedoe@example.com"}`

#### PUT /api/users/:id
Update an existing user
* Request: JSON user object
* Example: `{"name": "Jane Doe", "email": "janedoe@example.com"}`
* Response: JSON user object with updated fields
* Example: `{"id": 2, "name": "Jane Doe", "email": "janedoe@example.com"}`

#### DELETE /api/users/:id
Delete a user
* Response: 204 No Content

### Products
#### GET /api/products/
Retrieve a list of all products
* Response: JSON array of product objects
* Example: `[{"id": 1, "name": "Product 1", "price": 10.99}, ...]`

#### GET /api/products/:id
Retrieve a single product by ID
* Response: JSON product object
* Example: `{"id": 1, "name": "Product 1", "price": 10.99}`

#### POST /api/products/
Create a new product
* Request: JSON product object
* Example: `{"name": "Product 2", "price": 9.99}`
* Response: JSON product object with ID
* Example: `{"id": 2, "name": "Product 2", "price": 9.99}`

#### PUT /api/products/:id
Update an existing product
* Request: JSON product object
* Example: `{"name": "Product 2", "price": 9.99}`
* Response: JSON product object with updated fields
* Example: `{"id": 2, "name": "Product 2", "price": 9.99}`

#### DELETE /api/products/:id
Delete a product
* Response: 204 No Content

### Tasks
#### GET /api/tasks/
Retrieve a list of all tasks
* Response: JSON array of task objects
* Example: `[{"id": 1, "title": "Task 1", "description": "This is task 1"}, ...]`

#### GET /api/tasks/:id
Retrieve a single task by ID
* Response: JSON task object
* Example: `{"id": 1, "title": "Task 1", "description": "This is task 1"}`

#### POST /api/tasks/
Create a new task
* Request: JSON task object
* Example: `{"title": "Task 2", "description": "This is task 2"}`
* Response: JSON task object with ID
* Example: `{"id": 2, "title": "Task 2", "description": "This is task 2"}`

#### PUT /api/tasks/:id
Update an existing task
* Request: JSON task object
* Example: `{"title": "Task 2", "description": "This is task 2"}`
* Response: JSON task object with updated fields
* Example: `{"id": 2, "title": "Task 2", "description": "This is task 2"}`

#### DELETE /api/tasks/:id
Delete a task
* Response: 204 No Content

## Authentication
CRUDapp uses token-based authentication. To authenticate, send a POST request to `/api/token/` with your username and password.

### POST /api/token/
Obtain an authentication token
* Request: JSON object with username and password fields
* Example: `{"username": "johndoe", "password": "password123"}`
* Response: JSON object with token field
* Example: `{"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IkpvaGFuIjoiMjMwfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"}`

### Authorization Header
Include the obtained token in the Authorization header for subsequent requests
* Example: `Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IkpvaGFuIjoiMjMwfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c`

## Deployment
### Local Development
1. Clone the repository: `git clone https://github.com/your-username/CRUDapp.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start the development server: `python manage.py runserver`
5. Access the API at `http://localhost:8000/api/`

### Production Deployment
1. Create a virtual environment: `python -m venv env`
2. Activate the virtual environment: `source env/bin/activate` (on Linux/macOS) or `env\Scripts\activate` (on Windows)
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Collect static files: `python manage.py collectstatic`
6. Deploy to your preferred platform (e.g., Heroku, AWS, Google Cloud)

## Troubleshooting
* Check the Django debug logs for errors: `python manage.py runserver --verbosity 2`
* Verify that the database is properly configured and migrated
* Ensure that the authentication token is properly included in the Authorization header for requests
