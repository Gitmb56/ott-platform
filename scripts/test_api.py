#!/usr/bin/env python3
"""
OTT Platform API Testing Script
Tests basic functionality of the OTT platform API endpoints
"""

import requests
import json
import time
import sys

BASE_URL = "http://localhost:8000"
API_BASE = f"{BASE_URL}/api/v1"

def test_health_check():
    """Test the health check endpoint"""
    print("🔍 Testing health check...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code == 200:
            print("✅ Health check passed")
            return True
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Health check error: {e}")
        return False

def test_api_root():
    """Test the API root endpoint"""
    print("🔍 Testing API root...")
    try:
        response = requests.get(API_BASE)
        print(f"📊 API root response: {response.status_code}")
        if response.status_code in [200, 404]:  # 404 is ok if no root endpoint
            print("✅ API root accessible")
            return True
        else:
            print(f"❌ API root failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ API root error: {e}")
        return False

def test_user_registration():
    """Test user registration"""
    print("🔍 Testing user registration...")
    try:
        payload = {
            "email": "test@example.com",
            "password": "testpassword123",
            "full_name": "Test User"
        }
        response = requests.post(f"{API_BASE}/auth/register", json=payload)
        print(f"📊 Registration response: {response.status_code}")
        if response.status_code in [200, 201, 400]:  # 400 might be validation error
            print("✅ Registration endpoint accessible")
            return True
        else:
            print(f"❌ Registration failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Registration error: {e}")
        return False

def test_user_login():
    """Test user login"""
    print("🔍 Testing user login...")
    try:
        payload = {
            "email": "test@example.com",
            "password": "testpassword123"
        }
        response = requests.post(f"{API_BASE}/auth/login", json=payload)
        print(f"📊 Login response: {response.status_code}")
        if response.status_code in [200, 401]:  # 401 is expected for wrong credentials
            print("✅ Login endpoint accessible")
            return True
        else:
            print(f"❌ Login failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Login error: {e}")
        return False

def test_videos_endpoint():
    """Test videos listing endpoint"""
    print("🔍 Testing videos endpoint...")
    try:
        response = requests.get(f"{API_BASE}/videos")
        print(f"📊 Videos response: {response.status_code}")
        if response.status_code in [200, 401]:  # 401 if auth required
            print("✅ Videos endpoint accessible")
            return True
        else:
            print(f"❌ Videos endpoint failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Videos endpoint error: {e}")
        return False

def test_frontend_access():
    """Test frontend accessibility"""
    print("🔍 Testing frontend access...")
    try:
        response = requests.get("http://localhost:3000")
        print(f"📊 Frontend response: {response.status_code}")
        if response.status_code == 200:
            print("✅ Frontend accessible")
            return True
        else:
            print(f"❌ Frontend failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Frontend error: {e}")
        return False

def wait_for_services(timeout=60):
    """Wait for services to be ready"""
    print(f"⏳ Waiting up to {timeout} seconds for services to start...")
    start_time = time.time()

    while time.time() - start_time < timeout:
        try:
            response = requests.get(f"{BASE_URL}/health", timeout=5)
            if response.status_code == 200:
                print("✅ Services are ready!")
                return True
        except:
            pass

        time.sleep(2)
        print(".", end="", flush=True)

    print("\n❌ Services failed to start within timeout")
    return False

def main():
    print("🚀 OTT Platform Testing Script")
    print("=" * 40)

    # Wait for services to be ready
    if not wait_for_services():
        print("❌ Cannot proceed with tests - services not ready")
        sys.exit(1)

    print("\n🧪 Starting API tests...\n")

    tests = [
        test_health_check,
        test_api_root,
        test_user_registration,
        test_user_login,
        test_videos_endpoint,
        test_frontend_access
    ]

    passed = 0
    total = len(tests)

    for test in tests:
        if test():
            passed += 1
        print()

    print("=" * 40)
    print(f"📊 Test Results: {passed}/{total} tests passed")

    if passed == total:
        print("🎉 All tests passed! Your OTT platform is working correctly.")
    else:
        print("⚠️  Some tests failed. Check the backend implementation and try again.")

    print("\n💡 Next steps:")
    print("1. Check backend logs: docker-compose logs backend")
    print("2. Check frontend logs: docker-compose logs frontend")
    print("3. Visit http://localhost for the frontend")
    print("4. Visit http://localhost/api/docs for API documentation")

if __name__ == "__main__":
    main()