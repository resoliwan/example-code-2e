from collections import defaultdict
from math import inf
from typing import List

# https://leetcode.com/problems/majority-element/
"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example 1:
    Input: nums = [3,2,3]
    Output: 3
Example 2:
    Input: nums = [2,2,1,1,1,2,2]
    Output: 2
Constraints:
    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109

Follow-up: Could you solve the problem in linear time and in O(1) space?
nop
"""


class Solution:
    """
    # 방법 1
    - time O(n)
    - space O(n)

    카운팅을 map 으로 한다.
    nums 안에 모든 num에 대해서 루프를 돈다.
    맵을 만들고 1을 더한다. 끝나면 가장 큰 숫자를 리턴한다.
    """

    def majorityElement(self, nums: List[int]) -> int:
        m = defaultdict(int)
        for num in nums:
            m[num] += 1

        max_item = dict(num=-inf, cnt=-inf)
        for num, cnt in m.items():
            if max_item["cnt"] < cnt:
                max_item = dict(num=num, cnt=cnt)

        return max_item["num"]

    """
    # 방법 2
    - time O(n * lon n)
    - space O(1)
    - max 값을 사용한다.
    - 근데 그럴려면 솔팅해야 한다.
    """

    def majorityElement2(self, nums: List[int]) -> int:
        return sorted(nums)[int(len(nums) / 2)]


def test_majority_element():
    t1 = dict(nums=[3, 2, 3], output=3)
    t2 = dict(nums=[2, 2, 1, 1, 1, 2, 2], output=2)
    t3 = dict(nums=[1, 2, 1], output=1)

    ts = [t1, t2, t3]
    # ts = [t1]
    s = Solution()
    for t in ts:
        assert s.majorityElement2(t["nums"]) == t["output"]
