import unittest

'''
# Anagram

Write a program that, given a word and a list of possible anagrams, selects the correct sublist.

Given `"listen"` and a list of candidates like `"enlists" "google"
"inlets" "banana"` the program should return a list containing
`"inlets"`.
'''


def detect_anagrams(test_word, candidates):
    lower_test_word = test_word.lower()
    res_list = []

    for candi in candidates:
        if lower_test_word == candi.lower():
            continue
        if len(lower_test_word) != len(candi):
            continue

        lower_test_word_list = list(lower_test_word)
        lower_test_word_list.sort()
        lower_candi_list = list(candi.lower())
        lower_candi_list.sort()

        if lower_test_word_list == lower_candi_list:
            res_list.append(candi)

    return res_list


class AnagramTests(unittest.TestCase):
    def test_no_matches(self):
        self.assertEqual(
            [],
            detect_anagrams('diaper', 'hello world zombies pants'.split())
        )

    def test_detect_simple_anagram(self):
        self.assertEqual(
            ['tan'],
            detect_anagrams('ant', 'tan stand at'.split())
        )

    def test_detect_multiple_anagrams(self):
        self.assertEqual(
            ['stream', 'maters'],
            detect_anagrams('master', 'stream pigeon maters'.split())
        )

    def test_does_not_confuse_different_duplicates(self):
        self.assertEqual(
            [],
            detect_anagrams('galea', ['eagle'])
        )

    def test_eliminate_anagram_subsets(self):
        self.assertEqual(
            [],
            detect_anagrams('good', 'dog goody'.split())
        )

    def test_detect_anagram(self):
        self.assertEqual(
            ['inlets'],
            detect_anagrams('listen', 'enlists google inlets banana'.split())
        )

    def test_multiple_anagrams(self):
        self.assertEqual(
            'gallery regally largely'.split(),
            detect_anagrams(
                'allergy',
                'gallery ballerina regally clergy largely leading'.split()
            )
        )

    def test_anagrams_are_case_insensitive(self):
        self.assertEqual(
            ['Carthorse'],
            detect_anagrams('Orchestra',
                            'cashregister Carthorse radishes'.split())
        )

    def test_same_word_isnt_anagram(self):
        self.assertEqual(
            [],
            detect_anagrams('banana', ['banana'])
        )

        self.assertEqual(
            [],
            detect_anagrams('go', 'go Go GO'.split())
        )


if __name__ == '__main__':
    unittest.main()

    # a=detect_anagrams('Orchestra','cashregister Carthorse radishes'.split())
    # print a
