# python test_find_matching_pair.py

import unittest

from find_matching_pair import funtion_find_matching_pair

class TestFunction(unittest.TestCase):
    def test_correct_sum(self):
        result = funtion_find_matching_pair([2,3,6,7], 9)

        assert result == "OK, matching pair( 3 , 6 )"

    def test_incorrect_sum(self):
        result = funtion_find_matching_pair([1,3,3,7], 9)

        assert result == "No"

if __name__ == '__main__':
    unittest.main(exit=False)
