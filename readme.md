# Job Application API

A Django REST Framework API for job posting and application management with JWT authentication.

## Features

- 🔐 User authentication with JWT tokens
- 👥 Custom user model with education levels
- 📝 Job posting management
- 📋 Application system with file uploads
- 📊 Status tracking for applications
- 📖 Interactive API documentation

## API Documentation

Once running, visit:
- **Swagger UI**: `/api/docs/`
- **ReDoc**: `/api/redoc/`
- **Schema**: `/api/schema/`

## Setup

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd "DRF Test"
   ```

2. Create virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create `.env` file:
   ```env
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. Start development server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Authentication
- `POST /api/auth/register/` - Register new user
- `POST /api/auth/login/` - User login
- `POST /api/auth/logout/` - User logout
- `POST /api/auth/token/refresh/` - Refresh JWT token

### User Profile
- `GET /api/accounts/profile/` - Get user profile
- `PATCH /api/accounts/profile/` - Update user profile

### Job Posts
- `GET /api/posts/` - List all active job posts
- `POST /api/posts/create/` - Create new job post
- `GET /api/posts/<id>/` - Get job post details
- `GET /api/posts/my-posts/` - Get my job posts
- `PATCH /api/posts/update/<id>/` - Update my job post

### Applications
- `POST /api/posts/<id>/apply/` - Apply to job post
- `GET /api/posts/my-applications/` - Get my applications
- `GET /api/posts/<id>/applications/` - Get applications for my post
- `PATCH /api/posts/applications/<id>/status/` - Update application status

## Models

- **CustomUser**: Extended user with education levels
- **Post**: Job postings with requirements
- **Application**: Job applications with file uploads

## Technology Stack

- Django 5.2.2
- Django REST Framework 3.15.2
- JWT Authentication
- SQLite/PostgreSQL
- drf-spectacular (API docs)