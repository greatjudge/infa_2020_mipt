import math
import pygame
from pygame.draw import *

pygame.init()

display_width = 600
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))

fps = 30

# The values for background
smile_color = (255, 255, 0)

smile_center_x = display_width * 0.5
smile_center_y = display_height * 0.5
smile_center_coords = (smile_center_x, smile_center_y)

smile_radius = 100

circle(screen, smile_color, smile_center_coords, smile_radius)

# The values for EYES:
eye_color_one = (205, 133, 63)
eye_color_two = (0, 0, 0)
eye_color_three = (255, 255, 255)

eye_left_x = smile_center_coords[0] - smile_radius * 0.5
eye_left_y = smile_center_coords[1] - smile_radius * 0.4
eye_right_x = smile_center_coords[0] + smile_radius * 0.5
eye_right_y = smile_center_coords[1] - smile_radius * 0.4

eye_left_coords = (smile_center_coords[0] - smile_radius / 2, smile_center_coords[1] - smile_radius * 0.4)
eye_right_coords = (smile_center_coords[0] + smile_radius / 2, smile_center_coords[1] - smile_radius * 0.4)

eye_radius_one = smile_radius / 40
eye_radius_two = eye_radius_one * 3
eye_radius_three = eye_radius_one * 6

# The values for EYEBROWS:
eyebrow_color = (0, 0, 0)
eyebrow_width = 5

eyebrow_left_x1 = eye_left_coords[0] - eye_radius_three * 2
eyebrow_left_y1 = eye_left_coords[1]
eyebrow_left_x2 = eye_left_coords[0] + eye_radius_three * 2 
eyebrow_left_y2 = eye_left_coords[1] - eye_radius_three * 1.7
eyebrow_left_coords = ((eyebrow_left_x1, eyebrow_left_y1), (eyebrow_left_x2, eyebrow_left_y2))

eyebrow_right_x1 = eye_right_coords[0] - eye_radius_three * 2
eyebrow_right_y1 = eye_right_coords[1] - eye_radius_three * 1.7
eyebrow_right_x2 = eye_right_coords[0] + eye_radius_three * 2 
eyebrow_right_y2 = eye_right_coords[1]
eyebrow_right_coords = ((eyebrow_right_x1, eyebrow_right_y1), (eyebrow_right_x2, eyebrow_right_y2))

# The values for MOUTH:
mouth_color = (0, 0, 0)

mouth_width = smile_radius * 0.8
mouth_height = smile_radius / 8

x = smile_center_coords[0] - mouth_width / 2
y = smile_center_coords[1] + smile_radius / 2

mouth_coords = (x, y, mouth_width, mouth_height)

# Functions:
circle(screen, eye_color_three, eye_right_coords, eye_radius_three)
circle(screen, eye_color_two, eye_right_coords, eye_radius_two)
circle(screen, eye_color_one, eye_right_coords, eye_radius_one)

circle(screen, eye_color_three, eye_left_coords, eye_radius_three)
circle(screen, eye_color_two, eye_left_coords, eye_radius_two)
circle(screen, eye_color_one, eye_left_coords, eye_radius_one)

line(screen, eyebrow_color, eyebrow_left_coords[0], eyebrow_left_coords[1], eyebrow_width)
line(screen, eyebrow_color, eyebrow_right_coords[0], eyebrow_right_coords[1], eyebrow_width)

mouth_rect = pygame.Rect(mouth_coords)

arc(screen, mouth_color, mouth_rect, math.pi - math.pi / 4, math.pi / 3)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

