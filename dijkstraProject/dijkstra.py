from .constants import *
from .board import Board
import heapq
import pygame
from .node import Node


class Dijsktra:
    def __init__(self, board):
        self.board = board
        self.pathTo = {}
        self.pq = []
        heapq.heapify(self.pq)

    def __relax(self, currentnode, fromnode):
        # Relaxation rule
        if currentnode.dist > (fromnode.dist + 1 + currentnode.weight):
            currentnode.dist = fromnode.dist + 1 + currentnode.weight
            self.pathTo[currentnode.point] = fromnode.point
            if currentnode in self.pq:
                self.pq.remove(currentnode)

            heapq.heappush(self.pq, currentnode)

    def __newpoints(self, currentNode):
        # up
        col = currentNode.point[1]
        row = currentNode.point[0]-1
        if row >= 0:
            #print(f'up new point {row,col}')
            yield self.board.board[row][col]
        # down
        col = currentNode.point[1]
        row = currentNode.point[0]+1
        if row < ROWS:
            #print(f'down new point {row,col}')
            yield self.board.board[row][col]
        # left
        row = currentNode.point[0]
        col = currentNode.point[1]-1
        if col >= 0:
            #print(f'left new point {row,col}')
            yield self.board.board[row][col]
        # right
        row = currentNode.point[0]
        col = currentNode.point[1]+1
        if col < COLS:
            #print(f'right new point {row,col}')
            yield self.board.board[row][col]

    def findshortpath(self, initpoint, target):
        notFound = True
        # Obtain the Node in the board
        startNode = self.board.board[initpoint[0]][initpoint[1]]
        # Update the distance to the start Node
        startNode.dist = 0
        heapq.heappush(self.pq, startNode)
        while self.pq and notFound:
            currentNode = heapq.heappop(self.pq)
            # If the current node hasnt been visited
            if currentNode.unvisited:
                # It is marked as visited making it visible
                currentNode.unvisited = False
                if currentNode.type == 'normal':
                    self.board.drawpoint(currentNode.point, BLUE)
                # Get the adjacent nodes
                adjNodes = self.__newpoints(currentNode)
                # Filter the already visited nodes
                adjNodes = list(filter(lambda x: x.unvisited, adjNodes))
                # print(adjNodes)
                # draw the adjacent points
                self.board.drawevapoints(adjNodes)
                pygame.display.update()
                for adjNode in adjNodes:
                    self.__relax(adjNode, currentNode)
                    # Validates if we are at the target Node
                    if adjNode.point == target:
                        notFound = False
                        vertex = self.pathTo[target]
                        # there most be a path from init to target
                        while vertex != initpoint:
                            self.board.drawpoint(vertex, YELLOW)
                            pygame.display.update()
                            vertex = self.pathTo[vertex]
                        break
