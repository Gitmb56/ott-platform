# Testing Guide

This guide explains how to test the OTT Platform application.

## Prerequisites

- Docker and Docker Compose installed
- Python 3.11+ (for API testing script)
- Node.js 18+ (for frontend testing script)

## Quick Test

### 1. Start the Application

```bash
# Start all services
docker-compose up -d

# Wait for services to be ready (about 30-60 seconds)
```

### 2. Run Automated Tests

```bash
# Test the API endpoints
python scripts/test_api.py

# Test the frontend
node scripts/test_frontend.js
```

### 3. Manual Testing

#### Backend API Testing
- **API Documentation**: http://localhost:8000/api/docs (Swagger UI)
- **Health Check**: http://localhost:8000/health
- **API Base**: http://localhost:8000/api/v1

#### Frontend Testing
- **Application**: http://localhost:3000
- **Test user registration and login**
- **Test video browsing (if videos exist)**

## Detailed Testing

### Backend Unit Tests

```bash
# Run pytest
cd backend
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/test_api.py
```

### Frontend Tests

```bash
# Run Next.js tests (when implemented)
cd frontend
npm test

# Run linting
npm run lint
```

### Integration Tests

```bash
# Test with different browsers
# Test API endpoints with tools like Postman/Insomnia
# Test video streaming functionality
```

## Test Coverage

### Backend Tests
- API endpoint responses
- Authentication and authorization
- Database operations
- Business logic validation

### Frontend Tests
- Component rendering
- User interactions
- API integration
- Error handling

## Manual Test Checklist

### User Registration & Authentication
- [ ] Register new user
- [ ] Login with valid credentials
- [ ] Login with invalid credentials
- [ ] Password reset (if implemented)
- [ ] JWT token validation

### Video Management
- [ ] List videos
- [ ] View video details
- [ ] Video streaming (if content exists)
- [ ] Search videos (if implemented)

### User Profile
- [ ] View profile
- [ ] Update profile
- [ ] Change password

### Subscriptions
- [ ] View subscriptions
- [ ] Create subscription
- [ ] Cancel subscription

### Admin Features (if implemented)
- [ ] Upload videos
- [ ] Manage users
- [ ] View analytics

## Troubleshooting

### Services Not Starting
```bash
# Check container logs
docker-compose logs

# Check specific service
docker-compose logs backend
docker-compose logs frontend
docker-compose logs db
```

### API Tests Failing
- Ensure backend is running: `docker-compose ps`
- Check backend logs: `docker-compose logs backend`
- Verify database connection

### Frontend Tests Failing
- Ensure frontend is running: `docker-compose ps`
- Check frontend logs: `docker-compose logs frontend`
- Verify API connectivity

### Database Issues
```bash
# Reset database
docker-compose down -v
docker-compose up -d db
```

## Performance Testing

### Load Testing
```bash
# Use tools like Apache Bench or JMeter
ab -n 1000 -c 10 http://localhost:8000/health

# API load testing
ab -n 500 -c 5 -T 'application/json' -p payload.json http://localhost:8000/api/v1/auth/login
```

### Memory and CPU Monitoring
```bash
# Monitor containers
docker stats

# Check specific container
docker stats ott-platform-backend-1
```

## Continuous Integration

The project includes GitHub Actions for automated testing:

```yaml
# .github/workflows/ci.yml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Test Backend
        run: |
          cd backend
          pip install -r requirements.txt
          pytest
      - name: Test Frontend
        run: |
          cd frontend
          npm install
          npm run build
```

## Adding New Tests

### Backend Tests
```python
# backend/tests/test_new_feature.py
def test_new_feature():
    response = client.get("/api/v1/new-feature")
    assert response.status_code == 200
```

### Frontend Tests
```javascript
// frontend/__tests__/Component.test.js
import { render, screen } from '@testing-library/react'
import Component from '../components/Component'

test('renders component', () => {
  render(<Component />)
  expect(screen.getByText('Hello')).toBeInTheDocument()
})
```

## Test Data

For testing, you may need to create sample data:

```sql
-- Sample users
INSERT INTO users (email, password_hash, full_name) VALUES
('test@example.com', '$2b$12$...', 'Test User');

-- Sample videos
INSERT INTO videos (title, description, url) VALUES
('Sample Video', 'A test video', '/videos/sample.mp4');
```