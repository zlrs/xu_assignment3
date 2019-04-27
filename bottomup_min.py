"""
纯递归版本的解法
"""


def ss(arr):
    if len(arr) == 0:
        return 0
    avg = sum(arr) / len(arr)
    ss_ = 0
    for cell in arr:
        ss_ += (cell - avg)**2
    return ss_


def rec(arr, k):
    costs = []
    length = len(arr)
    if k == 1:
        return ss(arr)

    for i_apart in range(k - 1, length - 1 + 1):
        cost_left_side  = rec(arr[0: i_apart]     , k-1)
        cost_right_side = rec(arr[i_apart: length], 1)
        cost_both_sides = cost_left_side + cost_right_side
        costs.append(cost_both_sides)

    return min(costs)
