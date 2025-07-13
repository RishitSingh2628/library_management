# Library Management System

A RESTful API for managing library operations built with Django REST Framework.

## Features

- Book management (CRUD operations)
- Member management
- Book issue/return transactions
- Automatic inventory tracking
- Data validation


## Setup Instructions

### Prerequisites
- Python 3.8+
- PostgreSQL
- Docker (optional)

### Installation

1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate virtual environment: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Set up environment variables in `.env`
6. Run migrations: `python manage.py migrate`
7. Create superuser: `python manage.py createsuperuser`
8. Run server: `python manage.py runserver`

### Docker Setup

1. Run: `docker-compose up --build`
2. Access at: http://localhost:8000

## API Endpoints

### Books
- `GET /api/books/` - List all books
- `POST /api/books/` - Create new book
- `GET /api/books/{id}/` - Get book details
- `PUT /api/books/{id}/` - Update book
- `DELETE /api/books/{id}/` - Delete book

### Members
- `GET /api/members/` - List all members
- `POST /api/members/` - Register new member
- `PUT /api/members/{id}/` - Update member
- `DELETE /api/members/{id}/` - Delete member

### Transactions
- `GET /api/transactions/` - List all transactions
- `POST /api/transactions/issue/` - Issue book
- `POST /api/transactions/return/` - Return book

