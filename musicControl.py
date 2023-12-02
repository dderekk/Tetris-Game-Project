import pygame

class Music:
    """a class control the background music and sounds effect"""

    def __init__(self):
        """initialization"""
        self.is_paused = False
        self.current_track = "01 Main Theme - May Be Happy.mp3"

    def play(self, track=None):
        """a method for turn the music on"""
        if track:
            self.current_track = track
        pygame.mixer.music.load(self.current_track)
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play()

    def pause_or_resume(self):
        """switch the music on and off"""
        if self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False
        else:
            pygame.mixer.music.pause()
            self.is_paused = True

    def fadeout(self, time):
        """by the input time, to fadeout the current music in a certain time"""
        pygame.mixer.music.fadeout(time)

    def changeMusic1(self):
        """function for changing music"""
        pygame.mixer.music.load("01 Main Theme - May Be Happy.mp3")
        self.current_track = "01 Main Theme - May Be Happy.mp3"
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play()

    def changeMusic2(self):
        """function for changing music"""
        pygame.mixer.music.load("36 Dot Nurie Stage 1 - I Love Psg !!!.mp3")
        self.current_track = "36 Dot Nurie Stage 1 - I Love Psg !!!.mp3"
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play()

    def changeMusic3(self):
        """function for changing music"""
        pygame.mixer.music.load("115 Dot Nurie Lv2 - Magical July.mp3")
        self.current_track ="115 Dot Nurie Lv2 - Magical July.mp3"
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play()

    def changeMusic4(self):
        """function for changing music"""
        pygame.mixer.music.load("12 To The Groundwater - Gambling Without Luck.mp3")
        self.current_track ="12 To The Groundwater - Gambling Without Luck.mp3"
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play()

    def changeMusic5(self):
        """function for changing music"""
        pygame.mixer.music.load("188 Destroyed Castle - Fragments Of Memory.mp3")
        self.current_track ="188 Destroyed Castle - Fragments Of Memory.mp3"
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play()

    def movingeffect1(self):
        """function for changing sound effect"""
        sound_effect = pygame.mixer.Sound("drum.mp3")
        sound_effect.play()

    def movingeffect2(self):
        """function for changing sound effect"""
        sound_effect = pygame.mixer.Sound("drum2.mp3")
        sound_effect.play()

    def movingeffect3(self):
        """function for changing sound effect"""
        sound_effect = pygame.mixer.Sound("clap.mp3")
        sound_effect.play()

    def movingeffect4(self):
        """function for changing sound effect"""
        sound_effect = pygame.mixer.Sound("heavy.mp3")
        sound_effect.play()



