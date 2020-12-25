import math
import pygame
from pygame.draw import *


def draw_house(screen, house_coords, house_width, house_height): 
    wall_color = (101, 67, 33)
    wall_height = house_height * 0.55
    wall_width = house_width

    house_coords = (house_coords[0] - wall_width / 2, house_coords[1] - wall_height)

    rect(screen, wall_color, (*house_coords, wall_width, wall_height))

    roof_color = (150, 75, 0)
    roof_height = house_height - wall_height
    roof_width = house_width

    point_one = (house_coords[0], house_coords[1])
    point_two = (house_coords[0] + roof_width / 2, house_coords[1] - roof_height)
    point_three = (house_coords[0] + roof_width, house_coords[1])

    polygon(screen, roof_color, [point_one, point_two, point_three])

    window_color = (255, 255, 0)
    
    window_width = wall_width * 0.3
    window_height = wall_height * 0.3
    window_x = house_coords[0] + wall_width * 0.5 - window_width / 2
    window_y = house_coords[1] + wall_height * 0.5 - window_height / 2
    window_coords = (window_x, window_y)

    rect(screen, window_color, (*window_coords, window_width, window_height))
    rect(screen, (0, 0, 0), (*window_coords, window_width, window_height), 2)


def draw_tree(screen, tree_coords, tree_trunk_params, tree_crown_params):
    tree_x = tree_coords[0] - tree_trunk_params[0] / 2
    tree_y = tree_coords[1] - tree_trunk_params[1]
    
    tree_trunk_color = (0, 0, 0)

    rect(screen, tree_trunk_color, (tree_x, tree_y, tree_trunk_params[0], tree_trunk_params[1]))

    crown_color = tree_crown_params[2]
    crown_radius = tree_crown_params[1] / 2

    y_list = [tree_y - crown_radius * (0.4 + i) for i in range(3, 0, -2)]
    x_list = [tree_x + crown_radius * i/2 + tree_trunk_params[0] * (i/2 + 0.5) for i in range(-1, 2, 2)]
    x_center = tree_coords[0]

    for y in y_list:
        circle(screen, crown_color, (x_center, y), crown_radius)
        circle(screen, (0, 0, 0), (x_center, y), crown_radius, 2)

        for x in x_list:
            circle(screen, crown_color, (x, y + crown_radius), crown_radius)
            circle(screen, (0, 0, 0), (x, y + crown_radius), crown_radius, 2)


def shift_coord_center(x, y, coords_center):
    x -= coords_center[0]
    y -= coords_center[1]
    return (x, y)


def rotate_vector(x, y, angle):
    x_last, y_last = x, y

    x = x_last * math.cos(angle) + y_last * math.sin(angle)
    y = y_last * math.cos(angle) - x_last * math.sin(angle)

    return (x, y)


def draw_sun(screen, sun_coords, sun_radius):
    sun_color = (255, 255, 0)

    x_center = sun_coords[0]
    x_left = sun_coords[0] - sun_radius * 0.5
    x_right = sun_coords[0] + sun_radius * 0.5
    x_up = sun_coords[0]

    y_center = sun_coords[1]
    y_left = sun_coords[1]
    y_right = y_left
    y_up = sun_coords[1] - sun_radius

    polygon(screen, sun_color, [(x_up, y_up), (x_left, y_left), (x_right, y_right)])
    
    angle_deg = 20
    angle_radian = angle_deg * math.pi / 180
    n = 360 // angle_deg

    for _ in range(n):
        x_up, y_up = shift_coord_center(x_up, y_up, sun_coords)
        x_left, y_left = shift_coord_center(x_left, y_left, sun_coords)
        x_right, y_right = shift_coord_center(x_right, y_right, sun_coords)

        x_up, y_up = rotate_vector(x_up, y_up, angle_radian)
        x_left, y_left = rotate_vector(x_left, y_left, angle_radian)
        x_right, y_right = rotate_vector(x_right, y_right, angle_radian)

        x_up, y_up = shift_coord_center(x_up, y_up, (-sun_coords[0], -sun_coords[1]))
        x_left, y_left = shift_coord_center(x_left, y_left, (-sun_coords[0], -sun_coords[1]))
        x_right, y_right = shift_coord_center(x_right, y_right, (-sun_coords[0], -sun_coords[1])) 
        
        polygon(screen, sun_color, [(x_up, y_up), (x_left, y_left), (x_right, y_right)])


def draw_cloud(screen, cloud_color, cloud_coords, cloud_radius):
    x_list = [cloud_coords[0] + cloud_radius * i for i in range(4)]
    y_list = [cloud_coords[1] - cloud_radius * i for i in range(2)] 

    for y in y_list:
        for x in x_list:
            circle(screen, cloud_color, (x, y), cloud_radius)
            circle(screen, (0, 0, 0), (x, y), cloud_radius, 1)

        x_list = [cloud_coords[0] + cloud_radius * i for i in range(1, 3)]


pygame.init()

# Display
disp_width = 600
disp_height = 400
screen = pygame.display.set_mode((disp_width, disp_height))

# background
sky_height = disp_height * 0.4
sky_coords = (0, 0)
sky_width = disp_width
sky_color = (30, 144, 255)

earth_coords = (0, sky_height)
earth_height = disp_height - sky_height
earth_width = disp_width
earth_color = (0, 255, 0)

rect(screen, earth_color, (*earth_coords, earth_width, earth_height))
rect(screen, sky_color, (*sky_coords, sky_width, sky_height))

# the coordinate of the HOUSE is the lower point in the middle  
house_x = earth_width * 0.2
house_y = earth_coords[1] + earth_height / 2

house_coords = (house_x, house_y)
house_height = disp_height * 0.5
house_width = house_height * 0.8

draw_house(screen, house_coords, house_width, house_height)

# the TREE coordinate is the lowest point in the middle
tree_x = house_x + earth_width * 0.6
tree_y = earth_coords[1] + earth_height * 0.45

tree_coords = (tree_x, tree_y)
tree_trunk_height = house_height * 0.3
tree_trunk_width = house_width * 0.09
tree_trunk_params = (tree_trunk_width, tree_trunk_height)

tree_crown_height = house_height * 0.2
tree_crown_width = house_width * 0.4
tree_crown_color = (0, 100, 0)
tree_crown_params = (tree_crown_width, tree_crown_height, tree_crown_color)

draw_tree(screen, tree_coords, tree_trunk_params, tree_crown_params)

#SUN
sun_x = sky_width * 0.9
sun_y = sky_height * 0.2
sun_coords = (sun_x, sun_y)
sun_radius = 20
draw_sun(screen, sun_coords, sun_radius)

#CLOUD
cloud_y = sky_height * 0.5
cloud_x = sky_width * 0.5
cloud_coords = (cloud_x, cloud_y)
cloud_color = (255, 255, 255)
cloud_radius = math.sqrt((disp_width * 0.03) ** 2 + (disp_height * 0.03) ** 2)
draw_cloud(screen, cloud_color, cloud_coords, cloud_radius)


pygame.display.update()
clock = pygame.time.Clock()
fps = 30
finished = False

while not finished:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

