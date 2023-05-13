from __future__ import annotations

import random as ran
from enum import Enum, auto
from typing import Any

'''
    Author: Daniel Klic, 2019, VAI project, Brno University of Technlogies, Faculty of Mechanical Engineering, Mechatronics

    Snake script. Initialize the snake, obstacles and food and creates a functions for the right functionality of the game
'''


class Directions(Enum):
    left = auto()
    right = auto()
    up = auto()
    down = auto()


# Class for generation snake
class Snake:
    start: dict[Any, Any]
    direction: Directions
    tail: list[float | int | Any]
    body: list[list[float | int | Any]]
    pos: list[float | Any]
    start_pos: list[float | Any]

    def __init__(self, width: int, height: int):
        self.start_pos = [width / 2, height / 2]
        self.pos = [width / 2, height / 2]
        self.body = [[self.pos[0] - 10, self.pos[1]], [self.pos[0] - 20, self.pos[1]], [self.pos[0] - 30, self.pos[1]]]
        self.tail = self.body[-1]
        self.direction = Directions.right
        self.start = {}
        self.width = width
        self.height = height

    def move(self, food_pos: list) -> bool:
        if self.direction == Directions.right:
            self.pos[0] += 10
        elif self.direction == Directions.left:
            self.pos[0] -= 10
        elif self.direction == Directions.up:
            self.pos[1] -= 10
        elif self.direction == Directions.down:
            self.pos[1] += 10
        self.body.insert(0, list(self.pos))
        if self.pos == food_pos:
            return True
        else:
            self.body.pop()
            return False

    def automatic_move(self, food_pos: list[int]) -> list:
        self.body.insert(0, list(self.pos))
        if self.pos == food_pos:
            return self.body
        else:
            self.body.pop()
            return self.body

    def is_collision(self) -> bool:
        if self.pos[0] > self.width or self.pos[0] < 0:
            return True
        elif self.pos[1] > self.height or self.pos[1] < 0:
            return True
        for bodyPiece in self.body[1:]:
            if self.pos == bodyPiece:
                return True
        return False

    def direction_change(self, direction: Directions):
        if direction == Directions.right and self.direction != Directions.left:
            self.direction = Directions.right
        elif direction == Directions.left and self.direction != Directions.right:
            self.direction = Directions.left
        elif direction == Directions.up and self.direction != Directions.down:
            self.direction = Directions.up
        elif direction == Directions.down and self.direction != Directions.up:
            self.direction = Directions.down

    def random_direction(self):
        direction = ran.randint(0, 3)
        match direction:
            case 0:
                self.pos[0] += 10
            case 1:
                self.pos[0] -= 10
            case 2:
                self.pos[1] += 10
            case 3:
                self.pos[1] -= 10


class RandomFoodSpawn:
    """Generates food"""

    def __init__(self, width, height):
        self.runOutOfFood = 0
        self.pos = [ran.randrange(1, round(width / 10)) * 10, ran.randrange(1, round(height / 10)) * 10]
        self.val = 1
        self.width = width
        self.height = height

    def spawn_food(self):
        if self.runOutOfFood == 1:
            self.pos = [ran.randrange(1, round(self.width / 10)) * 10, ran.randrange(1, round(self.height / 10)) * 10]
            self.runOutOfFood = 0

        return self.pos

    def do_food(self, state):
        self.runOutOfFood = state


class Obstacles:
    """Generates obstacles"""

    def __init__(self, width, height):
        self.state = 'Obstacle'
        self.pos = [ran.randrange(1, round(width / 10)) * 10, ran.randrange(1, round(height / 10)) * 10]
        self.val = -1
        self.width = width
        self.height = height

    def is_on_food(self, foodPos):
        if self.pos == foodPos or foodPos == 1:
            return [ran.randrange(1, round(self.width / 10)) * 10, ran.randrange(1, round(self.height / 10)) * 10]
        return self.pos
