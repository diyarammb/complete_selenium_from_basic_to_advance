import unittest

class TestCaseDemo(unittest.TestCase):
    def setUp(self):
        print("run before every test")
    def test_methodA(self):
        print("I am Test A")
    def test_methodB(self):
        print("I am Test B")
    def tearDown(self):
        print("i am run After All Test Case")
if __name__ == '__main__':
    unittest.main(verbosity=2)
