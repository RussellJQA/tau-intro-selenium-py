"""
This module contains shared fixtures.
"""

import json

import pytest
import selenium.webdriver


@pytest.fixture
# Run config() fixture only once per session (only 1 time before the entire test suite)
def config(scope="session"):

    # Read the file
    with open("config.json") as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert config["browser"] in ["Firefox", "Chrome", "Headless Chrome"]
    assert isinstance(config["implicit_wait"], int)
    assert config["implicit_wait"] > 0

    # Return config so it can be used
    return config


@pytest.fixture
# Run browser() fixture once for each test case (scope="function", the default)
def browser(config):

    # Initialize the WebDriver instance
    if config["browser"] == "Firefox":
        b = selenium.webdriver.Firefox()

    elif config["browser"] == "Chrome":
        b = selenium.webdriver.Chrome()

    elif config["browser"] == "Headless Chrome":
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument("headless")

        b = selenium.webdriver.Chrome(options=opts)

    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Make its calls wait (up to specified duration) for elements to appear
    b.implicitly_wait(config["implicit_wait"])

    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the cleanup
    b.quit()
