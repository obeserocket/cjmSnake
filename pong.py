#!/usr/bin/python3

#-Recreation of pong by cjm

import pygame

screenx = 700
screeny = 700

def main():
    pygame.init()
    size = (screenx, screeny)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("PONG")
main()
