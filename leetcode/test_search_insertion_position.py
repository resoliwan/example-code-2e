import math


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
            mid = math.floor((low + high) / 2)

            midval = nums[mid]
            if midval == target:
                return mid
            elif midval > target:
                high = mid - 1
            else:
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


test_search_insert1()
