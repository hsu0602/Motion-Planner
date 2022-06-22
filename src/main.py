import pygame
import os
import objects
import fileHandler
import copy
import subprocess
import time

# Variables
WIDTH = 1280
HEIGHT = 720
FPS = 12
ANIMATE_FPS = 540

# Paths
def OBSTACLE_PATH(x) : return os.path.join(os.path.abspath(__file__), os.pardir, os.pardir, "docs", "obstacles", "obstacle"+ str(x) +".dat")
def ROBOT_PATH(x) : return os.path.join(os.path.abspath(__file__), os.pardir, os.pardir, "docs", "robots", "robot"+ str(x) +".dat")
THEME_PATH = os.path.join(os.path.abspath(__file__), os.pardir, os.pardir, "pics", "themes", "background1.png")
ICON_PATH = os.path.join(os.path.abspath(__file__), os.pardir, os.pardir, "pics", "MotionPlanner.ico")
BUTTON_PATH = os.path.join(os.path.abspath(__file__), os.pardir, os.pardir, "pics", "buttons","")
SEARCH_INPUT_PATH = os.path.join(os.path.abspath(__file__), os.pardir, os.pardir, "docs", "generates","search_input.txt")
SEARCH_RESULT_PATH = os.path.join(os.path.abspath(__file__), os.pardir, os.pardir, "docs", "generates","search_result.txt")

# Colors
BACKGROUND_COLOR = (255,255,255) # White
OBSTACLE_COLOR = (0, 0, 255) # Blue
ROBOT_INIT_COLOR = (0, 0, 0) # Black
ROBOT_GOAL_COLOR = (0, 255, 0) # Green

# Planner initialize 
pygame.init()
pygame.display.set_caption("Motion Planner")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BACKGROUND_COLOR)
clock = pygame.time.Clock()
running = True
planning = False

# Load pictures
THEME_IMG = pygame.image.load(THEME_PATH).convert()
ICON_IMG = pygame.image.load(ICON_PATH).convert()
SET0_IMG = pygame.image.load(BUTTON_PATH + "set0.png").convert()
SET1_IMG = pygame.image.load(BUTTON_PATH + "set1.png").convert()
SET2_IMG = pygame.image.load(BUTTON_PATH + "set2.png").convert()
SET3_IMG = pygame.image.load(BUTTON_PATH + "set3.png").convert()
SET4_IMG = pygame.image.load(BUTTON_PATH + "set4.png").convert()
INIT_IMG = pygame.image.load(BUTTON_PATH + "init.png").convert()
PLAN_IMG = pygame.image.load(BUTTON_PATH + "plan.png").convert()

pygame.display.set_icon(ICON_IMG)

# Load items
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
robots = pygame.sprite.Group()

# Load buttoms
button_set0 = objects.Button(850, 210, SET0_IMG, 1.0)
button_set1 = objects.Button(850, 280, SET1_IMG, 1.0)
button_set2 = objects.Button(850, 350, SET2_IMG, 1.0)
button_set3 = objects.Button(850, 420, SET3_IMG, 1.0)
button_set4 = objects.Button(850, 490, SET4_IMG, 1.0)
button_init = objects.Button(1050, 315, INIT_IMG, 1.0)
button_plan = objects.Button(1050, 385, PLAN_IMG, 1.0)
all_sprites.add(button_set0)
all_sprites.add(button_set1)
all_sprites.add(button_set2)
all_sprites.add(button_set3)
all_sprites.add(button_set4)
all_sprites.add(button_init)
all_sprites.add(button_plan)

# initial the planner
def init():
    all_sprites.empty()
    obstacles.empty()
    robots.empty()
    all_sprites.add(button_set0)
    all_sprites.add(button_set1)
    all_sprites.add(button_set2)
    all_sprites.add(button_set3)
    all_sprites.add(button_set4)
    all_sprites.add(button_init)
    all_sprites.add(button_plan)


