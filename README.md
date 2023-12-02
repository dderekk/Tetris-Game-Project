# Tetris Game Project

## Description
This project is a streamlined version of the classic Tetris game, developed for the 2805ICT System and Software Design, 3815ICT Software Engineering, and 7805ICT Principles of Software Engineering courses. It features an advanced AI algorithm for automated gameplay, alongside a traditional player-controlled mode.

## Features
- Customizable game settings via a start-up configuration page.
- Player control using keyboard inputs for movement and rotation of Tetris blocks.
- AI Mode featuring an advanced algorithm for automated gameplay.
- Scoring system based on line eliminations and game tactics.
- High score tracking for both player and AI modes.

## Usage
To start the game, run the following command in the project directory:
Keyboard controls for player mode:
- Arrow keys for moving and rotating blocks.
- 'P' to pause/resume.
- 'Esc' to exit.
- 'M' to toggle music.

## AI Implementation

### Overview
The core of our AI implementation is the `TetrisAI` class. This class controls the AI gameplay, making decisions based on the evaluation of various game metrics.

### Key Features of TetrisAI
- **Class Structure**: The `TetrisAI` class encapsulates the AI logic, including methods for scoring and move prediction.
- **Decision-Making**: Utilizes a range of metrics like row transitions, number of holes, and bumpiness to evaluate the game board.
- **Move Prediction**: Determines the optimal rotation and position for each block to maximize the overall score.
- **Collision Detection**: Essential for preventing illegal moves by the AI.
