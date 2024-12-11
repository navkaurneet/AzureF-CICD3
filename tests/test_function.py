import unittest
from unittest.mock import Mock
from function.__init__ import main
import azure.functions as func

class TestFunction(unittest.TestCase):
    def test_hello_world(self):
        # Mock the HTTP request
        req = Mock(spec=func.HttpRequest)

        # Call the function
        response = main(req)

        # Check the status code and response body
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_body().decode(), "Hello, World!")

if __name__ == "__main__":
    unittest.main()
