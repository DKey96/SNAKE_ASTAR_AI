"""
    Author: Daniel Klic, 2019, VAI project, Brno University of Technlogies, Faculty of Mechanical Engineering, Mechatronics

    This script contains the Astar algorithm
"""


class Astar:
    height: int
    width: int
    grid: object
    around_points: list[tuple[int, int]]

    def __init__(self, grid: object, width: int, height: int) -> object:
        self.grid = grid
        self.around_points = [(0, -10), (0, 10), (-10, 0), (10, 0)]
        self.width = width
        self.height = height

    # Compute the heuristic cost
    @staticmethod
    def heuristic(point_a: tuple, point_b: tuple):
        return (point_b[0] - point_a[0]) ** 2 + (point_b[1] - point_a[1]) ** 2

    # Define neighbours
    def get_neighbours(self, point: tuple):
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

    def path(self, start_point: tuple, end_point: tuple, obst_pos: list[tuple], body: list[list[int | float]]):
        opened, closed = [], []
        point_before = {}  # Dict of all the points before
        new_snake_body, new_obst_pos = [], []  # New snake's body and obstacle positions as lists of tuples

        for b in body:
            b = tuple(b)
            new_snake_body.append(b)

        for o in obst_pos:
            o = tuple(o)
            new_obst_pos.append(o)

        g_score = {start_point: 0}  # Initialize G score from f = g + h
        f_score = {start_point: self.heuristic(start_point, end_point)}  # Initialize F score from f = g + h
        opened.append((f_score[start_point], start_point))  # Add F score to the startPoint (snakes head)

        while opened:
            minim = min(opened, key=lambda param: param[0])  # Minimal value of the F from points around
            curr = minim[1]  # current position is the one with minimal f value
            opened.remove(minim)  # remove current minimum from opened array
            closed.append(minim)  # add current minimum to the closed

            if curr == end_point:  # If the Snake eats food, then return the whole path for the draw function
                data = []
                while curr in point_before:
                    data.append(list(curr))
                    curr = point_before[curr]
                return data[::-1]

            closed.append(curr)  # assert current position to closed
            neighbours = self.get_neighbours(curr)  # get neighbours

            for neighbour in neighbours:  # for all neighbours do...
                if neighbour not in closed and neighbour not in new_snake_body[
                                                                1:] and neighbour not in new_obst_pos:  # If neighbour not an obstacle or tail
                    tgs = g_score[curr] + self.heuristic(curr, neighbour)  # tentative G score

                    if neighbour in closed and tgs >= g_score.get(neighbour, 0):
                        continue
                    if neighbour in opened:
                        if tgs < g_score.get(neighbour, 0):
                            point_before[neighbour] = curr
                            g_score[neighbour] = tgs
                            f_score[neighbour] = tgs + self.heuristic(neighbour, end_point)
                    else:
                        point_before[neighbour] = curr
                        g_score[neighbour] = tgs
                        f_score[neighbour] = tgs + self.heuristic(neighbour, end_point)
                        opened.append((f_score[neighbour], neighbour))  # set to the opened with new F score
        return False
