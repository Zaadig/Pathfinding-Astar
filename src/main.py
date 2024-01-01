import pygame
from grid import *
from astar import astar
from settings import *



def main(win):
    grid = make_grid(ROWS, COLS)

    start = None
    end = None

    run = True
    while run:
        draw(win, grid, ROWS, COLS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]: # left click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos)
                node = grid[row][col]
                if not start and node != end:
                    start = node
                    start.color = GREEN
                elif not end and node != start:
                    end = node
                    end.color = RED
                elif node != end and node != start:
                    node.color = BLACK

            elif pygame.mouse.get_pressed()[2]: # right click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos)
                node = grid[row][col]
                node.color = WHITE
                if node == start:
                    start = None
                elif node == end:
                    end = None

            if event.type == pygame.KEYDOWN: # space bar to run astar
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)

                    astar_grid = convert_grid_for_astar(grid)
                    start_pos = (start.row, start.col)
                    end_pos = (end.row, end.col)

                    path = astar(astar_grid, start_pos, end_pos)

                    if path:
                        for pos in path:
                            row, col = pos
                            grid[row][col].color = BLUE
                            draw(win, grid, ROWS, COLS)
                            pygame.time.wait(50)
                elif event.key == pygame.K_m:  # 'm' key to generate maze
                    generate_random_maze(grid)
                    start, end = None, None  # reset start and end points

    pygame.quit()

if __name__ == "__main__":
    pygame.init()
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pathfinding Visualizer")
    main(WIN)
