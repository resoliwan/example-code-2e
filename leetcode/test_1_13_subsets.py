# https://leetcode.com/problems/subsets/
# 78. Subsets
# Medium
# Given an integer array nums of unique elements, return all possible
# subsets
#  (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:
#
# Input: nums = [0]
# Output: [[],[0]]
#
#
# Constraints:
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.

import unittest
from typing import Any, List


class Solution:
    def subsets(self, nums: List[int] | Any) -> List[List[int]] | Any:
        res = []
        sub = []
        self.subsets_recursion(nums, res, sub, 0)
        return res

    def subsets_recursion(
        self,
        nums: List[List[int]] | Any,
        res: List[List[int]],
        sub: List[List[int]],
        index: int,
    ) -> None:
        # 변수가 여러 역활을 하면서 지저분하게 되어 있다.
        # 이해할려고 2시간 정도 봤는데 보면 볼 수 록 추상화 되어 있지 않고
        # 정말 세부적으로 구현한 느낌.
        # t1 = dict(input=[0], output=[[], [0]])
        # t2 = dict(input=[0, 1], output=[[], [0], [1], [0, 1]])
        # t3 = dict(
        #     input=[0, 1, 2], output=[[], [0], [1], [2], [0, 1], [0, 2], [1, 2], [0, 1, 2]]
        # )
        if len(sub) > len(nums):
            return
        res.append(sub.copy())
        for i in range(index, len(nums)):
            sub.append(nums[i])
            self.subsets_recursion(nums, res, sub, i + 1)
            sub.pop()

    def cartesian_product(
        self,
        op1_arr: List[List[bool]] = [[True], [False]],
        op2_arr: List[List[bool]] = [[True], [False]],
        num: int = 1,
    ):
        if num <= 0:
            return op1_arr

        result = []
        for e1 in op1_arr:
            for e2 in op2_arr:
                temp = []
                temp.extend(e1)
                temp.extend(e2)
                result.append(temp)

        return self.cartesian_product(result, op2_arr, num - 1)

    def subsets_res(self, nums: List[int] | Any) -> List[List[int]] | Any:
        """
        0. key로 hash를 사용 할 수 있다.
            - 그냥 string 사용해도 될듯.
        2. 재귀로 넣는다. set에 계속 넣는다.
            - base 는 size_of_subset >= 0
            - 줄어는건 size_of_subset -= 1
            - 자기 호출
            - 함수에서 집합의 원소의 개수가 num_len인 모든 부분집합을 리턴한다.
        3. cartesian_product 를 만든다. true, false 에 따라서 배열에 집어 넣는다.
        """
        len_num = len(nums)
        bool_arr = []
        if len_num == 0:
            return [[]]
        elif len_num == 1:
            bool_arr = [[True], [False]]
        else:
            bool_arr = self.cartesian_product(
                [[True], [False]], [[True], [False]], len_num - 1
            )

        res = []
        for arr in bool_arr:
            temp = [n for selected, n in zip(arr, nums) if selected]
            res.append(temp)

        return sorted(res)

    def fixed_subset(self, nums: List[int], size_of_subset) -> List[List[int]]:
        if size_of_subset >= 0:
            return []
        """
        [0, 1, 2, 3]
        size_of_subset = 2  ->  [0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]
        size_of_subset = 3  ->  [1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]
        - [0, 1, 2, 3]
        - 제거한다. 
            - arrary.pop()
            - 나온것에 대해서 또 한 개를 빼는 방식으로 접근하면 결과 값이 너무
              커진다.
        - cartesian product 한다.
            - 확률 맵 만들듯이 한 개씩 추가 할 수는 없나? 

        """

        return self.fixed_subset(nums, size_of_subset - 1)

    def wrong_subsets(self, nums: List[int] | Any) -> List[List[int]] | Any:
        """
        0. key로 hash를 사용 할 수 있다.
            - 그냥 string 사용해도 될듯.
        1. 아이디어 포문을 돌면서 원소의 개수 대로 부분집합을 만들고 set에 계속 넣는다.
            - 원소의 개수 배열을 만든다. 1, 2, 3
            - 돌면서 넣는다.
        2. 재귀로 넣는다. set에 계속 넣는다.
        """
        s = set()
        s.add(())  # case 0
        for cnt in range(1, len(nums) + 1):
            for j in range(0, len(nums) + 1 - cnt):
                """
                x 슬라이스로 푼다.
                    윈도우 함수에 가깝다.
                        -> 이렇게 하면 안된다. 3번에서 0,2 가 안 나온다.
                            [[], [0], [0, 1], [0, 1, 2], [0, 2], [1], [1, 2], [2]]
                for문 돈다.
                    -

                1 => 0  1  2
                2 => 0,1  1,2
                3 => 0,1,2
                """
                s.add(tuple(nums[j : j + cnt]))
        return sorted([list(t) for t in s])

    def subsets_tunning(self, nums: List[int] | Any) -> List[List[int]] | Any:
        res = []
        len_nums = len(nums)
        default_bits = 1 << len_nums
        for i in range(2**len_nums):
            mask = bin(default_bits | i)[3:]
            res.append([nums[j] for j in range(len(nums)) if mask[j] == "1"])

        return res

    def subsets_bit(self, nums: List[int] | Any) -> List[List[int]] | Any:
        """
        [F,F,T] 즉 조합 배열은 [0,0,1] 로 바꿀 수 있고 이건 2진수와 같다.
        000, 001, 010, 011, 100, 101, 110, 111
          0,   1,   2,   3,   4,   5,   6,   7
        만약 배열의 수가 3이라면 2^3 만큼의 수를 만들면된다.
        2^n 그리고 만들어진 비트열을 선택기준으로 기존 리스트에서 새로운
        리스트를 뽑으면 된다.
        """
        bitmasks = []
        default_bits = 1 << len(nums)
        for i in range(2 ** len(nums)):
            # print(bin(default_bits | i)[3:])
            bitmasks.append(bin(default_bits | i)[3:])

        res = []
        for mask in bitmasks:
            # res.append([nums[j] for j in range(len(nums)) if mask[j] == "1"])
            res.append([num for bit, num in zip(mask, nums) if bit == "1"])

        return res


