# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/
# Companies
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
# Example 1:
#
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:
#
# Input: strs = [""]
# Output: [[""]]
# Example 3:
#
# Input: strs = ["a"]
# Output: [["a"]]


from collections import defaultdict
from typing import Any, List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        - 에너그램 찾기
            - 문자를 정렬한다.
            - 문자를 카운팅한다.
        - 정렬된 문자를 키로 만든다.
            - 딕셔너리에 넣는다.
        """

        res = defaultdict(list)
        for str in strs:
            key = "".join(sorted(str))
            res[key].append(str)

        return list(res.values())


def test_group_anagrams():
    s = Solution()

    t1 = dict(
        input=["eat", "tea", "tan", "ate", "nat", "bat"],
        output=sorted([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
    )
    t2 = dict(input=[""], output=[[""]])
    t3 = dict(input=["a"], output=[["a"]])

    ts: List[Any] = [t1, t2, t3]
    # ts: List[Any] = [t1]
    for t in ts:
        res = sorted([sorted(ele) for ele in s.groupAnagrams(t["input"])])
        output = sorted([sorted(ele) for ele in t["output"]])

        assert res == output
