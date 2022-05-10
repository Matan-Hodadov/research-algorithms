import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from scipy.optimize import fsolve

epsilon = 1e-2

f = lambda x: np.sin(x)
g = lambda x: 0.2*x


def plotIntersection(xRange, f1, f2):
    fig = plt.figure()
    plt.plot(xRange, f1(xRange))
    plt.plot(xRange, f2(xRange))

    res = []
    for x in xRange:
        ans = abs(f1(x)-f2(x))
        if ans < epsilon:
            if len(res) == 0:
                res.append(x)
            elif abs(abs(x)-abs(res[-1])) >= epsilon:
                res.append(x)
            # print(abs(x)-abs(res[-1]))
    print(res)
    print(f(res))
    plt.plot(res, f1(res), 'ro')
    plt.show()


plotIntersection(np.linspace(-10, 10, 1000), f, g)