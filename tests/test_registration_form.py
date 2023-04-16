from selene import browser, by, be, have
from tests.conftest import browser_open_page


def test_registration_form():
    browser.config.window_width = 1500
    browser.config.window_height = 1200
    browser.open('https://demoqa.com/automation-practice-form')

    browser.element('#firstName').type('Test')
    browser.element('#lastName').type('Test2')
    browser.element('#userEmail').type('test@test.test')
    browser.element("#gender-radio-1").double_click()
    browser.element('#userNumber').type('78484884844')
    browser.element('#dateOfBirthInput').
    browser.element()
    browser.element()
