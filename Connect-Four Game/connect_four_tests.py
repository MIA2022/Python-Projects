"""
Nan Chen
HW7---Test file.

Implement a test suite for class ConnectFour
using the unittest methodology.
"""


import unittest
from connect_four import ConnectFour


class ConnectFourTest(unittest.TestCase):

    def test_init_(self):
        """
         Test if it is right to initialize any other class attributes.
        :return:none.
        """
        my_game = ConnectFour()
        self.assertEqual([[' '] * 7] * 6, my_game.board)
        self.assertEqual([], my_game.position_stack)
        self.assertEqual([], my_game.player_stack)
        expected = list('XO' * 21)
        self.assertEqual(expected, my_game.queue)
        self.assertDictEqual({}, my_game.o_dict1)
        self.assertDictEqual({}, my_game.o_dict2)
        self.assertDictEqual({}, my_game.sum_o_dict)
        self.assertDictEqual({}, my_game.diff_o_dict)
        self.assertDictEqual({}, my_game.x_dict1)
        self.assertDictEqual({}, my_game.x_dict2)
        self.assertDictEqual({}, my_game.sum_x_dict)
        self.assertDictEqual({}, my_game.diff_x_dict)

    def test_str(self):
        """
        Test if it is right for a string that represents the board..
        :return:none
        """
        my_game = ConnectFour()
        expected = '| | | | | | | |\n---------------\n' * 6
        self.assertEqual(expected, my_game.__str__())

    def test_add_piece_value_error(self):
        """
        The column is invalid (outside of the playing area).
        If it doesn't raise an error, test fail.
        :return:none
        """
        try:
            my_game = ConnectFour()
            my_game.add_piece(7)
            self.fail('Should raised an error due to the out-ranged column')
        except ValueError:
            pass

    def test_add_piece_value_error1(self):
        """
        The column is already full
        If it doesn't raise an error, test fail.
        :return:none
        """
        try:
            my_game = ConnectFour()
            my_game.board[0] = ['X', 'O', 'X', 'O', 'X', 'O', 'X']
            my_game.board[1] = ['X', 'O', 'X', 'O', 'X', 'O', 'X']
            my_game.board[2] = ['X', 'O', 'X', 'O', 'X', 'O', 'X']
            my_game.board[3] = ['O', 'X', 'O', 'X', 'O', 'X', 'O']
            my_game.board[4] = ['O', 'X', 'O', 'X', 'O', 'X', 'O']
            my_game.board[5] = ['O', 'X', 'O', 'X', 'O', 'X', 'O']
            my_game.add_piece(3)
            self.fail('Should raised an error due to'
                      ' the column is already full')
        except ValueError:
            pass

    def test_add_piece_value_error2(self):
        """
        my_game.board[4] = ['O', 'O', 'O', ' ', ' ', ' ', ' ']
        my_game.board[5] = ['X', 'X', 'X', 'X', ' ', ' ', ' ']
        The winner is X. The game already is over.
        If it doesn't raise an error, test fail.
        :return:none
        """
        try:
            my_game = ConnectFour()
            my_game.x_dict1 = {5: {0, 1, 2, 3}}
            my_game.o_dict1 = {4: {0, 1, 2}}
            my_game.add_piece(3)
            self.fail('Should raised an error due to the game is over')
        except ValueError:
            pass

    def test_add_piece_value(self):
        """
        Add four pieces into the initial board. Check if the
        corresponding attributes of the objects are equal to the expected.
        :return:none
        """
        my_game = ConnectFour()
        my_game.add_piece(0)  # Add X in the first column of the 6th row.
        my_game.add_piece(0)  # Add O in the first column of the 5th row.
        my_game.add_piece(1)  # Add X in the second column of the 6th row.
        my_game.add_piece(1)  # Add O in the second column of the 5th row.
        expected_position_stack = [(5, 0), (4, 0), (5, 1), (4, 1)]
        expected_player_stack = ['X', 'O', 'X', 'O']
        expected_queue = list('XO' * 19)
        expected_x_dict1 = {5: {0, 1}}
        expected_x_dict2 = {0: {5}, 1: {5}}
        expected_sum_x_dict = {5: {0}, 6: {1}}
        expected_diff_x_dict = {5: {0}, 4: {1}}
        expected_o_dict1 = {4: {0, 1}}
        expected_o_dict2 = {0: {4}, 1: {4}}
        expected_sum_o_dict = {4: {0}, 5: {1}}
        expected_diff_o_dict = {4: {0}, 3: {1}}
        expected = [[' '] * 7] * 4
        expected.append(['O', 'O', ' ', ' ', ' ', ' ', ' '])
        expected.append(['X', 'X', ' ', ' ', ' ', ' ', ' '])
        self.assertEqual(expected, my_game.board)
        self.assertEqual(expected_queue, my_game.queue)
        self.assertEqual(expected_position_stack, my_game.position_stack)
        self.assertEqual(expected_player_stack, my_game.player_stack)
        self.assertDictEqual(expected_o_dict1, my_game.o_dict1)
        self.assertDictEqual(expected_o_dict2, my_game.o_dict2)
        self.assertDictEqual(expected_sum_o_dict, my_game.sum_o_dict)
        self.assertDictEqual(expected_diff_o_dict, my_game.diff_o_dict)
        self.assertDictEqual(expected_x_dict1, my_game.x_dict1)
        self.assertDictEqual(expected_x_dict2, my_game.x_dict2)
        self.assertDictEqual(expected_sum_x_dict, my_game.sum_x_dict)
        self.assertDictEqual(expected_diff_x_dict, my_game.diff_x_dict)

    def test_add_piece_after_undo(self):
        """
        If calling undo , then latest piece is undone, then call
        add_piece again, the undone piece is added again. Check if the
        corresponding attributes of the objects are equal to the expected.
        :return:none
        """
        my_game = ConnectFour()
        my_game.add_piece(0)  # Add X in the first column of the 6th row.
        my_game.add_piece(0)  # Add O in the first column of the 5th row.
        my_game.add_piece(1)  # Add X in the second column of the 6th row.
        my_game.add_piece(1)  # Add O in the second column of the 5th row.
        # Undo the last O.
        my_game.undo()
        my_game.add_piece(1)  # Add O in the second column of the 5th row.
        expected_position_stack = [(5, 0), (4, 0), (5, 1), (4, 1)]
        expected_player_stack = ['X', 'O', 'X', 'O']
        expected_queue = list('XO' * 19)
        expected_x_dict1 = {5: {0, 1}}
        expected_x_dict2 = {0: {5}, 1: {5}}
        expected_sum_x_dict = {5: {0}, 6: {1}}
        expected_diff_x_dict = {5: {0}, 4: {1}}
        expected_o_dict1 = {4: {0, 1}}
        expected_o_dict2 = {0: {4}, 1: {4}}
        expected_sum_o_dict = {4: {0}, 5: {1}}
        expected_diff_o_dict = {4: {0}, 3: {1}}
        expected = [[' '] * 7] * 4
        expected.append(['O', 'O', ' ', ' ', ' ', ' ', ' '])
        expected.append(['X', 'X', ' ', ' ', ' ', ' ', ' '])
        self.assertEqual(expected, my_game.board)
        self.assertEqual(expected_queue, my_game.queue)
        self.assertEqual(expected_position_stack, my_game.position_stack)
        self.assertEqual(expected_player_stack, my_game.player_stack)
        self.assertDictEqual(expected_o_dict1, my_game.o_dict1)
        self.assertDictEqual(expected_o_dict2, my_game.o_dict2)
        self.assertDictEqual(expected_sum_o_dict, my_game.sum_o_dict)
        self.assertDictEqual(expected_diff_o_dict, my_game.diff_o_dict)
        self.assertDictEqual(expected_x_dict1, my_game.x_dict1)
        self.assertDictEqual(expected_x_dict2, my_game.x_dict2)
        self.assertDictEqual(expected_sum_x_dict, my_game.sum_x_dict)
        self.assertDictEqual(expected_diff_x_dict, my_game.diff_x_dict)

    def test_is_game_over_true(self):
        """
        Check all conditions that the game is over. Returns a
        boolean that is True only if the game is over (the board
        is full or one player got 4 in a row, where "in a row"
        means a straight line of four in any direction)
        :return:none.
        """
        # The board is full and there is no winner.
        my_game = ConnectFour()
        my_game.board[0] = ['X', 'O', 'X', 'O', 'X', 'O', 'X']
        my_game.board[1] = ['X', 'O', 'X', 'O', 'X', 'O', 'X']
        my_game.board[2] = ['X', 'O', 'X', 'O', 'X', 'O', 'X']
        my_game.board[3] = ['O', 'X', 'O', 'X', 'O', 'X', 'O']
        my_game.board[4] = ['O', 'X', 'O', 'X', 'O', 'X', 'O']
        my_game.board[5] = ['O', 'X', 'O', 'X', 'O', 'X', 'O']
        self.assertEqual(True, my_game.is_game_over())

        # Player 'X' wins, get 4 in a row
        # my_game.board[0] = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        # my_game.board[1] = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        # my_game.board[2] = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        # my_game.board[3] = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        # my_game.board[4] = ['O', 'O', 'O', ' ', ' ', ' ', ' ']
        # my_game.board[5] = ['X', 'X', 'X', 'X', ' ', ' ', ' ']
        my_game = ConnectFour()
        my_game.x_dict1 = {5: {0, 1, 2, 3}}
        my_game.o_dict1 = {4: {0, 1, 2}}
        self.assertEqual(True, my_game.is_game_over())

        # Player 'O' wins, get 4 in a column
        # my_game.board[0] = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        # my_game.board[1] = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        # my_game.board[2] = [' ', ' ', ' ', ' ', ' ', 'O', ' ']
        # my_game.board[3] = [' ', ' ', ' ', ' ', ' ', 'O', 'X']
        # my_game.board[4] = [' ', ' ', ' ', ' ', ' ', 'O', 'X']
        # my_game.board[5] = [' ', ' ', ' ', ' ', 'X', 'O', 'X']
        my_game = ConnectFour()
        my_game.x_dict2 = {6: {3, 4, 5}, 4: {5}}
        my_game.o_dict2 = {5: {2, 3, 4, 5}}
        self.assertEqual(True, my_game.is_game_over())

        # Player 'O' wins, get 4 in a diagonal
        # my_game.board[0] = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        # my_game.board[1] = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        # my_game.board[2] = ['O', ' ', ' ', ' ', ' ', ' ', ' ']
        # my_game.board[3] = ['X', 'O', ' ', ' ', ' ', ' ', ' ']
        # my_game.board[4] = ['X', 'X', 'O', ' ', ' ', ' ', ' ']
        # my_game.board[5] = ['X', 'X', 'X', 'O', 'O', 'O', ' ']
        my_game = ConnectFour()
        my_game.diff_o_dict = {2: {0, 1, 2, 3}, 1: {4}, 0: {5}}
        my_game.diff_x_dict = {3: {0, 1, 2}, 4: {0, 1}, 5: {0}}
        self.assertEqual(True, my_game.is_game_over())

        # Player 'X' wins, get 4 in a diagonal
        # my_game.board[0] = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        # my_game.board[1] = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        # my_game.board[2] = [' ', ' ', ' ', ' ', ' ', ' ', 'X']
        # my_game.board[3] = [' ', ' ', ' ', ' ', ' ', 'X', 'X']
        # my_game.board[4] = [' ', ' ', ' ', ' ', 'X', 'O', 'O']
        # my_game.board[5] = [' ', ' ', 'O', 'X', 'O', 'O', 'X']
        my_game = ConnectFour()
        my_game.sum_x_dict = {8: {3, 4, 5, 6}, 9: {6}, 11: {6}}
        my_game.sum_o_dict = {7: {2}, 9: {4, 5}, 10: {5, 6}}
        self.assertEqual(True, my_game.is_game_over())

    def test_is_game_over_false(self):
        """
        Check if the method return false when there is no
        situations that makes the game finish.
        :return: none
        """
        # The board is not full and no winner.
        my_game = ConnectFour()
        my_game.board[0] = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        my_game.board[1] = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        my_game.board[2] = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        my_game.board[3] = [' ', ' ', ' ', ' ', ' ', 'X', ' ']
        my_game.board[4] = [' ', ' ', ' ', ' ', 'X', 'O', 'O']
        my_game.board[5] = [' ', ' ', ' ', 'X', 'O', 'O', 'X']
        my_game.sum_x_dict = {8: {3, 4, 5}, 11: {6}}
        my_game.sum_o_dict = {9: {4, 5}, 10: {5, 6}}
        self.assertEqual(False, my_game.is_game_over())

    def test_get_winner(self):
        """
        Check if the method return X when X is a winner.
        Check if the method return O when O is a winner.
        Check if the method return none when there is no winner.
        :return:none
        """
        # Player 'O' wins, get 4 in a diagonal
        # my_game.board[0] = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        # my_game.board[1] = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        # my_game.board[2] = ['O', ' ', ' ', ' ', ' ', ' ', ' ']
        # my_game.board[3] = ['X', 'O', ' ', ' ', ' ', ' ', ' ']
        # my_game.board[4] = ['X', 'X', 'O', ' ', ' ', ' ', ' ']
        # my_game.board[5] = ['X', 'X', 'X', 'O', 'O', 'O', ' ']
        my_game = ConnectFour()
        my_game.diff_o_dict = {2: {0, 1, 2, 3}, 1: {4}, 0: {5}}
        my_game.diff_x_dict = {3: {0, 1, 2}, 4: {0, 1}, 5: {0}}
        self.assertEqual('O', my_game.get_winner())

        # Player 'X' wins, get 4 in a row
        # my_game.board[0] = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        # my_game.board[1] = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        # my_game.board[2] = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        # my_game.board[3] = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        # my_game.board[4] = ['O', 'O', 'O', ' ', ' ', ' ', ' ']
        # my_game.board[5] = ['X', 'X', 'X', 'X', ' ', ' ', ' ']
        my_game = ConnectFour()
        my_game.x_dict1 = {5: {0, 1, 2, 3}}
        my_game.o_dict1 = {4: {0, 1, 2}}
        self.assertEqual('X', my_game.get_winner())

        # The board is not full and no winner.
        # my_game.board[0] = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        # my_game.board[1] = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        # my_game.board[2] = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        # my_game.board[3] = [' ', ' ', ' ', ' ', ' ', 'X', ' ']
        # my_game.board[4] = [' ', ' ', ' ', ' ', 'X', 'O', 'O']
        # my_game.board[5] = [' ', ' ', ' ', 'X', 'O', 'O', 'X']
        my_game = ConnectFour()
        my_game.sum_x_dict = {8: {3, 4, 5}, 11: {6}}
        my_game.sum_o_dict = {9: {4, 5}, 10: {5, 6}}
        self.assertEqual(None, my_game.get_winner())

    def test_undo_value_error(self):
        """
        If there is nothing to undo you should raise a value error.
        If it doesn't raise an error, test fail.
        :return:none.
        """
        try:
            my_game = ConnectFour()
            my_game.position_stack = []
            my_game.undo()
            self.fail('Should raised an error due to there is nothing to undo')
        except ValueError:
            pass

    def test_undo_no_error(self):
        """
        Add four pieces into the initial board
        then undo one piece. Check if the
        corresponding attributes of the
        objects are equal to the expected.
        :return:
        """
        my_game = ConnectFour()
        my_game.add_piece(0)  # Add X in the first column of the 6th row.
        my_game.add_piece(0)  # Add O in the first column of the 5th row.
        my_game.add_piece(1)  # Add X in the second column of the 6th row.
        my_game.add_piece(1)  # Add O in the second column of the 5th row.
        # Undo the last O.
        my_game.undo()
        expected_queue = list(('O' + 'XO' * 19))
        expected_position_stack = [(5, 0), (4, 0), (5, 1)]
        expected_player_stack = ['X', 'O', 'X']
        expected_x_dict1 = {5: {0, 1}}
        expected_x_dict2 = {0: {5}, 1: {5}}
        expected_sum_x_dict = {5: {0}, 6: {1}}
        expected_diff_x_dict = {5: {0}, 4: {1}}
        expected_o_dict1 = {4: {0}}
        expected_o_dict2 = {0: {4}, 1: set()}
        expected_sum_o_dict = {4: {0}, 5: set()}
        expected_diff_o_dict = {4: {0}, 3: set()}
        expected_board = [[' '] * 7] * 4
        expected_board.append(['O', ' ', ' ', ' ', ' ', ' ', ' '])
        expected_board.append(['X', 'X', ' ', ' ', ' ', ' ', ' '])
        self.assertEqual(expected_queue, my_game.queue)
        self.assertEqual(expected_position_stack, my_game.position_stack)
        self.assertEqual(expected_player_stack, my_game.player_stack)
        self.assertEqual(expected_board, my_game.board)
        self.assertDictEqual(expected_o_dict1, my_game.o_dict1)
        self.assertDictEqual(expected_o_dict2, my_game.o_dict2)
        self.assertDictEqual(expected_sum_o_dict, my_game.sum_o_dict)
        self.assertDictEqual(expected_diff_o_dict, my_game.diff_o_dict)
        self.assertDictEqual(expected_x_dict1, my_game.x_dict1)
        self.assertDictEqual(expected_x_dict2, my_game.x_dict2)
        self.assertDictEqual(expected_sum_x_dict, my_game.sum_x_dict)
        self.assertDictEqual(expected_diff_x_dict, my_game.diff_x_dict)
