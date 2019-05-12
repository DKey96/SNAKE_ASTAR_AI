import pygame as pg
from SNAKE_KLIC_DANIEL import PlayGame as Plg

'''
    Author: Daniel Klic, 2019, VAI project, Brno University of Technlogies, Faculty of Mechanical Engineering, Mechatronics

    Main function for playing the game
'''

def main():
    width, height = 500, 500
    window = pg.display.set_mode((500, 500))
    set_mode = 1 # Set mode 1 - Manual play; 2 - Astar autoplay; 3 - Astar with Forward Checking autoplay

    plg = Plg.PlayGame(window,width,height)

    if set_mode == 1:
        plg.Manual()
    elif set_mode == 2:
        plg.Astar()
    elif set_mode == 3:
        plg.AstarForwardChecking()
    else:
        print('No such a mode man or madam')

if __name__ == '__main__':
    main()