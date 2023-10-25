#!/usr/bin/env python3

import statistics
import math


class Stats:

    @classmethod
    def get_mean_of_means_with_stdevs(cls, means: list, stdevs: list) -> tuple:
        mean_ = None
        if cls.is_same_length((means, stdevs)):
            mean_ = statistics.mean(means)
        stdev_ = cls.get_stdev_from_stdevs(stdevs)

        return mean_, stdev_

    @classmethod
    def get_stdev_from_stdevs(cls, stdevs: list) -> float:
        return math.sqrt(sum([x * x for x in stdevs]))

    @classmethod
    def is_same_length(cls, *args: tuple) -> bool:
        bools: list = []
        idx = 0
        while idx + 1 < len(args):
            bools.append(len(args[idx]) == len(args[idx + 1]))
            idx += 1
        return all(bools)