# change to set x
def changeToSet(x):
    
    init()

    obstacles_list = fileHandler.fileIn()
    obstacles_list.getObstacle(OBSTACLE_PATH(x))

    with open(SEARCH_INPUT_PATH, 'w')as f:
        f.write(str(len(obstacles_list.verticess)) + '\n')
        for i in range(len(obstacles_list.verticess)):
            f.write(str(len(obstacles_list.verticess[i]))+'\n')
            for j in range(len(obstacles_list.verticess[i])):
                f.write(str(len(obstacles_list.verticess[i][j]))+'\n')
                for k in range(len(obstacles_list.verticess[i][j])):
                    f.write(str(obstacles_list.verticess[i][j][k][0]) + " " + str(obstacles_list.verticess[i][j][k][1]) + '\n')
            f.write(str(obstacles_list.init_configs[i][0]) + " " + str(obstacles_list.init_configs[i][1]) + " " + str(obstacles_list.init_configs[i][2]) + '\n')
    


    for i in range(len(obstacles_list.verticess)):
        tmp = copy.deepcopy(obstacles_list.verticess[i])
        obstacle = objects.Obstacle((WIDTH, HEIGHT), (WIDTH/2, HEIGHT/2), OBSTACLE_COLOR, tmp, obstacles_list.init_configs[i], WIDTH, HEIGHT)
        obstacles.add(obstacle)
        all_sprites.add(obstacle)
    
    robots_list = fileHandler.fileIn()
    robots_list.getRobot(ROBOT_PATH(x))

    with open(SEARCH_INPUT_PATH, 'a')as f:
        f.write(str(len(robots_list.verticess)) + '\n')
        for i in range(len(robots_list.verticess)):
            f.write(str(len(robots_list.verticess[i]))+'\n')
            for j in range(len(robots_list.verticess[i])):
                f.write(str(len(robots_list.verticess[i][j]))+'\n')
                for k in range(len(robots_list.verticess[i][j])):
                    f.write(str(robots_list.verticess[i][j][k][0]) + " " + str(robots_list.verticess[i][j][k][1]) + '\n')
            f.write(str(robots_list.init_configs[i][0]) + " " + str(robots_list.init_configs[i][1]) + " " + str(robots_list.init_configs[i][2]) + '\n')
            f.write(str(robots_list.goal_configs[i][0]) + " " + str(robots_list.goal_configs[i][1]) + " " + str(robots_list.goal_configs[i][2]) + '\n')
            f.write(str(len(robots_list.control_points[i])) + '\n')
            for l in range (len(robots_list.control_points[i])):
                 f.write(str(robots_list.control_points[i][l][0]) + " " + str(robots_list.control_points[i][l][1]) + '\n')

    for i in range(len(robots_list.verticess)):
        tmp = copy.deepcopy(robots_list.verticess[i])
        robot = objects.Robot((WIDTH, HEIGHT), (WIDTH/2, HEIGHT/2), ROBOT_INIT_COLOR, tmp, robots_list.init_configs[i], WIDTH, HEIGHT)
        robots.add(robot)
        all_sprites.add(robot)
        tmp = copy.deepcopy(robots_list.verticess[i])
        robot = objects.Robot((WIDTH, HEIGHT), (WIDTH/2, HEIGHT/2), ROBOT_GOAL_COLOR, tmp, robots_list.goal_configs[i], WIDTH, HEIGHT)
        all_sprites.add(robot)
 

#robot = objects.Robot((50, 50), (100, 100), ROBOT, [[40.2,40.2], [20,40], [10, 10]])
#all_sprites.add(robot)



# search
def plan():
    try:
        subprocess.check_call([".\search.exe"], shell=True)
    except:
        print("error : The search.cpp is not running correctly...")

    with open (SEARCH_RESULT_PATH, 'r') as f:
        lines = f.readlines()
    
    itr = 0
    for robot in robots:
        itr += 1
        stepnum = int(lines[itr])
        for j in range(stepnum):
            clock.tick(ANIMATE_FPS)

            if button_init.update() : 
                init()
                return True
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
            
            itr += 1
            x, y, theta = lines[itr].split()
            robot.update(float(x), float(y), float(theta))
            screen = pygame.display.set_mode((WIDTH, HEIGHT))
            screen.blit(THEME_IMG, (0, 0))
            all_sprites.draw(screen)
            pygame.display.update()

    return True

# Planner loop
while running:
    clock.tick(FPS)

    # Get Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update status
    if button_set0.update() : changeToSet(0)
    if button_set1.update() : changeToSet(1)
    if button_set2.update() : changeToSet(2)
    if button_set3.update() : changeToSet(3)
    if button_set4.update() : changeToSet(4)
    if button_init.update() : init()
    if button_plan.update() : running = plan()


    # Draw on screen
    #screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.blit(THEME_IMG, (0, 0))
    all_sprites.draw(screen)
    pygame.display.update()

pygame.quit()