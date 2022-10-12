# https://leetcode.com/problems/merge-sorted-array/
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
# representing the number of elements in nums1 and nums2 respectively.
#
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


import copy
from math import inf
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = [inf] * n

        len_result = m + n
        i1 = 0
        i2 = 0
        while i1 < len_result and i2 < n:
            if nums1[i1] <= nums2[i2]:
                pass
            elif nums1[i1] > nums2[i2]:
                for j in range(len_result - 1, i1, -1):
                    nums1[j] = nums1[j - 1]

                nums1[i1] = nums2[i2]
                i2 += 1

            i1 += 1

    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        res = nums1
        nums1 = copy.deepcopy(nums1)

        i1 = 0
        i2 = 0
        for i in range(0, len(res)):
            if i1 < m and i2 < n:
                if nums1[i1] <= nums2[i2]:
                    res[i] = nums1[i1]
                    i1 += 1
                else:
                    res[i] = nums2[i2]
                    i2 += 1
            elif i1 < m and i2 >= n:
                res[i] = nums1[i1]
                i1 += 1
            elif i1 >= m and i2 < n:
                res[i] = nums2[i2]
                i2 += 1
            else:
                raise Exception(i1, i2)

    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        tot = m + n
        i = tot
        i1 = m - 1
        i2 = n - 1
        while i > 0:
            i -= 1
            if i1 >= 0 and i2 >= 0:
                if nums1[i1] >= nums2[i2]:
                    nums1[i] = nums1[i1]
                    i1 -= 1
                elif nums1[i1] < nums2[i2]:
                    nums1[i] = nums2[i2]
                    i2 -= 1
                else:
                    Exception()
            elif i1 >= 0 and i2 < 0:
                pass
            elif i1 < 0 and i2 >= 0:
                nums1[i] = nums2[i2]
                i2 -= 1
            else:
                raise Exception("should not occur", i1, i2)


def test_code():
    print(list(range(4, 0, -1)))
    assert False


def test_merge2():
    s = Solution()
    t1 = {
        "nums1": [0, 10, 0, 0],
        "m": 2,
        "nums2": [20, 30],
        "n": 2,
        "Output": [0, 10, 20, 30],
    }
    t2 = {
        "nums1": [20, 30, 0, 0],
        "m": 2,
        "nums2": [10, 40],
        "n": 2,
        "Output": [10, 20, 30, 40],
    }
    t3 = {
        "nums1": [10, 50, 0, 0],
        "m": 2,
        "nums2": [10, 40],
        "n": 2,
        "Output": [10, 10, 40, 50],
    }
    t4 = {
        "nums1": [1],
        "m": 1,
        "nums2": [],
        "n": 0,
        "Output": [1],
    }

    # [1,0]
    t5 = {
        "nums1": [2, 0],
        "m": 1,
        "nums2": [1],
        "n": 1,
        "Output": [1, 2],
    }
    ts = [t1, t2, t3, t4, t5]

    for t in ts:
        s.merge2(t["nums1"], t["m"], t["nums2"], t["n"])
        assert t["nums1"] == t["Output"]


# test_merge1()


def test_merge1():
    s = Solution()
    t1 = {
        "nums1": [0, 10, 30, 0, 0, 0],
        "m": 3,
        "nums2": [20, 40, 50],
        "n": 3,
        "Output": [0, 10, 20, 30, 40, 50],
    }
    ts = [t1]

    for t in ts:
        s.merge(t["nums1"], t["m"], t["nums2"], t["n"])
        assert t["nums1"] == t["Output"]


# test_merge1()
