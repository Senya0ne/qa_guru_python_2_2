from selene.support.shared import browser
from selene import be, have
import pytest


@pytest.fixture()
def setup_responsive_for_window():
    browser.config.window_width, browser.config.window_height = 1800, 1000
    yield


def test_google_finds_selene_successful(setup_responsive_for_window):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_google_finds_selene_unsuccessful():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.no.text('Selenide - User-oriented Web UI browser tests in Python'))
