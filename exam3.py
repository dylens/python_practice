# /usr/bin/env python
# -*- coding: utf-8 -*-
# ROT13 is a weak form of encryption that involves "rotating" each letter in a
# word by 13 places. To rotate a letter means to shift it through the alphabet,
# wrapping around to the beginning if necessary, so 'A' shifted by 3 is 'D' and
# 'Z' shifted by 1 is 'A'. Write a function called rotate_word that takes a 
# string and an integer as parameters, and that returns a new string that 
# contains the letters from the original string 'rotated' by the given amount.
# For example, 'cheer' rotated by 7 is 'jolly' and 'melon' rotated by -10 is 
# 'cubed'. You might want to use the built-in functions ord, which converts a 
# character to a numeric code, and chr, which converts numeric codes to characters.
# Potentially offensive jokes on the Internet are sometimes encoded in ROT13. 
# If you are not easily offended, find and decode some of them.
import unittest


def rotate_word(word, n):
    chrl = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

    res_list = []

    for c in word:
        ascii_num = ord(c)
        char_index = ascii_num % 97
        offset = (char_index + n) % 26
        res_list.append(chrl[offset])

    return ''.join(res_list)


class ROT13Tests(unittest.TestCase):
    def test_rot13(self):
        self.assertEqual('jolly', rotate_word('cheer', 7))
        self.assertEqual('bunny', rotate_word('sleep', 9))

    def test_rot13_negative(self):
        self.assertEqual('cubed', rotate_word('melon', -10))


if __name__ == '__main__':
    unittest.main()
    # rotate_word('sleep', 9)
