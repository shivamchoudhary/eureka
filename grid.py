import random
from numpy import random
import math
class Grid(object):


    def __init__(self):

        self.x          = (0, 5)
        self.y          = (0, 5)
        self.src        = (3, 3)
        self.num_nodes  = 4
        self.destination= (5, 5)
        self.range      = 1
    
    def run(self):
        not_converged = True
        while not_converged:
            coordinates = self.generate()
            for tuples in coordinates:
                euclidean_distance = math.sqrt((self.src[0]-tuples[0])**2+\
                        (self.src[1]-tuples[1])**2)
                if euclidean_distance <= self.range:
                    print "Converged",tuples,euclidean_distance
                    not_converged=False
                    break


    def generate(self):

        recent_coordinates = []
        i = 0
        while i < self.num_nodes:
            x = random.randint(self.x[0], self.x[1])
            y = random.randint(self.y[0],self.y[1])
            if (x, y) != self.destination and (x, y) != self.src:
                recent_coordinates.append((x, y))
                i += 1
        return recent_coordinates

def main():
    grid = Grid()
    grid.run()
           
if __name__=="__main__":
    main()
