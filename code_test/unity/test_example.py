#
# This is a demo task.
#
# Write a function:
#
# def solution(A)
#
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
#
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
#
# Given A = [1, 2, 3], the function should return 4.
#
# Given A = [−1, −3], the function should return 1.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].


def get_positive_integer(sorted_arr):
    for i, val in enumerate(sorted_arr):
        if val > 0:
            return i

    return -1


def solution(A):
    """
    get_positive_integer -1
        return 1
    else
        A[pos_idx:] range(1, len_A)
                    [1,2,3,4,5]
        a_idx = 0
        for val in range(1, len_A)
            if A[a_idx] == val:
                continue
            else:
                return val
    """
    A = sorted(set(A))
    pos_idx = get_positive_integer(A)
    if pos_idx == -1:
        return 1

    pos_arr = A[pos_idx:]

    pos_integer = 1
    for val in pos_arr:
        if val != pos_integer:
            return pos_integer

        pos_integer += 1

    return pos_integer


def test_solution():
    t1 = dict(input=[1, 3, 6, 4, 1, 2], output=5)
    t2 = dict(input=[1, 2, 3], output=4)
    t3 = dict(input=[-1, -3], output=1)
    t4 = dict(input=[-1, -3, 1], output=2)
    # ts = [t1, t2, t3, t4]
    ts = [t1]

    for t in ts:
        assert solution(t["input"]), t["output"]
