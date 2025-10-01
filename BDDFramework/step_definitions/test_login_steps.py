import os

import pytest
from playwright.sync_api import expect
from pytest_bdd import scenarios, given, when, then, parsers
from pytest_playwright.pytest_playwright import page

from BDDFramework.Pages.Login import LoginPage

scenarios("../features/login.feature")

@given("user is on the login page")
def open_login_page(page, login_obj):
    login_obj.page_navigation(page)


@when(parsers.parse('user logs in with "{username}" and "{password}"'))
def login_valid(page, login_obj, username, password):

    login_obj.validLogin(username, password)


@then(parsers.parse('login should be "{expected_result}"'))
def login_scenarios(page,expected_result ):
    if expected_result=="pass":
        page.wait_for_url("https://automationexercise.com/", timeout=10000)
        print("logged in success")
    else:
        login_obj = LoginPage(page)
        expect(login_obj.error_message).to_be_visible()
        expect(login_obj.error_message).to_have_text("Your email or password is incorrect!")
        print("error message received")







