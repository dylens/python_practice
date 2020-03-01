import unittest


def l_cmp():
    a = [1, 3, 5, 7, 9]
    b = [10, 8, 6, 4, 2]
    li = list(map(max, a, b))
    print(li)


def l_square():
    a = [1, 3, 5, 7, 9]
    b = [2, 3, 4, 2, 2]
    li = list(map(lambda x, y: x ** y, a, b))
    print(li)


class DTest(unittest.TestCase):
    def test1(self):
        self.assertEqual([10, 8, 6, 7, 9], l_cmp())

    def test2(self):
        self.assertEqual([1, 27, 625, 49, 81], l_square())
