class Astar():

    def __init__(self, grid):
        self.grid = grid
        self.aroundPoints = [(0, -10), (0, 10), (-10, 0), (10, 0)]

    def heuristic(self,point_a,point_b):
        return (point_b[0] - point_a[0]) ** 2 + (point_b[1] - point_a[1]) ** 2

    def path(self, startPoint, endPoint, obstPos, body):
        grid = self.grid

        opened = [] # Initialization of the Opened list
        closed = [] # Initialization of the Closed list
        pointBefore = {} # Initialization of the Dictionary of all the points before

        gScore = {startPoint:0} # Initialize G score from f = g + h
        fScore = {startPoint:self.heuristic(startPoint,endPoint)} # Initialize F score from f = g + h
        opened.append((fScore[startPoint],startPoint)) # Add F score to the startPoint (snakes head)
        for b in body:
            closed.append((1, b))  # Add F score to the startPoint (snakes head)

        while opened is not []:

            minim = min(opened, key=lambda param: param[0]) #Minimal value of the F from points around
            curr = minim[1] # current position is the one with minimal f value
            opened.remove(minim) # remove current minimum from opened array
            closed.append(minim) # add current minimum to the closed

            if curr == endPoint: # If the Snake eats food, then return the whole path for the draw function
                data = []
                while curr in pointBefore:
                    data.append(list(curr))
                    curr = pointBefore[curr]
                return data[::-1]

            closed.append(curr) # assert current position to closed

            for i, j in self.aroundPoints:
                neighbour = curr[0] + i, curr[1] + j
                tgs = gScore[curr] + self.heuristic(curr, neighbour)

                if 0 <= neighbour[0] < grid.shape[0]:
                    if 0 <= neighbour[1] < grid.shape[1]:
                        if grid[int(neighbour[0])][int(neighbour[1])] == 1 and grid(neighbour[0], neighbour[1]) != endPoint:
                            continue
                    else:
                        continue
                else:
                    continue

                if neighbour in closed and tgs >= gScore.get(neighbour, 0):
                    continue

                if tgs < gScore.get(neighbour, 0) or neighbour not in [i[1] for i in opened]:
                    pointBefore[neighbour] = curr
                    gScore[neighbour] = tgs
                    fScore[neighbour] = tgs + self.heuristic(neighbour, endPoint)
                    opened.append((fScore[neighbour],neighbour))

        return False
