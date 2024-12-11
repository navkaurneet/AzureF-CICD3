import unittest
from function.__init__ import main
 
class TestFunction(unittest.TestCase):
    def test_hello_world(self):
        response = main(req=None)
        self.assertEqual(response["status"], 200)
        self.assertEqual(response["body"], "Hello, World!")
 
if __name__ == "__main__":
    unittest.main()
 
