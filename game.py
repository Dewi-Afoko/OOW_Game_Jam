import pygame
import random

# Initialize Pygame
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('./assets/soundtrack.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0)

# Game window settings

WIDTH, HEIGHT = 1440, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))


pygame.display.set_caption("Save The Turtles!")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

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
    return pygame.Rect(random.randint(150, WIDTH-150), random.randint(150, HEIGHT-150), 150, 150)

# Stole the trash logic for turtles
def spawn_turtle():
    return pygame.Rect(random.randint(150, WIDTH-150), random.randint(150, HEIGHT-150), 150, 150)

trash = spawn_trash()

turtle = spawn_turtle()

trash_list = [spawn_trash() for _ in range(4)]
turtle_list = [spawn_turtle() for _ in range(2)]

# Pollution tracking
pollution_level = 50
last_pollution_update = pygame.time.get_ticks()  # Track time for pollution increase

font = pygame.font.Font(None, 36)
alert_font = pygame.font.Font(None, 72)


winning_pollution_level = 0
losing_pollution_level = 100
game_over = False

clock = pygame.time.Clock()

# Game loop
running = True
while running:
    screen.blit(background, (0,0)) 
    clock.tick(60)
    if not game_over:

        current_pollution_level = pygame.time.get_ticks()

        if 0 < (current_pollution_level - pollution_level) > 100:
            pollution_level += 0.017
            last_pollution_update = current_pollution_level 

        # Draw trash from trash_list 
        for trash in trash_list:
            screen.blit(TRASH_IMAGE, (trash.x, trash.y))
        
        # Draw turtle
        for turtle in turtle_list:
            screen.blit(TURTLE_IMAGE, (turtle.x, turtle.y))

        # Display pollution_level
        pollution_text = font.render(f"Pollution level: {int(pollution_level)}", True, WHITE)
        screen.blit(pollution_text, (20, 20))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:  # Detect mouse click
                for trash in trash_list[:]: #Copy trash_list to maintain range/spawn number
                    if trash.collidepoint(event.pos):  # If clicked on trash
                        pollution_level -= 5
                        trash_list.remove(trash)  # Delete clicked trash
                        trash_list.append(spawn_trash()) #Spawn new trash

            if event.type == pygame.MOUSEMOTION:  # Detect mouse moving over turtle
                for turtle in turtle_list[:]: #Copy trash_list to maintain range/spawn number
                    if turtle.collidepoint(event.pos):  # If clicked on trash
                        pollution_level += 10
                        turtle_list.remove(turtle)  # Delete clicked trash
                        turtle_list.append(spawn_turtle()) #Spawn new trash

        if pollution_level < 30:
            keep_going = font.render("Great job, keep going!", True, WHITE)
            screen.blit(keep_going, (WIDTH // 2 - 200, HEIGHT // 2 - 50))

        if pollution_level > 70:
            turtle_killer = font.render("Try and clean up the trash, while avoiding turtles!", True, RED)
            screen.blit(turtle_killer, (WIDTH // 2 - 200, HEIGHT // 2 - 50))

        if pollution_level <= winning_pollution_level or pollution_level >= losing_pollution_level:
                game_over = True

    if pollution_level <= winning_pollution_level:
        winning_message = alert_font.render("You win!", True, (255, 255, 0))
        screen.blit(winning_message, (WIDTH // 2 - 200, HEIGHT // 2 - 50))

        restart_text = font.render("Click or press any key to restart on hard mode", True, (255, 255, 255))
        screen.blit(restart_text, (WIDTH // 2 - 200, HEIGHT // 2 + 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type in (pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN):  # Restart game on click or key press
                pollution_level = 50
                game_over = False
                trash_list = [spawn_trash() for _ in range(4)]
                turtle_list = [spawn_turtle() for _ in range(4)]

    if pollution_level >= losing_pollution_level:
        winning_message = alert_font.render("You lose!", True, (255, 255, 0))
        screen.blit(winning_message, (WIDTH // 2 - 200, HEIGHT // 2 - 50))

        restart_text = font.render("Click or press any key to restart on easy mode", True, (255, 255, 255))
        screen.blit(restart_text, (WIDTH // 2 - 200, HEIGHT // 2 + 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type in (pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN):  # Restart game on click or key press
                pollution_level = 50
                game_over = False
                trash_list = [spawn_trash() for _ in range(6)]
                turtle_list = [spawn_turtle() for _ in range(2)]
        


    pygame.display.flip()  # Update display

pygame.mixer.music.stop()
pygame.quit()
