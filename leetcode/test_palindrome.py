# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
# removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
# Example 1:
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:
#
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
#
from typing import Any, List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        1. 알파 뉴메릭만 뽑아서 만든다.
            - 정규식을 사용한다.
            - 리스트 배열을 만들고 배열사용
            - s가 불변이라 다른 방식을 쓸 수 없다.
        2. 스트링의 반이 같은지 확인한다.
            - 인덱스 역으로 뒤집으먼 됨.
        """

        str = [char for char in s.lower() if char.isalnum()]
        return str == str[::-1]


def test_str():
    str = "abc"

    assert str[::-1] == "cba"


def test_is_palindrome():
    t1 = dict(input="A man, a plan, a canal: Panama", output=True)
    t2 = dict(input="race a car", output=False)
    t3 = dict(input=" ", output=True)
    s = Solution()

    ts: List[Any] = [t1, t2, t3]
    # ts: List[Any] = [t2]
    for t in ts:
        assert s.isPalindrome(t["input"]) == t["output"]
