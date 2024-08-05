"""Empty Fetcher Tests."""

import pytest
from openbb_core.app.service.user_service import UserService
from openbb_empty_provider.models.empty_function import EmptyFetcher

test_credentials = UserService().default_user_settings.credentials.model_dump(
    mode="json"
)


@pytest.fixture(scope="module")
def vcr_config():
    """VCR configuration."""
    return {
        "filter_headers": [("User-Agent", None)],
    }


@pytest.mark.record_http
def test_empty_function(credentials=None):
    """Test empty function fetcher."""
    params = {}

    fetcher = EmptyFetcher()
    result = fetcher.test(params, credentials)
    assert result is None
