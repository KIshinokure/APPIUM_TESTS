import pytest
from utils.driver_factory import create_driver

@pytest.fixture
def driver():
    instance = create_driver()
    yield instance
    instance.quit()
