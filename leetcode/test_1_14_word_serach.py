# https://leetcode.com/problems/word-search/
# 79. Word Search
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells
# are horizontally or vertically neighboring. The same letter cell may not be used more than once.
# 시간에서 아웃.
import copy
from collections import Counter, namedtuple
from typing import List, Tuple

FourSide = namedtuple("FourSide", ["east", "south", "north", "west"])


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

    def exist(self, raw_board: List[List[str]], word: str) -> bool:
        """
        [( A, 0, 0 ), ( B, 0, 1 ), ( C, 1, 0 ), ( D, 1, 1 )]
        res = list
        - 재귀로 푼다.
            - 4방에 없으면 리턴
                - 한번 사용한 것은 4방 찾을 때 안나오게 제약
        1. 시작점을 찾는다.
            각 시작점 순서로
        2. 4방에 다음을 찾는다.
            4방 순서로 다음을 찾는다.
            get4side((A, 0, 0))
            [북, 서, 남, 동]
            -> [[]]
        3. 될때까지 찾는다.
        """
        if not self.is_include_number_of_characters(
            "".join(["".join(row) for row in raw_board]), word
        ):
            return False

        res = list()
        board = self.get_point_board(raw_board)
        for row in board:
            for point in [p for p in row if p[0] == word[0]]:
                res.append(point)
                self.append_next_point(1, point, res, word, board)

                if self.get_word(res) == word:
                    return True
                else:
                    res = list()

        return self.get_word(res) == word

    def get_word(self, res):
        return "".join([ele[0] for ele in res])

    def append_next_point(
        self,
        next_idx: int,
        point: List,
        res: List,
        word: str,
        board: List[List],
    ) -> None:
        if next_idx >= len(word):
            return

        len_original_res = len(res)
        sides = [s for s in self.get4side(board, point) if s is not None]
        for side in [side for side in sides if side[0] == word[next_idx]]:
            if side in res:
                continue

            res.append(side)
            self.append_next_point(next_idx + 1, side, res, word, board)

            if self.get_word(res) == word:
                break
            else:
                while len_original_res < len(res):
                    res.pop()

    def get4side(self, board: List[List], point: List):
        north = self.get_point(board, ("", point[1] - 1, point[2] + 0))
        west = self.get_point(board, ("", point[1] + 0, point[2] - 1))
        south = self.get_point(board, ("", point[1] + 1, point[2] + 0))
        east = self.get_point(board, ("", point[1] + 0, point[2] + 1))

        return FourSide(
            east,
            south,
            north,
            west,
        )

    def get_point(self, board, point):
        if point[1] < 0 or point[2] < 0:
            return None

        result = None
        try:
            result = board[point[1]][point[2]]
        except IndexError:
            result = None

        return result

    def get_point_board(self, raw_board):
        board = [[] for _ in range(len(raw_board))]
        for row_i, row in enumerate(raw_board):
            for col_i, col in enumerate(row):
                board[row_i].append((col, row_i, col_i))

        return board


def test_get_4_side():
    t0 = dict(
        board=[["A", "B"], ["C", "D"]],
        word="AB",
        output=True,
    )
    s = Solution()
    board = s.get_point_board(t0["board"])
    sides = s.get4side(board, ("A", 0, 0))
    assert sides.north is None
    assert sides.west is None
    assert sides.south == ("C", 1, 0)
    assert sides.east == ("B", 0, 1)

    sides = s.get4side(board, ("D", 1, 1))
    assert sides.north == ("B", 0, 1)
    assert sides.west == ("C", 1, 0)
    assert sides.south is None
    assert sides.east is None


def test_get_point_board():
    t0 = dict(
        board=[["A", "B"], ["C", "D"]],
        word="AB",
        output=True,
    )
    s = Solution()

    board = s.get_point_board(t0["board"])
    assert board == [[("A", 0, 0), ("B", 0, 1)], [("C", 1, 0), ("D", 1, 1)]]


def test_get_point():
    t0 = dict(
        board=[["A", "B"], ["C", "D"], []],
        word="AB",
        output=True,
    )
    s = Solution()
    board = s.get_point_board(t0["board"])
    a = s.get_point(board, ("", 0, 0))
    assert a == ("A", 0, 0)
    e = s.get_point(board, ("", 2, 2))
    assert e is None


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
    # ts = [t0, t1, t2, t3]
    ts = [t3]
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
