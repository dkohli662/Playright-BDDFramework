import os

import pytest
from playwright.sync_api import expect
from pytest_bdd import scenarios, given, when, then, parsers
from pytest_playwright.pytest_playwright import page

from ..Pages.Login import LoginPage

scenarios("../features/login.feature")

@given("user is on the login page")
def open_login_page(page, login_obj):
    login_obj.page_navigation(page)


@when(parsers.parse('user logs in with "{username}" and "{password}"'))
def login_valid(page, login_obj, username, password):

    login_obj.validLogin(username, password)


@then(parsers.parse('login should be "{expected_result}"'))
def login_scenarios(page,expected_result ):
    login_obj = LoginPage(page)

    if expected_result=="pass":
        page.wait_for_url("https://automationexercise.com/", timeout=70000)
        print("logged in success")

    else:

        try:
            page.wait_for_selector("p:has-text('Your email or password is incorrect!')", timeout=15000)
            expect(login_obj.error_message).to_be_visible()
            print("Login failed as expected - Error message displayed")
        except Exception:
            print("Error message not visible. Debugging below:")
            print(page.content())  # print full page HTML for analysis
            raise










