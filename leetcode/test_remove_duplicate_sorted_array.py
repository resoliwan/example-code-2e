import math


class Solution(object):
    # pylint: disable=R0201
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)
        mid = math.floor(start + end)
        # for i, val in enumerate(nums):
        #     if val >= target:
        #         break
        #
        #     i += 1

        return i

    # pylint: disable=R0201
    def searchInsert1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        for i, val in enumerate(nums):
            if val >= target:
                break

            i += 1

        return i


def test_search_insert_example():
    e0 = dict(nums=[10, 20, 30, 40], target=10, out=0)
    s = Solution()

    for t in [e0]:
        assert s.searchInsert(t["nums"], t["target"]) == t["out"]


def test_search_insert():
    t1 = dict(nums=[1, 3, 5, 6], target=5, out=2)
    t2 = dict(nums=[1, 3, 5, 6], target=2, out=1)
    t3 = dict(nums=[1, 3, 5, 6], target=7, out=4)

    s = Solution()
    for t in [t1, t2, t3]:
        assert s.searchInsert(t["nums"], t["target"]) == t["out"]


test_search_insert_example()
