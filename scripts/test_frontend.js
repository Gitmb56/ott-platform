#!/usr/bin/env node

/**
 * OTT Platform Frontend Testing Script
 * Tests basic functionality of the frontend application
 */

const http = require('http');

const FRONTEND_URL = 'http://localhost:3000';

function testFrontendAccess() {
    return new Promise((resolve) => {
        console.log('🔍 Testing frontend access...');

        const url = new URL(FRONTEND_URL);
        const options = {
            hostname: url.hostname,
            port: url.port,
            path: '/',
            method: 'GET'
        };

        const req = http.request(options, (res) => {
            console.log(`📊 Frontend response: ${res.statusCode}`);

            if (res.statusCode === 200) {
                console.log('✅ Frontend accessible');
                resolve(true);
            } else {
                console.log(`❌ Frontend failed: ${res.statusCode}`);
                resolve(false);
            }
        });

        req.on('error', (e) => {
            console.log(`❌ Frontend error: ${e.message}`);
            resolve(false);
        });

        req.setTimeout(5000, () => {
            console.log('❌ Frontend request timeout');
            req.destroy();
            resolve(false);
        });

        req.end();
    });
}

function testAPIAccess() {
    return new Promise((resolve) => {
        console.log('🔍 Testing API access from frontend...');

        const url = new URL('http://localhost:8000');
        const options = {
            hostname: url.hostname,
            port: url.port,
            path: '/health',
            method: 'GET'
        };

        const req = http.request(options, (res) => {
            console.log(`📊 API response: ${res.statusCode}`);

            if (res.statusCode === 200) {
                console.log('✅ API accessible from frontend');
                resolve(true);
            } else {
                console.log(`❌ API access failed: ${res.statusCode}`);
                resolve(false);
            }
        });

        req.on('error', (e) => {
            console.log(`❌ API access error: ${e.message}`);
            resolve(false);
        });

        req.setTimeout(5000, () => {
            console.log('❌ API request timeout');
            req.destroy();
            resolve(false);
        });

        req.end();
    });
}

async function waitForServices(timeout = 60) {
    console.log(`⏳ Waiting up to ${timeout} seconds for services to start...`);

    const startTime = Date.now();

    while (Date.now() - startTime < timeout * 1000) {
        try {
            const response = await testFrontendAccess();
            if (response) {
                console.log('✅ Services are ready!');
                return true;
            }
        } catch (e) {
            // Continue waiting
        }

        await new Promise(resolve => setTimeout(resolve, 2000));
        process.stdout.write('.');
    }

    console.log('\n❌ Services failed to start within timeout');
    return false;
}

async function main() {
    console.log('🚀 OTT Platform Frontend Testing Script');
    console.log('=' .repeat(40));

    // Wait for services to be ready
    if (!(await waitForServices())) {
        console.log('❌ Cannot proceed with tests - services not ready');
        process.exit(1);
    }

    console.log('\n🧪 Starting frontend tests...\n');

    const tests = [
        testFrontendAccess,
        testAPIAccess
    ];

    let passed = 0;
    const total = tests.length;

    for (const test of tests) {
        const result = await test();
        if (result) passed++;
        console.log();
    }

    console.log('=' .repeat(40));
    console.log(`📊 Test Results: ${passed}/${total} tests passed`);

    if (passed === total) {
        console.log('🎉 All frontend tests passed!');
    } else {
        console.log('⚠️  Some frontend tests failed.');
    }

    console.log('\n💡 Next steps:');
    console.log('1. Open http://localhost:3000 in your browser');
    console.log('2. Try registering a new account');
    console.log('3. Try logging in');
    console.log('4. Check browser developer tools for any errors');
}

main().catch(console.error);