import random
import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation
class Grid(object):

    def __init__(self, dict):
        """
        Initializes the coordinate system
        """
        self.x1         = 0
        self.xlimit     = dict['xlimit']
        self.y1         = 0
        self.ylimit     = dict['ylimit']
        self.src_x      = dict['src_x']
        self.src_y      = dict['src_y']
        self.range      = dict['range']
        self.iterations = dict['iterations']
        self.nodes      = dict['nodes']
        self.sink_x     = dict['sink_x']
        self.sink_y     = dict['sink_y']
        self.generate_data()
        self.draw()

    def generate_data(self):
        self.x_range = [i for i in range(self.x1, self.xlimit+1)]
        self.y_range = [i for i in range(self.y1, self.ylimit+1)]
        self.x_range.remove(self.src_x)
        self.y_range.remove(self.src_y)
    
    def draw(self):
        plt.plot([self.src_x, self.sink_x],[self.src_y,self.sink_y],'ro')
        plt.axis([self.x1, self.xlimit, self.y1, self.ylimit])
        plt.show()
    
    def select_random(self):
        pass


def main():
    config = {
            "xlimit":100,
            "ylimit":100,
            "src_x":50,
            "src_y":50,
            "range":1, #MAX distance to which node can hear
            "iterations":100,
            "nodes":4,
            "sink_x":100,
            "sink_y":100
            }
    a = Grid(config)

if __name__=="__main__":
    main()


