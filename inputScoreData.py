import pygame
import sys
from dataProcess import dataProcess
pygame.init()

# Screen size
screen_width = 800
screen_height = 750
pygame.display.set_caption("Congratulation")

clock = pygame.time.Clock()


class enterData:
    """a class for popup window when game is finish"""

    def __init__(self):
        """initilazation"""
        self.surface = pygame.Surface((500, 350))
        self.rect = self.surface.get_rect(center=(screen_width // 2, screen_height // 2))
        self.active = False
        self.text = ""
        self.font = pygame.font.Font(None, 36)

    def draw(self, screen,score):
        """draw this window, input: screen-> where the pop up window draw on, score-> show and record it"""
        self.surface.fill((255, 255, 255))
        pygame.draw.rect(self.surface, (0, 0, 0), self.surface.get_rect(), 3)

        # Text above the input box
        top_text = self.font.render('Congratulation, you are top 10!!', True, (0, 0, 0))
        score_text = self.font.render(f'Your Score is: {score}', True, (0, 0, 0))
        name_text = self.font.render('Please enter your name', True, (0, 0, 0))

        # Calculate the width of the input box
        txt_surface = self.font.render(self.text, True, (0, 0, 0))
        width = max(200, txt_surface.get_width() + 10)

        input_rect = pygame.Rect(50, 200, width, 50)
        pygame.draw.rect(self.surface, (0, 0, 0), input_rect, 2)

        # Blit the text above the input box
        self.surface.blit(top_text,(50,75))
        self.surface.blit(score_text, (50, 120))  # Adjust the position as needed
        self.surface.blit(name_text, (50, 165))  # Adjust the position as needed

        # Blit the input box and text
        self.surface.blit(txt_surface, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = width

        # Blit the surface
        screen.blit(self.surface, self.rect.topleft)

    def handle_event(self, event,score):
        """a function for handle the mouse and keyborad action,
        input: event-> for handle the event, score-> for showing and recording"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    data_processor = dataProcess()
                    print(f"{self.text}")
                    print(score)
                    data_processor.addNewData(self.text, score)
                    self.text = ""
                    return "DONE"
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
        return None

    def whileloop(self,score):
        """a function to continus show the popup window until a 'enter' key is pressed,
        input screen -> where the popup window draw on"""
        screen = pygame.display.set_mode((screen_width, screen_height))
        result = None
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                result = self.handle_event(event,score)
            if result == "DONE":
                self.active = False
                break

            screen.fill((30, 30, 30))
            if self.active:
                self.draw(screen,score)
            pygame.display.update()
            clock.tick(30)