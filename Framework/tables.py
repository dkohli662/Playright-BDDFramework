from playwright.sync_api import Page, expect


def test_table(page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for i in range(page.locator("th").count()):
        if page.locator("th").nth(i).filter(has_text="price").count()>0:
            colValue=i
            print("coloumn found :", colValue)
            break
    row=page.locator("tr").filter(has_text="Rice")
    print("row found :", row)
    expect(row.locator("td").nth(colValue)).to_have_text("37")

# print price of rice
def test_table2(page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for i in range(page.locator("th").count()):
        if page.locator("th").nth(i).filter(has_text="price").count()>0:
            colValue = i
            print("coloumn found :", colValue)
            break
    row=page.locator("tr").filter(has_text="Rice")

    cell=row.locator(f"td:nth-child({colValue+1})")
    cell_text=cell.inner_text()
    assert cell_text=="37"
    print("price of rice is :", cell_text)




# validate discount price of potato?

def test_table3(page:Page):
        page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
        for i in range(page.locator("th").count()):
            if page.locator("th").nth(i).filter(has_text="Discount price").count() > 0:
                colNum = i
                print("coloumn found :", colNum)
                break
        row = page.locator("tr").filter(has_text="Potato")

        cell = row.locator(f"td:nth-child({colNum + 1})")
        cell_text = cell.inner_text()

        print("price of potato is :", cell_text)

        # ✅ pick the row that contains "Potato"

        # ✅ then pick the cell inside that row (colNum is 0-based, so +1 for nth-child)
        cell = row.locator(f"td:nth-child({colNum + 1})")

        cell_text = cell.inner_text()
        print("Cell text for Potato @ Discount column =", cell_text)





