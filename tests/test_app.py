import unittest


class TestAppFunctions(unittest.TestCase):
    def test_foo(self):
        self.assertEqual("", '')

    def test_bar(self):
        self.assertEqual('', "baz")


if __name__ == '__main__':
    unittest.main()
