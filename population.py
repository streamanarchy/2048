import genome
import itertools
import random
import numpy as np
import copy


class Population:
    def __init__(self):
        self.populationArray = []
        self.populationsize = 1000
        self.newgeneration = []
        self.scoreplot = []

    def start(self):
        for x in xrange(1, self.populationsize):
            self.populationArray.append(genome.gene())

    def sorted_score(self):
        scorearray = sorted(self.populationArray, key=lambda x: x.game.score)
        avg_score = 0
        for each in scorearray:
            avg_score += each.game.score
            print each.game.view(), each.game.score
        self.scoreplot.append(avg_score/self.populationsize)

    def selection(self):
        genepool = []
        for gene in self.populationArray:
            genepool += list(itertools.repeat(gene, (gene.game.score/1000)))

        for each in genepool:
            print each.game.score/1000

        for x in xrange(1, self.populationsize):
            p1 = random.choice(self.populationArray)
            p2 = random.choice(self.populationArray)
            self.newgeneration.append(self.crossover(p1, p2))

    def crossover(self, p1, p2):
        newgene = genome.gene()
        w1list = p1.net.w1.tolist()
        w2list = p1.net.w2.tolist()
        r1 = random.randint(0, w1list.__len__()-1)
        newgene.net.w1 = np.array(w1list[:r1] + p2.net.w1.tolist()[r1:])
        r2 = random.randint(0, w2list.__len__()-1)
        newgene.net.w2 = np.array(w2list[:r2] + p2.net.w2.tolist()[r2:])
        newgene = self.mutation(newgene)
        return newgene

    def mutation(self, newgene):
        nmut1 = random.randint(0, (newgene.net.w1.__len__() * newgene.net.w1[0].__len__())/50)
        for x in xrange(0, nmut1):
            r1 = random.randint(0, newgene.net.w1.__len__()-1)
            r2 = random.randint(0, newgene.net.w1[0].__len__()-1)
            newgene.net.w1[r1][r2] = np.random.uniform(-1, 1, 1)[0]
        nmut2 = random.randint(0, (newgene.net.w2.__len__() * newgene.net.w2[0].__len__())/50)
        for x in xrange(0, nmut2):
            r1 = random.randint(0, newgene.net.w2.__len__()-1)
            r2 = random.randint(0, newgene.net.w2[0].__len__()-1)
            newgene.net.w2[r1][r2] = np.random.uniform(-1, 1, 1)[0]
        return newgene

    def generation(self):
        self.newgeneration = []
        self.selection()
        self.populationArray = copy.deepcopy(self.newgeneration)
        for genes in self.populationArray:
            genes.play()
        popul.sorted_score()


if __name__ == "__main__":
    popul = Population()
    popul.start()
    for gene in popul.populationArray:
        gene.play()
    popul.sorted_score()
    flag = 1
    while flag == 1:
        print "Enter the number of generation to proceed or 0 to end:"
        choice = int(raw_input())
        if choice == 0:
            flag = 0
        else:
            for x in xrange(0, choice):
                popul.generation()
