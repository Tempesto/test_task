# API Test Project

## Description
This project contains automated API tests using Python and Docker.

## Prerequisites
- Docker
- Python 3.13 (for local run)
- pip (for local run)

## Environment Setup

1. Create `.env` file in the project root:
```bash
cp dotenv .env
```

2. Edit the `.env` file by adding required variables:
```env
BASE_URL=<your_base_url>
TOKEN=<your_auth_token>
```

**Important:** 
- The `.env` file is required for tests to work
- Don't commit `.env` file to repository (it's already added to .gitignore)
- Make sure variable values match your test environment

## Installation and Running

### Option 1: Using Docker (recommended)

1. Clone the repository:
```bash
git clone https://github.com/Tempesto/test_task.git
cd test_task
```

2. Build Docker container:
```bash
docker build -t api-tests .
```

3. Run tests via Docker:
```bash
docker run --rm -v $(pwd)/logs_docker:/app/logs_docker -v $(pwd)/reports_docker:/app/reports_docker api-tests
```

**Docker commands explanation:**
- `docker build -t api-tests .` - creates Docker image with "api-tests" tag
- `docker run` - runs the container
- `--rm` - automatically removes container after completion
- `-v $(pwd)/logs_docker:/app/logs_docker` - mounts local directory for logs
- `-v $(pwd)/reports_docker:/app/reports_docker` - mounts local directory for reports

**Important:** Make sure that:
- Docker is installed and running on your system
- You have permissions to create and run containers
- `logs_docker` and `reports_docker` directories have appropriate access rights

### Option 2: Local Run

1. Clone the repository:
```bash
git clone https://github.com/Tempesto/test_task.git
cd test_task
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # for Linux/Mac
# or
venv\Scripts\activate  # for Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run tests:
```bash
pytest tests/
```

## Project Structure
- `api/` - API clients and helper functions
- `fixtures/` - test fixtures
- `logs/` - directory for request and response logs
- `reports/` - directory for reports
- `tests/` - test files
- `config.py` - configuration file
- `conftest.py` - pytest configuration
- `Dockerfile` - file for creating Docker container

## Logging

### Local Logs
The `logs/` directory stores detailed logs for local test runs:
- Outgoing requests:
  - HTTP method
  - URL
  - Headers
  - Request body (if any)
- Incoming responses:
  - Status code
  - Response headers
  - Response body
  - Request execution time

### Docker Logs
When running tests in container, logs are stored in `logs_docker/` directory. This directory is automatically created thanks to volume configuration in Docker run command:
```bash
docker run --rm -v $(pwd)/logs_docker:/app/logs_docker -v $(pwd)/reports_docker:/app/reports_docker api-tests
```

The structure and format of logs are identical to local ones but stored in a separate directory for convenient environment separation.

### Log File Format:
```txt
[TIMESTAMP] REQUEST: POST /api/endpoint
Headers: {...}
Body: {...}

[TIMESTAMP] RESPONSE: 200 OK
Headers: {...}
Body: {...}
Execution time: 0.234s
```

Logs help with:
- Test debugging
- Error analysis
- Verification of requests and responses

**Note:** When using Docker, ensure the `logs_docker` directory has appropriate write permissions.

## Reports
After test execution, reports will be available in:
- `reports_docker/` (when running via Docker)
- `reports/` (when running locally)
