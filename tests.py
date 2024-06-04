import unittest

if __name__ == "__main__":
    # Load all tests from the 'startgpt/tests' package
    suite = unittest.defaultTestLoader.discover("startgpt/tests")

    # Run the tests
    unittest.TextTestRunner().run(suite)
