import sys
import pygame as pg
from SNAKE_KLIC_DANIEL import AstarFinite, Snake as s
import numpy as np

'''
    Author: Daniel Klic, 2019, VAI project, Brno University of Technlogies, Faculty of Mechanical Engineering, Mechatronics
    
    This script contains the Draw function for visual part of the project and also all algorithms (Astar, Astar with
    Forward Checking and Manual play)
'''

class PlayGame():
    def __init__(self, window, width, height):
        self.window = window
        self.width = width
        self.height = height
        self.grid = np.zeros((width, height))
        self.score = 0
        self.speed = 10
        self.fps = pg.time.Clock()
        self.obtCount = 50

        self.obst = s.Obstacles(self.width, self.height)
        self.obstPos = []

        for i in range(self.obtCount):
            self.obstPos.append(self.obst.isOnFood(1))


    # Manual mode for playing snake
    def Manual(self):

        snk = s.Snake(self.width, self.height)
        food = s.RandomFoodSpawn(self.width, self.height)
        foodPos = food.spawnFood()

        while True:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_d:
                        snk.dirChange('RIGHT')
                    elif event.key == pg.K_a:
                        snk.dirChange('LEFT')
                    elif event.key == pg.K_w:
                        snk.dirChange('UP')
                    elif event.key == pg.K_s:
                        snk.dirChange('DOWN')
                    elif event.key == pg.K_ESCAPE:
                        pg.quit()
                        sys.exit()

            if snk.move(foodPos) == 1:
                self.score += 1
                food.doFood(1)
                foodPos = food.spawnFood()

                if self.score == 10:
                    self.speed += 5
                elif self.score == 20:
                    self.speed += 5
                elif self.score == 30:
                    self.speed += 5
                elif self.score == 40:
                    self.speed += 5
                elif self.score == 50:
                    self.speed += 5

            self.Draw(snk,self.obstPos,foodPos)
            self.Check(snk)

    def Astar(self):

        snk = s.Snake(self.width,self.height)
        food = s.RandomFoodSpawn(self.width, self.height)
        foodPos = food.spawnFood()

        aStar = AstarFinite.Astar(self.grid, self.width, self.height)

        # Find path to the food
        path = aStar.path(tuple(snk.startPos), tuple(foodPos), self.obstPos, snk.body)

        if path != False or path != []:
            while True:
                for p in path:
                    snk.pos = p

                    snk.body = snk.Automove(foodPos)

                    if snk.pos == foodPos:
                        self.score += 1
                        food.doFood(1)
                        foodPos = food.spawnFood()

                        snk.startPos = snk.pos
                        path = aStar.path(tuple(snk.startPos), tuple(foodPos), self.obstPos, snk.body)

                        if self.score == 10:
                            self.speed += 5
                        elif self.score == 20:
                            self.speed += 5
                        elif self.score == 30:
                            self.speed += 5
                        elif self.score == 40:
                            self.speed += 5
                        elif self.score == 50:
                            self.speed += 5

                    self.Draw(snk, self.obstPos, foodPos)
                    self.Check(snk)

    def AstarForwardChecking(self):

        snk = s.Snake(self.width, self.height)
        # Create virtual snake
        virSnk = s.Snake(self.width, self.height)
        food = s.RandomFoodSpawn(self.width, self.height)
        foodPos = food.spawnFood()

        aStar = AstarFinite.Astar(self.grid, self.width, self.height)

        # Find the path to the food
        path = aStar.path(tuple(snk.startPos), tuple(foodPos), self.obstPos, snk.body)

        while True:
            if path != False or path != []:

                # Check if virtual snake can eat the food
                while virSnk.pos != foodPos:
                    for p in path:
                        virSnk.pos = p
                        virSnk.body = virSnk.Automove(foodPos)

                # Create path to the snakes tail
                virPath = aStar.path(tuple(virSnk.pos), tuple(virSnk.tail), self.obstPos, virSnk.body)

                # Check if the tail can be 'eaten' and if it can be, the real snake eats
                if virPath != False or virPath != []:
                    for p in path:
                        snk.pos = p

                        snk.body = snk.Automove(foodPos)

                        if snk.pos == foodPos:
                            self.score += 1
                            food.doFood(1)
                            foodPos = food.spawnFood()

                            snk.startPos = snk.pos
                            path = aStar.path(tuple(snk.startPos), tuple(foodPos), self.obstPos, snk.body)

                            if self.score == 10:
                                self.speed += 5
                            elif self.score == 20:
                                self.speed += 5
                            elif self.score == 30:
                                self.speed += 5
                            elif self.score == 40:
                                self.speed += 5
                            elif self.score == 50:
                                self.speed += 5

                        self.Draw(snk,self.obstPos,foodPos)
                        self.Check(snk)
                else:
                    # If food cannot be eaten, than go for a while after tail
                    path = aStar.path(tuple(snk.pos), tuple(snk.tail), self.obstPos, virSnk.body)
                    for i in range(250):
                        for p in path:
                            snk.pos = p

                            for event in pg.event.get():
                                if event.type == pg.KEYDOWN:
                                    if event.key == pg.K_ESCAPE:
                                        pg.quit()
                                        sys.exit()

                            snk.body = snk.Automove(foodPos)

                            if snk.pos == foodPos:
                                self.score += 1
                                food.doFood(1)
                                foodPos = food.spawnFood()

                                snk.startPos = snk.pos
                                path = aStar.path(tuple(snk.startPos), tuple(foodPos), self.obstPos, snk.body)

                                if self.score == 10:
                                    self.speed += 5
                                elif self.score == 20:
                                    self.speed += 5
                                elif self.score == 30:
                                    self.speed += 5
                                elif self.score == 40:
                                    self.speed += 5
                                elif self.score == 50:
                                    self.speed += 5

                            self.Draw(snk, self.obstPos, foodPos)
                            self.Check(snk)

                    path = aStar.path(tuple(snk.startPos), tuple(foodPos), self.obstPos, snk.body)

            else:
                path = aStar.path(tuple(snk.pos), tuple(snk.tail), self.obstPos, virSnk.body)
                if path == False or path == []:
                    for i in range(50):
                        snk.randomDir()
                        self.Draw(snk,self.obstPos,foodPos)
                else:
                    path = aStar.path(tuple(snk.startPos), tuple(foodPos), self.obstPos, snk.body)
                    continue

    # Draw the whole thing
    def Draw(self,snk, obstPos, foodPos):

        pg.display.set_caption('DK\'s Snake AI')

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()

        self.window.fill(pg.Color(225, 225, 225))

        for i in range(len(obstPos)):
            pg.draw.rect(self.window, pg.Color(0, 0, 225), pg.Rect(obstPos[i][0], obstPos[i][1], 10, 10))

        for pos in snk.body:
            pg.draw.rect(self.window, pg.Color(225, 0, 0), pg.Rect(pos[0], pos[1], 10, 10))  # Draw snakes body

        pg.draw.rect(self.window, pg.Color(0, 0, 0), pg.Rect(foodPos[0], foodPos[1], 10, 10))  # Draw food

        pg.display.set_caption('Your score is: ' + str(self.score))
        pg.display.flip()
        self.fps.tick(self.speed)

    # Check collisions
    def Check(self,snk):
        for i in range(len(self.obstPos)):
            if snk.pos[0] == self.obstPos[i][0] and snk.pos[1] == self.obstPos[i][1]:
                print(snk.pos, self.obstPos[i], 'I just front ended obstacle. Your score is: ' + str(self.score))
                pg.quit()
                sys.exit()

        if snk.isCollision() == 1:
            print(snk.pos, 'I just ate myself. Your score is: ' + str(self.score))
            pg.quit()
            sys.exit()