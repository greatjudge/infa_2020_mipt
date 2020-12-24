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

 
    """
    crown_x_four_center = tree_coords[0]
    crown_y_four_center = tree_y - crown_radius * 3.4 
    circle(screen, crown_color, (crown_x_four_center, crown_y_four_center), crown_radius)
    circle(screen, (0, 0, 0), (crown_x_four_center, crown_y_four_center), crown_radius, 2)

    crown_x_three_left = tree_x - crown_radius * 0.5
    crown_y_three_left = tree_y - crown_radius * 2.4 
    circle(screen, crown_color, (crown_x_three_left, crown_y_three_left), crown_radius)
    circle(screen, (0, 0, 0), (crown_x_three_left, crown_y_three_left), crown_radius, 2)

    crown_x_three_right = tree_x + crown_radius * 0.5 + tree_trunk_params[0]
    crown_y_three_right = tree_y - crown_radius * 2.4 
    circle(screen, crown_color, (crown_x_three_right, crown_y_three_right), crown_radius)
    circle(screen, (0, 0, 0), (crown_x_three_right, crown_y_three_right), crown_radius, 2)

    crown_x_two_center = tree_coords[0]
    crown_y_two_center = tree_y - crown_radius * 1.4
    circle(screen, crown_color, (crown_x_two_center, crown_y_two_center), crown_radius)
    circle(screen, (0, 0, 0), (crown_x_two_center, crown_y_two_center), crown_radius, 2)

    crown_x_one_right = tree_x + crown_radius * 0.5 + tree_trunk_params[0]
    crown_y_one_right = tree_y - crown_radius * 0.5
    circle(screen, crown_color, (crown_x_one_right, crown_y_one_right), crown_radius)
    circle(screen, (0, 0, 0), (crown_x_one_right, crown_y_one_right), crown_radius, 2)

    crown_x_one_left = tree_x - crown_radius * 0.5
    crown_y_one_left = tree_y - crown_radius * 0.5
    circle(screen, crown_color, (crown_x_one_left, crown_y_one_left), crown_radius)
    circle(screen, (0, 0, 0), (crown_x_one_left, crown_y_one_left), crown_radius, 2)
    """

def draw_sun(screen, sun_coords):
    pass


def draw_cloud(screen, cloud_color, cloud_coords, cloud_radius):
    x_list = [cloud_coords[0] + cloud_radius * i for i in range(4)]
    y_list = [cloud_coords[1] - cloud_radius * i for i in range(2)] 

    for y in y_list:
        for x in x_list:
            circle(screen, cloud_color, (x, y), cloud_radius)
            circle(screen, (0, 0, 0), (x, y), cloud_radius, 1)

        x_list = [cloud_coords[0] + cloud_radius * i for i in range(1, 3)]

    """
    x_1_1 = cloud_coords[0]
    y_1_1 = cloud_coords[1]
    circle(screen, cloud_color, (x_1_1, y_1_1), cloud_radius)
    circle(screen, (0, 0, 0), (x_1_1, y_1_1), cloud_radius, 1)

    x_1_2 = cloud_coords[0] + cloud_radius
    y_1_2 = cloud_coords[1]
    circle(screen, cloud_color, (x_1_2, y_1_2), cloud_radius)
    circle(screen, (0, 0, 0), (x_1_2, y_1_2), cloud_radius, 1)

    x_1_3 = cloud_coords[0] + cloud_radius * 2
    y_1_3 = cloud_coords[1]
    circle(screen, cloud_color, (x_1_3, y_1_3), cloud_radius)
    circle(screen, (0, 0, 0), (x_1_3, y_1_3), cloud_radius, 1)
 
    x_1_4 = cloud_coords[0] + cloud_radius * 3
    y_1_4 = cloud_coords[1]
    circle(screen, cloud_color, (x_1_4, y_1_4), cloud_radius)
    circle(screen, (0, 0, 0), (x_1_4, y_1_4), cloud_radius, 1)

    x_2_1 = cloud_coords[0] + cloud_radius * 1
    y_2_1 = cloud_coords[1] - cloud_radius
    circle(screen, cloud_color, (x_2_1, y_2_1), cloud_radius)
    circle(screen, (0, 0, 0), (x_2_1, y_2_1), cloud_radius, 1)

    x_2_2 = cloud_coords[0] + cloud_radius * 2
    y_2_2 = cloud_coords[1] - cloud_radius
    circle(screen, cloud_color, (x_2_2, y_2_2), cloud_radius)
    circle(screen, (0, 0, 0), (x_2_2, y_2_2), cloud_radius, 1)
    """


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
sun_x = 0
sun_y = 0
sun_coords = (sun_x, sun_y)
draw_sun(screen, sun_coords)

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

