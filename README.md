# OTT Platform

A modern, scalable Over-The-Top (OTT) video streaming platform built with microservices architecture. This platform provides video streaming, user management, subscriptions, and content management capabilities.

## Features

- **Video Streaming**: Adaptive bitrate streaming with HLS/DASH support
- **User Management**: Authentication, profiles, and role-based access
- **Subscription System**: Flexible subscription plans and payment integration
- **Content Management**: Video upload, encoding, and metadata management
- **Analytics**: Viewing analytics and user engagement metrics
- **Responsive UI**: Modern web interface built with Next.js
- **API-First**: RESTful API with comprehensive documentation
- **Docker Support**: Containerized deployment with Docker Compose
- **CI/CD Ready**: GitHub Actions workflow for automated deployment

## Tech Stack

### Backend
- **Framework**: FastAPI (Python)
- **Database**: PostgreSQL
- **Authentication**: JWT tokens
- **ORM**: SQLAlchemy
- **Background Tasks**: Celery for video encoding

### Frontend
- **Framework**: Next.js with TypeScript
- **Styling**: Tailwind CSS
- **State Management**: Zustand
- **Video Player**: Custom video player component

### Infrastructure
- **Reverse Proxy**: Nginx
- **Containerization**: Docker & Docker Compose
- **CI/CD**: GitHub Actions
- **Monitoring**: (To be implemented)

## Project Structure

```
ott-platform/
├── backend/                 # FastAPI backend application
│   ├── app/                # Main application code
│   │   ├── api/           # API routes
│   │   ├── core/          # Core functionality
│   │   ├── db/            # Database models and sessions
│   │   ├── models/        # SQLAlchemy models
│   │   ├── schemas/       # Pydantic schemas
│   │   ├── services/      # Business logic services
│   │   └── utils/         # Utility functions
│   ├── Dockerfile         # Backend Docker configuration
│   └── requirements.txt   # Python dependencies
├── frontend/               # Next.js frontend application
│   ├── src/               # Source code
│   │   ├── app/          # Next.js app router
│   │   ├── components/   # React components
│   │   ├── hooks/        # Custom React hooks
│   │   ├── services/     # API service functions
│   │   ├── store/        # State management
│   │   ├── types/        # TypeScript type definitions
│   │   └── utils/        # Utility functions
│   ├── public/           # Static assets
│   └── package.json      # Node.js dependencies
├── infra/                 # Infrastructure configuration
│   ├── nginx/            # Nginx configuration
│   ├── docker/           # Dockerfiles for services
│   └── ci-cd/            # CI/CD pipelines
├── docs/                  # Documentation
│   ├── api.md            # API documentation
│   ├── architecture.md   # System architecture
│   ├── streaming.md      # Streaming documentation
│   └── deployment.md     # Deployment guide
├── docker-compose.yml     # Docker Compose configuration
└── README.md             # This file
```

## Quick Start

### Prerequisites
- Docker and Docker Compose
- Git
- Node.js 18+ (for local frontend development)
- Python 3.11+ (for local backend development)

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Gitmb56/ott-platform.git
   cd ott-platform
   ```

2. **Start the services**
   ```bash
   docker-compose up -d
   ```

3. **Access the application**
   - Frontend: http://localhost
   - Backend API: http://localhost/api
   - API Documentation: http://localhost/api/docs (Swagger UI)

### Manual Setup (Alternative)

#### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

#### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

## API Documentation

The API documentation is available at `/api/docs` when the backend is running, or refer to [docs/api.md](docs/api.md) for detailed endpoint information.

### Key Endpoints
- `POST /api/v1/auth/login` - User authentication
- `GET /api/v1/videos` - List available videos
- `GET /api/v1/streaming/{videoId}/manifest` - Get streaming manifest
- `GET /api/v1/subscriptions` - User subscriptions

## Environment Variables

### Backend (.env)
```env
DATABASE_URL=postgresql://user:password@localhost/ott_platform
SECRET_KEY=your-secret-key-here
CORS_ORIGINS=http://localhost:3000
REDIS_URL=redis://localhost:6379
```

### Frontend (.env.local)
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_CDN_URL=http://localhost:8000/static
```

## Development

### Running Tests
```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test
```

### Code Quality
```bash
# Backend linting
cd backend
flake8
black .

# Frontend linting
cd frontend
npm run lint
```

## Deployment

For production deployment instructions, see [docs/deployment.md](docs/deployment.md).

### Docker Deployment
```bash
docker-compose -f docker-compose.prod.yml up -d
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 for Python code
- Use TypeScript for all frontend code
- Write tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support, email support@ott-platform.com or create an issue in this repository.

## Roadmap

- [ ] Mobile app development
- [ ] Advanced analytics dashboard
- [ ] Multi-language support
- [ ] Social features (comments, ratings)
- [ ] Offline viewing capabilities
- [ ] Integration with popular payment gateways
- [ ] Content recommendation engine

---

Built with ❤️ for modern video streaming experiences.