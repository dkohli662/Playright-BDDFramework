
import pytest

from playwright.sync_api import Page, expect


def test_hover(page:Page):
    page.goto("https://www.amazon.in/customer-preferences/edit?ie=UTF8&preferencesReturnUrl=%2F&ref_=topnav_lang")
    page.locator("#icp-nav-flyout").hover()
    items=page.locator("#nav-flyout-icp ul li a.nav-link")
    expect(items.first).to_be_visible(timeout=5000)

    c=items.count()
    print("total languages allowed:", c)
    for i in range(c):
        text=items.nth(i).inner_text()
        print(f"{i+1}->{text}")

    items.nth(1).click()
