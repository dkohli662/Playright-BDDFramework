from playwright.sync_api import Playwright
data={"userEmail":"dkohli@ex2india.com","userPassword":"Test@123"} # body section for login
payload={"orders":[{"country":"India","productOrderedId":"68a961459320a140fe1ca57a"}]} # body section for create order


class API:
    # method to get an authorization token while login in
    def getToken(self, playwright:Playwright, creds):
        email=creds["userEmail"]
        password=creds["userPassword"]
        context=playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response=context.post(url="/api/ecom/auth/login", data={"userEmail" : email, "userPassword": password})
        assert response.ok
        responseBody=response.json()
        return responseBody["token"]

    # method to create an order after login

    def createOrder(self, playwright:Playwright, creds):
        token=self.getToken(playwright, creds)
        context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response2=context.post(url="/api/ecom/order/create-order", # passing base endpoints
                     headers={"Authorization":token, "Content-Type":"application/json"}, # passing headers (key value pair)
                     data=payload)                    # passing payload data (body section)


        print(response2.json())
        response_Body=response2.json()
        orderId=response_Body["orders"][0] # retervidng 0 index of response list
        return orderId


