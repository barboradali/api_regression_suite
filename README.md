cat << 'EOF' > README.md
# Advanced API Regression Suite with CI/CD

## Overview
This project is an automated API testing framework built with Pytest, designed to validate REST API endpoints, generate interactive HTML reports, and run automatically through a Continuous Integration/Continuous Delivery (CI/CD) pipeline using GitHub Actions. It includes positive and negative API tests, a data-driven approach using JSON test cases, advanced test outcomes (pass, fail, skip, xfail, xpass, error, rerun), schema validation using JSON Schema, response time checks, automatic HTML report generation, and CI/CD pipeline integration with GitHub Actions. The current demonstration uses the OpenWeather API, but the framework is adaptable to any REST API.

## Project Structure
.
├── tests/
│   ├── test_api_endpoints.py   # Main test suite
│   ├── test_data.json          # Test cases and expected results
│   ├── schemas/                # JSON schemas for validation
│   └── __init__.py
├── reports/
│   └── html/                   # Generated HTML reports
├── requirements.txt            # Python dependencies
├── .github/
│   └── workflows/
│       └── api-tests.yml       # GitHub Actions workflow file for CI/CD
└── README.md                   # Project documentation

## Installation, Setup, and Usage
To set up and run this project locally or via CI/CD, follow these steps:

1. Clone the repository:
git clone https://github.com/yourusername/api-regression-suite.git
cd api-regression-suite

2. (Optional) Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. Install dependencies:
pip install -r requirements.txt

4. Update `test_data.json` with the endpoints you want to test. For the OpenWeather API example, replace `YOUR_API_KEY` with your actual key either in the JSON file or through environment variables.

5. Run the tests locally:
pytest tests/test_api_endpoints.py --html=reports/html/report.html --self-contained-html -v

6. (Optional) Enable reruns for flaky tests:
pytest tests/test_api_endpoints.py --reruns 1 --reruns-delay 0.5 --html=reports/html/report.html --self-contained-html -v

## CI/CD Integration
This project uses GitHub Actions for Continuous Integration and Continuous Delivery. Every push to the `main` branch or pull request triggers the workflow `.github/workflows/api-tests.yml`, which:
- Checks out the repository
- Sets up a Python environment
- Installs dependencies from `requirements.txt`
- Runs the Pytest suite
- Generates an HTML report
- Uploads the report as an artifact to the GitHub Actions run

While Continuous Delivery in this project does not deploy code to production, the automated tests ensure code readiness and could easily be extended for deployment.

## Example Test Outcomes
The suite includes tests that result in Passed (endpoint returned expected status and schema), Failed (unexpected status or schema mismatch), XFailed (known/expected failure), XPassed (test marked to fail but passed), Skipped (intentionally not run), Error (unhandled exception), and Rerun (flaky test passed after retry).

## Reports
HTML reports are stored locally at `reports/html/report.html`. In CI/CD runs, the report is uploaded as an artifact and can be downloaded from the GitHub Actions interface.

## Extending the Suite
You can add new APIs to `test_data.json`, add JSON schemas for validation, mark tests with `skip`, `xfail`, or `flaky`, and integrate notifications or deployment steps in CI/CD.

## Technologies Used
Python 3.x, Pytest, pytest-html, pytest-rerunfailures, Requests, JSON Schema, GitHub Actions.

## Example Use Cases
Regression testing for REST APIs, contract testing with schemas, API monitoring in CI/CD pipelines, performance threshold validation.

## Author
Barbora Dali
barboradali@gmail.com
LinkedIn: https://linkedin.com/in/barboradali
GitHub: https://github.com/barboradali
EOF
