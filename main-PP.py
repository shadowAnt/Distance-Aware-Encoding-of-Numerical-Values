import numpy as np
import bitarray

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm


def distanceEncoding(x, b1, b2, t, s, ran, epsilon):
    output = bitarray.bitarray('0' * s)
    for i in range(s):
        # randomNum = np.random.random() * (b2 - b1) + b1
        randomNum = ran[i]
        rNum = np.random.rand() * (np.exp(epsilon) + 1)
        threshold = np.exp(epsilon)
        if x >= randomNum - t and x <= randomNum + t:
            output[i] = True
        if rNum > threshold:
            output[i] = output[i] ^ True
    return output


def draw(b2, de, s):
    x = np.arange(1, b2 + 1)
    y = np.arange(1, b2 + 1)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, de, c='black', label='expectation')
    ax.plot(x, y, c='red', label='fact')
    # ax.legend()
    ax_title_text = ax.set_title('relationship between expectation distance and actual distance, s = ' + str(s))
    ax_xlabel_text = ax.set_xlabel('index')
    ax_ylabel_text = ax.set_ylabel('distance')
    # plt.ylim(0, 6)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    b1 = 0
    b2 = 99
    t = 10
    s = 512
    epsilon = 2

    ran = []
    for i in range(s):
        ran.append(np.random.random() * (b2 - b1 + 2 * t) + b1 - t)

    # inputData = np.random.random(1000) * 100
    # outputData = [distanceEncoding(x, b1, b2, t, s) for x in inputData]
    inputNum = [i for i in range(b2 + 1)]
    outputData = [distanceEncoding(x, b1, b2, t, s, ran, epsilon) for x in inputNum]
    onesNum = [x.count() for x in outputData]
    factEw = np.mean(onesNum)
    Ew = s * 2. * t / (b2 - b1)

    factDist = [bitarray.bitdiff(outputData[0], outputData[i]) for i in range(1, b2 + 1)]
    de = [(b2 - b1) * dh * np.square((np.exp(epsilon) + 1) / (np.exp(epsilon) - 1)) / (2. * s) - (np.exp(epsilon) * (b2 - b1)) / np.square((np.exp(epsilon) - 1)) for dh in factDist]

    draw(b2, de, s)
