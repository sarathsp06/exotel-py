# -*- coding: utf-8 -*-


import pytest
import requests_mock


@pytest.fixture(scope='function', autouse=True)
def mock_http():
    """pytest fixture to intercept outbound HTTP requests."""

    with requests_mock.mock() as m:
        yield m
