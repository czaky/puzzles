"""Test module for the string puzzles."""

import unittest

import strings as s


class TestStrings(unittest.TestCase):
    """Test class for the string puzzles."""

    def test_reverse_words(self):
        """Test the `reverse_words` function."""
        assert s.reverse_words("") == ""
        assert s.reverse_words("jello") == "jello"
        assert s.reverse_words("hello sunny world") == "world sunny hello"
        assert s.reverse_words("so-much-fun", "-") == "fun-much-so"

    def test_palindrome(self):
        """Test the `palindrome` function."""
        assert s.palindrome("a")
        assert s.palindrome("aa")
        assert s.palindrome("aba")
        assert s.palindrome("abba")

        assert not s.palindrome("abc")
        assert not s.palindrome("ab")

    def test_isomorphic(self):
        """Test the `isomorphic` function."""
        assert s.isomorphic("aba", "xyx")
        assert s.isomorphic("aa", "bb")

        assert not s.isomorphic("abb", "xxy")
        assert not s.isomorphic("aba", "xxy")

    def test_common_prefix(self):
        """Test the `common_prefix` function."""
        assert s.common_prefix([]) == ""
        assert s.common_prefix(["abc"]) == "abc"
        assert s.common_prefix(["a", "ab", "abc"]) == "a"
        assert s.common_prefix(["abc", "ab", "a"]) == "a"
        assert s.common_prefix(["abc", "abc", "abc"]) == "abc"
        assert s.common_prefix(["abd", "abc", "abc"]) == "ab"
        assert s.common_prefix(["abc", "abc", "aec"]) == "a"

    def test_equal_rotated(self):
        """Test the `equal_rotated` function."""
        assert s.equal_rotated("a", "a", 0)
        assert s.equal_rotated("a", "a", 1)
        assert s.equal_rotated("a", "a", 2)
        assert s.equal_rotated("ab", "ba", 1)
        assert s.equal_rotated("aba", "aab", 2)
        assert s.equal_rotated("abba", "baab", 2)

        assert not s.equal_rotated("abc", "abc", 1)
        assert not s.equal_rotated("ab", "ab", 1)

    def test_first_unique(self):
        """Test the `first_unique` function."""
        assert s.first_unique("hallo") == "h"
        assert s.first_unique("abba") == "$"
        assert s.first_unique("babassus") == "u"

    def test_roman_to_decimal(self):
        """Test the `roman_to_decimal` function."""
        assert s.roman_to_decimal("V") == 5
        assert s.roman_to_decimal("IV") == 4
        assert s.roman_to_decimal("MDXIX") == 1519

    def test_max_distinct_char_substring(self):
        """Test the `max_distinct_char_substring` function."""
        assert s.max_distinct_char_substring("aa") == 1
        assert s.max_distinct_char_substring("hallo") == 3
        assert s.max_distinct_char_substring("abba") == 2
        assert (
            s.max_distinct_char_substring(
                "aldshflasghdfasgfkhgasdfasdgvfyweofyewyrtyefgv"
            )
            == 10
        )

    def test_edit_distance(self):
        """Test the `edit_distance` function."""
        assert s.edit_distance("aa", "aa") == 0
        assert s.edit_distance("hallo", "hey") == 4
        assert s.edit_distance("abba", "baba") == 2

    def test_longest_palindrome(self):
        """Test the `longest_palindrome` function."""
        assert s.longest_palindrome("") == ""
        assert s.longest_palindrome("a") == "a"
        assert s.longest_palindrome("aa") == "aa"
        assert s.longest_palindrome("ab") == "a"
        assert s.longest_palindrome("abc") == "a"
        assert s.longest_palindrome("hallo") == "ll"
        assert s.longest_palindrome("aba") == "aba"
        assert s.longest_palindrome("abba") == "abba"
        assert s.longest_palindrome("babassus") == "bab"
        assert s.longest_palindrome("12aba") == "aba"
        assert s.longest_palindrome("12abba") == "abba"
        assert s.longest_palindrome("aba12") == "aba"
        assert s.longest_palindrome("abba12") == "abba"
        assert s.longest_palindrome("12abacd@dc") == "cd@dc"
        assert s.longest_palindrome("12abbacd@@dc") == "cd@@dc"
        assert s.longest_palindrome("cd@dcaba12") == "cd@dc"
        assert s.longest_palindrome("cd@@dcabba12") == "cd@@dc"
        assert s.longest_palindrome("abaaaaabba") == "baaaaab"

    def test_distinct_palindrome_substrings(self):
        """Test `distinct_palindrome_substrings`."""
        assert s.distinct_palindrome_substrings("") == 0
        assert s.distinct_palindrome_substrings("a") == 1
        assert s.distinct_palindrome_substrings("aa") == 2
        assert s.distinct_palindrome_substrings("ab") == 2
        assert s.distinct_palindrome_substrings("aba") == 3
        assert s.distinct_palindrome_substrings("abc") == 3
        assert s.distinct_palindrome_substrings("abba") == 4
        assert s.distinct_palindrome_substrings("bbaa") == 4
        assert s.distinct_palindrome_substrings("abaa") == 4
        assert s.distinct_palindrome_substrings("cdgdcdgd") == 8
        assert s.distinct_palindrome_substrings("abaaaaabba") == 10
        assert s.distinct_palindrome_substrings("abcdabbabcdfdc") == 10
        assert s.distinct_palindrome_substrings("abcdabbabcdfdccdgdc") == 15
        assert (
            s.distinct_palindrome_substrings(
                "mdnvznwlylygvstwarpibrfgvdhkdcrlmfgqweveqyo"
            )
            == 26
        )

    def test_palindromic_partitions(self):
        """Test the `palindromic_partitions` function."""
        assert s.palindromic_partitions("") == 0
        assert s.palindromic_partitions("a") == 0
        assert s.palindromic_partitions("aa") == 0
        assert s.palindromic_partitions("ab") == 1
        assert s.palindromic_partitions("abc") == 2
        assert s.palindromic_partitions("hallo") == 3
        assert s.palindromic_partitions("aba") == 0
        assert s.palindromic_partitions("abba") == 0
        assert s.palindromic_partitions("babassus") == 3
        assert s.palindromic_partitions("12aba") == 2
        assert s.palindromic_partitions("12abba") == 2
        assert s.palindromic_partitions("aba12") == 2
        assert s.palindromic_partitions("abba12") == 2
        assert s.palindromic_partitions("12abacd@dc") == 3
        assert s.palindromic_partitions("12abbacd@@dc") == 3
        assert s.palindromic_partitions("cd@dcaba12") == 3
        assert s.palindromic_partitions("cd@@dcabba12") == 3

    def test_subsequence_count(self):
        """Test the `subsequence_count` function."""
        assert s.subsequence_count("aa", "") == 1
        assert s.subsequence_count("", "a") == 0
        assert s.subsequence_count("b", "a") == 0
        assert s.subsequence_count("bcd", "a") == 0
        assert s.subsequence_count("aa", "a") == 2
        assert s.subsequence_count("aa", "a") == 2
        assert s.subsequence_count("aba", "a") == 2
        assert s.subsequence_count("baba", "a") == 2
        assert s.subsequence_count("abab", "a") == 2
        assert s.subsequence_count("baba5", "a") == 2
        assert s.subsequence_count("aa", "aa") == 1
        assert s.subsequence_count("aba", "aa") == 1
        assert s.subsequence_count("baba", "aa") == 1
        assert s.subsequence_count("abab", "aa") == 1
        assert s.subsequence_count("baba5", "aa") == 1
        assert s.subsequence_count("abcdefg", "bdf") == 1
        assert s.subsequence_count("abcdefg@abcdefg", "bdf") == 4

    def test_smallest_window_with_all_characters(self):
        """Test the `smallest_window_with_all_characters` function."""
        assert s.smallest_window_with_all_characters("aa", "") == ""
        assert None is s.smallest_window_with_all_characters("", "a")
        assert None is s.smallest_window_with_all_characters("b", "a")
        assert None is s.smallest_window_with_all_characters("bcd", "a")
        assert s.smallest_window_with_all_characters("aa", "a") == "a"
        assert s.smallest_window_with_all_characters("aa", "aa") == "aa"
        assert s.smallest_window_with_all_characters("aba", "aa") == "aba"
        assert s.smallest_window_with_all_characters("baba", "aa") == "aba"
        assert s.smallest_window_with_all_characters("abab", "aa") == "aba"
        assert s.smallest_window_with_all_characters("baba5", "aa") == "aba"
        assert s.smallest_window_with_all_characters("abc@de4fg", "bdf") == "bc@de4f"
        assert (
            s.smallest_window_with_all_characters("abc3de4fg@abc@def2g", "bdf")
            == "bc@def"
        )

    def test_boolean_parentheses(self):
        """Test the `boolean_parentheses` function."""
        assert s.boolean_parentheses("T|F") == 1
        assert s.boolean_parentheses("T|F^F&T") == 5
        assert s.boolean_parentheses("T|F^F&T|F^F^F^T|T&T^T|F^T^F&F^T|T^F") == 99632640

    def test_artistic_photo_count(self):
        """Test the `artistic_photo_count` function."""
        assert s.artistic_photo_count("APABA", 1, 2) == 1
        assert s.artistic_photo_count("APABA", 2, 3) == 0
        assert s.artistic_photo_count("PBAAP.B", 1, 3) == 3
        assert s.artistic_photo_count(".PBAAP.B", 1, 3) == 3

    def test_distinct_subsequence_count(self):
        """Test the `distinct_subsequence_count` function."""
        assert s.distinct_subsequence_count("") == 1
        assert s.distinct_subsequence_count("a") == 2
        assert s.distinct_subsequence_count("ab") == 4
        assert s.distinct_subsequence_count("aa") == 3
        assert s.distinct_subsequence_count("aba") == 7

    def test_permutations(self):
        """Test the `permutations` function."""
        assert [""] == s.permutations("")
        assert ["a"] == s.permutations("a")
        assert ["ab", "ba"] == s.permutations("ab")
        assert ["abc", "acb", "bac", "bca", "cab", "cba"] == s.permutations("abc")
        assert len(s.permutations("abcd")) == 24

    def test_pattern_match(self):
        """Test `pattern_match`."""
        assert s.pattern_match("*", "")
        assert s.pattern_match("*", "a")
        assert s.pattern_match("*", "aa")
        assert s.pattern_match("?", "a")
        assert not s.pattern_match("?", "")
        assert not s.pattern_match("?", "ab")
        assert s.pattern_match("??", "aa")
        assert not s.pattern_match("??", "a")
        assert not s.pattern_match("??", "abc")
        assert s.pattern_match("?*a*", "cab")
        assert s.pattern_match("?*a*", "cart")
        assert s.pattern_match("?*a*", "ca")
        assert not s.pattern_match("?*a*", "ab")

    def test_longest_repeating_substring(self):
        """Test `longest_repeating_substring`."""
        assert s.longest_repeating_substring("ab123acb") == "a"
        assert s.longest_repeating_substring("dedb123baaacead") == "d"
        assert s.longest_repeating_substring("teeth_for_teeth") == "teeth"

    def test_longest_prefix_suffix_length(self):
        """Test `longest_prefix_suffix_length`."""
        assert s.longest_prefix_suffix_length("abcd") == 0
        assert s.longest_prefix_suffix_length("aaaaa") == 4
        assert s.longest_prefix_suffix_length("acccbaa3acccbaac") == 2

    def test_extra_palindrome_chars(self):
        """Test (upfront) `extra_palindrome_chars`."""
        assert s.extra_palindrome_chars("") == 0
        assert s.extra_palindrome_chars("a") == 0
        assert s.extra_palindrome_chars("aa") == 0
        assert s.extra_palindrome_chars("aba") == 0
        assert s.extra_palindrome_chars("ab") == 1
        assert s.extra_palindrome_chars("abcd") == 3
        assert s.extra_palindrome_chars("aaaaa") == 0
        assert s.extra_palindrome_chars("aa3a3aaa") == 1

    def test_word_wrap(self):
        """Test `word_wrap` ."""
        assert s.word_wrap([], 6) == 0
        assert s.word_wrap([3], 6) == 0
        assert s.word_wrap([3, 2], 6) == 0
        assert s.word_wrap([3, 2, 2], 6) == 0
        assert s.word_wrap([3, 2, 2, 5], 6) == 10

        assert s.word_wrap([], 4) == 0
        assert s.word_wrap([3], 4) == 0
        assert s.word_wrap([3, 2], 4) == 1
        assert s.word_wrap([3, 2, 2], 4) == 5
        assert s.word_wrap([3, 2, 2, 4], 4) == 9

    def test_sum_string(self):
        """Test `sum_string`."""
        assert not s.sum_string("")
        assert not s.sum_string("0")
        assert not s.sum_string("00")
        assert s.sum_string("123")
        assert not s.sum_string("124")
        assert s.sum_string("0123")
        assert not s.sum_string("0124")
        assert s.sum_string("1023")
        assert not s.sum_string("1024")
        assert s.sum_string("1203")
        assert not s.sum_string("1204")
        assert not s.sum_string("1230")
        assert s.sum_string("12243660")
        assert not s.sum_string("12243661")
        assert s.sum_string("11111122233355588931451")
        assert not s.sum_string("11111122233355588931450")

    def test_word_parts(self):
        """Test `word_parts`."""
        assert ["cat"] == s.word_parts(
            ["rat", "cats", "cat", "and", "sand", "dog"], "cat"
        )
        assert [] == s.word_parts(
            ["rat", "cats", "cat", "and", "sand", "dog"], "catsandog"
        )
        assert ["cats and dog", "cat sand dog"] == s.word_parts(
            ["rat", "cats", "cat", "and", "sand", "dog"], "catsanddog"
        )
        assert ["rat cats and dog", "rat cat sand dog"] == s.word_parts(
            ["rat", "cats", "cat", "and", "sand", "dog"], "ratcatsanddog"
        )

    def test_k_alphabet_string_with_all_substrings(self):
        """Test `k_alphabet_string_with_all_substrings`."""
        assert s.k_alphabet_string_with_all_substrings(0, 5) == ""
        assert s.k_alphabet_string_with_all_substrings(5, 0) == ""
        assert s.k_alphabet_string_with_all_substrings(5, 1) == "00000"
        assert s.k_alphabet_string_with_all_substrings(2, 2) == "00110"
        assert s.k_alphabet_string_with_all_substrings(3, 2) == "0001110100"
        assert s.k_alphabet_string_with_all_substrings(2, 3) == "0011210220"
        assert s.k_alphabet_string_with_all_substrings(1, 10) == "1234567890"

    def test_longest_common_subsequence_length(self):
        """Test `longest_common_subsequence_length`."""
        assert s.longest_common_subsequence_length("", "bbb") == 0
        assert s.longest_common_subsequence_length("b", "bbb") == 1
        assert s.longest_common_subsequence_length("bb", "bbb") == 2
        assert s.longest_common_subsequence_length("bbb", "bbb") == 3

        assert s.longest_common_subsequence_length("aaa", "bbb") == 0
        assert s.longest_common_subsequence_length("aba", "bbb") == 1
        assert s.longest_common_subsequence_length("bab", "bbb") == 2
        assert s.longest_common_subsequence_length("bbb", "bbb") == 3

        assert s.longest_common_subsequence_length("caaa", "dbbb") == 0
        assert s.longest_common_subsequence_length("caba", "dbbb") == 1
        assert s.longest_common_subsequence_length("cbab", "dbbb") == 2
        assert s.longest_common_subsequence_length("cbbb", "dbbb") == 3

        assert s.longest_common_subsequence_length("aaae", "bbbf") == 0
        assert s.longest_common_subsequence_length("abae", "bbbf") == 1
        assert s.longest_common_subsequence_length("babe", "bbbf") == 2
        assert s.longest_common_subsequence_length("bbbe", "bbbf") == 3

        assert s.longest_common_subsequence_length("caaae", "dbbbf") == 0
        assert s.longest_common_subsequence_length("cabae", "dbbbf") == 1
        assert s.longest_common_subsequence_length("cbabe", "dbbbf") == 2
        assert s.longest_common_subsequence_length("cbbbe", "dbbbf") == 3

    def test_all_longest_common_subsequences(self):
        """Test `all_longest_common_subsequences`."""
        assert s.all_longest_common_subsequences("cfb", "aceba") == ["cb"]
        assert s.all_longest_common_subsequences("abaaa", "abaaa") == ["abaaa"]
        assert s.all_longest_common_subsequences("baabaca", "abaaa") == [
            "aaaa",
            "abaa",
            "baaa",
        ]
        assert s.all_longest_common_subsequences("abaaa", "baabaca") == [
            "aaaa",
            "abaa",
            "baaa",
        ]

    def test_scrambled(self):
        """test_scrambled."""
        assert s.scrambled("coder", "ocder")
        assert s.scrambled("coerd", "coder")
        assert s.scrambled("coerd", "ocder")
        assert not s.scrambled("abcde", "caebd")

    def test_palindrome_pairs(self):
        assert not s.palindrome_pairs(["l"])
        assert s.palindrome_pairs(["abc", "xyxcba", "leekst", "or", "bc"])
        assert not s.palindrome_pairs(["abc", "bc"])
        assert s.palindrome_pairs(["abc", "ba"])
        assert s.palindrome_pairs(["abc", "cba"])
        assert s.palindrome_pairs(["leekf", "leeks", "or", "keel", "abc", "bc"])
