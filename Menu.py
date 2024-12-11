import pygame
import sys
import importlib
import os

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man Menu")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GRAY = (100, 100, 100)

# Load background image
try:
    background = pygame.image.load(os.path.join("Assets", "Pac_Man_Map.png"))
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
except:
    background = None

# Fonts
try:
    title_font = pygame.font.Font(os.path.join("Assets", "AlphaSmart3000.ttf"), 74)
except:
    title_font = pygame.font.Font(None, 74)

menu_font = pygame.font.Font(None, 50)

class Button:
    def __init__(self, x, y, width, height, text, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.color = YELLOW
        self.hover_color = WHITE

    def draw(self, surface):
        current_color = self.hover_color if self.is_hovered() else self.color
        pygame.draw.rect(surface, current_color, self.rect, 3)
        text_surface = menu_font.render(self.text, True, current_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.is_hovered() and self.action:
                self.action()

def run_game_section(module_name):
    """
    Dynamically import and run a game section
    
    Args:
        module_name (str): Name of the Python module to import and run
    """
    try:
        # Close the current Pygame window
        pygame.quit()
        
        # Dynamically import the module
        game_module = importlib.import_module(module_name)
        
        # Reset Pygame
        pygame.init()
        
        # Run the main function of the imported module
        if hasattr(game_module, 'main'):
            game_module.main()
        else:
            print(f"No 'main' function found in {module_name}")
        
    except ImportError:
        print(f"Could not import module: {module_name}")
    except Exception as e:
        print(f"Error running {module_name}: {e}")
    
    # Ensure Pygame is closed after running the game
    pygame.quit()
    sys.exit()

def start_section_1():
    """Start the first game section"""
    run_game_section('bolum1')  # Import and run bolum1.py


def main_menu():
    """Main menu loop"""
    # Create buttons
    bolum_1_button = Button(
        SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2, 300, 75, "Bölüm 1", start_section_1
    )

    # Main game loop
    running = True
    while running:
        # Clear screen with black
        screen.fill(BLACK)
        
        # Draw background if available
        if background:
            screen.blit(background, (0, 0))

        # Draw semi-transparent overlay for better text visibility
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(128)  # 128 is semi-transparent
        screen.blit(overlay, (0, 0))

        # Draw title with shadow effect
        shadow_offset = 3
        title_shadow = title_font.render("Pac-Man Menüsü", True, BLACK)
        title_text = title_font.render("Pac-Man Menüsü", True, YELLOW)
        
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        shadow_rect = title_rect.copy()
        shadow_rect.x += shadow_offset
        shadow_rect.y += shadow_offset
        
        screen.blit(title_shadow, shadow_rect)
        screen.blit(title_text, title_rect)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            
            bolum_1_button.handle_event(event)

        # Draw buttons
        bolum_1_button.draw(screen)
        
        # Update display
        pygame.display.flip()

    # Quit the game
    pygame.quit()
    sys.exit()

# Run the game
if __name__ == "__main__":
    main_menu()