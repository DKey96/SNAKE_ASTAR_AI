"""
    Author: Daniel Klic, 2019, VAI project, Brno University of Technologies, Faculty of Mechanical Engineering, Mechatronics
    
    This script contains the Draw function for visual part of the project and also all algorithms (Astar, Astar with
    Forward Checking and Manual play)
"""

import sys

import pygame as pg
import numpy as np

from astar import Astar
from snake import RandomFoodSpawn, Snake, Obstacles, Directions


class PlayGame:
    obt_count: int
    fps: pg.time.Clock
    speed: int
    score: int
    grid: np.array

    def __init__(self, window: pg.display, width: int, height: int):
        self.window = window
        self.width = width
        self.height = height
        self.grid = np.zeros((width, height))
        self.score = 0
        self.speed = 40
        self.fps = pg.time.Clock()
        self.obt_count = 20

        self.obst = Obstacles(self.width, self.height)
        self.obst_pos = []

        for i in range(self.obt_count):
            self.obst_pos.append(self.obst.is_on_food(1))

    # Manual mode for playing snake
    def manual(self):
        snk: Snake = Snake(self.width, self.height)
        food: RandomFoodSpawn = RandomFoodSpawn(self.width, self.height)
        food_pos: list[int] = food.spawn_food()

        while True:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key in [pg.K_d, pg.K_RIGHT]:
                        snk.direction_change(Directions.right)
                    elif event.key in [pg.K_a, pg.K_LEFT]:
                        snk.direction_change(Directions.left)
                    elif event.key in [pg.K_w, pg.K_UP]:
                        snk.direction_change(Directions.up)
                    elif event.key in [pg.K_s, pg.K_DOWN]:
                        snk.direction_change(Directions.down)
                    elif event.key == pg.K_ESCAPE:
                        pg.quit()

            if snk.move(food_pos):
                self.score += 1
                food.do_food(1)
                food_pos = food.spawn_food()

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

            self.draw(snk, self.obst_pos, food_pos)
            self.check(snk)

    def astar(self):
        snk = Snake(self.width, self.height)
        food = RandomFoodSpawn(self.width, self.height)
        food_pos = food.spawn_food()

        astar = Astar(self.grid, self.width, self.height)

        # Find path to the food
        path = astar.path(tuple(snk.start_pos), tuple(food_pos), self.obst_pos, snk.body)

        if path:
            while True:
                for p in path:
                    snk.pos = p

                    snk.body = snk.automatic_move(food_pos)

                    if snk.pos == food_pos:
                        self.score += 1
                        food.do_food(1)
                        food_pos = food.spawn_food()

                        snk.start_pos = snk.pos
                        path = astar.path(
                            tuple(snk.start_pos), tuple(food_pos), self.obst_pos, snk.body
                        )

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

                    self.draw(snk, self.obst_pos, food_pos)
                    self.check(snk)

    def astar_forward_checking(self):
        snk = Snake(self.width, self.height)
        # Create virtual snake
        vir_snk: Snake = Snake(self.width, self.height)
        food: RandomFoodSpawn = RandomFoodSpawn(self.width, self.height)
        food_pos: list[int] = food.spawn_food()

        aStar: Astar = Astar(self.grid, self.width, self.height)

        # Find the path to the food
        path = aStar.path(tuple(snk.start_pos), tuple(food_pos), self.obst_pos, snk.body)

        while True:
            if path:
                # Check if virtual snake can eat the food
                while vir_snk.pos != food_pos:
                    for p in path:
                        vir_snk.pos = p
                        vir_snk.body = vir_snk.automatic_move(food_pos)

                # Create path to the snakes tail
                virPath = aStar.path(
                    tuple(vir_snk.pos), tuple(vir_snk.tail), self.obst_pos, vir_snk.body
                )

                # Check if the tail can be 'eaten' and if it can be, the real snake eats
                if virPath:
                    for p in path:
                        snk.pos = p

                        snk.body = snk.automatic_move(food_pos)

                        if snk.pos == food_pos:
                            self.score += 1
                            food.do_food(1)
                            food_pos = food.spawn_food()

                            snk.start_pos = snk.pos
                            path = aStar.path(
                                tuple(snk.start_pos),
                                tuple(food_pos),
                                self.obst_pos,
                                snk.body,
                            )

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

                        self.draw(snk, self.obst_pos, food_pos)
                        self.check(snk)
                else:
                    # If food cannot be eaten, then go for a while after tail
                    path = aStar.path(
                        tuple(snk.pos), tuple(snk.tail), self.obst_pos, vir_snk.body
                    )
                    for i in range(250):
                        for p in path:
                            snk.pos = p

                            for event in pg.event.get():
                                if event.type == pg.KEYDOWN:
                                    if event.key == pg.K_ESCAPE:
                                        pg.quit()

                            snk.body = snk.automatic_move(food_pos)

                            if snk.pos == food_pos:
                                self.score += 1
                                food.do_food(1)
                                food_pos = food.spawn_food()

                                snk.start_pos = snk.pos
                                path = aStar.path(
                                    tuple(snk.start_pos),
                                    tuple(food_pos),
                                    self.obst_pos,
                                    snk.body,
                                )

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

                            self.draw(snk, self.obst_pos, food_pos)
                            self.check(snk)

                    path = aStar.path(
                        tuple(snk.start_pos), tuple(food_pos), self.obst_pos, snk.body
                    )

            else:
                path = aStar.path(
                    tuple(snk.pos), tuple(snk.tail), self.obst_pos, vir_snk.body
                )
                if not path:
                    for i in range(50):
                        snk.random_direction()
                        self.draw(snk, self.obst_pos, food_pos)
                else:
                    path = aStar.path(
                        tuple(snk.start_pos), tuple(food_pos), self.obst_pos, snk.body
                    )
                    continue

    # Draw the whole thing
    def draw(self, snake: Snake, obst_pos: list, food_pos: list):
        pg.display.set_caption("DK's Snake AI")

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()

        self.window.fill(pg.Color(225, 225, 225))

        for i in range(len(obst_pos)):
            pg.draw.rect(
                self.window,
                pg.Color(0, 0, 225),
                pg.Rect(obst_pos[i][0], obst_pos[i][1], 10, 10),
            )

        for pos in snake.body:
            pg.draw.rect(
                self.window, pg.Color(225, 0, 0), pg.Rect(pos[0], pos[1], 10, 10)
            )  # Draw snakes body

        pg.draw.rect(
            self.window, pg.Color(0, 0, 0), pg.Rect(food_pos[0], food_pos[1], 10, 10)
        )  # Draw food

        pg.display.set_caption("Your score is: " + str(self.score))
        pg.display.flip()
        self.fps.tick(self.speed)

    # Check collisions
    def check(self, snk: Snake) -> None:
        for i in range(len(self.obst_pos)):
            if snk.pos[0] == self.obst_pos[i][0] and snk.pos[1] == self.obst_pos[i][1]:
                print(
                    snk.pos,
                    self.obst_pos[i],
                    "I just front ended obstacle. Your score is: " + str(self.score),
                )
                pg.quit()

        if snk.is_collision():
            print(snk.pos, "I just ate myself. Your score is: " + str(self.score))
            pg.quit()
            sys.exit()
