import random

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
        self.draw()
    
    def draw(self):
        self.x_range = [i for i in range(self.x1, self.xlimit+1)]
        self.y_range = [i for i in range(self.y1, self.ylimit+1)]
        self.x_range.remove(self.src_x)
        self.y_range.remove(self.src_y)
    def select_random(self):


def main():
    config = {
            "xlimit":100,
            "ylimit":100,
            "src_x":3,
            "src_y":3,
            "range":1,
            "iterations":100,
            "nodes":4
            }
    a = Grid(config)
    a.select_random()

if __name__=="__main__":
    main()


