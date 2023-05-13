import pygame as pg
from play_game import PlayGame

"""
    Author: Daniel Klic, 2019, VAI project, Brno University of Technlogies, Faculty of Mechanical Engineering, Mechatronics

    Main function for playing the game
"""


def main():
    width, height = 500, 500
    window = pg.display.set_mode((500, 500))
    set_mode = 3  # Set mode 1 - Manual play; 2 - Astar autoplay; 3 - Astar with Forward Checking autoplay

    play_game = PlayGame(window, width, height)

    if set_mode == 1:
        play_game.manual()
    elif set_mode == 2:
        play_game.astar()
    elif set_mode == 3:
        play_game.astar_forward_checking()
    else:
        print("No such a mode, man or madam")


if __name__ == "__main__":
    main()
