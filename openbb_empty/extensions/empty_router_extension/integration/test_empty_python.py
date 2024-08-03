"""Test Empty Router extension."""

import pytest
from openbb_core.app.model.obbject import OBBject

# pylint: disable=redefined-outer-name


@pytest.fixture(scope="session")
def obb(pytestconfig):  # pylint: disable=inconsistent-return-statements
    """Fixture to setup obb."""
    if pytestconfig.getoption("markexpr") != "not integration":
        import openbb  # pylint: disable=import-outside-toplevel

        return openbb.obb


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "provider": "empty",
            }
        ),
    ],
)
@pytest.mark.integration
def test_empty_function(params, obb):
    """Test the empty function endpoint."""
    params = {p: v for p, v in params.items() if v}

    result = obb.empty.empty_function(**params)
    assert result
    assert isinstance(result, OBBject)
    assert type(result.results).__name__ == "EmptyData"
