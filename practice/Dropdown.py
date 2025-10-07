from playwright.sync_api import Page


def test_dropdown(page:Page):
    page.goto("https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_g50zekzm1_e&adgrpid=155259812313&hvpone=&hvptwo=&hvadid=774088017553&hvpos=&hvnetw=g&hvrand=4287689316143889889&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007764&hvtargid=kwd-29089120&hydadcr=5496_2466962&gad_source=1")
    page.locator("#searchDropdownBox").click()
    page.select_option("#searchDropdownBox", index=17)
    selected_text = page.locator("#searchDropdownBox option:checked").inner_text()
    print("Currently selected:", selected_text)
    assert selected_text == "Electronics"

    #handeling dyanamic search bar
    search_bar = page.locator("#twotabsearchtextbox")
    search_bar.fill("mobile")

    results=page.locator("#sac-autocomplete-results-container div.s-suggestion-container")
    results.first.wait_for(state="visible", timeout=10000)

    count = results.count()
    print(f"Found {count} suggestions")
    suggestion_texts = [results.nth(i).text_content(timeout=5000) for i in range(count)] # will retrun list of items
    print("Suggestions:", suggestion_texts)
    results.nth(1).click()









