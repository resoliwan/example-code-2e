# https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1
# Given two sorted arrays arr1[] and arr2[] of sizes n and m in non-decreasing order.
# Merge them in sorted order without using any extra space.
# Modify arr1 so that it contains the first N elements and modify arr2 so that
# it contains the last M elements.
from typing import List


class Solution:
    def merge(self, arr1, arr2, n, m):
        i = n + m
        i2 = m

        while i > 0:
            i -= 1
            if i >= n:
                i2 -= 1
                if arr1[-1] > arr2[i2]:
                    arr2[i2], arr1[-1] = arr1[-1], arr2[i2]
                    # sort arr1
                elif arr1[-1] <= arr2[i2]:
                    pass
            elif i < n:
                pass

            for j in range(1, n):
                if arr1[j - 1] > arr1[j]:
                    arr1[j], arr1[j - 1] = arr1[j - 1], arr1[j]
                elif arr1[j - 1] <= arr1[j]:
                    pass

    """
    # arr1,2 정렬
    - space complexity O(1)
    - time complexity O(mn)
    - 둘 다 정렬되어 있음으로 arr1을 기준으로 정렬시킨다.
    - arr1[i]과 arr2[0]을 비교 함으로 arr2의 정렬이 어긋날 수 있다. 그럼으로 교환이 발생하면 arr2를 재정렬한다.
    - arr1을 순회한다.
    - 각 arr1의 요소마다.
    -   arr1의 요소와 arr2의 첫번째 요소를 비교한다.
    -   arr1의 요소가 arr2의 요소보다 크다면 두 요소를 교환한다.
    -   arr2의 정렬이 어긋 날 수 있음으로 매회 arr2를 재정렬한다.
    ### arr2 정렬
    -         arr2에서 단 한개의 요소만 어긋나 있음으로 삽입 정렬을 구현한다.
    -         첫요소가 둘째 요소보다 크다면 재 정렬한다.
    -         arr2의 첫 요소를 temp에 넣고 arr2를 순회하면서 첫요소보다 큰 요소를 찾기 전까지 각 요소를 한칸 앞으로 이동시킨다.
                첫 요소 보다 크거나 같은 요소를 찾으면 그 요소 앞에 temp를 추가한다. 정렬을 멈춘다.
    """

    def merge2(self, arr1, arr2, n, m):
        i = 0
        while i < n:
            if arr1[i] > arr2[0]:
                arr1[i], arr2[0] = arr2[0], arr1[i]

                if arr2[0] > arr2[1]:
                    temp = arr2[0]
                    j = 1
                    while j < m:
                        if temp > arr2[j]:
                            arr2[j - 1] = arr2[j]
                        elif temp <= arr2[j]:
                            break
                        else:
                            raise Exception(i, j)
                        j += 1

                    arr2[j - 1] = temp

            elif arr1[i] <= arr2[0]:
                pass
            i += 1

    def merge3(self, nums1: List[int], nums2: List[int], m: int, n: int) -> None:
        for i, nums1_item in enumerate(nums1):
            if nums1_item > nums2[0]:
                nums1[i] = nums2[0]
                nums2[0] = nums1_item

                # 먼가 혼잡하다. 나중에 해보자
                for k, item in enumerate(nums2[1:], start=1):
                    nums2[k - 1] = nums2[k]

                    if nums1_item >= item:
                        nums2[k] = nums1_item
                        break


def test_merge2():
    t1 = {
        "arr1": [0, 1],
        "arr2": [2, 3],
        "n": 2,
        "m": 2,
        "output_arr1": [0, 1],
        "output_arr2": [2, 3],
    }
    t2 = {
        "arr1": [2, 3],
        "arr2": [0, 1],
        "n": 2,
        "m": 2,
        "output_arr1": [0, 1],
        "output_arr2": [2, 3],
    }
    t3 = {
        "arr1": [1, 3, 5, 7],
        "arr2": [0, 2, 6, 8, 9],
        "n": 4,
        "m": 5,
        "output_arr1": [0, 1, 2, 3],
        "output_arr2": [5, 6, 7, 8, 9],
    }
    #
    ts = [t1, t2, t3]
    # ts = [t2]
    for t in ts:
        s = Solution()
        s.merge2(t["arr1"], t["arr2"], t["n"], t["m"])
        assert t["arr1"] == t["output_arr1"]
        assert t["arr2"] == t["output_arr2"]


# >           assert t["arr1"] == t["output_arr1"]
# E           assert [0, 2] == [0, 1]
# E             At index 1 diff: 2 != 1
# E             Use -v to get more diff

# >           assert t["arr2"] == t["output_arr2"]
# E           assert [1, 1] == [2, 3]
# E             At index 0 diff: 1 != 2
# E             Use -v to get more diff


def test_merge1():
    t1 = {
        "arr1": [1, 3, 5, 7],
        "arr2": [0, 2, 6, 8, 9],
        "n": 4,
        "m": 5,
        "output_arr1": [0, 1, 2, 3],
        "output_arr2": [5, 6, 7, 8, 9],
    }

    ts = [t1]
    for t in ts:
        s = Solution()
        s.merge(t["arr1"], t["arr2"], t["n"], t["m"])
        assert t["arr1"] == t["output_arr1"]
        assert t["arr2"] == t["output_arr2"]
