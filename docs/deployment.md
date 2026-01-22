# Deployment Guide

## Prerequisites
- Docker and Docker Compose installed
- Git repository access
- Domain name (optional)
- SSL certificate (optional)

## Local Development
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ott-platform
   ```

2. Start services using Docker Compose:
   ```bash
   docker-compose up -d
   ```

3. Access the application:
   - Frontend: http://localhost
   - Backend API: http://localhost/api
   - Admin panel: http://localhost/admin

## Production Deployment

### Using Docker Compose
1. Update environment variables in `docker-compose.yml`
2. Configure domain and SSL certificates
3. Run production build:
   ```bash
   docker-compose -f docker-compose.prod.yml up -d
   ```

### Manual Deployment
1. Build Docker images:
   ```bash
   # Backend
   docker build -f infra/docker/backend.Dockerfile -t ott-backend ./backend

   # Frontend
   docker build -f infra/docker/frontend.Dockerfile -t ott-frontend ./frontend

   # Nginx
   docker build -t ott-nginx ./infra/nginx
   ```

2. Push images to registry:
   ```bash
   docker tag ott-backend <registry>/ott-backend:latest
   docker push <registry>/ott-backend:latest
   # Repeat for other images
   ```

3. Deploy using orchestration tool (Kubernetes, Docker Swarm, etc.)

## Environment Variables
Configure the following environment variables:

### Backend
- `DATABASE_URL`: PostgreSQL connection string
- `SECRET_KEY`: JWT secret key
- `CORS_ORIGINS`: Allowed CORS origins
- `REDIS_URL`: Redis connection for caching

### Frontend
- `NEXT_PUBLIC_API_URL`: Backend API URL
- `NEXT_PUBLIC_CDN_URL`: CDN base URL for videos

## Database Setup
1. Create PostgreSQL database
2. Run migrations:
   ```bash
   docker-compose exec backend alembic upgrade head
   ```

## SSL Configuration
1. Obtain SSL certificate (Let's Encrypt recommended)
2. Configure Nginx for HTTPS
3. Update DNS records

## Monitoring
- Set up logging aggregation (ELK stack)
- Configure monitoring (Prometheus + Grafana)
- Set up alerts for critical metrics

## Backup Strategy
- Database backups: Daily automated backups
- Video files: Replicated storage with versioning
- Configuration: Version controlled in Git

## Scaling
- Horizontal scaling for backend services
- CDN for video content delivery
- Database read replicas for high traffic
- Load balancer for multiple instances

## Troubleshooting
- Check container logs: `docker-compose logs`
- Verify network connectivity between services
- Monitor resource usage
- Check database connections