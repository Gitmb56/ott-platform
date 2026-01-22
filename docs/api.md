# API Documentation

## Overview
This document describes the API endpoints for the OTT Platform.

## Authentication
All API requests require authentication via JWT tokens.

### Endpoints

#### User Management
- `POST /api/v1/auth/login` - User login
- `POST /api/v1/auth/register` - User registration
- `GET /api/v1/users/profile` - Get user profile
- `PUT /api/v1/users/profile` - Update user profile

#### Video Management
- `GET /api/v1/videos` - List videos
- `GET /api/v1/videos/{id}` - Get video details
- `POST /api/v1/videos` - Upload video (admin only)
- `PUT /api/v1/videos/{id}` - Update video (admin only)
- `DELETE /api/v1/videos/{id}` - Delete video (admin only)

#### Streaming
- `GET /api/v1/streaming/{videoId}/manifest` - Get streaming manifest
- `POST /api/v1/streaming/{videoId}/start` - Start streaming session

#### Subscriptions
- `GET /api/v1/subscriptions` - Get user subscriptions
- `POST /api/v1/subscriptions` - Create subscription
- `PUT /api/v1/subscriptions/{id}` - Update subscription
- `DELETE /api/v1/subscriptions/{id}` - Cancel subscription

## Error Responses
- `400 Bad Request` - Invalid request data
- `401 Unauthorized` - Authentication required
- `403 Forbidden` - Insufficient permissions
- `404 Not Found` - Resource not found
- `500 Internal Server Error` - Server error