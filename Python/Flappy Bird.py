import pygame
import random

# Initialize Pygame
pygame.init()

# Game window dimensions
WIDTH = 800
HEIGHT = 600

# Colors
CYAN = (0, 255, 255)
LIMEGREEN = (50, 205, 50)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Bird position and velocity
bird_x = 100
bird_y = 250
bird_radius = 20
bird_vel = 0
bird_acc = 0.1

# Pipe positions
pipe_x = WIDTH
pipe_y = random.randint(150, 450)
pipe_gap = 200
pipe_width = 50

# Game variables
score = 0
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_vel = -3

    # Update bird position and velocity
    bird_y += bird_vel
    bird_vel += bird_acc

    # Update pipe position
    pipe_x -= 6
    if pipe_x < -pipe_width:
        pipe_x = WIDTH
        pipe_y = random.randint(150, 450)
        score += 1

    # Check for collision
    if bird_y < 0 or bird_y + bird_radius > HEIGHT or (
            bird_x + bird_radius > pipe_x and bird_x - bird_radius < pipe_x + pipe_width and (
            bird_y - bird_radius < pipe_y or bird_y + bird_radius > pipe_y + pipe_gap)):
        running = False

    # Draw background
    screen.fill(CYAN)

    # Draw bird
    pygame.draw.circle(screen, YELLOW, (bird_x, int(bird_y)), bird_radius)
    pygame.draw.circle(screen, BLACK, (bird_x, int(bird_y)), bird_radius, 2)

    # Draw pipe
    pygame.draw.rect(screen, LIMEGREEN, (pipe_x, 0, pipe_width, pipe_y))
    pygame.draw.rect(screen, LIMEGREEN, (pipe_x, pipe_y + pipe_gap, pipe_width, HEIGHT - pipe_y - pipe_gap))
    pygame.draw.rect(screen, BLACK, (pipe_x, 0, pipe_width, pipe_y), 2)
    pygame.draw.rect(screen, BLACK, (pipe_x, pipe_y + pipe_gap, pipe_width, HEIGHT - pipe_y - pipe_gap), 2)

    # Display score
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
