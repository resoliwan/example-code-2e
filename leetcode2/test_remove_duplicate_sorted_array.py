class Solution:
    def removeDuplicates(self, nums):
        s = set(nums)
        for i, val in enumerate(sorted(list(s))):
            nums[i] = val

        return len(s)

    def removeDuplicates1(self, nums):
        curr = nums[0]
        new_idx = 0
        for i in range(1, len(nums)):
            if curr != nums[i]:
                new_idx += 1
                curr = nums[i]
                nums[new_idx] = curr

        return new_idx + 1


def test_remove_duplicates():
    t1 = dict(nums=[1, 1, 2], out1=2, expect=[1, 2])
    t2 = dict(nums=[-1, 0, 0, 0, 0, 3, 3], out1=3, expect=[-1, 0, 3])
    s = Solution()
    for t in [t1, t2]:
        assert s.removeDuplicates(t["nums"]) == t["out1"]
        for i in range(0, t["out1"]):
            assert t["expect"][i] == t["nums"][i]


def test_remove_duplicates1():
    t1 = dict(nums=[1, 1, 2], out1=2, expect=[1, 2])
    t2 = dict(nums=[-1, 0, 0, 0, 0, 3, 3], out1=3, expect=[-1, 0, 3])
    s = Solution()
    for t in [t1, t2]:
        assert s.removeDuplicates1(t["nums"]) == t["out1"]
        for i in range(0, t["out1"]):
            assert t["expect"][i] == t["nums"][i]


test_remove_duplicates()
