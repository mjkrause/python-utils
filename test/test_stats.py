#!/usr/bin/env python3

import unittest
from src.stats import Stats


class TestStats(unittest.TestCase):

    def test_get_stdev_from_stdevs(self):
        means = [1, 2, 3]
        stdevs = [4, 5, 6]
        expected = (2, 8.774964387392123)
        observed = Stats.get_mean_of_means_with_stdevs(means=means, stdevs=stdevs)
        self.assertEqual(expected, observed)

    def test_is_same_length(self):
        arr1 = [1, 2, 3]
        arr2 = [4, 5, 6]
        self.assertTrue(Stats.is_same_length(arr1, arr2))

        arr1 = [1, 2, 3]
        arr2 = [4, 5]
        self.assertFalse(Stats.is_same_length(arr1, arr2))

        arr1 = [1, 2, 3]
        arr2 = [4, 5, 6]
        arr3 = [7, 8, 9]
        self.assertTrue(Stats.is_same_length(arr1, arr2))


if __name__ == '__main__':
    unittest.main()
