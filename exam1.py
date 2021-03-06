import unittest

'''
# Rna Transcription

Write a program that, given a DNA strand, returns its RNA complement (per RNA transcription).

Both DNA and RNA strands are a sequence of nucleotides.

The four nucleotides found in DNA are adenine (**A**), cytosine (**C**),
guanine (**G**) and thymidine (**T**).

The four nucleotides found in RNA are adenine (**A**), cytosine (**C**),
guanine (**G**) and uracil (**U**).

Given a DNA strand, its transcribed RNA strand is formed by replacing
each nucleotide with its complement:

* `G` -> `C`
* `C` -> `G`
* `T` -> `A`
* `A` -> `U`
'''


def to_rna(input_string):
    input_list = list(input_string)

    res = []

    for c in input_list:
        res.append(trans(c))
    return ''.join(res)


def trans(c):
    if c == 'G':
        return 'C'
    if c == 'C':
        return 'G'
    if c == 'T':
        return 'A'
    if c == 'A':
        return 'U'


class DNATests(unittest.TestCase):

    def test_transcribes_guanine_to_cytosine(self):
        self.assertEqual('C', to_rna('G'))

    def test_transcribes_cytosine_to_guanine(self):
        self.assertEqual('G', to_rna('C'))

    def test_transcribes_thymine_to_adenine(self):
        self.assertEqual('A', to_rna('T'))

    def test_transcribes_adenine_to_uracil(self):
        self.assertEqual('U', to_rna('A'))

    def test_transcribes_all_occurences(self):
        self.assertEqual('UGCACCAGAAUU', to_rna('ACGTGGTCTTAA'))


if __name__ == '__main__':
    unittest.main()
