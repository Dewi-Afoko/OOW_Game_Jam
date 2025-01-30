import pygame
import random

# Initialise Pygame
pygame.init()
pygame.mixer.init()

# Load and play background music
pygame.mixer.music.load('./assets/soundtrack.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0)

# Load sound effects
success_sound = pygame.mixer.Sound('./assets/sonic_ring.mp3')
success_sound.set_volume(0.1)
fail_sound = pygame.mixer.Sound('./assets/fail.mp3')
fail_sound.set_volume(0.1)

# Game window settings
WIDTH, HEIGHT = 1440, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Save The Turtles!")

# Colours
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (55, 134, 29)
PURPLE = (184, 12, 227)

# Load background image
background_img = pygame.image.load('./assets/background.jpg')
background = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

# Load images
TRASH_IMAGE = pygame.image.load("./assets/trash.png")
TRASH_IMAGE = pygame.transform.scale(TRASH_IMAGE, (150, 150))
TURTLE_IMAGE = pygame.image.load("./assets/turtle.png")
TURTLE_IMAGE = pygame.transform.scale(TURTLE_IMAGE, (150, 150))

# Helper functions
def spawn_trash():
    return pygame.Rect(random.randint(150, WIDTH - 150), random.randint(150, HEIGHT - 150), 150, 150)

def spawn_turtle():
    return pygame.Rect(random.randint(150, WIDTH - 150), random.randint(150, HEIGHT - 150), 150, 150)

# Pollution tracking
pollution_level = 50
last_pollution_update = pygame.time.get_ticks()
winning_pollution_level = 0
losing_pollution_level = 100
game_over = False

# Fonts
font = pygame.font.Font(None, 48)
alert_font = pygame.font.Font(None, 72)

def instructions_screen():
    screen.fill((0, 0, 0))
    title = alert_font.render("Our Only World - Clean Up The Ocean!", True, WHITE)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 200))
    rules = font.render("Click trash to remove it but avoid touching turtles!", True, WHITE)
    screen.blit(rules, (WIDTH // 2 - rules.get_width() // 2, 600))
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False

# Show instructions before starting the game
instructions_screen()

# Game objects
trash_list = [spawn_trash() for _ in range(4)]
turtle_list = [spawn_turtle() for _ in range(2)]

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(60)
    screen.blit(background, (0, 0))
    
    if not game_over:
        current_time = pygame.time.get_ticks()
        if current_time - last_pollution_update >= 1000:
            pollution_level += 1
            last_pollution_update = current_time

        for trash in trash_list:
            screen.blit(TRASH_IMAGE, (trash.x, trash.y))
        for turtle in turtle_list:
            screen.blit(TURTLE_IMAGE, (turtle.x, turtle.y))

        pollution_text = alert_font.render(f"Pollution level: {int(pollution_level)}", True, GREEN)
        screen.blit(pollution_text, (60, 60))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for trash in trash_list[:]:
                    if trash.collidepoint(event.pos):
                        success_sound.play()
                        pollution_level -= 5
                        trash_list.remove(trash)
                        trash_list.append(spawn_trash())
            if event.type == pygame.MOUSEMOTION:
                for turtle in turtle_list[:]:
                    if turtle.collidepoint(event.pos):
                        fail_sound.play()
                        pollution_level += 10
                        turtle_list.remove(turtle)
                        turtle_list.append(spawn_turtle())
        
        if pollution_level <= winning_pollution_level or pollution_level >= losing_pollution_level:
            game_over = True
    
    if game_over:
        if pollution_level <= winning_pollution_level:
            message = "You win! Click to restart on hard mode"
        else:
            message = "You lose! Click to restart on easy mode"
        game_over_text = alert_font.render(message, True, (255, 255, 0))
        screen.blit(game_over_text, (WIDTH // 2 - 300, HEIGHT // 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type in (pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN):
                pollution_level = 50
                game_over = False
                trash_list = [spawn_trash() for _ in range(6 if pollution_level > winning_pollution_level else 4)]
                turtle_list = [spawn_turtle() for _ in range(2)]
    
    pygame.display.flip()

pygame.mixer.music.stop()
pygame.quit()
