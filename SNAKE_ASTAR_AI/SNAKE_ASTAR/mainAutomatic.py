import pygame as pg
import sys
from SNAKE_KLIC_DANIEL import Snake as s
import AstarForward
import numpy as np

np.set_printoptions(threshold=sys.maxsize)

def mainAutomaticAstar():
    width, height = 300, 300
    window = pg.display.set_mode((500, 500))

    pg.display.set_caption('DK\'s Snake AI')

    obstPos = []
    grid = np.zeros((width, height))
    score = 0
    speed = 100
    numOfObt = 50
    fps = pg.time.Clock()

    snk = s.Snake(width, height)
    food = s.RandomFoodSpawn(width, height)
    obst = s.Obstacles(width, height)
    foodPos = food.spawnFood()

    for i in range(numOfObt):
        obstPos.append(obst.isOnFood(1))

    print(str(obstPos))

    aStar = AstarForward.Astar(grid,width,height)
    path = aStar.path(tuple(snk.startPos), tuple(foodPos), obstPos, snk.body)

    if path != []:
        while True:
            for p in path:
                snk.pos = p

                snk.body = snk.Automove(foodPos)

                if snk.pos == foodPos:
                    score += 1
                    food.doFood(1)
                    foodPos = food.spawnFood()

                    snk.startPos = snk.pos
                    path = aStar.path(tuple(snk.startPos), tuple(foodPos), obstPos, snk.body)

                    if score == 10:
                        speed += 5
                    elif score == 20:
                        speed += 5
                    elif score == 30:
                        speed += 5
                    elif score == 40:
                        speed += 5
                    elif score == 50:
                        speed += 5



                for i in range(len(obstPos)):
                    if snk.pos[0] == obstPos[i][0] and snk.pos[1] == obstPos[i][1]:
                        print(snk.pos,' Shit I just frontended obstacle. Your score is: ' + str(score),obstPos[i])
                        pg.quit()
                        sys.exit()


                if snk.isCollision() == 1:
                    print(snk.pos, ' Shit I just ate myself. Your score is: ' + str(score))
                    pg.quit()
                    sys.exit()

                pg.display.set_caption('Your score is: ' + str(score))
                pg.display.flip()
                fps.tick(speed)

mainAutomaticAstar()
