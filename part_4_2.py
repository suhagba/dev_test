"""
Use a mock so that this test still works but no longer makes a HTTP request to example.com

You can test that it is not making HTTP requests by turning off your internet and
checking if it still works.

It should be possible to run the test in this file using PyTest
eg.
    pytest part_4_2.py

"""
from checker import check_website_text
from unittest.mock import Mock, patch

# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, text, status_code):
            self.text = text
            self.status_code = status_code

    if args[0] == 'http://example.com/':
        return MockResponse("Example Domain asking for permission", 200)
    elif args[0] == 'http://google.com':
        return MockResponse("google mock", 200)

    return MockResponse(None, 404)

@patch('requests.get', side_effect=mocked_requests_get)
def test_example(mock_get):
    """
    Use mocking to rewrite this test so it doesn't make HTTP requests to example.com
    """

    assert check_website_text("http://example.com/", "Example Domain")
    assert check_website_text("http://example.com/", "asking for permission")
    assert not check_website_text("http://example.com/", "some random text 123 123")
    assert not check_website_text("http://google.com", "Example Domain")
