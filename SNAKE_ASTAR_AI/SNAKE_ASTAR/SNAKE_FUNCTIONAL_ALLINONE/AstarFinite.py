'''
    Author: Daniel Klic, 2019, VAI project, Brno University of Technlogies, Faculty of Mechanical Engineering, Mechatronics

    This script contains the Astar algorithm
'''

class Astar():

    def __init__(self, grid, width, height):
        self.grid = grid
        self.aroundPoints = [(0, -10), (0, 10), (-10, 0), (10, 0)]
        self.width = width
        self.height = height

    # Compute the heuristic cost
    def heuristic(self, point_a, point_b):
        return (point_b[0] - point_a[0]) ** 2 + (point_b[1] - point_a[1]) ** 2

    # Define neighbours
    def getNeighbouirs(self, point):
        neighbours = []
        if point[0] < self.width - 10:
            neighbours.append((point[0] + 10, point[1]))
        if point[1] > 0:
            neighbours.append((point[0], point[1] - 10))
        if point[0] > 0:
            neighbours.append((point[0] - 10, point[1]))
        if point[1] < self.height - 10:
            neighbours.append((point[0], point[1] + 10))
        return neighbours

    def path(self, startPoint, endPoint, obstPos, body):
        opened = []  # Initialization of the Opened list
        closed = []  # Initialization of the Closed list
        pointBefore = {}  # Initialization of the Dictionary of all the points before
        newBody = []    # New body in tuple list type
        newObstPos = [] # New obstacles in tuple list type

        for b in body:
            b = tuple(b)
            newBody.append(b)

        for o in obstPos:
            o = tuple(o)
            newObstPos.append(o)

        gScore = {startPoint: 0}  # Initialize G score from f = g + h
        fScore = {startPoint: self.heuristic(startPoint, endPoint)}  # Initialize F score from f = g + h
        opened.append((fScore[startPoint], startPoint))  # Add F score to the startPoint (snakes head)

        while opened is not []:

            minim = min(opened, key=lambda param: param[0])  # Minimal value of the F from points around
            curr = minim[1]  # current position is the one with minimal f value
            opened.remove(minim)  # remove current minimum from opened array
            closed.append(minim)  # add current minimum to the closed

            if curr == endPoint:  # If the Snake eats food, then return the whole path for the draw function
                data = []
                while curr in pointBefore:
                    data.append(list(curr))
                    curr = pointBefore[curr]
                return data[::-1]

            closed.append(curr)  # assert current position to closed
            neighbours = self.getNeighbouirs(curr) # get neighbours

            for neighbour in neighbours: # for all neighbours do...
                if neighbour not in closed and neighbour not in newBody[1:] and neighbour not in newObstPos: # If neighbour not an obstacle or tail
                    tgs = gScore[curr] + self.heuristic(curr, neighbour) # tentative G score

                    if neighbour in closed and tgs >= gScore.get(neighbour, 0):
                        continue
                    if neighbour in opened:
                        if tgs < gScore.get(neighbour, 0):
                            pointBefore[neighbour] = curr
                            gScore[neighbour] = tgs
                            fScore[neighbour] = tgs + self.heuristic(neighbour, endPoint)
                    else:
                        pointBefore[neighbour] = curr
                        gScore[neighbour] = tgs
                        fScore[neighbour] = tgs + self.heuristic(neighbour, endPoint)
                        opened.append((fScore[neighbour], neighbour)) # set to the opened with new F score
        return False