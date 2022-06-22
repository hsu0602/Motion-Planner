import numpy as np
import math as m

def AffineTransform(points, scale, rotataion, flip, translation):
    
    Tr = [[1.0, 0.0], [0.0, 1.0]]
    Tr = np.dot(Tr, [[scale[0], 0.0],[0.0, scale[1]]])
    Tr = np.dot(Tr, [[m.cos((rotataion/180)*m.pi), m.sin((rotataion/180)*m.pi)],[-m.sin((rotataion/180)*m.pi), m.cos((rotataion/180)*m.pi)]])
    flipx, flipy = 1.0, 1.0
    if flip[0] : flipx = -1.0
    if flip[1] : flipy = -1.0
    Tr = np.dot(Tr, [[flipx, 0.0],[0.0, flipy]])
    # print(Tr)
    
    for i in range(len(points)):    
        points[i] = np.dot(points[i], Tr.T) + [translation[0], translation[1]]
    return points