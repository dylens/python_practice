import unittest


# 列表生成式
# l = [<x> for x in iterable]
def list_gen(l1):
    # l1 = {'d', 'y', 'e'}
    l2 = {str(x).upper() for x in l1}
    print(l2)
    return l2


# 集合生成式
# s = {<x> for x in iterable}
def set_gen(s1):
    # s1 = set('dye test')
    s2 = {str(x).upper() for x in s1}
    print(s2)
    return s2


# 字典生成式
# d = {<k>:<v> for (k,v) in dict}
def dict_gen(d1):
    # d1 = {'x': 1, 'y': 2, 'z': 3}
    d2 = {str(k).upper(): v + 2 for (k, v) in d1.items()}
    print(d2)
    return d2


# 生成器
# 生成器是一种迭代过程才生成对应元素的可迭代对象
# 生成器的元素在访问前不会生成，只有当访问时才会生成，如果继续向后访问，那么当前的元素会销毁。
# 生成器的一种生成方式是将列表生成式改为小括号包裹：
# 可以使用next()来迭代生成器
def generator1(num):
    res = []
    g = fib(num)
    while True:
        try:
            x = next(g)
            res.append(x)
            print("g:", x)
        except StopIteration as e:
            print('返回值等于:', e.value)
            break
    return res


# 也可以用for来迭代生成器
def generator2(num):
    res = []
    for x in fib(num):
        res.append(x)
        print("x:", x)
    return res


def fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield b
        a, b = b, a + b
        n = n + 1


def detect_anagrams(test_word, candidates):
    counter = {x: test_word.lower().count(x) for x in set(test_word.lower())}
    return [x for x in candidates if
            len(test_word) == len(x) and test_word.lower() != x.lower() and counter == {c: x.lower().count(c) for c in
                                                                                        set(x.lower())}]


class AnagramTests(unittest.TestCase):
    def test_detect_multiple_anagrams(self):
        self.assertEqual(
            ['stream', 'maters'],
            detect_anagrams('master', 'stream pigeon maters'.split())
        )

    def test_dict_gen(self):
        self.assertEqual(
            {'X': 3, 'Y': 4, 'Z': 5},
            dict_gen({'x': 1, 'y': 2, 'z': 3})
        )

    def test_list_gen(self):
        self.assertEqual(
            {'D', 'Y', 'E'},
            list_gen({'d', 'y', 'e'})
        )

    def test_set_gen(self):
        self.assertEqual(
            {'T', 'E', 'D', ' ', 'S', 'Y'},
            set_gen(set('dye test'))
        )

    def test_generator1(self):
        self.assertEqual(
            [1, 1, 2, 3, 5, 8],
            generator1(6)
        )

# 是set，而不是list
# {1,1,2,3,5,8} 会转换成 {1,2,3,5,8}
