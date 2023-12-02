import pygame

pygame.init()

# screen size
screen_width = 800
screen_height = 600
pygame.display.set_caption("Yes or No")

clock = pygame.time.Clock()

class PopupWindow:
    """a pop up window for show exiting game options"""

    def __init__(self):
        """initilization"""
        self.surface = pygame.Surface((300, 250))
        self.rect = self.surface.get_rect(center=(screen_width // 5 + 20, screen_height // 2))

    def draw(self,screen):
        """input screen, and draw the pop up window in to this screen"""
        self.surface.fill((255, 255, 255))
        pygame.draw.rect(self.surface, (0, 0, 0), self.surface.get_rect(), 3)

        # YES or NO buttorn
        font = pygame.font.Font(None, 36)
        yes_text = font.render("YES", True, (0, 0, 0))
        no_text = font.render("NO", True, (0, 0, 0))

        yes_rect = yes_text.get_rect(center=(self.surface.get_width() // 4, self.surface.get_height() // 2 + 50))
        no_rect = no_text.get_rect(center=(3 * self.surface.get_width() // 4, self.surface.get_height() // 2 + 50))

        # EEC TEXT
        font = pygame.font.Font(None, 36)
        esc_text = font.render("end the game ?", True, (0, 0, 0))
        esc_rect = esc_text.get_rect(center=(self.surface.get_width() // 2, self.surface.get_height() // 2 -30))

        self.surface.blit(esc_text, esc_rect)
        self.surface.blit(yes_text, yes_rect)
        self.surface.blit(no_text, no_rect)

        screen.blit(self.surface, self.rect)

    def handle_event(self, event):
        """handle the event in the popup wind, the input is the event of game"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                if self.rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                    if self.rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                        if self.surface.get_rect(center=(
                        self.rect.x + self.rect.width // 4, self.rect.y + self.rect.height // 2)).collidepoint(
                                mouse_pos):
                            return "YES"
                        elif self.surface.get_rect(center=(
                        3 * self.rect.x + self.rect.width // 4, self.rect.y + self.rect.height // 2)).collidepoint(
                                mouse_pos):
                            return "NO"

        return None

