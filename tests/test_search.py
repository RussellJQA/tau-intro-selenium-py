"""
These tests cover DuckDuckGo searches.
"""

import pytest

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage

# Without parallelization, this took me:
#   28.66 seconds in Firefox
#   19.41 seconds in headless Chrome
# With parallelization, in headless Chrome, it took me 8.80 seconds
@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
def test_basic_duckduckgo_search(browser, phrase: str):

    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for "panda"
    search_page.search(phrase)

    # Then the search result query is "panda"
    assert phrase == result_page.search_input_value()

    # And the search result links pertain to "panda"
    titles = result_page.result_link_titles()
    matches = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0

    # And the search result title contains "panda"

    # (Putting this assertion last guarantees that the page title will be ready)
    assert phrase in result_page.title()
