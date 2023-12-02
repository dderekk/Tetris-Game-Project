.. autoDoc documentation master file, created by
   sphinx-quickstart on Wed Oct 11 00:48:04 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to autoDoc's documentation!
===================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

TetrisAI Class
==========

.. autoclass:: pythonSchoolProject.TetrisAI
   :members:

The `TetrisAI` class is the AI component of the Tetris game, designed to predict the best cube moves and rotations to achieve the highest scores.

Pseudocode
-------
.. code-block:: python

   # Initialize weights for scoring features
   function calculate_score(game_board, tetris_block):
       score = 0
       for each feature in features:
           score += weight[feature] * calculate_feature_value(game_board, tetris_block, feature)
       return score

   function predict_best_move(game_board, current_block):
       best_score = -infinity
       best_rotation = 0
       best_position = 0

       for each rotation in possible_rotations:
           for each position in possible_positions:
               if not has_collision(game_board, current_block, rotation, position):
                   score = calculate_score(game_board, current_block)
                   if score > best_score:
                       best_score = score
                       best_rotation = rotation
                       best_position = position

       return best_rotation, best_position

   function has_collision(game_board, current_block, rotation, position):
       // Check if placing the block at the specified rotation and position results in a collision
       // Return true if collision, false otherwise

   // Main game loop
   while game_not_over:
       current_block = get_next_block()
       best_rotation, best_position = predict_best_move(game_board, current_block)
       make_move(best_rotation, best_position)



