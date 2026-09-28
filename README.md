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
```
# Full Framework structure
    playwright-capstone/
├──
pages/
login_page.py 
products_page.py
checkout_page.py
├──
tests/
ui/ 
api/
├──
testdata/
login_data.json
registration_data.json
├──
utils/
logger.py
json_utils.py
session_storage.py
user_model.py
├──
logs/
├──
screenshots/
├──
conftest.py
├──
pytest.ini
├──
requirements.txt
├──
.gitignore
└──
README.md

# 1. Clone repository
git clone [https://github.com/your-username/playwright-capstone.git](https://github.com/your-username/playwright-capstone.git)
cd playwright-capstone

# git commands used
git init

git clone https://github.com/srsyamal/playwright-capstone.git

## git workflow failed due to case sensitive workflow folder name

### command to modify folder name

```
# rename folder
git mv .github/Workflows .github/workflows_temp && git mv .github/workflows_temp .github/workflows

# commit changes to github
git add .github/workflows
git commit -m "fix: lowercase workflows folder name"
git push
```

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install Playwright browser binaries
playwright install

# 5. Run tests
pytest
pytest -m smok

# 6. Success screens

## all test pass
![all case pass](/Errors/all-case-pass.png)

## git hub actions
![alt text](/Errors/gitActions.png)

# 7. Email notifications

- Email notification on successful github action

![Success email notification](/Errors/email.png)

- Email notification on failed github action

![failure email notification](/Errors/email1.png)

![failure email content](/Errors/email2.png)

# 8. Errors while testing and resolution steps

## Error 1
### playwright._impl._errors.Error: BrowserType.launch: Executable doesn't exist

![alt text](/Errors/error1.png)

### fix: installed chromium browsers 'playwright install' 

## git actions failed due to yaml configuration errors
### Error2
![alt text](/Errors/workflowError1.png)

### fix: Configuraion change

![alt text](/Errors/workflowFix1.png)

### Error3
![alt text](/Errors/workflowError2.png)

### fix: Configuration change
![alt text](/Errors/workflowFix2.png)

### Error4
Workflow executed, artifacts stored successfully except Email configuraitons

![alt text](/Errors/workflowError3.png)

### fix: configure 'EMAIL_TO' variable
Configured the github secrets environment variable `EMAIL_TO` in settings
Configured email and pass key as well

# Project overiew
    This capstone project demonstrates an end-to-end Playwright Python automation framework structured into four core areas:
## Part 1: Project Overview & Framework Architecture
 
### Directory Structure:
Show the modular structure in IDE (pages/, tests/ui/, tests/api/, testdata/, utils/, conftest.py, pytest.ini).

### Design Choices:
#### Locators: 
Used semantic Playwright locators (get_by_role, get_by_placeholder, get_by_text) over hardcoded XPath for robust DOM querying.   

#### API Response Models: 
Implemented User model classes with @property decorators to validate API response structures and avoid direct dictionary manipulation.   

#### Synchronization: 
Used Playwright's native auto-waiting alongside explicit condition-based waits (wait_for_url, wait_for_load_state) rather than static sleeps.   

# Part 2: Key Capabilities & Technical Highlights
## Data-Driven Testing: 
Demonstrate @pytest.mark.parametrize reading from testdata/login_data.json to run valid and invalid login scenarios.   

## Session Storage Utility: 
Demonstrate reading, writing, saving to JSON, and restoring sessionStorage.

## Deep JSON Comparison:
Implemented recursive deep_compare_json function in utils/json_utils.py that compares nested JSON structures and pinpoints exact path mismatches.   

## Window Handling: 
Demonstrate page.context.expect_page() navigating multi-tab/window workflows.   

# Part 3: Failure Debugging Example
## Scenario: Show a simulated or historical test failure
### Debugging Workflow:
Open the pytest HTML report (report.html) generated from the failed run.   

Demonstrate viewing the failure screenshot captured in test-results/.   

Load the Playwright Trace artifact in the Trace Viewer (playwright show-trace trace.zip).   

Inspect the action timeline, DOM snapshot, console logs, and network requests to isolate the root cause.   

#### Explain the distinction between failure artifacts:
    Screenshot: Static visual snapshot at the exact millisecond of failure. 
    Trace: Interactive diagnostic zip file containing network logs, DOM snapshots, action timelines, and console output for deep post-mortem analysis.   

# Part 4: CI/CD Pipeline & Automated Email

## GitHub Actions Workflow: 
Open .github/workflows/playwright.yml and highlight the pipeline triggers (push, pull_request, workflow_dispatch).   

## Execution & Artifacts: 
Show the successful workflow run on GitHub Actions, the uploaded pytest-html-report artifact, and the received automated email containing build details and the HTML report attachment.



