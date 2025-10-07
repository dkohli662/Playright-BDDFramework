from playwright.sync_api import Page, expect


def test_showHide(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    print("button is hidden")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
    page.get_by_role("button", name="Show").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    print("button is visible")




