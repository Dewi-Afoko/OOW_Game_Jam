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

# Load a background image
background_img = pygame.image.load('./assets/background.jpg')
# Resize background to fit screen
background = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

# Load trash image (use a placeholder if you don't have one yet)
TRASH_IMAGE = pygame.image.load("./assets/trash.png")  # Replace with your image file
TRASH_IMAGE = pygame.transform.scale(TRASH_IMAGE, (50, 50))  # Resize

# Load trash image (use a placeholder if you don't have one yet)
TURTLE_IMAGE = pygame.image.load("./assets/turtle.png")  # Replace with your image file
TURTLE_IMAGE = pygame.transform.scale(TURTLE_IMAGE, (50, 50))  # Resize

# Trash object (random position)
def spawn_trash():
    return pygame.Rect(random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50), 50, 50)

def spawn_turtle():
    return pygame.Rect(random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50), 50, 50)

trash = spawn_trash()

turtle = spawn_turtle()

# Score tracking
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    screen.blit(background, (0,0)) 

    # Draw trash
    screen.blit(TRASH_IMAGE, (trash.x, trash.y))
    
    # Draw turtle
    screen.blit(TURTLE_IMAGE, (turtle.x, turtle.y))

    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (20, 20))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:  # Detect mouse click
            if trash.collidepoint(event.pos):  # If clicked on trash
                score += 5
                trash = spawn_trash()  # Spawn new trash
        if event.type == pygame.MOUSEBUTTONDOWN:  # Detect mouse click
            if turtle.collidepoint(event.pos):  # If clicked on trash
                score -= 5
                turtle = spawn_turtle()  # Spawn new trash

    pygame.display.flip()  # Update display

pygame.quit()
