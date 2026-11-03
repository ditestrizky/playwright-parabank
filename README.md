# ParaBank UI Test Automation

Automated UI tests for [ParaBank](https://parabank.parasoft.com), a public demo banking application, built with Python, Playwright, and pytest using the Page Object Model.

## Test coverage

| Area | Scenario | Expected result |
|---|---|---|
| Login | Valid credentials | Redirects to the accounts overview and shows **Log Out** |
| Login | Empty password | Shows "Please enter a username and password." |
| Logout | Log out from a logged-in session | **Log In** is shown and **Log Out** is hidden |
| Register | Valid form with a unique username | Shows the welcome message |
| Register | Required field left empty (first name, last name, city, username) | Shows an "is required" error for that field |

The suite has 8 test cases: the required-field test runs once per field through `pytest.mark.parametrize`.

## Tech stack

- Python 3.13
- Playwright for Python
- pytest with the `pytest-playwright` plugin
- `python-dotenv` for local credentials

## Project structure

```text
.
├── pages/
│   ├── base_page.py       # Shared page setup and navigation
│   ├── login_page.py      # Login form and logout actions
│   └── register_page.py   # Registration form actions and errors
├── tests/
│   ├── test_login.py      # Login and logout tests
│   └── test_register.py   # Registration tests
├── conftest.py            # Shared fixtures
├── pytest.ini             # pytest configuration, including base_url
├── requirements.txt       # Direct dependencies
└── .env.example           # Template for required environment variables
```

## Design decisions

- **Page Object Model:** tests describe what the user does, while page classes own the locators and actions.
- **`BasePage` inheritance:** each page sets its own `path` and inherits `goto()`. If a page forgets to set `path`, `goto()` raises a clear error.
- **Layered fixtures:** `logged_in_page` builds on a session-scoped `credentials` fixture, so credentials are read and validated in one place.
- **Central configuration:** the application URL is set once in `pytest.ini`. It can be overridden per run with `--base-url`.
- **No secrets in the repository:** credentials stay in a git-ignored `.env` file. If they are missing, tests that need them stop with a message pointing to `.env.example`.

## Getting started

### Prerequisites

- Python 3.13
- A ParaBank account, which you can create on the [registration page](https://parabank.parasoft.com/parabank/register.htm)

### Installation

```bash
git clone https://github.com/ditestrizky/playwright-parabank.git
cd playwright-parabank
python -m venv .venv
```

Activate the virtual environment:

```bash
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate
```

Install the dependencies and the browser:

```bash
pip install -r requirements.txt
playwright install chromium
```

### Configuration

Copy `.env.example` to `.env`, then fill in your ParaBank account:

```text
PB_USER=your_username
PB_PASS=your_password
```

## Running the tests

```bash
# Run all tests
pytest -v

# Run one file
pytest tests/test_login.py -v

# Watch the browser while the tests run
pytest --headed

# Re-run only the tests that failed last time
pytest --lf
```

## Known limitations

- ParaBank is a shared public demo, so its availability and data are outside this project's control.
- Demo data can be reset. If login starts failing, register the account again and update `.env`.
- Registration test data is hardcoded, except for the generated username.
