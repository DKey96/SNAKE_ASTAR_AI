import random as ran

'''
    Author: Daniel Klic, 2019, VAI project, Brno University of Technlogies, Faculty of Mechanical Engineering, Mechatronics

    Snake script. Initialize the snake, obstacles and food and creates a functions for the right functionality of the game
'''

# Class for generation snake
class Snake():
    def __init__(self, width, height):
        self.startPos = [width / 2, height / 2]
        self.pos = [width / 2, height / 2]
        self.body = [[self.pos[0] - 10, self.pos[1]], [self.pos[0] - 20, self.pos[1]], [self.pos[0] - 30, self.pos[1]]]
        self.tail = self.body[-1]
        self.dir = 'RIGHT'
        self.start = {}
        self.width = width
        self.height = height

    def move(self, foodPos):
        if self.dir == 'RIGHT':
            self.pos[0] += 10
        elif self.dir == 'LEFT':
            self.pos[0] -= 10
        elif self.dir == 'UP':
            self.pos[1] -= 10
        elif self.dir == 'DOWN':
            self.pos[1] += 10
        self.body.insert(0, list(self.pos))
        if self.pos == foodPos:
            return 1
        else:
            self.body.pop()
            return 0

    def Automove(self, foodPos):

        self.body.insert(0, list(self.pos))
        if self.pos == foodPos:
            return self.body
        else:
            self.body.pop()
            return self.body

    def isCollision(self):
        if self.pos[0] > self.width or self.pos[0] < 0:
            return 1
        elif self.pos[1] > self.height or self.pos[1] < 0:
            return 1
        for bodyPiece in self.body[1:]:
            if self.pos == bodyPiece:
                return 1

    def dirChange(self, dir):
        if dir == 'RIGHT' and self.dir != 'LEFT':
            self.dir = 'RIGHT'
        elif dir == 'LEFT' and self.dir != 'RIGHT':
            self.dir = 'LEFT'
        elif dir == 'UP' and self.dir != 'DOWN':
            self.dir = 'UP'
        elif dir == 'DOWN' and self.dir != 'UP':
            self.dir = 'DOWN'

    def randomDir(self):
        dir = ran.randint(0,3)
        if dir == 0:
            self.pos[0] += 10
        elif dir == 1:
            self.pos[0] -= 10
        elif dir == 2:
            self.pos[1] += 10
        elif dir == 3:
            self.pos[1] -= 10

# Class for generation food
class RandomFoodSpawn():
    def __init__(self, width, height):
        self.runOutOfFood = 0
        self.pos = [ran.randrange(1, round(width / 10)) * 10, ran.randrange(1, round(height / 10)) * 10]
        self.val = 1
        self.width = width
        self.height = height

    def spawnFood(self):
        if self.runOutOfFood == 1:
            self.pos = [ran.randrange(1, round(self.width / 10)) * 10, ran.randrange(1, round(self.height / 10)) * 10]
            self.runOutOfFood = 0

        return self.pos

    def doFood(self, state):
        self.runOutOfFood = state


# Class for generating obstacles
class Obstacles():
    def __init__(self, width, height):
        self.state = 'Obstacle'
        self.pos = [ran.randrange(1, round(width / 10)) * 10, ran.randrange(1, round(height / 10)) * 10]
        self.val = -1
        self.width = width
        self.height = height

    def isOnFood(self, foodPos):
        if self.pos == foodPos or foodPos == 1:
            return [ran.randrange(1, round(self.width / 10)) * 10, ran.randrange(1, round(self.height / 10)) * 10]
        return self.pos
