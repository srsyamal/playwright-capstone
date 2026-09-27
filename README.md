# Playwright Python Automation Framework (Capstone Project)

A production-grade, maintainable Playwright Python automation framework supporting UI and API automation, Page Object Model (POM) design pattern, data-driven testing, diagnostic logging, artifacts, continuous integration via GitHub Actions, and email notification integration.

## Framework Architecture

```text
playwright-capstone/
├── .github/workflows/    # GitHub Actions Workflow definition
├── pages/                # Page Object Model encapsulation
├── tests/                # UI and API test scenarios
│   ├── ui/
│   └── api/
├── testdata/             # JSON test data files
├── utils/                # Logging, JSON deep-compare, Session Storage, Models
├── logs/                 # Execution logs
└── pytest.ini            # Pytest configuration and markers


# 1. Clone repository
git clone [https://github.com/your-username/playwright-capstone.git](https://github.com/your-username/playwright-capstone.git)
cd playwright-capstone

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install Playwright browser binaries
playwright install

# 4. Run tests
pytest
pytest -m smok

# Success screens

## all test pass
![all case pass](/Errors/all-case-pass.png)

# Errors while testing and Diagnose steps

## Error 1
### playwright._impl._errors.Error: BrowserType.launch: Executable doesn't exist

![alt text](/Errors/error1.png)

### fix: installed chromium browsers 'playwright install' 

# git commands used
git init

git clone https://github.com/srsyamal/playwright-capstone.git