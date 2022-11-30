from typing import List

"""
https://leetcode.com/problems/rotate-array/
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        방법0 
            - k 번 순회한다.
            - 배열을 옆으로 이동한다.


        방법1
            파이썬슬라이스로 처리한다.
            k 만큼 이동할 경우 k를 기준으로 두 개의 배열로 분리한다.
                - k 는 배열보다 작다고 가정(모듈러로 줄인다.), 0<=k<=105
                    - k = k % len(nums)
                    - example) len(nums) = 2, nums = [0, 1]
                        - k = 1일 경우
                        - [:-k], [len(nums) - k:]
                            - [0], [1]
                        - 뒤집어서 더 한다.
                            - [1, 0]
                    - example) len(nums) = 3
                        - k = 0, 3 일 경우 제자리
                            if 0 return
                        - k = 1일 경우
                            - 밀 배열 [:-1] = [0, 10], 앞 이동 배열[2:] = [20]
                                - [:-k], [len(nums] - k):]
                            - [20] + [0, 10]
                        - k = 22일 경우
                            - 밀 배열 [:-2] = [0], 앞 이동 배열[1:] = [10, 20]
                                - [:-k], [len(nums] - k):]
                            - [10, 20] + [0]
                    - example) len(nums) = 4, 0<=k<=105
                        TODO: 여기서 부터 풀기
        방법3
            책에서 슬라이스 처리하는 부분이 있다. 내 코드와 다르니 참조하자.
        """
        # t7 = dict(nums=[0, 10, 20], k=1, output=[20, 0, 10])
        #     assert [20, 0] == [20, 0, 10]
        len_nums = len(nums)
        k = k % len_nums
        if k == 0:
            return

        front = nums[:-k]
        back = nums[len_nums - k :]
        nums[:] = back + front

    def rotate0(self, nums: List[int], k: int) -> None:
        """
        방법0
            - k 번 순회한다.
            - 배열을 옆으로 이동한다.
                - 맨 끝에걸 temp 에 넣는다.
                - 전체 배열을 오른쪽으로 한칸 움직인다.
            시간 O(n*n)
            공간 O(1)
        """
        len_nums = len(nums)
        k = k % len_nums
        for _ in range(k):
            last = nums[-1]
            for i in range(len_nums - 1, 0, -1):
                nums[i] = nums[i - 1]
            nums[0] = last

    def rotate1(self, nums: List[int], k: int) -> None:
        """
        언제나 정렬되어야 한다.
        뒤집어 놓고 특정 인덱스를 기준으로 각각 뒤집으면 정렬된 상태의 배열을
        얻을 수 있다.
        """
        len_nums = len(nums)
        k = k % len_nums
        nums = nums[::-1]
        nums[:k] = list(reversed(nums[:k]))
        nums[k:] = list(reversed(nums[k:]))


def test_rotate():
    t1 = dict(nums=[0, 10], k=0, output=[0, 10])
    t2 = dict(nums=[0, 10], k=1, output=[10, 0])
    t3 = dict(nums=[0, 10], k=2, output=[0, 10])
    t4 = dict(nums=[0, 10], k=3, output=[10, 0])
    t5 = dict(nums=[0, 10], k=4, output=[0, 10])

    t6 = dict(nums=[0, 10, 20], k=0, output=[0, 10, 20])
    t7 = dict(nums=[0, 10, 20], k=1, output=[20, 0, 10])
    t8 = dict(nums=[0, 10, 20], k=2, output=[10, 20, 0])
    t9 = dict(nums=[0, 10, 20], k=3, output=[0, 10, 20])
    # ts = [t1, t2, t3, t4, t5]
    ts = [t1, t2, t3, t4, t5, t6, t7, t8, t9]
    s = Solution()

    for t in ts:
        s.rotate1(t["nums"], t["k"])
        assert t["nums"] == t["output"], t
