import pytest

@pytest.mark.regression
def test_multiple_windows(page, logger):
    """8. Test handling multiple windows/tabs."""
    logger.info("Navigating to Herokuapp Windows page")
    page.goto("https://the-internet.herokuapp.com/windows")
    parent_url = page.url

    # Listen for new tab creation
    with page.context.expect_page() as new_page_info:
        page.get_by_role("link", name="Click Here").click()

    child_page = new_page_info.value
    child_page.wait_for_load_state("domcontentloaded")

    # Validations
    assert len(page.context.pages) == 2
    assert parent_url == "https://the-internet.herokuapp.com/windows"
    assert child_page.url == "https://the-internet.herokuapp.com/windows/new"
    
    heading = child_page.get_by_role("heading", name="New Window")
    heading.wait_for(state="visible")
    assert heading.inner_text() == "New Window"

    child_page.close()
    assert len(page.context.pages) == 1