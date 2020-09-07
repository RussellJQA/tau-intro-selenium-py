"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo result page.
"""

from typing import List

from selenium.webdriver.common.by import By


class DuckDuckGoResultPage:

    # Locators

    # Locate links with class="result__a"
    RESULTS_LINKS = (By.CSS_SELECTOR, "a.result__a")
    SEARCH_INPUT = (By.ID, "search_form_input")

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    def result_link_titles(self) -> List[str]:
        links = self.browser.find_elements(*self.RESULTS_LINKS)
        titles = [link.text for link in links]
        return titles

    def search_input_value(self) -> str:
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute("value")
        return value

    def title(self) -> str:
        return self.browser.title