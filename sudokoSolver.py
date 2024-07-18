import pygame
import requests

width = 550
bg_color = (245, 251, 250)
buffer = 5
original_grid_element_color = (0, 0, 0)

def draw_grid(window):
    for i in range(0, 10):
        if i % 3 == 0:
            pygame.draw.line(window, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
            pygame.draw.line(window, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)
        else:
            pygame.draw.line(window, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
            pygame.draw.line(window, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)
    pygame.display.update()

def fetch_sudoku_board():
    try:
        response_API = requests.get("https://sudoku-api.vercel.app/api/dosuku?difficulty=easy")
        response_API.raise_for_status()
        json_response = response_API.json()
        print(json_response)  # Print the entire JSON response for debugging

        # Adjust this based on the actual structure of the response
        if 'board' in json_response:
            return json_response['board']
        else:
            print("Error: 'board' key not found in the JSON response.")
            return None
    except (requests.exceptions.RequestException, ValueError) as e:
        print(f"Error fetching the Sudoku board: {e}")
        return [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]

def draw_board(window, grid):
    font = pygame.font.SysFont('Comic Sans MS', 35)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if 0 < grid[i][j] < 10:
                value = font.render(str(grid[i][j]), True, original_grid_element_color)
                window.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50))
    pygame.display.update()

def is_empty(number):
    return number == 0

def is_valid(grid, position, number):
    for i in range(len(grid)):
        if grid[position[0]][i] == number or grid[i][position[1]] == number:
            return False

    x = position[0] // 3 * 3
    y = position[1] // 3 * 3

    for i in range(3):
        for j in range(3):
            if grid[x + i][y + j] == number:
                return False

    return True

def sudoku_solver(window, grid):
    global solving
    font = pygame.font.SysFont('Comic Sans MS', 35)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if is_empty(grid[i][j]):
                for k in range(1, 10):
                    if is_valid(grid, (i, j), k):
                        grid[i][j] = k
                        pygame.draw.rect(window, bg_color, ((j + 1) * 50 + buffer, (i + 1) * 50 + buffer, 50 - 2 * buffer, 50 - 2 * buffer))
                        value = font.render(str(k), True, (0, 0, 0))
                        window.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50))
                        pygame.display.update()
                        pygame.time.delay(10)

                        sudoku_solver(window, grid)

                        if solving == 1:
                            return

                        grid[i][j] = 0
                        pygame.draw.rect(window, bg_color, ((j + 1) * 50 + buffer, (i + 1) * 50 + buffer, 50 - 2 * buffer, 50 - 2 * buffer))
                        return
                solving = 1

def main():
    pygame.init()
    window = pygame.display.set_mode((width, width))
    pygame.display.set_caption("Sudoku using Backtracking")
    window.fill(bg_color)
    draw_grid(window)

    grid_board = fetch_sudoku_board()

    if grid_board:
        draw_board(window, grid_board)
    else:
        print("Using fallback board.")
        grid_board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        draw_board(window, grid_board)

    global solving
    solving = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        sudoku_solver(window, grid_board)

if __name__ == "__main__":
    main()
