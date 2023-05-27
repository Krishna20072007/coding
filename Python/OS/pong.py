import pygame
from pygame.locals import *
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pong")

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the initial positions and velocities
ball_x = WINDOW_WIDTH // 2
ball_y = WINDOW_HEIGHT // 2
ball_dx = random.choice([-3, 3])
ball_dy = random.choice([-3, 3])

paddle_width = 10
paddle_height = 80
paddle_speed = 5

player_paddle_x = 10
player_paddle_y = WINDOW_HEIGHT // 2 - paddle_height // 2

opponent_paddle_x = WINDOW_WIDTH - 10 - paddle_width
opponent_paddle_y = WINDOW_HEIGHT // 2 - paddle_height // 2

score_font = pygame.font.Font(None, 72)
player_score = 0
opponent_score = 0

clock = pygame.time.Clock()

# Game loop
running = True
first_time = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[K_UP] and player_paddle_y > 0:
        player_paddle_y -= paddle_speed
    if keys[K_DOWN] and player_paddle_y < WINDOW_HEIGHT - paddle_height:
        player_paddle_y += paddle_speed

    # Computer opponent logic
    if opponent_paddle_y + paddle_height // 2 < ball_y:
        if opponent_paddle_y < WINDOW_HEIGHT - paddle_height:
            opponent_paddle_y += paddle_speed
    if opponent_paddle_y + paddle_height // 2 > ball_y:
        if opponent_paddle_y > 0:
            opponent_paddle_y -= paddle_speed

    ball_x += ball_dx
    ball_y += ball_dy

    # Check collision with paddles
    if ball_x <= player_paddle_x + paddle_width and player_paddle_y < ball_y < player_paddle_y + paddle_height:
        ball_dx = -ball_dx
    if ball_x >= opponent_paddle_x - paddle_width and opponent_paddle_y < ball_y < opponent_paddle_y + paddle_height:
        ball_dx = -ball_dx

    # Check collision with walls
    if ball_y <= 0 or ball_y >= WINDOW_HEIGHT:
        ball_dy = -ball_dy

    # Check if ball goes out of bounds
    if ball_x < 0:
        if first_time:
            first_time = False
        else:
            opponent_score += 1
        ball_x = WINDOW_WIDTH // 2
        ball_y = WINDOW_HEIGHT // 2
        ball_dx = random.choice([-4, 4])
        ball_dy = random.choice([-4, 4])
    elif ball_x > WINDOW_WIDTH:
        player_score += 1
        ball_x = WINDOW_WIDTH // 2
        ball_y = WINDOW_HEIGHT // 2
        ball_dx = random.choice([-4, 4])
        ball_dy = random.choice([-4, 4])

    window.fill(BLACK)

    # Draw paddles
    pygame.draw.rect(window, WHITE, (player_paddle_x, player_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(window, WHITE, (opponent_paddle_x, opponent_paddle_y, paddle_width, paddle_height))

    # Draw ball
    pygame.draw.circle(window, WHITE, (ball_x, ball_y), 10)

    # Draw scores
    player_text = score_font.render(str(player_score), True, WHITE)
    opponent_text = score_font.render(str(opponent_score), True, WHITE)
    score_separator = score_font.render("|", True, WHITE)
    window.blit(player_text, (WINDOW_WIDTH // 2 - player_text.get_width() - 10, 10))
    window.blit(score_separator, (WINDOW_WIDTH // 2 - score_separator.get_width() // 2, 10))
    window.blit(opponent_text, (WINDOW_WIDTH // 2 + 10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
