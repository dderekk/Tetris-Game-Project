import pygame

class gamePlayPage:
    """a class for show the game play page"""

    def __init__(self, screen):
        """initilazation"""
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 30)
        self.is_active = False
        self.close_rect = None

    def draw(self,screen):
        """draw the gamefile in the input screen"""
        # set screen size
        screen_width = 800
        screen_height = 750
        # colour defined
        black = (0, 0, 0)

        pg.draw.rect(screen, (140, 130, 195), (250 * s, 0, 383 * s, 500 * s))

        # Team nunmber
        font = pygame.font.Font(None, 36)
        gamesTeam_text = font.render("Team Number: 2", True, black)
        gamesTeam_rect = gamesTeam_text.get_rect(
            center=(screen_width // 2 + 160, screen_height // 5 + 120))
        screen.blit(gamesTeam_text, gamesTeam_rect)

        # Current score of the session.
        font = pygame.font.Font(None, 36)
        gamesScore_text = font.render(f"Score: {str(Blocks.score[0])}", True, black)
        gamesScore_rect = gamesScore_text.get_rect(center=(screen_width // 2 + 160, screen_height // 5 + 60))
        screen.blit(gamesScore_text, gamesScore_rect)

        # Number of lines eliminated in the session
        font = pygame.font.Font(None, 36)
        gamesLines_text = font.render(f"{str(Blocks.complete_row_counts)} lines eliminated", True, black)
        gamesLines_rect = gamesLines_text.get_rect(
            center=(screen_width // 2 + 160, screen_height // 5 + 180))
        screen.blit(gamesLines_text, gamesLines_rect)

        # Current level
        font = pygame.font.Font(None, 36)
        gamesLevel_text = font.render(f"Current level: {gameLevel}", True,
                                      black)
        gamesLevel_rect = gamesLevel_text.get_rect(
            center=(screen_width // 2 + 160, screen_height // 5 + 240))
        screen.blit(gamesLevel_text, gamesLevel_rect)

        # Extended or normal game
        font = pygame.font.Font(None, 36)
        gamesExtend_text = font.render("Extend: OFF", True,
                                       black)
        gamesExtend_rect = gamesExtend_text.get_rect(
            center=(screen_width // 2 + 160, screen_height // 5 + 300))
        screen.blit(gamesExtend_text, gamesExtend_rect)

        # Game Mode
        font = pygame.font.Font(None, 36)
        gamesMode_text = font.render("Player Mode", True,
                                     black)
        gamesMode_rect = gamesMode_text.get_rect(
            center=(screen_width // 2 + 160, screen_height // 5))
        screen.blit(gamesMode_text, gamesMode_rect)

        # Next Block
        font = pygame.font.Font(None, 36)
        nextBlock_text = font.render("Next Block", True,
                                     black)
        nextBlock_rect = nextBlock_text.get_rect(
            center=(screen_width // 2 + 160, screen_height // 5 + 360))
        screen.blit(nextBlock_text, nextBlock_rect)

    def activate(self):
        """let the play page be active"""
        self.is_active = True

    def deactivate(self):
        """let the play page be deactive"""
        self.is_active = False
