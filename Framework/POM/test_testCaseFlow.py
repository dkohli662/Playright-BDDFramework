import json

import pytest
from playwright.sync_api import Page, Playwright, expect

from Framework.POM.Dashboard import Dashboard
from Framework.POM.Login import Login
from Framework.POM.OrderHistory import OrderHistory
from Framework.utils.ApiUtils import API

# json file->util->access into test
with open('Data/credentials.json') as f:
    test_data = json.load(f)  # will change json into python obj stored in test_data
    list = test_data['user_credentials']  # will return list of item in form of ind, value

@pytest.mark.parametrize('creds' , list) # creds is any var name that will hold paramtr values
def test_e2e(playwright:Playwright, creds): # user_creds is my fixture define in conftext
    email = creds["userEmail"]
    password = creds["userPassword"]
    browser=playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page=context.new_page()
# create order->get order id
    obj = API()  # creating an obj of class API
    orderId = obj.createOrder(playwright, creds)

# browser launch & login

    obj=Login(page) # creating obj of class Login
    obj.navigate()
    dashboard_obj=obj.login(email,password) # getting of dashboard obj which is returing from login method
    historyPage_obj=dashboard_obj.OrderClick()
    detailPage_obj=historyPage_obj.OderHistory(orderId)
    detailPage_obj.getMessaeg(orderId)















