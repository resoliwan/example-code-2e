"""
https://leetcode.com/problems/missing-number/
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.
Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
Constraints:

n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.
"""
from typing import List


class Solution:
    """
    두 개의 그룹의 차집합을 찾는 문제.

    아이디어1
        - 정렬 후, range(0, n)을 만들고 비교한다.
    아이디어2
        - range(0, n)을 만들고 for 문을 돌면서 맵 안에 있는지 확인한다.
    아이디어3
        - range(0, n)을 만들고 특정 수가 있는지 어래이에서 찾는다.
    아이디어4
        - 어래이를 만들고 빈 배열에 숫자대로 집어 넣는다. 빈 인덱스를 리턴한다.
    아이디어5.
        - 두 개 집합을 만들고 차집합을 구한다.

    """

    def missingNumber(self, nums: List[int]) -> int:
        nums_len = len(nums)
        s1 = set(range(0, nums_len + 1))
        s2 = set(nums)
        return s1.difference(s2).pop()


def test_missingNumber():
    t1 = dict(nums=[0, 1], output=2)
    t2 = dict(nums=[0, 1, 3], output=2)

    ts = [t1, t2]
    s = Solution()
    for t in ts:
        assert s.missingNumber(t["nums"]) == t["output"]
