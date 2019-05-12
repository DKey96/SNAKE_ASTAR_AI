import pygame as pg
import sys
from SNAKE_KLIC_DANIEL import AstarFinite, Snake as s
import numpy as np

np.set_printoptions(threshold=sys.maxsize)


def mainAutomaticAstarForward():
    width, height = 500, 500
    window = pg.display.set_mode((500, 500))

    pg.display.set_caption('DK\'s Snake AI')

    obstPos = []
    grid = np.zeros((width, height))
    score = 0
    speed = 100
    numOfObt = 50
    fps = pg.time.Clock()

    snk = s.Snake(width, height)
    virSnk = s.Snake(width, height)
    food = s.RandomFoodSpawn(width, height)
    obst = s.Obstacles(width, height)
    foodPos = food.spawnFood()

    for i in range(numOfObt):
        obstPos.append(obst.isOnFood(1))

    aStar = AstarFinite.Astar(grid, width, height)
    path = aStar.path(tuple(snk.startPos), tuple(foodPos), obstPos, snk.body)

    while True:
        if path != False or path != []:

            while virSnk.pos != foodPos:
                for p in path:
                    virSnk.pos = p
                    virSnk.body = virSnk.Automove(foodPos)

            virPath = aStar.path(tuple(virSnk.pos), tuple(virSnk.tail), obstPos, virSnk.body)

            if virPath != False or virPath != []:
                for p in path:
                    snk.pos = p

                    for event in pg.event.get():
                        if event.type == pg.KEYDOWN:
                            if event.key == pg.K_ESCAPE:
                                pg.quit()
                                sys.exit()

                    window.fill(pg.Color(225, 225, 225))

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
                        pg.draw.rect(window, pg.Color(0, 0, 225), pg.Rect(obstPos[i][0], obstPos[i][1], 10, 10))

                    for pos in snk.body:
                        pg.draw.rect(window, pg.Color(225, 0, 0), pg.Rect(pos[0], pos[1], 10, 10))  # Draw snakes body

                    pg.draw.rect(window, pg.Color(0, 0, 0), pg.Rect(foodPos[0], foodPos[1], 10, 10))  # Draw food

                    for i in range(len(obstPos)):
                        if snk.pos[0] == obstPos[i][0] and snk.pos[1] == obstPos[i][1]:
                            print(snk.pos, ' Shit I just frontended obstacle. Your score is: ' + str(score), obstPos[i])
                            pg.quit()
                            sys.exit()

                    if snk.isCollision() == 1:
                        print(snk.pos, ' Shit I just ate myself. Your score is: ' + str(score))
                        pg.quit()
                        sys.exit()

                    pg.display.set_caption('Your score is: ' + str(score))
                    pg.display.flip()
                    fps.tick(speed)
            else:
                path = aStar.path(tuple(snk.pos), tuple(snk.tail), obstPos, virSnk.body)
                for i in range(250):
                    for p in path:
                        snk.pos = p

                        for event in pg.event.get():
                            if event.type == pg.KEYDOWN:
                                if event.key == pg.K_ESCAPE:
                                    pg.quit()
                                    sys.exit()

                        window.fill(pg.Color(225, 225, 225))

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
                            pg.draw.rect(window, pg.Color(0, 0, 225), pg.Rect(obstPos[i][0], obstPos[i][1], 10, 10))

                        for pos in snk.body:
                            pg.draw.rect(window, pg.Color(225, 0, 0),
                                         pg.Rect(pos[0], pos[1], 10, 10))  # Draw snakes body

                        pg.draw.rect(window, pg.Color(0, 0, 0), pg.Rect(foodPos[0], foodPos[1], 10, 10))  # Draw food

                        for i in range(len(obstPos)):
                            if snk.pos[0] == obstPos[i][0] and snk.pos[1] == obstPos[i][1]:
                                print(snk.pos, ' Shit I just frontended obstacle. Your score is: ' + str(score),
                                      obstPos[i])
                                pg.quit()
                                sys.exit()

                        if snk.isCollision() == 1:
                            print(snk.pos, ' Shit I just ate myself. Your score is: ' + str(score))
                            pg.quit()
                            sys.exit()

                        pg.display.set_caption('Your score is: ' + str(score))
                        pg.display.flip()
                        fps.tick(speed)

                path = aStar.path(tuple(snk.startPos), tuple(foodPos), obstPos, snk.body)
        else:
            path = aStar.path(tuple(snk.pos), tuple(snk.tail), obstPos, virSnk.body)
            if path == False or path == []:
                for i in range(50):
                    snk.randomDir()
            else:
                path = aStar.path(tuple(snk.startPos), tuple(foodPos), obstPos, snk.body)

