import math


def func(i, j):
    return 0.0015 * i - 0.99 * j + i / (i + j)


num_node = 20
with open('foo.txt', 'w') as f:
    for i in range(1, num_node):
        for j in range(1, num_node):
            ii = i * 1.0 / num_node
            jj = j * 1.0 / num_node
            print(ii, jj, func(ii, jj))
            print(ii, jj, func(ii, jj), file=f)
