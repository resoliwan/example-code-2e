# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
# https://leetcode.com/problems/pascals-triangle/

import math
from typing import List


class Solution:
    """
    num row 만큼 돌면서 여
        output 배열을 반든다. [[1]], [[1,1]]
        i 사이즈의 배열을 만든다. [0] = 1, [-1] = 1
            i=1 이면 [1] 리턴
            i=2 이면 [1, 1] 리턴
            i=3 이면 [1:-1]까지 돌면서 이전 인덱스 -1에 대하여 더한 값을
                넣는다.

        배열을 아웃풋에 추가한다.
    """

    def generate(self, num_rows: int) -> List[List[int]]:
        output = [[1], [1, 1]]
        for cur_rows in range(3, num_rows + 1):
            pre_arr = output[cur_rows - 2]
            cur_arr = [1] * cur_rows
            for j, _ in enumerate(cur_arr[1:-1], start=1):
                cur_arr[j] = pre_arr[j - 1] + pre_arr[j]

            output.append(cur_arr)

        return output[:num_rows]

    def generate2(self, num_rows: int) -> List[List[int]]:
        """
        결과 배열을 만든다.
        1, 2에 대한 결과값을 넣는다.
        numRows가 3보다 크거나 같다면
            - 3부터 num_rows + 1 만큼
            - numRows 크기에 1로 세팅된 배열을 만든다.
            - 방법 1
                - 전 배열을 가져와 1부터 루프를 돈다.
                - 원 배열의 같은 i에 전 배열의 이전 아이템과 i아이템을 더해서 할당한다.
        numRows를 키로 결과맵에 추가한다.
        키로 결과배열을 슬라이스 해서 리턴한다.
        """
        output = [[1], [1, 1]]
        for cur_rows in range(3, num_rows + 1):
            pre_arr = output[cur_rows - 2]
            cur_arr = [1] * cur_rows
            for i, _ in enumerate(pre_arr[1:], start=1):
                cur_arr[i] = pre_arr[i - 1] + pre_arr[i]

            output.append(cur_arr)

        return output[:num_rows]

    def generate3(self, num_rows: int) -> List[List[int]]:
        """
        XXX 에러난다. 오히려 바반을 만들고 복사하는게 빠를 수도?
        결과 배열을 만든다.
        1, 2에 대한 결과값을 넣는다.
        numRows가 3보다 크거나 같다면
            - 3부터 num_rows + 1 만큼
            - numRows 크기에 1로 세팅된 배열을 만든다.
            - 방법 2
                - 전 배열을 가져와 1부터 전 배열의 길이 반의 내림 만큼 루프를 돈다.
                - 현 배열의 i 아이템과 i 전 아이템의 값을 더한다.
                    - i 인덱스와 -i 인덱스에 값을 넣는다.
                - 만약 전배열이 짝수라면 반인덱스 아이템과  반 인덱스 아이템의 이후
                    아이템을 현 배열의 반인덱스에 추가한다.

        numRows를 키로 결과맵에 추가한다.
        키로 결과배열을 슬라이스 해서 리턴한다.
        """
        output = [[1], [1, 1]]
        for cur_rows in range(3, num_rows + 1):
            pre_arr = output[cur_rows - 2]
            cur_arr = [1] * cur_rows
            half_index = math.ceil(len(pre_arr))
            for i, _ in enumerate(pre_arr[1:half_index], start=1):
                val = pre_arr[i - 1] + pre_arr[i]
                cur_arr[i] = cur_arr[-(i + 1)] = val

            if len(pre_arr) % 2 == 0 and num_rows > 3:
                cur_arr[half_index] = pre_arr[half_index - 1] + pre_arr[half_index]

            output.append(cur_arr)

        return output[:num_rows]


def test_generate1():
    t1 = {"num_rows": 1, "output": [[1]]}
    t2 = {"num_rows": 2, "output": [[1], [1, 1]]}
    t3 = {"num_rows": 3, "output": [[1], [1, 1], [1, 2, 1]]}
    t5 = {
        "num_rows": 5,
        "output": [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]],
    }

    s = Solution()
    # ts = [t3]
    ts = [t1, t2, t3, t5]
    # ts = [t1]
    for t in ts:
        assert s.generate(t["num_rows"]) == t["output"]
