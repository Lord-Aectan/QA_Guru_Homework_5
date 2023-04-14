from selene import browser, by, be, have
from tests.conftest import browser_open_page


def test_registration_form():
    browser_open_page()
