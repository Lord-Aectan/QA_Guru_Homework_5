from selene import browser, by, be, have


def browser_open_page():
    browser.config.window_width = 1500
    browser.config.window_height = 1200
    browser.open('https://demoqa.com/automation-practice-form')

