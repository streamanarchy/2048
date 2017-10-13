import numpy as np
import game2048
import operator
import math


class neuralnet:

    def __init__(self):
        self.n1 = 16
        self.n2 = 10
        self.n3 = 4
        self.w1 = np.random.uniform(-1, 1, (16, 26))
        self.w2 = np.random.uniform(-1, 1, (26, 4))
        self.nop1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.op1 = []
        self.nop2 = [0, 0, 0, 0]
        self.op2 = []

    def feedforward(self, inp):
        index, value = max(enumerate(inp), key=operator.itemgetter(1))
        if value != 0:
            inp[:] = [float(x) / value for x in inp]

        for i in xrange(0, 16):
            for j in xrange(0, 26):
                self.nop1[j] += inp[i]*self.w1[i][j]

        """index, value = max(enumerate(self.nop1), key=operator.itemgetter(1))
        if value != 0:
            self.nop1[:] = [x / value for x in self.nop1]"""

        for val in self.nop1:
            self.op1.append(self.sigmoid(val))

        for i in xrange(0, 26):
            for j in xrange(0, 4):
                self.nop2[j] += self.op1[i]*self.w2[i][j]

        """index, value = max(enumerate(self.nop2), key=operator.itemgetter(1))
        if value != 0:
            self.nop2[:] = [x / value for x in self.nop2]"""

        for val in self.nop2:
            self.op2.append(self.sigmoid(val))
        temp = self.op2

        self.nop1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.op1 = []
        self.nop2 = [0, 0, 0, 0]
        self.op2 = []
        return temp

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))


if __name__ == "__main__":
    nn = neuralnet()
    inp = []
    p1 = game2048.playground()
    p1.start()
    inpMat = p1.grid
    print inpMat

    for each in inpMat:
        inp += each
    nn.feedforward(inp)
