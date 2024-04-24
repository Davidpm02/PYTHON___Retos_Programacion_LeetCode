import unittest
from ..scripts.code import *

class TestLetterCombinations(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_digits(self):
        digits = ""
        expected = []
        self.assertEqual(self.solution.letterCombinations(digits), expected)

    def test_single_digit(self):
        digits = "2"
        expected = ["a", "b", "c"]
        self.assertEqual(self.solution.letterCombinations(digits), expected)

    def test_multiple_digits(self):
        digits = "23"
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertEqual(self.solution.letterCombinations(digits), expected)

    def test_all_digits(self):
        digits = "23456789"
        expected = ["adg", "adh", "adi", "adj", "adk", "adl", "adm", "adn", "ado", "adp", "adq", "adr", "ads", "adt", "adu", "adv", "adw", "adx", "ady", "adz", "aeb", "aec", "aed", "aee", "aef", "aeg", "aeh", "aei", "aej", "aek", "ael", "aem", "aen", "aeo", "aep", "aeq", " aer", "aes", "aet", "aeu", "aev", "aew", "aex", "aey", "aez", "afb", "afc", "afd", "afe", "aff", "afg", "afh", "afi", "afj", "afk", "afl", "afm", "afn", "afp", "afo", "afq", "afs", "afu", "afv", "afw", "afx", "afy", "afz", "bdg", "bdh", "bdi", "bdj", "bdk", "bdl", "bdm", "bdn", "bdo", "bdp", "bdq", "bdr", "bds", "bdt", "bdu", "bdv", "bdw", "bdx", "bdy", "bdz", "beh", "bei", "bej", "bek", "bel", "bem", "ben", "beo", "bep", "beq", "ber", "bes", "bet", "beu", "bev", "bew", "bex", "bey", "bez", "bfg", "bfh", "bfi", "bfj", "bfk", "bfl", "bfm", "bfn", "bfo", "bfp", "bfq", "bfr", "bfs", "bft", "bfu", "bfv", "bfw", "bfx", "bfy", "bfz", "cdf", "cde", "cdg", "cdf", "cde", "cdg", "cdh", "cdi", "cjk", "cdl", "cmm", "cnn", "cno", "cqp", "cqq", "crr", "cst", "cut", "cuv", "cwx", "cxy", "czyx"]
        self.assertEqual(self.solution.letterCombinations(digits), expected)

if __name__ == '__main__':
    unittest.main()