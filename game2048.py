import random
import copy


class playground():

    def __init__(self):
        self.grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.score = 0
        self.noplace = False

    def view(self):
        for each_row in self.grid:
            print each_row
        
    def start(self):
        x1 = random.choice([0, 1, 2, 3])
        y1 = random.choice([0, 1, 2, 3])

        x2 = random.choice([0, 1, 2, 3])
        y2 = random.choice([0, 1, 2, 3])
        if x1 != x2 or y1 != y2:
            self.grid[x1][y1] = 2
            self.grid[x2][y2] = 2
        else:
            self.start()
            
    def aftermove(self, prevGrid):
        if prevGrid == self.grid:
            self.noplace = True
            return
        rand = random.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4])
        x1 = random.choice([0, 1, 2, 3])
        y1 = random.choice([0, 1, 2, 3])
        if self.grid[x1][y1] == 0:
            self.grid[x1][y1] = rand
            self.noplace = False
        else:
            for each in self.grid:
                if 0 in each:
                    self.aftermove(prevGrid)
                    return
                else:
                    continue
            self.noplace = True

    def upmove(self):
        prevGrid = copy.deepcopy(self.grid)
        for i in xrange(0, 4):
            if self.grid[0][i] == self.grid[1][i]:
                self.grid[0][i] = 2*self.grid[0][i]
                self.score += 2*self.grid[1][i]
                self.grid[1][i] = 0
            elif self.grid[0][i] == self.grid[2][i] and self.grid[1][i] == 0:
                self.grid[0][i] = 2*self.grid[0][i]
                self.score += 2*self.grid[2][i]
                self.grid[2][i] = 0
            elif self.grid[0][i] == self.grid[3][i] and self.grid[1][i] == 0 and self.grid[2][i] == 0:
                self.grid[0][i] = 2*self.grid[0][i]
                self.score += 2*self.grid[3][i]
                self.grid[3][i] = 0
            if self.grid[1][i] == self.grid[2][i]:
                self.grid[1][i] = 2*self.grid[1][i]
                self.score += 2*self.grid[2][i]
                self.grid[2][i] = 0
            elif self.grid[1][i] == self.grid[3][i] and self.grid[2][i] == 0:
                self.grid[1][i] = 2*self.grid[1][i]
                self.score += 2*self.grid[3][i]
                self.grid[3][i] = 0
            if self.grid[2][i] == self.grid[3][i]:
                self.grid[2][i] = 2*self.grid[2][i]
                self.score += 2*self.grid[3][i]
                self.grid[3][i] = 0

            if self.grid[0][i] == 0:
                if self.grid[1][i] == 0:
                    if self.grid[2][i] == 0:
                        if self.grid[3][i] == 0:
                            continue
                        else:
                            self.grid[0][i] = self.grid[3][i]
                            self.grid[3][i] = 0
                    else:
                        self.grid[0][i] = self.grid[2][i]
                        self.grid[2][i] = 0
                else:
                    self.grid[0][i] = self.grid[1][i]
                    self.grid[1][i] = 0

            if self.grid[1][i] == 0:
                if self.grid[2][i] == 0:
                    if self.grid[3][i] == 0:
                        continue
                    else:
                        self.grid[1][i] = self.grid[3][i]
                        self.grid[3][i] = 0
                else:
                    self.grid[1][i] = self.grid[2][i]
                    self.grid[2][i] = 0

            if self.grid[2][i] == 0:
                if self.grid[3][i] == 0:
                    continue
                else:
                    self.grid[2][i] = self.grid[3][i]
                    self.grid[3][i] = 0

        self.aftermove(prevGrid)

    def downmove(self):
        prevGrid = copy.deepcopy(self.grid)
        for i in xrange(0, 4):
            if self.grid[3][i] == self.grid[2][i]:
                self.grid[3][i] = 2*self.grid[3][i]
                self.score += 2*self.grid[2][i]
                self.grid[2][i] = 0
            elif self.grid[3][i] == self.grid[1][i] and self.grid[2][i] == 0:
                self.grid[3][i] = 2*self.grid[3][i]
                self.score += 2*self.grid[1][i]
                self.grid[1][i] = 0
            elif self.grid[3][i] == self.grid[0][i] and self.grid[1][i] == 0 and self.grid[2][i] == 0:
                self.grid[3][i] = 2*self.grid[3][i]
                self.score += 2*self.grid[0][i]
                self.grid[0][i] = 0
            if self.grid[2][i] == self.grid[1][i]:
                self.grid[2][i] = 2*self.grid[2][i]
                self.score += 2*self.grid[1][i]
                self.grid[1][i] = 0
            elif self.grid[2][i] == self.grid[0][i] and self.grid[1][i] == 0:
                self.grid[2][i] = 2*self.grid[2][i]
                self.score += 2*self.grid[0][i]
                self.grid[0][i] = 0
            if self.grid[1][i] == self.grid[0][i]:
                self.grid[1][i] = 2*self.grid[1][i]
                self.score += 2*self.grid[0][i]
                self.grid[0][i] = 0

            if self.grid[3][i] == 0:
                if self.grid[2][i] == 0:
                    if self.grid[1][i] == 0:
                        if self.grid[0][i] == 0:
                            continue
                        else:
                            self.grid[3][i] = self.grid[0][i]
                            self.grid[0][i] = 0
                    else:
                        self.grid[3][i] = self.grid[1][i]
                        self.grid[1][i] = 0
                else:
                    self.grid[3][i] = self.grid[2][i]
                    self.grid[2][i] = 0

            if self.grid[2][i] == 0:
                if self.grid[1][i] == 0:
                    if self.grid[0][i] == 0:
                        continue
                    else:
                        self.grid[2][i] = self.grid[0][i]
                        self.grid[0][i] = 0
                else:
                    self.grid[2][i] = self.grid[1][i]
                    self.grid[1][i] = 0

            if self.grid[1][i] == 0:
                if self.grid[0][i] == 0:
                    continue
                else:
                    self.grid[1][i] = self.grid[0][i]
                    self.grid[0][i] = 0
        self.aftermove(prevGrid)

    def leftmove(self):
        prevGrid = copy.deepcopy(self.grid)
        for i in xrange(0, 4):
            if self.grid[i][0] == self.grid[i][1]:
                self.grid[i][0] = 2*self.grid[i][0]
                self.score += 2*self.grid[i][1]
                self.grid[i][1] = 0
            elif self.grid[i][0] == self.grid[i][2] and self.grid[i][1] == 0:
                self.grid[i][0] = 2*self.grid[i][0]
                self.score += 2*self.grid[i][2]
                self.grid[i][2] = 0
            elif self.grid[i][0] == self.grid[i][3] and self.grid[i][2] == 0 and self.grid[i][1] == 0:
                self.grid[i][0] = 2*self.grid[i][0]
                self.score += 2*self.grid[i][3]
                self.grid[i][3] = 0
            if self.grid[i][1] == self.grid[i][2]:
                self.grid[i][1] = 2*self.grid[i][1]
                self.score += 2*self.grid[i][2]
                self.grid[i][2] = 0
            elif self.grid[i][1] == self.grid[i][3] and self.grid[i][2] == 0:
                self.grid[i][1] = 2*self.grid[i][1]
                self.score += 2*self.grid[i][3]
                self.grid[i][3] = 0
            if self.grid[i][2] == self.grid[i][3]:
                self.grid[i][2] = 2*self.grid[i][2]
                self.score += 2*self.grid[i][3]
                self.grid[i][3] = 0

            if self.grid[i][0] == 0:
                if self.grid[i][1] == 0:
                    if self.grid[i][2] == 0:
                        if self.grid[i][3] == 0:
                            continue
                        else:
                            self.grid[i][0] = self.grid[i][3]
                            self.grid[i][3] = 0
                    else:
                        self.grid[i][0] = self.grid[i][2]
                        self.grid[i][2] = 0
                else:
                    self.grid[i][0] = self.grid[i][1]
                    self.grid[i][1] = 0

            if self.grid[i][1] == 0:
                if self.grid[i][2] == 0:
                    if self.grid[i][3] == 0:
                        continue
                    else:
                        self.grid[i][1] = self.grid[i][3]
                        self.grid[i][3] = 0
                else:
                    self.grid[i][1] = self.grid[i][2]
                    self.grid[i][2] = 0

            if self.grid[i][2] == 0:
                if self.grid[i][3] == 0:
                    continue
                else:
                    self.grid[i][2] = self.grid[i][3]
                    self.grid[i][3] = 0
        self.aftermove(prevGrid)

    def rightmove(self):
        prevGrid = copy.deepcopy(self.grid)
        for i in xrange(0, 4):
            if self.grid[i][3] == self.grid[i][2]:
                self.grid[i][3] = 2*self.grid[i][3]
                self.score += 2 * self.grid[i][2]
                self.grid[i][2] = 0
            elif self.grid[i][3] == self.grid[i][1] and self.grid[i][2] == 0:
                self.grid[i][3] = 2*self.grid[i][3]
                self.score += 2 * self.grid[i][1]
                self.grid[i][1] = 0
            elif self.grid[i][3] == self.grid[i][0] and self.grid[i][1] == 0 and self.grid[i][2] == 0:
                self.grid[i][3] = 2*self.grid[i][3]
                self.score += 2 * self.grid[i][0]
                self.grid[i][0] = 0
            if self.grid[i][2] == self.grid[i][1]:
                self.grid[i][2] = 2*self.grid[i][2]
                self.score += 2 * self.grid[i][1]
                self.grid[i][1] = 0
            elif self.grid[i][2] == self.grid[i][0] and self.grid[i][1] == 0:
                self.grid[i][2] = 2*self.grid[i][2]
                self.score += 2 * self.grid[i][0]
                self.grid[i][0] = 0
            if self.grid[i][1] == self.grid[i][0]:
                self.grid[i][1] = 2*self.grid[i][1]
                self.score += 2 * self.grid[i][0]
                self.grid[i][0] = 0

            if self.grid[i][3] == 0:
                if self.grid[i][2] == 0:
                    if self.grid[i][1] == 0:
                        if self.grid[i][0] == 0:
                            continue
                        else:
                            self.grid[i][3] = self.grid[i][0]
                            self.grid[i][0] = 0
                    else:
                        self.grid[i][3] = self.grid[i][1]
                        self.grid[i][1] = 0
                else:
                    self.grid[i][3] = self.grid[i][2]
                    self.grid[i][2] = 0

            if self.grid[i][2] == 0:
                if self.grid[i][1] == 0:
                    if self.grid[i][0] == 0:
                        continue
                    else:
                        self.grid[i][2] = self.grid[i][0]
                        self.grid[i][0] = 0
                else:
                    self.grid[i][2] = self.grid[i][1]
                    self.grid[i][1] = 0

            if self.grid[i][1] == 0:
                if self.grid[i][0] == 0:
                    continue
                else:
                    self.grid[i][1] = self.grid[i][0]
                    self.grid[i][0] = 0
        self.aftermove(prevGrid)


if __name__ == "__main__":
    p1 = playground()
    p1.start()
    p1.view()
    p1.rightmove()
    p1.view()
