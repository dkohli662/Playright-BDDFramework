from playwright.sync_api import Page

from playwright.sync_api import Page


def test_table(page: Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    # Locate all rows in the table (tr inside table body)
    rows = page.locator("tbody tr").count() # number of rows inside body without header row
    rows1=page.locator("table tr").count() # include header row & body row
    col=page.locator("th").count()
    print("Total rows in table:", rows)
    print("Total rows in table:", rows1)
    print("Total col in table:", col)

def test_printTable(page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    all_rows=page.locator("tr") # will fetch all rows
    row_count=all_rows.count()
    for i in range(row_count):
        print(all_rows.nth(i).inner_text())
    page.get_by_role("button", name="Next").click() # will move to next page
    rows=page.locator("tbody tr")
    count=rows.count()
    for i in range(count):
        print(rows.nth(i).inner_text())

# fetch value of col 2 and row 5
    row=page.locator("tr").nth(4) # will fetch 5th row
    col=page.locator("th").nth(1) # will fetch 2nd col
    cell=row.locator("td").nth(1).inner_text()
    print("value of cell is :", cell)

    # fetch price of guava

    headers=page.locator("th") # get locator of all headers
    column=-1
    for i in range(headers.count()): # loop till all header
        if headers.nth(i).inner_text()=="Price": # match header name with Price
            column=i;
            break
        row2=page.locator("tr").filter(has_text="guava")
        cell=row2.locator("td").nth(column).inner_text()
        print("price of a guava is :", cell)
























