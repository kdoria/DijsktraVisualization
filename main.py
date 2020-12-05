import pygame
from dijkstraProject import WIDTH, HEIGHT, GREEN, RED, SQUARE_SIZE
from dijkstraProject.board import Board
from dijkstraProject.dijkstra import Dijsktra


FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dijkstra')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return (row, col)


def main():
    run = True
    clock = pygame.time.Clock()
    tablet = Board(WIN)
    tablet.initiateGrid()
    # print(tablet.board)
    initpoint = tablet.initpoint()
    # mark the initpoint as the start
    startNode = tablet.board[initpoint[0]][initpoint[1]]
    startNode.type = 'start'
    print(initpoint)
    targetpoint = tablet.targetpoint(initpoint)
    tablet.drawcircle(initpoint, GREEN)
    tablet.drawcircle(targetpoint, RED)
    targetNode = tablet.board[targetpoint[0]][targetpoint[1]]
    targetNode.type = 'target'
    dij = Dijsktra(tablet)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                #dij.findshortpath(initpoint, targetpoint)
                pos = pygame.mouse.get_pos()
                weight = get_row_col_from_mouse(pos)
                tablet.drawWeights(weight)

            elif event.type == event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dij.findshortpath(initpoint, targetpoint)

        # game.update()
        #tablet.update(initpoint, targetpoint)
        pygame.display.update()

    pygame.quit()


main()
