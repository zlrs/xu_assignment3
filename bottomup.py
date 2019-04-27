# 现有一个不严格单増的正整数数组（包含n个元素），需要将其分为k组，使每组的「离均差平方和」之和最小。输出这个最小值。
# 离均差平方和（SS，sum of squares of deviation from mean）  （即不用除以元素个数的方差）
#
# 输入第一行为 n和k 的值，第二行为以空格分隔的n个数。
import time  # 性能测试
import pprint

keeper = {
    # (i, j): cost   i: inclusive; j:exclusive
}


# 计算一个序列的离均差平方和(ss)
def ss(arr):
    if len(arr) == 0:
        return 0
    avg = sum(arr) / len(arr)
    ss_ = 0
    for cell in arr:
        ss_ += (cell - avg)**2
    return ss_


def rec(arr, n, k, rec_top=True):
    """
    返回答案.
    利用递增条件：因为是递增，所以为了使ss最小，同一组内的元素必定是连续的
    时间复杂度：纯递归是 O((n-k)^2)。利用keeper后是（性能测试表明绝对用时减少了三倍多，但时间复杂度不知道如何计算）
    :param arr: 数组
    :type n: 数组长度 i.e. len(arr)
    :param k: 份数：将数组切分成 k 份
    :param rec_top: 表明是否为递归算法的顶层调用者。函数内对自身的调用在传参时必须设置 rec_top 为False
    :return: 目标值
    """

    if k == 1:
        if (0, n) in keeper:
            return keeper[(0, n)]
        else:
            t = ss(arr)
            keeper[(0, n)] = t
            return t

    costs = []
    for i_apart in range(k - 1, n - 1 + 1):  # [k - 1, n - 1]   i.e. 2, 3, 4  if n = 5 and k=3
        cost_left_side = rec(arr[0: i_apart], i_apart, k - 1, rec_top=False)  # i_apart-1 >= k-1 才能切

        if (i_apart, n) in keeper:
            cost_right_side = keeper[(i_apart, n)]
        else:
            cost_right_side = ss(arr[i_apart: n])
            keeper[(i_apart, n)] = cost_right_side

        cost_both_sides = cost_left_side + cost_right_side
        costs.append(cost_both_sides)

    if rec_top:  # clear keeper to reuse it in next test case
        keeper.clear()
    # print("return costs[]: ", costs)
    return min(costs)


def performance_test(m):
    print("=" * 15, f"m={m}", f"=" * 15)
    start = time.time()
    print(rec([4, 5, 7, 11, 21] * m, n=5*m, k=m))
    end = time.time()
    print(f"耗时：{end - start} s")


if __name__ == '__main__':
    # run test here
    # assert ss([7, 11, 21]) == 104.0
    # assert rec([7, 11, 21], 3, 1) == 104.0
    #
    # array = [7, 11, 21, 10000, 55, 1] * 100
    # assert rec(array, len(array), len(array)) == 0
    #
    # print(rec([4, 5, 7, 11, 21], n=5, k=3))  # answer: 4.666666
    #
    #
    # a = [2, 2, 3, 5, 6, 6, 7, 9, 9, 10, 11, 24, 24, 24, 25, 28, 31, 33, 40, 45, 46]
    # assert int(rec(a, len(a), 7)) == 19
    #
    # b = [1, 1, 1, 2, 2, 5, 8, 8, 9, 9, 11, 21, 22]
    # assert int(rec(b, len(b), 3)) == 18
    #
    # d = [1, 2, 3, 4, 5, 6, 7, 9, 9, 9, 9, 9, 9, 22, 45, 66]
    # assert int(rec(d, len(d), 5)) == 19
    #
    # c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 100, 101, 102, 103, 104, 105,
    #      106, 107, 108, 109, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210]
    # assert int(rec(c, len(c), 8)) == 54

    # performance_test(5)
    # performance_test(6)
    # performance_test(7)  # ~6.7s without keeper; ~1.7s with keeper enabled as global variable
    # performance_test(8)  # ~77s without keeper ; ~20s with keeper enabled as global variable

    pprint.pprint(keeper)
