import pygame

class StartUpPage:
    """a class to show the startup page, it is the first page when game is statrting"""

    def __init__(self, screen):
        """initlization"""
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 30)
        self.is_active = True
        self.score_rect = None
        self.play_rect = None
        self.options_rect = None
        self.quit_rect = None

    def draw(self,screen,size):
        """draw the startup page into the screen
        input:screen-> where the startup page draw on, size-> to control the size of start up page"""
        # set screen size
        screen_width = 800*size
        screen_height = 750*size
        # colour defined
        black = (0, 0, 0)

        # Game title
        font = pygame.font.Font(None, 64)
        title_text = font.render("Tetris Game", True, black)
        title_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 5))

        # Year and course code: 2023-7805ICT
        font = pygame.font.Font(None, 24)
        course_text = font.render("2023      7805ICT - Software Design", True, black)
        course_rect = course_text.get_rect(center=(screen_width // 2 - 230, screen_height // 3))

        # list of students
        font = pygame.font.Font(None, 24)
        student_text = font.render("Derek   Talia   Pouya   Vy", True, black)
        student_rect = student_text.get_rect(center=(screen_width // 2 - 230, screen_height // 3 + 30))

        # Option Buttons
        font = pygame.font.Font(None, 40)
        play_button = font.render("Play", True, black)
        play_rect = play_button.get_rect(center=(screen_width // 2, screen_height // 2))

        font = pygame.font.Font(None, 36)
        score_button = font.render("Score", True, black)
        score_rect = score_button.get_rect(center=(screen_width // 2, screen_height // 2 + 60))

        options_button = font.render("Configure", True, black)
        options_rect = options_button.get_rect(center=(screen_width // 2, screen_height // 2 + 120))

        quit_button = font.render("Exit", True, black)
        quit_rect = quit_button.get_rect(center=(screen_width // 2, screen_height // 2 + 180))

        screen.blit(title_text, title_rect)
        screen.blit(course_text, course_rect)
        screen.blit(student_text, student_rect)
        screen.blit(play_button, play_rect)
        screen.blit(score_button, score_rect)
        screen.blit(options_button, options_rect)
        screen.blit(quit_button, quit_rect)
        pygame.display.flip()

        self.score_rect = score_rect
        self.play_rect = play_rect
        self.options_rect = options_rect
        self.quit_rect = quit_rect
        pygame.display.flip()
    def activate(self):
        """show the startup page"""
        self.is_active = True

    def deactivate(self):
        """do not show the startup page"""
        self.is_active = False
