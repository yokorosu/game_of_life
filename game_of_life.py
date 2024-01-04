import os
import time
import random
import copy


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def initialize_grid(rows, cols):
    grid = [[0] * cols for _ in range(rows)]
    return grid


def randomize_grid(grid):
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = random.randint(0, 1)


def render_grid(grid):
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            cell = grid[i][j]
            print('◼' if cell else '◻', end=' ')
        print()
    print()


def get_neighbours(grid, row, col):
    rows = len(grid)
    cols = len(grid[0])
    neighbours = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            neighbour_row = (row + i + rows) % rows
            neighbour_col = (col + j + cols) % cols
            neighbours.append(grid[neighbour_row][neighbour_col])
    return neighbours


def update_grid(grid):
    rows = len(grid)
    cols = len(grid[0])
    new_grid = copy.deepcopy(grid)
    for i in range(rows):
        for j in range(cols):
            cell = grid[i][j]
            neighbours = get_neighbours(grid, i, j)
            live_neighbours = neighbours.count(1)
            if cell == 1 and (live_neighbours < 2 or live_neighbours > 3):
                new_grid[i][j] = 0
            elif cell == 0 and live_neighbours == 3:
                new_grid[i][j] = 1
    return new_grid


def count_alive_cells(grid):
    return sum(sum(row) for row in grid)


def main():
    rows = 5
    cols = 5
    grid = initialize_grid(rows, cols)
    randomize_grid(grid)

    game_running = True
    game_speed = 1
    start_time = time.time()

    while game_running:
        current_time = time.time()
        elapsed_time = current_time - start_time

        clear_screen()
        print(f"Elapsed time: {elapsed_time:.2f}s")
        print(f"Game speed: {game_speed}")

        render_grid(grid)

        alive_cells = count_alive_cells(grid)
        print(f"Alive cells: {alive_cells}")


        key = input("Чтобы увеличить скорость напишите '+', чтобы уменьшить '-', если хотите закончить игру напишите 'end', если нечего не нужно изменять, то ничего не пишите : ")
        if key == '+':
            game_speed += 1
        elif key == '-':
            if game_speed > 1:
                game_speed -= 1
        elif key == 'end':
            game_running = False

        grid = update_grid(grid)
        time.sleep(1 / game_speed)


if __name__ == '__main__':
    main()