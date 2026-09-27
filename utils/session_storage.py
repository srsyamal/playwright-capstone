import json
from playwright.sync_api import Page

def set_session_storage(page: Page, key: str, value: str):
    page.evaluate(f"sessionStorage.setItem('{key}', '{value}')")

def get_session_storage(page: Page) -> dict:
    return page.evaluate("() => Object.fromEntries(Object.entries(sessionStorage))")

def clear_session_storage(page: Page):
    page.evaluate("sessionStorage.clear()")

def save_session_storage_to_file(page: Page, filepath: str = "testdata/session_data.json"):
    data = get_session_storage(page)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def restore_session_storage_from_file(page: Page, filepath: str = "testdata/session_data.json"):
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    for key, value in data.items():
        set_session_storage(page, key, str(value))