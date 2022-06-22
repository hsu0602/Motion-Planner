

class fileIn:
    def __init__(self):
        self.verticess = []
        self.init_configs = []
        self.goal_configs=[]
        self.control_points = []
    
    def getObstacle(self, file):
        with open(file, 'r') as f:
            lines = f.readlines()
        
        
        filtered_lines = []
        
        for line in lines:
            if line[0] == '#' or line[0] == ' ' or line[0] == '\n':
                continue
            else:
                filtered_lines.append(line.replace('\n', ''))
        
        # print(filtered_lines)
        
        itr = 0
        no = int(filtered_lines[itr])
        for i in range (no):
            itr += 1
            nc = int(filtered_lines[itr])
            vertices = []
            for j in range (nc):
                itr += 1
                nv = int(filtered_lines[itr])
                vertice = []
                for k in range(nv):
                    itr += 1
                    x, y = filtered_lines[itr].split(' ')
                    x, y = float(x), float(y)
                    vertice.append([x, y])
                vertices.append(vertice)
            
            itr += 1
            x, y, theta = filtered_lines[itr].split(' ')
            x, y, theta = float(x), float(y), float(theta)
            self.init_configs.append([x, y, theta])
            self.verticess.append(vertices)

        # print(self.verticess)
            
    def getRobot(self, file):
        with open(file, 'r') as f:
            lines = f.readlines()
        
        filtered_lines = []
        
        for line in lines:
            if line[0] == '#' or line[0] == ' ' or line[0] == '\n':
                continue
            else:
                filtered_lines.append(line.replace('\n', ''))
        
        #print(filtered_lines)
        
        itr = 0
        no = int(filtered_lines[itr])
        for i in range (no):
            itr += 1
            nc = int(filtered_lines[itr])
            vertices = []
            for j in range (nc):
                itr += 1
                nv = int(filtered_lines[itr])
                vertice = []
                for k in range(nv):
                    itr += 1
                    x, y = filtered_lines[itr].split(' ')
                    x, y = float(x), float(y)
                    vertice.append([x, y])
                vertices.append(vertice)
            
            self.verticess.append(vertices)

            itr += 1
            x, y, theta = filtered_lines[itr].split(' ')
            x, y, theta = float(x), float(y), float(theta)
            self.init_configs.append([x, y, theta])
            #print([x, y, theta])

            itr += 1
            x, y, theta = filtered_lines[itr].split(' ')
            x, y, theta = float(x), float(y), float(theta)
            self.goal_configs.append([x, y, theta])
            
            #print([x, y, theta])

            itr += 1
            ncp = int(filtered_lines[itr])
            control_point = []
            for l in range(ncp):
                itr += 1
                x, y = filtered_lines[itr].split(' ')
                x, y = float(x), float(y)
                control_point.append([x, y])
            self.control_points.append(control_point)

        #print(self.verticess)
        #print(self.control_points)
            
            
