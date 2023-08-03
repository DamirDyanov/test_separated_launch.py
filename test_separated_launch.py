from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.fixture()
def run(playwright):
    webkit = playwright.webkit
    browser = webkit.launch()
    context = browser.new_context()
    page = context.new_page()


@pytest.fixture()
def test_separated_launch():
    page = run()
    page.goto('https://github.com/DamirDyanov?tab=repositories')
    page.locator("//a[@href='/DamirDyanov/first_test']").click()
    page.locator("//a[@data-tab-item='i1issues-tab']").click()

    issue_locators = page.locator("//h2/..//a[contains(@class,'Link--primary')]")
    count_issue_locators = issue_locators.count()
    print()
    print("Всего локаторов:" + str(count_issue_locators))
    check_locator = page.locator("//div[@class='Layout-main']")
    for i in range(count_issue_locators):
        if issue_locators.nth(i).is_visible():
            print("Посещаем issue №" + str(i+1))
            issue_locators.nth(i).click()
            expect(check_locator).to_be_visible()
            page.go_back()
            count_issue_locators = count_issue_locators - 1
        else:
            print("issues закончились")
            break

