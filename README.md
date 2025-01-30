Makers gamejam 2025 repo

Setting Up Your Pygame Project in VS Code
To structure your project cleanly, here’s how you should organize your directory:

bash
Copy
Edit
ocean_cleanup_game/
│── assets/              # Folder for images, sounds, etc.
│   ├── background.png   # Static background image of the sea
│   ├── garbage1.png     # Garbage sprite (plastic bottle, can, etc.)
│   ├── garbage2.png     # Another garbage sprite
│── main.py              # Main game loop and logic
│── settings.py          # Game settings and constants
│── sprites.py           # Defines game objects like garbage
│── requirements.txt     # List of dependencies (e.g., pygame)
│── README.md            # Project description and setup guide
1. Install Dependencies
First, install pygame:

sh
Copy
Edit
pip install pygame
To ensure consistency, create a requirements.txt file:

Copy
Edit
pygame
2. Code Implementation
main.py (Handles the game loop)
This script initializes the game, loads assets, and runs the main loop.

python
Copy
Edit
import pygame
import random
from settings import *
from sprites import Garbage

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ocean Cleanup")

# Load background
background = pygame.image.load("assets/background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Group for garbage objects
all_sprites = pygame.sprite.Group()

# Create garbage objects
for _ in range(NUM_GARBAGE):
    all_sprites.add(Garbage())

# Game loop
running = True
while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Check for mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            for sprite in all_sprites:
                if sprite.rect.collidepoint(event.pos):
                    sprite.kill()  # Remove the clicked garbage

    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
settings.py (Game Constants)
Keeps the settings organized in one place.

python
Copy
Edit
WIDTH = 800
HEIGHT = 600
NUM_GARBAGE = 5  # Number of garbage items to appear
GARBAGE_IMAGES = ["assets/garbage1.png", "assets/garbage2.png"]
sprites.py (Garbage Object Class)
Defines the garbage sprites with random positions.

python
Copy
Edit
import pygame
import random
from settings import WIDTH, HEIGHT, GARBAGE_IMAGES

class Garbage(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(random.choice(GARBAGE_IMAGES))
        self.image = pygame.transform.scale(self.image, (50, 50))  # Resize if needed
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, WIDTH - 50)
        self.rect.y = random.randint(50, HEIGHT - 50)
3. Running the Game
Save all files.
Open a terminal in VS Code.
Run the game:
sh
Copy
Edit
python main.py
Additional Features to Consider
Score System: Show a score for each garbage item collected.
Timer: Encourage quick cleanup before time runs out.
Sound Effects: Play a sound when garbage is clicked.
Animations: Have floating or wavy effects on the garbage.
This setup ensures a well-structured, maintainable, and scalable project. Let me know if you need refinements! 🚀
