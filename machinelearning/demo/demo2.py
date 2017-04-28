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


mothed = 0
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

    xArr.append(xArr_origin[1][:])
    xArr[0] = xArr[0] + xArr_origin[0][:]
    yArr.append(yArr_origin[1])
    yHat[0] = yArr_origin[1]
    for i in range(2, m - 3):
        k = best_k(xArr, yArr)
        x = xArr_origin[i][:] + xArr_origin[i - 1][:]
        y = regression.lwlr(x, xArr, yArr, k)
        # print(y.flatten().A[0][0])
        yHat[i - 1] = y.flatten().A[0][0]
        while yHat[i] <= 0:
            k = k + 0.01
            y = regression.lwlr(x, xArr, yArr, k)
            yHat[i] = y.flatten().A[0][0]
        xArr.append(x)
        yArr.append(yArr_origin[i])
        print(k, yHat[i - 1], yArr[i - 1])
        # print(yArr)

# k = best_k(xArr, yArr)
# yHat = regression.lwlrTest(xArr, xArr, yArr, k)
print(yHat)
# print(regression.rssError(yArr, yHat))

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
