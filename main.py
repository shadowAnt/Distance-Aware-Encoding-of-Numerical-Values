import numpy as np
import bitarray

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

def distanceEncoding(x, b1, b2, t, s):
    output = bitarray.bitarray('0' * s)
    for i in range(s):
        randomNum = np.random.random() * (b2 - b1) + b1
        if x >= randomNum - t and x <= randomNum + t:
            output[i] = True
    return output


if __name__ == '__main__':
    b1 = 0
    b2 = 999
    t = 5
    s = 512
    Ew = s * 2. * t / (b2 - b1)

    # inputData = np.random.random(1000) * 100
    # outputData = [distanceEncoding(x, b1, b2, t, s) for x in inputData]
    inputNum = [i for i in range(b2 + 1)]
    outputData = [distanceEncoding(x, b1, b2, t, s) for x in inputNum]
    onesNum = [x.count() for x in outputData]
    factEw = np.mean(onesNum)
    factDist = [bitarray.bitdiff(outputData[0], outputData[i]) for i in range(1, b2 + 1)]
    Edh = [2. * s * de / (b2 - b1) for de in range(1, b2 + 1)]

    x = np.arange(1, b2 + 1)
    y = np.arange(1, b2 + 1)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, Edh, c='black', label='expectation')
    ax.plot(x, y, c='red', label='fact')
    # ax.legend()
    ax_title_text = ax.set_title('relationship between expectation distance and actual distance, s = '+ str(s))
    ax_xlabel_text = ax.set_xlabel('index')
    ax_ylabel_text = ax.set_ylabel('distance')
    # plt.ylim(0, 6)
    plt.legend()
    plt.show()
