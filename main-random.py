import numpy as np
import bitarray

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm


def distanceEncoding(x, b1, b2, t, s):
    output = bitarray.bitarray('0' * s)
    for i in range(s):
        randomNum = np.random.random() * (b2 - b1 + 2 * t) + b1 - t
        # randomNum = ran[i]
        if x >= randomNum - t and x <= randomNum + t:
            output[i] = True
    return output




if __name__ == '__main__':
    b1 = 0
    b2 = 999
    t = 50
    s = 512

    # ran = []
    # for i in range(s):
    #     ran.append(np.random.random() * (b2 - b1) + b1)

    # inputData = np.random.random(1000) * 100
    # outputData = [distanceEncoding(x, b1, b2, t, s) for x in inputData]
    inputNum = [i for i in range(b2 + 1)]
    outputData = [distanceEncoding(x, b1, b2, t, s) for x in inputNum]
    onesNum = [x.count() for x in outputData]
    factEw = np.mean(onesNum)
    Ew = s * 2. * t / (b2 - b1)

    factDist = [bitarray.bitdiff(outputData[0], outputData[i]) for i in range(1, b2 + 1)]
    de = [(b2 - b1) * dh / (2. * s) for dh in factDist]


    draw(b2, de, s)

