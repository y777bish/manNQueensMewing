import pygame
import sys

class Solution:

    def solveNQueens(self, n: int):
        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."

        backtrack(0)
        return res

def draw_board(board, n, index):
    # Constants
    WIDTH, HEIGHT = 800, 800
    SQUARE_SIZE = WIDTH // n
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("N-Queens Visualization")

    # Load queen image
    queen_img = pygame.image.load('queen.png')
    queen_img = pygame.transform.scale(queen_img, (SQUARE_SIZE, SQUARE_SIZE))
    SCREEN.fill((255, 255, 255))  # White background

    for row in range(n):
        for col in range(n):
            color = (118,150,86) if (row + col) % 2 == 0 else   (238,238,210)
            pygame.draw.rect(SCREEN, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            if board[row][col] == "Q":
                queen_img = pygame.image.load('queen.png')
                queen_img = pygame.transform.scale(queen_img, (SQUARE_SIZE, SQUARE_SIZE))
                SCREEN.blit(queen_img, (col * SQUARE_SIZE, row * SQUARE_SIZE))
    
    # Display index of the solution
    # font = pygame.font.Font(None, 36)
    # text = font.render(f"Solution {index+1}/{len(board)}", True, (0, 0, 0))
    # text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT - 50))
    # SCREEN.blit(text, text_rect)
    # print(f"Solution {index+1}/{len(board)}")

# Initialize Pygame
pygame.init()



# Main function
def main():
    n = int(input("Podaj n: "))
    solution = Solution()
    results = solution.solveNQueens(n)
    
    # Main loop
    running = True
    index = 0
    total_solutions = len(results)
    needs_update = True
    
    while running:
        if needs_update:
            draw_board(results[index], n, index)
            pygame.display.update()
            needs_update = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    index = (index - 1) % total_solutions
                    needs_update = True
                elif event.key == pygame.K_RIGHT:
                    index = (index + 1) % total_solutions
                    needs_update = True

# Run the main function
if __name__ == "__main__":
    main()
