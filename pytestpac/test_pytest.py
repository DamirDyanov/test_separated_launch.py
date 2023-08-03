from playwright.sync_api import Page, expect


def test_example(page: Page) ->None:
    page.goto("https://sso.teachable.com/secure/673/identity/login")
    page.get_by_label("Email").click()
    page.get_by_label("Email").fill("dummy@test.com")
    page.get_by_label("Email").press("Tab")
    page.get_by_label("Password").fill("test")


print("test execution complete")