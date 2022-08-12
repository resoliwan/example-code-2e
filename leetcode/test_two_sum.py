from collections import defaultdict


class Solution(object):
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for op1i, op1 in enumerate(nums):
            op2StartIdx = op1i + 1
            for op2i, op2 in enumerate(nums[op2StartIdx:]):
                if op1 + op2 == target:
                    return [op1i, op2i + op2StartIdx]

        return [-1, -1]

    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return [-1, -1]

    def twoSum3(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # make map
        map = defaultdict(list)
        # set val: index
        for idx, val in enumerate(nums):
            map[val].append(idx)

        for op1, op1_idxs in map.items():
            # op1 + op2 = target
            op2 = target - op1
            op2_idxs = map.get(op2, [])
            if len(op2_idxs) > 1:
                return [op1_idxs[0], op2_idxs[1]]
            elif len(op2_idxs) > 0:
                if op1_idxs[0] == op2_idxs[0]:
                    continue
                return [op1_idxs[0], op2_idxs[0]]

        return [-1, -1]

    def twoSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # make map
        map = {}
        # set val: index
        for op1_idx, op1 in enumerate(nums):
            op2 = target - op1
            op2_idx = map.get(op2)
            if op2_idx is not None and op1_idx != op2_idx:
                return sorted([op1_idx, op2_idx])

            map[op1] = op1_idx

        return [-1, -1]


def test_twoSum():
    s = Solution()
    t1 = dict(nums=[2, 7, 11, 15], target=9, output=[0, 1])
    t2 = dict(nums=[3, 3], target=6, output=[0, 1])
    t3 = dict(nums=[2, 3, 11, 3], target=6, output=[1, 3])

    for t in [t1, t2, t3]:
        assert s.twoSum1(t["nums"], t["target"]) == t["output"]
        assert s.twoSum2(t["nums"], t["target"]) == t["output"]
        assert s.twoSum3(t["nums"], t["target"]) == t["output"]
        assert s.twoSum4(t["nums"], t["target"]) == t["output"]
