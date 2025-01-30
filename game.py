import pygame
import random

# Initialize Pygame
pygame.init()

# Game window settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Save The Turtles!")



# Colors
WHITE = (255, 255, 255)

# Load a background image
background_img = pygame.image.load('./assets/background.jpg')
# Resize background to fit screen
background = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

# Load trash image (use a placeholder if you don't have one yet)
TRASH_IMAGE = pygame.image.load("./assets/trash.png")  # Replace with your image file
TRASH_IMAGE = pygame.transform.scale(TRASH_IMAGE, (150, 150))  # Resize

# Load trash image (use a placeholder if you don't have one yet)
TURTLE_IMAGE = pygame.image.load("./assets/turtle.png")  # Replace with your image file
TURTLE_IMAGE = pygame.transform.scale(TURTLE_IMAGE, (150, 150))  # Resize

# Trash object (random position)
def spawn_trash():
    return pygame.Rect(random.randint(150, WIDTH-50), random.randint(50, HEIGHT-50), 150, 150)

# Stole the trash logic for turtles
def spawn_turtle():
    return pygame.Rect(random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50), 150, 150)

trash = spawn_trash()

turtle = spawn_turtle()

trash_list = [spawn_trash() for _ in range(4)]
turtle_list = [spawn_turtle() for _ in range(4)]

# Score tracking
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    screen.blit(background, (0,0)) 

    # Draw trash from trash_list 
    for trash in trash_list:
        screen.blit(TRASH_IMAGE, (trash.x, trash.y))
    
    # Draw turtle
    for turtle in turtle_list:
        screen.blit(TURTLE_IMAGE, (turtle.x, turtle.y))

    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (20, 20))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:  # Detect mouse click
            for trash in trash_list[:]: #Copy trash_list to maintain range/spawn number
                if trash.collidepoint(event.pos):  # If clicked on trash
                    score += 3
                    trash_list.remove(trash)  # Delete clicked trash
                    trash_list.append(spawn_trash()) #Spawn new trash

        if event.type == pygame.MOUSEBUTTONDOWN:  # Detect mouse click
            for turtle in turtle_list[:]: #Copy trash_list to maintain range/spawn number
                if turtle.collidepoint(event.pos):  # If clicked on trash
                    score -= 5
                    turtle_list.remove(turtle)  # Delete clicked trash
                    turtle_list.append(spawn_turtle()) #Spawn new trash

    if score > 30:
        win_message = font.render("Congrats", True, WHITE)
        screen.blit(win_message, (400, 300))

    if score < 0:
        turtle_killer = font.render("Please try and save the turtles!", True, WHITE)
        screen.blit(turtle_killer, (250, 250))

    pygame.display.flip()  # Update display

pygame.quit()
