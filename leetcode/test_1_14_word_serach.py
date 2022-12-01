# https://leetcode.com/problems/word-search/
# 79. Word Search
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells
# are horizontally or vertically neighboring. The same letter cell may not be used more than once.
from collections import Counter, namedtuple
from typing import List


class Solution:
    def is_include_number_of_characters(self, a_word, b_word):
        a_dic = Counter(a_word)
        b_dic = Counter(b_word)

        res = True
        for char in b_dic:
            if a_dic[char] - b_dic[char] < 0:
                res = False
                break

        return res

    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        [( A, 0, 0 ), ( B, 0, 1 ), ( C, 1, 0 ), ( D, 1, 1 )]
        res = list
        - 재귀로 푼다.
            - 4방에 없으면 리턴
                - 한번 사용한 것은 판을 변경한다.
        1. 시작점을 찾는다.
            각 시작점 순서로
        2. 4방에 다음을 찾는다.
            4방 순서로 다음을 찾는다.
            get4side((A, 0, 0))
            [북, 서, 남, 동]
            -> [[]]
        3. 될때까지 찾는다.


        1. 보드 배열의 모든 요소를 순회한다.
        2. word[0]과 board[x][y]요소가 같다면
            - 재귀호출

            - x, y가 보드를 벗어나는지 확인
            - word[i]와 board[x][y]가 같은지 확인
                - 같다면 방문했다는 표시로 board[x][y]의 . 를 변경.
            - board[x-1][y]와 다음 문자로 호출
            - board[x+1][y]와 다음 문자로 호출
            - board[x][y-1]와 다음 문자로 호출
            - board[x][y2+]와 다음 문자로 호출


        """
        if not self.is_include_number_of_characters(
            "".join(["".join(row) for row in board]), word
        ):
            return False

        for x, row in enumerate(board):
            for y, col in enumerate(row):
                if col == word[0] and self.is_word_exist(x, y, word, board):
                    return True

        return False

    def is_word_exist(self, x, y, word, board):
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[x]):
            return False

        if word[0] != board[x][y]:
            return False

        if len(word) == 1:
            return True

        board[x][y] = "."

        for next_x, next_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if self.is_word_exist(next_x, next_y, word[1:], board):
                return True

        board[x][y] = word[0]
        return False

    def get_word(self, res):
        return "".join([ele[0] for ele in res])


def test_simple_exist():
    t0 = dict(
        board=[["A", "B"], ["C", "D"], []],
        word="AB",
        output=True,
    )
    t1 = dict(
        board=[["A", "B"], ["C", "D"], []],
        word="BC",
        output=False,
    )
    t2 = dict(
        board=[["A", "B"], ["C", "D"], []],
        word="ABDC",
        output=True,
    )
    t3 = dict(
        board=[["A", "B"], ["C", "D"], ["C", "D"]],
        word="ABDCCD",
        output=True,
    )

    s = Solution()
    ts = [t0, t1, t2, t3]
    # ts = [t1]
    for t in ts:
        print(t)
        assert s.exist(t["board"], t["word"]) == t["output"]


def test_real_exist():
    t1 = dict(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="ABCCED",
        output=True,
    )
    t2 = dict(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="SEE",
        output=True,
    )
    t3 = dict(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="ABCB",
        output=False,
    )

    s = Solution()
    ts = [t1, t2, t3]
    for t in ts:
        assert s.exist(t["board"], t["word"]) == t["output"]


def test_real_slow_exist():
    t4 = dict(
        board=[
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
            ["A", "A", "A", "A", "A", "A"],
        ],
        word="AAAAAAAAAAAAAAB",
        output=False,
    )
    s = Solution()
    ts = [t4]
    for t in ts:
        assert s.exist(t["board"], t["word"]) == t["output"]


def test_is_include_number_of_characters():
    s = Solution()
    res = s.is_include_number_of_characters("aa", "aa")
    assert res

    res = s.is_include_number_of_characters("aa", "ab")
    assert res is False

    res = s.is_include_number_of_characters("aa", "aaa")
    assert res is False

    res = s.is_include_number_of_characters("aaccc", "ac")
    assert res

    res = s.is_include_number_of_characters("ABCESFCSADEE", "ABCCED")
    assert res
