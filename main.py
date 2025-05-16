import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Falling Blocks")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10
player_speed = 7

# Blocks
block_size = 50
block_speed = 5
block_list = []

# Score
score = 0
font = pygame.font.SysFont("Arial", 28)

def drop_blocks(block_list):
    delay = random.random()
    if len(block_list) < 10 and delay < 0.1:
        x_pos = random.randint(0, WIDTH - block_size)
        block_list.append([x_pos, 0])

def draw_blocks(block_list):
    for block in block_list:
        pygame.draw.rect(screen, RED, (block[0], block[1], block_size, block_size))

def update_blocks(block_list, score):
    for idx, block in enumerate(block_list):
        if block[1] >= 0 and block[1] < HEIGHT:
            block[1] += block_speed
        else:
            block_list.pop(idx)
            score += 1
    return score

def collision(player_x, player_y, block_list):
    for block in block_list:
        if (player_x < block[0] + block_size and
            player_x + player_size > block[0] and
            player_y < block[1] + block_size and
            player_y + player_size > block[1]):
            return True
    return False

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key press logic
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    drop_blocks(block_list)
    score = update_blocks(block_list, score)
    draw_blocks(block_list)
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))

    if collision(player_x, player_y, block_list):
        running = False

    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
print(f"Game Over! Final Score: {score}")
