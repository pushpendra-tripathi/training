## Week 4 · Day 4 — HTTP/REST + Python requests

### Problem Definition (Answer BEFORE starting)
**What exactly are you building today?**  
A robust API client with error handling, retry logic, and rate limiting, plus a static web page rendering API data.

**Why does this matter for Django?**  
Django often consumes external APIs and provides REST APIs. Understanding HTTP, requests, and error handling prepares you for building Django views that interact with third-party services.

**What does success look like?**  
- API client with comprehensive error handling (network, HTTP)
- Retry logic with exponential backoff
- Static page rendering API data with loading/error states

---

### Objectives
- Understand HTTP fundamentals and REST principles
- Master Python `requests` library
- Build robust API clients with error handling

### Tasks
1) HTTP Fundamentals
   - Methods: GET, POST, PUT, PATCH, DELETE
   - Status codes: 2xx (success), 3xx (redirect), 4xx (client error), 5xx (server error)
   - Headers: Content-Type, Authorization, User-Agent
   - Request/Response cycle

2) REST Principles
   - Resources and URIs
   - Stateless communication
   - HTTP verbs for CRUD operations
   - JSON as data format

3) Python `requests` Library
   - GET requests: fetch data
   - POST requests: send data
   - Query parameters and request headers
   - Response: status_code, headers, json(), text
   - Session objects for persistent parameters

4) Error Handling
   - Network errors: Timeout, ConnectionError
   - HTTP errors: response.raise_for_status()
   - Retry logic with exponential backoff
   - Rate limiting

5) Authentication
   - Basic auth
   - Token/Bearer authentication
   - API keys in headers

6) Hands-on
   - Build API client for public API (e.g., GitHub, OpenWeather, JSONPlaceholder)
   - Features:
     - Fetch data with GET
     - Handle pagination
     - Error handling and retries
     - Rate limit awareness
   - Create simple static page rendering API data (reuse week02 web basics)
   - Mock API responses in tests

7) Problem solving
   - Consume public API and transform data
   - Error handling for network failures
   - Retry logic with backoff

### Outcomes
- Build robust API clients
- Handle network errors gracefully
- Understand REST API design

### Deliverables
- API client module (`api_client.py`):
  - Fetch data from public API
  - Handle errors (network, HTTP)
  - Retry logic with exponential backoff
  - Rate limiting awareness
  - Session for efficiency
  - Comprehensive tests (using `responses` library for mocking)
- Static web page:
  - Renders API data with JavaScript
  - Shows loading/error states
  - Uses provided `frontend_template/`
- Example usage and output

### Submission checklist
- [ ] API client working with public API
- [ ] Error handling comprehensive
- [ ] Retry logic implemented
- [ ] Tests with mocked API responses
- [ ] Static page renders API data
- [ ] Code passes `black .`, `isort .`, `pylint **/*.py`
- [ ] **Daily reflection completed** (see [DAILY_TEMPLATE.md](../../DAILY_TEMPLATE.md)):
  - [ ] Problem definition answered before coding
  - [ ] Can explain why today's work matters for Django
  - [ ] Documented patterns learned and when to apply them


