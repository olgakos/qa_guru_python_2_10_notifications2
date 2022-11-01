import allure
from selene.support.shared import browser
from selene import be, have
import pytest


@pytest.fixture(autouse=True)
def browser_open_baseURL():
    browser.open('https://google.com')
    yield


@pytest.fixture(scope="session")
def browser_open_setting():
    browser.config.window_width = 800
    browser.config.window_height = 600
    yield


@pytest.fixture(scope="session")
def browser_open_setting2():
    browser.config.window_width = 1024
    browser.config.window_height = 768
    yield


def test_google_positive(browser_open_setting):
    #with allure.step("Open"):
        #browser.open('https://google.com')
    with allure.step("Search"):
        browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    with allure.step("Check"):
        browser.element('[id="search"]').should(have.text('Селена - Википедия'))