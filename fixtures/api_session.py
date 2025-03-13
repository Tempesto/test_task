import pytest

from api.api_session import APISession


@pytest.fixture(scope="session")
def api_session():
    """Create APISession instance."""
    session = APISession()
    return session
