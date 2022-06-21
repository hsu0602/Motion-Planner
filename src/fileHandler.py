from transform import AffineTransform

class fileIn:
    def __init__(self):
        self.verticess = []
        self.init_configs = []
        self.goal_configs=[]
    
    def getObstacle(self, file, width, height):
        with open(file, 'r') as f:
            lines = f.readlines()
        f.close()
        
        filtered_lines = []
        
        for line in lines:
            if line[0] == '#' or line[0] == ' ' or line[0] == '\n':
                continue
            else:
                filtered_lines.append(line.replace('\n', ''))
        
        print(filtered_lines)
        
        itr = 0
        no = int(filtered_lines[itr])
        for i in range (no):
            itr += 1
            nc = int(filtered_lines[itr])
            vertices = []
            for j in range (nc):
                itr += 1
                nv = int(filtered_lines[itr])
                for k in range(nv):
                    itr += 1
                    x, y = filtered_lines[itr].split(' ')
                    x, y = float(x), float(y)
                    vertices.append([x, y])
            
            itr += 1
            x, y, theta = filtered_lines[itr].split(' ')
            x, y, theta = float(x), float(y), float(theta)
            self.init_configs.append([x, y, theta])
            vertices = AffineTransform(vertices, (4.0,4.0), theta, (False, True), (4*x + width/10, -4*y + height - height/5))
            self.verticess.append(vertices)
            
        def getRobot(self, file, width, height):
            with open(file, 'r') as f:
                lines = f.readlines()
            f.close()
            
            filtered_lines = []
            
            for line in lines:
                if line[0] == '#' or line[0] == ' ' or line[0] == '\n':
                    continue
                else:
                    filtered_lines.append(line.replace('\n', ''))
            
            print(filtered_lines)
            
            itr = 0
            no = int(filtered_lines[itr])
            for i in range (no):
                itr += 1
                nc = int(filtered_lines[itr])
                vertices = []
                for j in range (nc):
                    itr += 1
                    nv = int(filtered_lines[itr])
                    for k in range(nv):
                        itr += 1
                        x, y = filtered_lines[itr].split(' ')
                        x, y = float(x), float(y)
                        vertices.append([x, y])
                
                itr += 1
                x, y, theta = filtered_lines[itr].split(' ')
                x, y, theta = float(x), float(y), float(theta)
                self.init_configs.append([x, y, theta])
                vertices = AffineTransform(vertices, (4.0,4.0), theta, (False, True), (4*x + width/10, -4*y + height - height/5))
                self.verticess.append(vertices)
            
            