Relevent Code:
-------
.. code-block:: python

   import random
   from blockData import BlockData
   from blockControl import BlocksControl


   class TetrisAI:
       """
           TetrisAI class for AI-controlled Tetris gameplay.

           This class defines the TetrisAI and its methods for playing Tetris.
       """

       # Define the weights for each feature
       WEIGHTS = {
           'landing_height': -5.5500158825082766,
           'rows_eliminated': 3.4181268101392694,
           'row_transitions': -3.2178882868487753,
           'column_transitions': -9.348695305445199,
           'number_of_holes': -7.899265427351652,
           'well_sums': -3.3855972247263626,
           'bumpiness': -2.111,
           'height_difference': -4.500158825082766
       }

       def __init__(self, block_data: BlockData, block_control: BlocksControl):
           """
                  Initialize TetrisAI with block data and control.

                  :param block_data: BlockData object containing game data.
                  :param block_control: BlocksControl object for controlling blocks.
           """
           self.background = block_data
           self.block_control = block_control
           self.blocks = block_data.blocks

       def calculate_aggregate_height(self,background,original_data):
           """
           Calculate the aggregate height of the current block.

           :param background: Current game background.
           :type background: list of list of int
           :param original_data: Original game data before placing the block.
           :type original_data: list of list of int

           :return: Aggregate height of the block.
           :rtype: int
           """
           height = 0
           Oheight = 0
           bheight = 0
           for col in range(10):
               for row in range(22, -1, -1):
                   if original_data[row][col] == 1:
                       Oheight += row
                       break
           for col in range(10):
               for row in range(22, -1, -1):
                   if background[row][col] == 1:
                       bheight += row
                       break
           height = bheight-Oheight
           return height

       def calculate_height_difference(self, background):
           """
                   Calculate the height difference between the highest and lowest points on the game board.

                   :param background: Current game background.
                   :type background: list of list of int

                   :return: Height difference on the game board.
                   :rtype: int
           """
           max_height = -1
           min_height = float('inf')

           for col in range(len(background[0])):
               for row in range(22, -1, -1):
                   if background[row][col] == 1:
                       max_height = max(max_height, row)
                       min_height = min(min_height, row)
                       break

           return max_height - min_height

       def calculate_complete_lines(self,background):
           """
                   Calculate the number of complete lines in the game background.

                   :param background: Current game background.
                   :type background: list of list of int

                   :return: Number of complete lines.
                   :rtype: int
           """
           complete_lines = 0
           for row in range(1, 23):
               if all(background[row]):
                   complete_lines += 1
           return complete_lines

       def calculate_holes(self, background):
           """
                   Calculate the number of holes in the game background.

                   :param background: Current game background.
                   :type background: list of list of int

                   :return: Number of holes.
                   :rtype: int
           """
           holes = 0
           rowHoles = [0] * len(background[0])  # Initialize rowHoles with zeros

           # Start from the second last row since the last row is the bottom of the container
           for row in range(len(background)-2,0,-1):
               currentRowHoles = [0] * len(background[0])  # Initialize currentRowHoles with zeros

               for col in range(0, len(background[0])):  # Exclude the first and last columns
                   # Check if the current position is a hole and the position above it is filled
                   if background[row][col] == 0 and (background[row + 1][col] == 1 or rowHoles[col] == 1):
                       currentRowHoles[col] = 1
                       holes += 1

               rowHoles = currentRowHoles  # Update rowHoles for the next iteration

           return holes

       def calculate_bumpiness(self, background):
           """
                   Calculate the bumpiness score of the game background.

                   :param background: Current game background.
                   :type background: list of list of int

                   :return: Bumpiness score.
                   :rtype: int
           """
           bumpiness = 0
           previous_height = 0

           for col in range(1, len(background[0])):
               for row in range(len(background) - 1, -1, -1):
                   if background[row][col] == 1:
                       current_height = len(background) - row
                       bumpiness += abs(current_height - previous_height)
                       previous_height = current_height
                       break

           return bumpiness

       def calculate_well_sums(self, background):
           """
                   Calculate the sum of well sums in the game background.

                   :param background: Current game background.
                   :type background: list of list of int

                   :return: Sum of well sums.
                   :rtype: int
           """
           well_sums = 0
           for col in range(1, 9):  # Starting at the second column and ending at the penultimate column
               for row in range(len(background)):
                   # Check that the current position is empty and has squares on its left and right sides
                   if background[row][col] == 0 and background[row][col - 1] == 1 and background[row][col + 1] == 1:
                       well_sums += 1
                       # Check below the current position until you encounter a square or reach the bottom
                       for k in range(row + 1, len(background)):
                           if background[k][col] == 0:
                               well_sums += 1
                           else:
                               break
           return well_sums

       def calculate_row_transitions(self, background):
           """
                   Calculate the number of row transitions in the game background.

                   :param background: Current game background.
                   :type background: list of list of int

                   :return: Number of row transitions.
                   :rtype: int
           """
           transitions = 0
           for row in range(len(background) - 1):  # Disregard the last row as it is the bottom of the container
               last_bit = 0  # Initialised to 0 for a null position
               for col in range(len(background[0])):
                   curr_bit = background[row][col]
                   if curr_bit != last_bit:
                       transitions += 1
                   last_bit = curr_bit
           return transitions

       def calculate_column_transitions(self, background):
           """
                   Calculate the number of column transitions in the game background.

                   :param background: Current game background.
                   :type background: list of list of int

                   :return: Number of column transitions.
                   :rtype: int
           """
           transitions = 0
           for col in range(len(background[0])):
               last_bit = 0  # Initialised to 0 for a null position
               for row in range(len(background)):
                   curr_bit = background[row][col]
                   if curr_bit != last_bit:
                       transitions += 1
                   last_bit = curr_bit
           return transitions

       def calculate_score(self, background,original_data):
           """
                  Calculate the overall score for the game state using the El-Tetris algorithm.

                  :param background: Current game background.
                  :type background: list of list of int
                  :param original_data: Original game data before placing the block.
                  :type original_data: list of list of int

                  :return: Overall game score.
                  :rtype: float
           """
           score = (
                   self.WEIGHTS['landing_height'] * self.calculate_aggregate_height(background,original_data) +
                   self.WEIGHTS['rows_eliminated'] * self.calculate_complete_lines(background) +
                   self.WEIGHTS['row_transitions'] * self.calculate_row_transitions(background) +
                   self.WEIGHTS['column_transitions'] * self.calculate_column_transitions(background) +
                   self.WEIGHTS['number_of_holes'] * self.calculate_holes(background) +
                   self.WEIGHTS['well_sums'] * self.calculate_well_sums(background) +
                   self.WEIGHTS['bumpiness'] * self.calculate_bumpiness(background) +
                   self.WEIGHTS['height_difference'] * self.calculate_height_difference(background)
           )
           return score

       def predict_best_move(self, background, block_ini_position, current_block_shape):
           """
                   Predict the best move for the current block based on the game state.

                   :param background: Current game background.
                   :type background: list of list of int
                   :param block_ini_position: Initial position of the current block.
                   :type block_ini_position: list of int
                   :param current_block_shape: Shape of the current block.
                   :type current_block_shape: list of tuple

                   :return: List of best moves [rotation, leftOrRightMove, moveDown].
                   :rtype: list of int
           """
           best_score = float('-inf')
           best_rotation = 0
           best_position = 0
           moveDown = 0

           original_data = [row[:] for row in background]
           original_position = block_ini_position.copy()

           for rotation in range(4):
               for position in range(10):
                   background = [row[:] for row in original_data]
                   block_ini_position = original_position.copy()


                   # Simulate movement to the desired position
                   while block_ini_position[1] != position:
                       # Check for collision after moving
                       if self.has_collision(background, block_ini_position, current_block_shape):
                           break

                       if position > block_ini_position[1]:
                           block_ini_position[1] += 1
                       else:
                           block_ini_position[1] -= 1



                   if self.has_collision(background, block_ini_position, current_block_shape):
                       continue

                   # Simulate dropping the block
                   while not self.has_collision(background, block_ini_position, current_block_shape):
                       block_ini_position[0] -= 1

                   # Update the background with the dropped block
                   for x, y in current_block_shape:
                       if 0 <= block_ini_position[0] + x < len(background) and 0 <= block_ini_position[1] + y < len(
                               background[0]):
                           background[block_ini_position[0] + x][block_ini_position[1] + y] = 1

                   score = self.calculate_score(background,original_data)

                   if score > best_score:
                       best_score = score
                       best_rotation = rotation
                       best_position = position
                       moveDown = original_position[0] - block_ini_position[0]
                       print(score,rotation)

               current_block_shape = [(col,-row) for row, col in current_block_shape]

           leftOrRightMove = best_position - 5
           if not isinstance(moveDown, int):
               moveDown = 0
           elif not moveDown:
               moveDown = 0
           print([best_rotation, leftOrRightMove, moveDown])
           print("-------------------------------------------------------------")
           return [best_rotation, leftOrRightMove, moveDown]

       def has_collision(self, background, position, shape):
           """
                   Check if there is a collision between the current block and the game background.

                   :param background: Current game background.
                   :type background: list of list of int
                   :param position: Position of the current block.
                   :type position: list of int
                   :param shape: Shape of the current block.
                   :type shape: list of tuple

                   :return: True if there is a collision, False otherwise.
                   :rtype: bool
           """
           y_drop, x_move = position
           for row, col in shape:
               row += y_drop
               col += x_move
               # Check if it is beyond the left, right or lower boundaries
               if col < 0 or col > 9 or row < 1 or row >= len(background):
                   return True
               # Checks for collisions with other squares in the background
               if background[row-1][col] == 1:
                   return True
           return False

