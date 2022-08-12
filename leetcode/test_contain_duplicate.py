# from collections import defaultdict
from collections import defaultdict


class Solution:
    def containsDuplicate(self, nums):
        counter = defaultdict(int)
        for i in range(len(nums)):
            if counter[nums[i]] > 0:
                return True
            counter[nums[i]] += 1
        return False


def test_s1():
    a = [2, 3].sort()
    print(a)
    s = Solution()
    assert s.containsDuplicate([1, 2]) is False
