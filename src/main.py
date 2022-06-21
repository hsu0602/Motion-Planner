import pygame
import os
import objects
import fileHandler as fileHandler
import numpy as np

# Variables
WIDTH = 1280
HEIGHT = 720
FPS = 144

OBSTACLE_PATH = "docs/obstacles"

# Colors
BACKGROUND_COLOR = (255,255,255) # White
ROBOT_COLOR = (0, 0, 0) # Black
OBSTACLE_COLOR = (0, 0, 255) # Blue


# Planner initialize 
pygame.init()
pygame.display.set_caption("Motion Planner")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BACKGROUND_COLOR)
clock = pygame.time.Clock()
running = True

all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

obstacles_list = fileHandler.fileIn()
obstacles_list.getObstacle(os.path.abspath(os.path.join(OBSTACLE_PATH, "obstacle2.dat")), WIDTH, HEIGHT)

for i in range(len(obstacles_list.verticess)):
    obstacle = objects.Obstacle( (WIDTH, HEIGHT), (WIDTH/2, HEIGHT/2), OBSTACLE_COLOR, obstacles_list.verticess[i])
    all_sprites.add(obstacle)
    
#robot = objects.Robot((50, 50), (100, 100), ROBOT, [[40.2,40.2], [20,40], [10, 10]])
#all_sprites.add(robot)

# Animation loop
while running:
    clock.tick(FPS)

    # Get Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update status
    all_sprites.update()

    # Draw on screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(BACKGROUND_COLOR)
    all_sprites.draw(screen)
    pygame.display.update()

pygame.quit()