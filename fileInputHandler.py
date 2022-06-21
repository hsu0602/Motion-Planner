import numpy as np

class fileInputHandler:
    def __init__(self):
        self.vertices = []
        self.init_configs = []
        self.goal_configs=[]
    
    def getObstacle(file):
        with open(file, 'r') as f:
            f.read()