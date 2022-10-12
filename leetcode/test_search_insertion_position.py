# https://leetcode.com/problems/search-insert-position/
# Given a sorted array of distinct integers and a target value,
# return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.

# t1 = dict(nums=[0, 10, 20, 30], target=20, output=2)
# t2 = dict(nums=[0, 10, 20, 30], target=5, output=1)


class Solution:
    def searchInsert(self, nums, target):
        i = -1
        for i, val in enumerate(nums):
            if val >= target:
                return i

        return i + 1

    def searchInsert1(self, nums, target):
        index = 0
        while index < len(nums):
            if nums[index] >= target:
                break
            index += 1

        return index

    def searchInsert2(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = int((low + high) / 2)

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1

        return low


def test_search_insert1():
    s = Solution()
    # t1 = dict(nums=[1, 3, 5, 6], target=5, output=2)
    t2 = dict(nums=[1, 3, 5, 6], target=2, output=1)
    # t3 = dict(nums=[1, 3, 5, 6], target=7, output=4)
    # for t in [t1, t2, t3]:
    for t in [t2]:
        # assert t["output"] == s.searchInsert(t["nums"], t["target"])
        # assert t["output"] == s.searchInsert1(t["nums"], t["target"])
        assert t["output"] == s.searchInsert2(t["nums"], t["target"])


def test_simple_example_search_insert():
    s = Solution()
    t1 = dict(nums=[0, 10, 20, 30], target=20, output=2)
    t2 = dict(nums=[0, 10, 20, 30], target=5, output=1)
    # t3 = dict(nums=[1, 3, 5, 6], target=7, output=4)
    # for t in [t1, t2, t3]:
    for t in [t1]:
        # assert t["output"] == s.searchInsert(t["nums"], t["target"])
        # assert t["output"] == s.searchInsert1(t["nums"], t["target"])
        assert t["output"] == s.searchInsert2(t["nums"], t["target"])


test_search_insert1()
