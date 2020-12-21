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


def draw_tree(screen, tree_coords, tree_trunk_params, tree_crown_params):
    tree_x = tree_coords[0] - tree_trunk_params[0] / 2
    tree_y = tree_coords[1] - tree_trunk_params[1]
    
    tree_trunk_color = (0, 0, 0)

    rect(screen, tree_trunk_color, (tree_x, tree_y, tree_trunk_params[0], tree_trunk_params[1]))


def draw_sun(screen, sun_coords):
    pass


def draw_cloud(screen):
    pass


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

# the coordinate of the house is the lower point in the middle  
house_x = earth_width * 0.2
house_y = earth_coords[1] + earth_height / 2

house_coords = (house_x, house_y)
house_height = disp_height * 0.5
house_width = house_height * 0.8

draw_house(screen, house_coords, house_width, house_height)

# the tree coordinate is the lowest point in the middle
tree_x = 100
tree_y = 200

tree_coords = (tree_x, tree_y)
tree_trunk_height = 30
tree_trunk_width = 10
tree_trunk_params = (tree_trunk_width, tree_trunk_height)
tree_crown_height = 20
tree_crown_width = 20
tree_crown_color = (0, 0 , 0)
tree_crown_params = (tree_crown_width, tree_crown_height, tree_crown_color)

draw_tree(screen, tree_coords, tree_trunk_params, tree_crown_params)

#...
sun_x = 0
sun_y = 0
sun_coords = (sun_x, sun_y)
draw_sun(screen, sun_coords)

#...
draw_cloud(screen)


pygame.display.update()
clock = pygame.time.Clock()
fps = 30
finished = False

while not finished:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

