import pygame
import random
from .constants import *
from .node import Node
import time


class Board:
    def __init__(self, win):
        self.board = []
        self.win = win

    # Create the Grid
    def __draw_squares(self):
        self.win.fill(WHITE)
        for row in range(1, ROWS):
            pygame.draw.line(self.win, GREY, (0, row*SQUARE_SIZE),
                             (WIDTH, row*SQUARE_SIZE))

        for col in range(1, COLS):
            pygame.draw.line(self.win, GREY, (col*SQUARE_SIZE, 0),
                             (col*SQUARE_SIZE, HEIGHT))

    # Create the Nodes
    def __fillboard(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append(Node((row, col)))

    def initiateGrid(self):
        self.__draw_squares()
        self.__fillboard()

    def initpoint(self):
        """Select a random position to start """
        col = int(random.uniform(0, COLS))
        row = int(random.uniform(0, ROWS))
        return (row, col)

    def targetpoint(self, initpoint):
        """Select a random position as the target as long it is not the same start """
        while True:
            col = int(random.uniform(0, COLS))
            row = int(random.uniform(0, ROWS))
            if (row, col) != initpoint:
                break
        return (row, col)

    def drawcircle(self, point, color):
        radius = SQUARE_SIZE//2 - PADDLING
        pygame.draw.circle(
            self.win, color, (point[1]*SQUARE_SIZE+SQUARE_SIZE//2, point[0]*SQUARE_SIZE+SQUARE_SIZE//2), radius)

    def drawpoint(self, point, color):
        pygame.draw.rect(
            self.win, color, (point[1]*SQUARE_SIZE, point[0]*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def update(self, initpoint, targetpoint):
        self.__draw_squares()
        # draw init point
        self.drawcircle(initpoint, GREEN)
        self.drawcircle(targetpoint, RED)
        # pygame.display.flip()
        pygame.display.update()

    def drawevapoints(self, nodelist):
        color = GREY
        for i, x in enumerate(nodelist):
            if x.type == 'normal':
                self.drawpoint(x.point, color)

    def drawWeights(self, point):
        # if the current Node is normal, it changes it to weighted Node
        currentNode = self.board[point[0]][point[1]]
        if currentNode.type == 'normal':
            currentNode.weight = 25
            currentNode.type = 'weight'
            color = BLACK
        elif currentNode.type == 'weight':
            currentNode.weight = 25
            currentNode.type = 'normal'
            color = WHITE
        else:
            return
        self.drawcircle(point, color)
