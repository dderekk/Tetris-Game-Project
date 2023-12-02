import pygame
from dataProcess import dataProcess

class ScorePage:
    """a class for show the score page, include top 10 players' name and score"""

    def __init__(self, screen):
        """initialization"""
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 30)
        self.is_active = False
        self.close_rect = None

    def draw(self,screen,size):
        """draw the score page into the screen,
        input: screen -> where to draw on, size-> control the size of the pages"""
        # set screen size
        screen_width = 800*size
        screen_height = 750*size
        # colour defined
        black = (0, 0, 0)

        font = pygame.font.Font(None, 48)
        top_text = font.render("Top 10 Score", True, black)
        top_rect = top_text.get_rect(center=(screen_width // 2, screen_height // 7))

        font = pygame.font.Font(None, 30)
        close_button = font.render("Close", True, black)
        close_rect = close_button.get_rect(center=(screen_width // 2 + 260, screen_height // 1.5 + 160))

        # get top 10 data here:
        scoredata = dataProcess()
        top10data = scoredata.getTop10Data()
        rank = 1
        font = pygame.font.Font(None, 28)
        for eachPlayer, eachScores in top10data:
            player_text = font.render(f"{rank}. {eachPlayer} :   {eachScores}", True, black)
            player_rect = player_text.get_rect(center=(screen_width // 2 + 20, screen_height // 6 + rank * 45))
            rank += 1
            screen.blit(player_text, player_rect)

        screen.blit(close_button, close_rect)
        screen.blit(top_text, top_rect)

        self.close_rect = close_rect

    def activate(self):
        """show the score page"""
        self.is_active = True

    def deactivate(self):
        """do not show the score page"""
        self.is_active = False
