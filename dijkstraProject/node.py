class Node:
    def __init__(self, point):
        self.point = point
        self.dist = float('Inf')
        self.weight = 0
        self.unvisited = True
        self.type = 'normal'

    def __repr__(self):
        return f'point: {self.point}'

    def __lt__(self, other):
        return self.dist < other.dist

    def __eq__(self, other):
        return self.point == other.point
