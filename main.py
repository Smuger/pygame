#!/usr/bin/python                                                                                                      #
# ____________________________________________________________________________________________________________________ #
#                                                                                                                      #
# Pygame (the library) is a Free and Open Source python programming language library for making multimedia             #
# applications like games built on top of the excellent SDL library.                                                   #
# Please respect our Python Community Code of Conduct.                                                                 #
# ____________________________________________________________________________________________________________________ #

import os, sys
import pygame
from pygame.examples.scrap_clipboard import screen
from pygame.locals import *
import array
import math

musicPlaying = True
gameIsDead = False
main_menu_music = 'src/music/main_menu.ogg'
main_menu_logo = 'src/img/Logo_smooth.png'


def main():
    print("Program Start")
    def __init__(self):
        print("Display adaptation")

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(main_menu_music)
    pygame.mixer.music.play()
    myfont = pygame.font.SysFont("monospace", 15)

    supported_res_list = pygame.display.list_modes()
    print("List of operational displays: " + str(supported_res_list))

    i = 0
    while i < len(supported_res_list):
        if pygame.display.mode_ok(supported_res_list[i]) == 0:
            print("Resolution: " + str(supported_res_list[i]) + "Not supported")
        else:
            pygame.font.Font.render(str(supported_res_list[i]), True, (0, 0, 0))
            myfont.render("Some text!", 1, (255, 255, 0))
            print("Resolution presented " + str(supported_res_list[i]))
        i += 1
    last_resolution = supported_res_list[len(supported_res_list) - 1]
    screen = pygame.display.set_mode((last_resolution), pygame.FULLSCREEN)
    print("Window created")
    screen.fill((255, 255, 255))
    x, y = pygame.Surface.get_size(screen)
    print(str(x) + " " + str(y))
    logo = pygame.image.load(main_menu_logo)
    correct_size_logo = pygame.transform.scale(logo, (200, 200))

    screen.blit(correct_size_logo, (0, 0))

    pygame.display.flip()


if __name__ == "__main__":
    main()

while not gameIsDead:
    for event in pygame.event.get():
        # any other key event input
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quit()
                gameIsDead = True
                print()
            elif event.key == K_q:
                if musicPlaying == True:
                    pygame.mixer.music.pause()
                    musicPlaying = False
                    print("Stop music!")

                else:
                    pygame.mixer.music.unpause()
                    musicPlaying = True
                    print("Start music!")
