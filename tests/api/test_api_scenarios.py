import pytest
from utils.user_model import User
from utils.json_utils import deep_compare_json

@pytest.mark.smoke
def test_get_users_and_parse_model(api_context, logger):
    """1. GET Request, Response Model parsing, and search without index."""
    logger.info("Executing GET /users API test.")
    response = api_context.get("/users")
    assert response.status == 200
    
    users_raw = response.json()
    assert isinstance(users_raw, list)
    
    # Convert JSON to Response Model Objects
    users = [User.from_json(u) for u in users_raw]
    
    # Search without knowing index
    target_user = next((u for u in users if u.name == "Leanne Graham"), None)
    assert target_user is not None
    assert target_user.id == 1
    assert target_user.username == "Bret"
    assert target_user.email == "Sincere@april.biz"

@pytest.mark.regression
def test_create_post(api_context):
    """2. POST Request validation."""
    payload = {
        "title": "Playwright Automation",
        "body": "Testing API with Playwright Python",
        "userId": 1
    }
    response = api_context.post("/posts", data=payload)
    assert response.status == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert "id" in data

@pytest.mark.regression
def test_update_post(api_context):
    """3. PUT Request validation."""
    payload = {
        "id": 1,
        "title": "Updated Title",
        "body": "Updated Body Content",
        "userId": 1
    }
    response = api_context.put("/posts/1", data=payload)
    assert response.status == 200
    data = response.json()
    assert data["title"] == payload["title"]

@pytest.mark.regression
def test_delete_post(api_context):
    """4. DELETE Request validation."""
    response = api_context.delete("/posts/1")
    assert response.status in [200, 204]

@pytest.mark.regression
def test_deep_json_comparison(api_context):
    """5. Deep JSON comparison utility verification."""
    response = api_context.get("/users/1")
    assert response.status == 200
    actual_user = response.json()

    # Exact equality check
    assert actual_user["id"] == 1

    # Deep JSON compare against partial dynamic schema check
    expected_sample = {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
        "address": {
            "street": "Kulas Light",
            "city": "Gwenborough"
        }
    }
    
    # Extract matching subset for comparison
    actual_subset = {
        "id": actual_user["id"],
        "name": actual_user["name"],
        "username": actual_user["username"],
        "email": actual_user["email"],
        "address": {
            "street": actual_user["address"]["street"],
            "city": actual_user["address"]["city"]
        }
    }

    mismatches = deep_compare_json(actual_subset, expected_sample)
    assert len(mismatches) == 0, f"JSON mismatches found: {mismatches}"