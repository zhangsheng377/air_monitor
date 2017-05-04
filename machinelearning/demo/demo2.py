import regression
from numpy import *
import matplotlib.pyplot as plt


def best_k(xArr, yArr):
    k_small = 0.01
    k_big = 2.0
    k = (k_big + k_small) / 2.0
    while True:
        yHat = regression.lwlrTest(xArr, xArr, yArr, k)
        yHat_small = regression.lwlrTest(xArr, xArr, yArr, k_small)
        yHat_big = regression.lwlrTest(xArr, xArr, yArr, k_big)
        re = regression.rssError(yArr, yHat)
        re_small = regression.rssError(yArr, yHat_small)
        re_big = regression.rssError(yArr, yHat_big)
        if re_small > re and re_big > re:
            k_big = k + (k_big - k) / 2.0
            k_small = k_small + (k - k_small) / 2.0
        elif re_small > re and re_big < re:
            k_small = k
            k = (k_big + k_small) / 2.0
        elif re_small < re and re_big > re:
            k_big = k
            k = (k_big + k_small) / 2.0
        else:
            k_big = k + (k_big - k) / 2.0
            k_small = k_small + (k - k_small) / 2.0
        if k_big - k_small < 0.01:
            k = k_small
            break
    return k


start_count = 10
sum_rate = 0.0
count = 0

mothed = 1
if mothed == 0:
    xArr, yArr = regression.loadDataSet("foo.txt")
    k = best_k(xArr, yArr)
    yHat = regression.lwlrTest(xArr, xArr, yArr, k)
    print(k)
else:
    xArr_origin, yArr_origin = regression.loadDataSet("foo.txt")
    # print(yArr_origin)
    xArr = []
    yArr = []
    m = (shape(xArr_origin))[0]
    yHat = zeros(m)

    xArr.append(xArr_origin[0][:])
    yArr.append(yArr_origin[0])
    yHat[0] = yArr_origin[0]

    for i in range(1, m):
        # k = best_k(xArr, yArr)
        k = 0.06830078125
        x = xArr_origin[i][:]
        y = regression.lwlr(x, xArr, yArr, k)
        # print(y.flatten().A[0][0])
        yHat[i] = y.flatten().A[0][0]
        while yHat[i] <= 0:
            k = k + 0.01
            y = regression.lwlr(x, xArr, yArr, k)
            yHat[i] = y.flatten().A[0][0]
        xArr.append(x)
        yArr.append(yArr_origin[i])
        print(i, k, yHat[i], yArr[i])
        with open('workfile', 'a') as f:
            f.write(str(i))
            f.write("\t")
            f.write(str(k))
            f.write("\t")
            f.write(str(yHat[i]))
            f.write("\t")
            f.write(str(yArr[i]))
            f.write("\t")
            rate = abs(yHat[i] - yArr[i]) * 1.0 / yArr[i]
            f.write(str(rate))
            f.write("\n")
        if i > sum_rate:
            sum_rate += rate
            count += 1
            # print(yArr)  # k = best_k(xArr, yArr)
# yHat = regression.lwlrTest(xArr, xArr, yArr, k)
# print(yHat)
# print(regression.rssError(yArr, yHat))
print(sum_rate * 1.0 / count)
# print(yArr)
# print(yHat)
xMat = mat(xArr)
srtInd = xMat[:, 0].argsort(0)
# print(srtInd)
# print(yHat[srtInd])
xSort = xMat[srtInd][:, 0, :]
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(xSort[:, 0], yHat[srtInd])
ax.scatter(xMat[:, 0].flatten().A[0], mat(yArr).T.flatten().A[0], s=2, c="red")
plt.show()
