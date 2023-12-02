import random
import pygame

class BlockData():
    """a class that holds block data"""
    extendMode = False
    blocks = [
        [[0, 0], [0, -1], [0, 1], [0, 2]],  # I
        [[0, 0], [0, -1], [-1, 0], [-1, 1]],  # Z
        [[0, 0], [0, 1], [1, 1], [1, 0]],  # squre
        [[0, 0], [0, 1], [-1, 1], [-1, 0]],  # rev_Z
        [[0, 0], [0, 1], [1, 0], [0, -1]],  # T
        [[0, 0], [1, 0], [-1, 0], [1, -1]],  # L
        [[0, 0], [1, 0], [-1, 0], [1, 1]]  # rev_L
    ]

    background = [[0 for clo in range(10)] for row in range(23)]
    background[0] = [1 for gr in range(10)]
    block_ini_position = [22, 5]
    block_size = 1.5
    score = [0]
    complete_row_counts = 0
    Next_Block = random.choice(blocks)
    select_Block = []
    gameOver = False

    def __init__(self):
        """initialize"""
        # Define the initial state of the game
        self.select_Block = None  # Currently selected block
        self.Next_Block = list(random.choice(self.blocks))  # Next block to com
        self.score = [0]  # Initial score
        self.complete_row_counts = 0  # Number of rows completed
        self.gameOver = False  # Game over flag
        self.background = [[0 for clo in range(10)] for row in range(23)]  # create back ground
        self.background[0] = [1 for gr in range(10)]  # make a ground, stop blocks fall below the ground
        self.block_ini_position = [22, 5]
        self.extendMode = False
        self.block_size = 1.5

    def extendMode_switch(self):
        """switch the mode"""
        if self.extendMode:
            self.blocks = [
                [[0, 0], [0, -1], [0, 1], [0, 2]],  # I
                [[0, 0], [0, -1], [-1, 0], [-1, 1]],  # Z
                [[0, 0], [0, 1], [1, 1], [1, 0]],  # squre
                [[0, 0], [0, 1], [-1, 1], [-1, 0]],  # rev_Z
                [[0, 0], [0, 1], [1, 0], [0, -1]],  # T
                [[0, 0], [1, 0], [-1, 0], [1, -1]],  # L
                [[0, 0], [1, 0], [-1, 0], [1, 1]]  # rev_L
            ]
            self.extendMode = False
        else:
            self.blocks = [
                [[0, 0], [0, -1], [0, 1], [0, 2]],  # I
                [[0, 0], [0, -1], [-1, 0], [-1, 1]],  # Z
                [[0, 0], [0, 1], [1, 1], [1, 0]],  # squre
                [[0, 0], [0, 1], [-1, 1], [-1, 0]],  # rev_Z
                [[0, 0], [0, 1], [1, 0], [0, -1]],  # T
                [[0, 0], [1, 0], [-1, 0], [1, -1]],  # L
                [[0, 0], [1, 0], [-1, 0], [1, 1]],  # rev_L
                [[0, 0], [0, -1], [0, 1]],  # little I
                [[0, 0], [1, 0], [1, -1]]
            ]
            self.extendMode = True

    def getExtendMode(self):
        """give the Mode state to other class"""
        return self.extendMode