"""Configuration for pytest."""

import os


def pytest_configure():
    """Set environment variables for testing."""
    os.environ["OPENBB_AUTO_BUILD"] = "false"
