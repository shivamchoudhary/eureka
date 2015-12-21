import random
import math
import time
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

class Grid(object):
    """
    Creates the graph for the system.
    """
    def __init__(self):
        self.x          = (0, 5)
        self.y          = (0, 5)
        self.src        = (3, 3)
        self.cursrc     = (3, 3) #current_src
        self.num_nodes  = 4 
        self.dst        = (5, 5)
        self.range      = 1
        self.counter    = 0
        self.path_x     =[] 
        self.path_y     =[] 
    def distance(self, src, dst):
        """
        Calculates the distance between the src and the dst.
        param src = src tuple
        param dst = dst tuple
        returns True if distance is less than range.
        """
        if euclidean_distance(src, dst) <= self.range:
            return True
        else:
            return False

    def run(self):
        """
        Recursively computes the distance and staggers them.
        """
        msg_not_sent = True
        while msg_not_sent:
            if self.distance(self.cursrc, self.dst):
                self.counter += 1
                print "Message Successfully Delivered in {},last hop {}".\
                        format(self.counter, self.cursrc)
                msg_not_sent = False
            else:
                in_range = False
                while not in_range:
                    neighbours = self.generate(self.cursrc)
                    for neighbour in neighbours:
                        if self.distance(neighbour, self.cursrc):
                            self.cursrc = neighbour
                            self.path_x.append(self.cursrc[0])
                            self.path_y.append(self.cursrc[1])
                            self.counter += 1 
                            in_range = True
                    time.sleep(0.2)
        self.plot()
    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        mobile_path, = ax.plot(self.path_x, self.path_y, 'r--',label='Mobile Path')
        ax.annotate('src',xy=(self.src[0], self.src[1]))
        ax.annotate('dst', xy=(self.dst[0], self.dst[1]))
        ax.annotate('final-hop',xy=(self.cursrc[0],self.cursrc[1]))
        fixed_path, = ax.plot([self.src[0], self.dst[0],self.cursrc[0]],\
                [self.src[1],self.dst[1],self.cursrc[1]],'g^',label="Fixed Path")
        ax.axis([0, 8, 0, 8])
        plt.xlabel("X - Coordinate(units)")
        plt.ylabel("Y - Coordinate(units)")
        stats = "Number of Hops to Converge:{}\n Last Hop:{}\n \
                Number of Nodes:{} \n Range:{}".format (self.counter,self.cursrc,\
                self.num_nodes,self.range)
        ax.text(0.95,0.01, stats,verticalalignment='bottom', 
                horizontalalignment='right',transform=ax.transAxes, color='blue',
                fontsize=15)
        plt.legend([mobile_path,fixed_path],["Path taken by Nodes",'Direct Path'])
        plt.title("Path Taken for Convergence")
        plt.show()

    def generate(self, exclusion_tuple):
        """
        param: exclusion_tuple Tuple that has to be removed neighbours:.
        return list of neighbours
        """
        neighbours = []
        i = 0
        while i < self.num_nodes:
            x = random.uniform(self.x[0], self.x[1])
            y = random.uniform(self.y[0], self.y[1])
            if (x, y) != self.dst and (x, y) != exclusion_tuple:
                neighbours.append((x, y))
                i += 1
        return neighbours


def euclidean_distance(src,dst):
    """
    returns the euclidean_distance between the two coordinates.
    param: (x1,y1): First Coordinate Tuple
    param: (x2,y2): Second Coordinate Tuple
    """
    distance = math.sqrt((src[0]-dst[0])**2+(src[1]-dst[1])**2)
    return distance

def main():
    for i in range (1, 2):
        grid = Grid()
        grid.run()
           
if __name__ == "__main__":
    main()