def test_bit():
    t1 = dict(input=[0], output=[[], [0]])
    t2 = dict(input=[0, 1], output=[[], [0], [1], [0, 1]])
    t3 = dict(
        input=[0, 1, 2], output=[[], [0], [1], [2], [0, 1], [0, 2], [1, 2], [0, 1, 2]]
    )
    ts = [t3]
    s = Solution()
    for t in ts:
        # print(s.subsets(t["input"]))
        # print(sorted(t["output"]))
        assert sorted(s.subsets_bit(t["input"])) == sorted(t["output"])


def test_catesian_product():
    s = Solution()
    res1 = s.cartesian_product([[True], [False]], [[True], [False]], 1)
    assert res1 == [[True, True], [True, False], [False, True], [False, False]]

    res2 = s.cartesian_product([[True], [False]], [[True], [False]], 2)
    assert res2 == [
        [True, True, True],
        [True, True, False],
        [True, False, True],
        [True, False, False],
        [False, True, True],
        [False, True, False],
        [False, False, True],
        [False, False, False],
    ]


def test_subset():
    t1 = dict(input=[0], output=[[], [0]])
    t2 = dict(input=[0, 1], output=[[], [0], [1], [0, 1]])
    t3 = dict(
        input=[0, 1, 2], output=[[], [0], [1], [2], [0, 1], [0, 2], [1, 2], [0, 1, 2]]
    )
    ts = [t1, t2, t3]
    s = Solution()
    for t in ts:
        # print(s.subsets(t["input"]))
        # print(sorted(t["output"]))
        assert s.subsets(t["input"]) == sorted(t["output"])
