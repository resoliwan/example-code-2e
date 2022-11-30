def sum_for(nums):
    tot = 0
    for n in nums:
        tot += n

    return tot


def test_sum_for():
    assert sum_for([1, 2, 3, 4]) == 10


def sum_recur(nums):
    if len(nums) <= 1:
        return nums[0]

    return nums[0] + sum_recur(nums[1:])


def test_sum_recur():
    assert sum_recur([1, 2, 3, 4]) == 10
