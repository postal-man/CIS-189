"""
Program: test_average_scores.py
Author: Liam P Reardon
Last date modified: 10/18/2023
Class: CIS-189
"""

import unittest
from dictionary_update import average_scores

class MyTestCase(unittest.TestCase):

    def test_average(self):
        # Arrange
        self.scores_dict = {"Test 1": 31, "Test 2": 34, "Test 3": 54}
        expected = 39.66666666  # 7 decimal places, remove one and see the test fail
        # Act
        actual = average_scores(self.scores_dict)
        # Assert
        self.assertAlmostEqual(expected, actual)

    def test_average_five(self):
        # Arrange
        self.scores_dict = {"Test 1": 85, "Test 2": 91, "Test 3": 89, "Test 4": 100, "Test 5": 100}
        expected = sum(self.scores_dict.values()) / len(self.scores_dict)
        # Act
        actual = average_scores(self.scores_dict)
        # Assert
        self.assertEqual(expected, actual)

    def test_average_zero(self):
        # Arrange
        self.scores_dict = {}

        # Act & Assert
        with self.assertRaises(ValueError):
            average_scores(self.scores_dict)

if __name__ == '__main__':
    unittest.main()
