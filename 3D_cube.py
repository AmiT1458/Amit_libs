import pygame
import numpy as np
from math import cos,sin
pygame.init()

pygame.display.set_caption('3D shapes')

window_height = 900
window_width = 1500
FPS = 60
screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()
falcon_image = pygame.image.load('original.png')
falcon_image = pygame.transform.scale(falcon_image, (200, 200))
GREEN = (0, 225, 0)
WHITE = (255, 255, 255)

projection_matrix = [[1, 0, 0],
                     [0, 1, 0],
                     [0, 0, 0]]


def initialize_points(kind_points):
    shape_points = [n for n in range(8)]

    if kind_points == 'cube':
        shape_points = [n for n in range(8)]
        shape_points[0] = [[-1], [-1], [1]]
        shape_points[1] = [[1], [-1], [1]]
        shape_points[2] = [[1], [1], [1]]
        shape_points[3] = [[-1], [1], [1]]
        shape_points[4] = [[-1], [-1], [-1]]
        shape_points[5] = [[1], [-1], [-1]]
        shape_points[6] = [[1], [1], [-1]]
        shape_points[7] = [[-1], [1], [-1]]

    elif kind_points == 'triangle':
        shape_points = [n for n in range(8)]
        shape_points[0] = [[-1], [-1], [1]]
        shape_points[1] = [[1], [-1], [1]]
        shape_points[2] = [[1], [1], [1]]
        shape_points[3] = [[-1], [1], [1]]
        shape_points[4] = [[-1], [-1], [-1]]
        shape_points[5] = [[1], [-1], [-1]]
        shape_points[6] = [[1], [1], [-1]]
        #shape_points[7] = [[-1], [1], [-1]]

    else:
        pass

    return shape_points

def move_shape(angle_x, angle_y, angle_z, last_mouse_pos):
    mouse_pos = pygame.mouse.get_pos()

    #angle_x_velo = (mouse_pos[0] - last_mouse_pos[0]) / 100
    #angle_z_velo = (mouse_pos[1] - last_mouse_pos[1]) / 100
    #print(mouse_pos[0] - last_mouse_pos[0])
    angle_y_velo = (mouse_pos[0] - last_mouse_pos[0]) / 100
    angle_z_velo = 0
    angle_x_velo = (mouse_pos[1] - last_mouse_pos[1]) / 100

    last_mouse_pos = pygame.mouse.get_pos()
    return [angle_x_velo, angle_y_velo, angle_z_velo]


def connect_points(i, j, points):
    pygame.draw.line(screen, (255, 0, 0), (points[i][0], points[i][1]), (points[j][0], points[j][1]))


def image_pos(x, y):
    global image_rect
    image_rect = pygame.Rect((x, y), (100, 100))


def draw_points(points_shape):
    triangle_points = [2, 3, 6, 7, 8]
    blue_points = [1, 2, 3, 4]
    color = GREEN

    rotation_x = [[1, 0, 0],
                  [0, cos(angle_x), -sin(angle_x)],
                  [0, sin(angle_x), cos(angle_x)]]

    rotation_y = [[cos(angle_y), 0, sin(angle_y)],
                  [0, 1, 0],
                  [-sin(angle_y), 0, cos(angle_y)]]

    rotation_z = [[cos(angle_z), -sin(angle_z), 0],
                  [sin(angle_z), cos(angle_z), 0],
                  [0, 0, 1]]

    point_scale = 100
    i = 0
    global points
    shape_points = initialize_points(points_shape)
    points = [0 for _ in range(len(shape_points))]
    for point in shape_points:

        rotate_x = np.dot(rotation_x,point)
        rotate_y = np.dot(rotation_y, rotate_x)
        rotate_z = np.dot(rotation_z, rotate_y)

        point_2d = np.dot(projection_matrix,rotate_z)
        x = (point_2d[0][0] * point_scale) + window_width//2
        y = (point_2d[1][0] * point_scale) + window_width//2 - 200

        points[i] = (x, y)
        if i == 0:
            image_pos(x, y)
        i += 1
        if points_shape == 'triangle':
            if i in triangle_points:
                pygame.draw.circle(screen, color, (x, y), 5)

        if points_shape == 'cube':
            if i in blue_points:
                color = WHITE
            else:
                color = GREEN
            pygame.draw.circle(screen, color, (x, y), 5)


    if points_shape == 'triangle':
        connect_points(1, 2, points)
        connect_points(1, 5, points)
        connect_points(2, 6, points)
        connect_points(2, 7, points)
        connect_points(1, 7, points)
        connect_points(5, 7, points)
        connect_points(6, 5, points)
        connect_points(6, 7, points)
    #screen.blit(falcon_image, (points[0]))

    if points_shape == 'cube':
        connect_points(0, 1, points)
        connect_points(2, 1, points)
        connect_points(5, 1, points)
        connect_points(0, 3, points)
        connect_points(3, 2, points)
        connect_points(0, 4, points)
        connect_points(6, 5, points)
        connect_points(3, 7, points)
        connect_points(4, 5, points)
        connect_points(4, 7, points)
        connect_points(6, 2, points)
        connect_points(6, 7, points)


angle_x = angle_y = angle_z = 0

change_angle = False
shape = 'cube'
mouse_down = False
last_mouse_pos = pygame.mouse.get_pos()
image_rect = pygame.Rect((0,0), (100,100))

while True:
    screen.fill((0,0,0))
    if change_angle:
        angle_x += 0.01
        angle_y += 0.01
        angle_z += 0.01
        #print(angle_x)

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            last_mouse_pos = pygame.mouse.get_pos()
            mouse_down = True

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                change_angle = not change_angle

            if event.key == pygame.K_t:
                shape = 'cube'

            if event.key == pygame.K_y:
                shape = 'triangle'

    if mouse_down:
        move_angles = move_shape(angle_x, angle_y, angle_z, last_mouse_pos)
        angle_x += move_angles[0]
        angle_y += move_angles[1]
        angle_z += move_angles[2]
        last_mouse_pos = pygame.mouse.get_pos()

    draw_points(shape)
    #screen.blit(falcon_image, (image_rect.x, image_rect.y))

    pygame.display.update()