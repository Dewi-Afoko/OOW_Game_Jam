import pygame
import random

# Initialize Pygame
pygame.init()

# Game window settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ocean Cleanup Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (135, 206, 250)

# Load trash image (use a placeholder if you don't have one yet)
TRASH_IMAGE = pygame.image.load("trash.png")  # Replace with your image file
TRASH_IMAGE = pygame.transform.scale(TRASH_IMAGE, (50, 50))  # Resize

# Trash object (random position)
def spawn_trash():
    return pygame.Rect(random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50), 50, 50)

trash = spawn_trash()

# Score tracking
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    screen.fill(BLUE)  # Background color

    # Draw trash
    screen.blit(TRASH_IMAGE, (trash.x, trash.y))

    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (20, 20))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Detect mouse click
            if trash.collidepoint(event.pos):  # If clicked on trash
                score += 1
                trash = spawn_trash()  # Spawn new trash

    pygame.display.flip()  # Update display

pygame.quit()
