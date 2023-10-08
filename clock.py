import pygame
import sys
import math
import datetime

pygame.init()
screen = pygame.display.set_mode((640, 480))
screen.fill((255, 255, 255))
pygame.display.set_caption("Analog clock")
clock = pygame.time.Clock()


def small_radiating_lines():
    n = 60
    delta_angle = 2 * math.pi/n
    x = 320
    y = 240
    r = 200

    for i in range(n):
        theta = i * delta_angle
        x_end = x + r * math.cos(theta)
        y_end = y + r * math.sin(theta)
        pygame.draw.line(screen, (0, 0, 0), (x, y), (x_end, y_end), width=3)


small_radiating_lines()


def white_cirle_big():
    pygame.draw.circle(screen, (255, 255, 255), (320, 240), 187)

 
white_cirle_big()

def radiating_lines():
    n = 12
    delta_angle = 2 * math.pi/n
    x = 320
    y = 240
    r = 200

    for i in range(n):
        theta = i * delta_angle
        x_end = x + r * math.cos(theta)
        y_end = y + r * math.sin(theta)
        pygame.draw.line(screen, (0, 0, 0), (x, y), (x_end, y_end), width=5)


radiating_lines()


def white_cirle_small():
    pygame.draw.circle(screen, (255, 255, 255), (320, 240), 165)

white_cirle_small()


def outer_circle():
    pygame.draw.circle(screen, (0, 0, 0), (320, 240), 201, 5)

outer_circle()

def draw_hands():
    now = datetime.datetime.now()
    second = now.second
    minutes = now.minute
    hours = now.hour % 12
    seconds = second + (now.microsecond / 1000000)

    angle_second = (2 * math.pi * seconds / 60) - (math.pi / 2)
    endx = 320 + 150 * math.cos(angle_second)
    endy = 240 + 150 * math.sin(angle_second)
    pygame.draw.line(screen, (0, 0, 0), (320, 240), (endx, endy), 2)


    angle_minute = (2 * math.pi * (minutes / 60) - (math.pi / 2))
    endx = 320 + 165 * math.cos(angle_minute)
    endy = 240 + 165 * math.sin(angle_minute)
    pygame.draw.line(screen, (0, 0, 0), (320, 240), (endx, endy), 4)

    angle_hour = (2 * math.pi * (hours / 12) - (math.pi / 2))
    endx = 320 + 90 * math.cos(angle_hour)
    endy = 240 + 90 * math.sin(angle_hour)
    pygame.draw.line(screen, (0, 0, 0), (320, 240), (endx, endy), 6)


def clock():
    small_radiating_lines()
    white_cirle_big()
    radiating_lines()
    white_cirle_small()
    outer_circle()
    draw_hands()
    pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))

    clock()
