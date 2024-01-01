import pygame
import random
from astar import astar
from settings import *


class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = row * GRID_SIZE
        self.y = col * GRID_SIZE
        self.color = WHITE
        self.neighbors = []

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, GRID_SIZE, GRID_SIZE))

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < ROWS - 1 and grid[self.row + 1][self.col].color != BLACK: # Down
            self.neighbors.append(grid[self.row + 1][self.col])
        if self.row > 0 and grid[self.row - 1][self.col].color != BLACK: # Up
            self.neighbors.append(grid[self.row - 1][self.col])
        if self.col < COLS - 1 and grid[self.row][self.col + 1].color != BLACK: # Right
            self.neighbors.append(grid[self.row][self.col + 1])
        if self.col > 0 and grid[self.row][self.col - 1].color != BLACK: # Left
            self.neighbors.append(grid[self.row][self.col - 1])

def make_grid(rows, cols):
    grid = []
    for i in range(rows):
        grid.append([])
        for j in range(cols):
            node = Node(i, j)
            grid[i].append(node)
    return grid

def draw_grid(win, rows, cols):
    for i in range(rows):
        pygame.draw.line(win, BLACK, (0, i * GRID_SIZE), (WIDTH, i * GRID_SIZE))
    for j in range(cols):
        pygame.draw.line(win, BLACK, (j * GRID_SIZE, 0), (j * GRID_SIZE, HEIGHT))

def draw(win, grid, rows, cols):
    win.fill(WHITE)

    for row in grid:
        for node in row:
            node.draw(win)

    draw_grid(win, rows, cols)
    pygame.display.update()

def get_clicked_pos(pos):
    y, x = pos
    row = y // GRID_SIZE
    col = x // GRID_SIZE
    return row, col


def convert_grid_for_astar(grid):
    astar_grid = []
    for row in grid:
        astar_row = []
        for node in row:
            if node.color == BLACK:  # Wall
                astar_row.append(1)
            else:
                astar_row.append(0)
        astar_grid.append(astar_row)
    return astar_grid


def generate_random_maze(grid, wall_density=0.3):
    for row in grid:
        for node in row:
            if random.random() < wall_density:
                node.color = BLACK