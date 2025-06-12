# Job Application API

A Django REST Framework API for job posting and application management with JWT authentication.

## Features

- 🔐 User authentication with JWT tokens
- 👥 Custom user model with education levels
- 📝 Job posting management
- 📋 Application system with file uploads
- 📊 Status tracking for applications
- 📖 Interactive API documentation
- 🐳 Docker containerization with PostgreSQL

## Quick Start with Docker 

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd "DRF Test"
   ```

2. Run with Docker Compose:
   ```bash
   docker-compose up --build
   ```

3. Create superuser (in a new terminal):
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

4. Visit the API:
   - **API Root**: http://localhost:8000/api/
   - **Swagger UI**: http://localhost:8000/api/schema/swagger-ui/
   - **Admin Panel**: http://localhost:8000/admin/

## Manual Setup 

<details>
<summary>Click to expand manual setup instructions</summary>

1. Create virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create `.env` file:
   ```env
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   DATABASE_URL=sqlite:///db.sqlite3
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. Start development server:
   ```bash
   python manage.py runserver
   ```

</details>

## API Documentation

Once running, visit:
- **Swagger UI**: `/api/schema/swagger-ui/`
- **ReDoc**: `/api/schema/redoc/`
- **Schema**: `/api/schema/`

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
- Django REST Framework 3.16.0
- JWT Authentication (djangorestframework-simplejwt)
- PostgreSQL (Docker) / SQLite (Manual)
- drf-spectacular (API docs)
- Docker & Docker Compose

## Development

### Using Docker
```bash
# Start services
docker-compose up

# Run migrations
docker-compose exec web python manage.py migrate

# Create superuser
docker-compose exec web python manage.py createsuperuser

# View logs
docker-compose logs web

# Stop services
docker-compose down
```

### Environment Variables
Create a `.env` file with:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0
DATABASE_URL=postgres://postgres:postgres@db:5432/jobapp
```