import neuralnet
import game2048
import operator


class gene:

    def __init__(self):
        self.game = game2048.playground()
        self.game.start()
        self.net = neuralnet.neuralnet()

    def play(self):
        for x in xrange(0, 1000):
            inparr = []
            for each in self.game.grid:
                inparr += each
            movarray = self.net.feedforward(inparr)
            index, value = max(enumerate(movarray), key=operator.itemgetter(1))

            movarray[index] = -999
            temp = self.game.score
            self.move(index)
            while self.game.score == temp and self.game.noplace:
                index, value = max(enumerate(movarray), key=operator.itemgetter(1))
                movarray[index] = -999
                if value == -999:
                    return
                self.move(index)

    def move(self, index):
        if index == 0:
            self.game.upmove()
        elif index == 1:
            self.game.downmove()
        elif index == 2:
            self.game.leftmove()
        elif index == 3:
            self.game.rightmove()

    def fitness(self):
        return self.game.score


if __name__ == "__main__":
    genetest = gene()
    genetest.play()
