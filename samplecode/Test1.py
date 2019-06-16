import unittest


def add1(v):
    return v + 1


class TestAdd1(unittest.TestCase):
    def test_call(self):
        self.assertEqual(add1(1), 2)


def canDivideBy2(v):
    return ((v % 2) == 0)


class TestCanDivideBy2(unittest.TestCase):
    def test_call(self):
        self.assertTrue(canDivideBy2(4))
        self.assertFalse(canDivideBy2(5))