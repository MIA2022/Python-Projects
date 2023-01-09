"""
Nan Chen
HW7

Creating a ConnectFour class, which has the several
initial attributes and the method to play Connect Four
game.
"""


class ConnectFour:

    def __init__(self):
        """
         Initialize board with  a 2D list of length 6, and each
         item in that list is a list of length 7, with a space
         in each position. Initialize empty lists and dictionaries
         for the position and category information of the pieces added.
         Initialize a queue for player  so that the next player
         should automatically switch to the other player.
        """
        self.board = [[' '] * 7 for _ in range(6)]
        # Initialize the position and category
        # information of the pieces added
        self.position_stack = []
        self.player_stack = []
        # Initialize a queue for players so that the next player
        # should automatically switch to the other player.
        self.queue = []
        player_order = 'XO' * 21
        for player in player_order:
            self.queue.append(player)
        # The key is row number and the value
        # is a set which contain all column
        # numbers which have the same row number.
        self.x_dict1 = {}
        self.o_dict1 = {}
        # The key is column number and the value
        # is a set which contain all row
        # numbers which have the same column number.
        self.o_dict2 = {}
        self.x_dict2 = {}
        # The key is the sum of row and column and
        # the value is a set which contain all column numbers.
        self.sum_x_dict = {}
        self.sum_o_dict = {}
        # The key is the difference between row and column and
        # the value is a set which contain all column numbers.
        self.diff_x_dict = {}
        self.diff_o_dict = {}

    def __str__(self):
        """
        Creating a string according to the board attributes
        :return:a string that represents the board
        """
        board_string = ''
        for row in self.board:
            for column in row:
                board_string += '|' + column
            board_string += '|' + '\n'
            board_string += '---------------' + '\n'

        return board_string

    @ staticmethod
    def update_dict(key, value, dictionary):
        """
        Update the dictionary according to the key-value pairs.
        If the key is not in dictionary, add it and its value.
        If the key is already in dictionary, update its value set.
        :param key: int|any int.
        :param value: int|any int
        :param dictionary: dictionary|a dictionary whose key
            is an int and the corresponding value is a set.
        :return: dictionary| the updated dictionary
            which add the key-value pairs.
        """
        if key in dictionary:
            dictionary[key].add(value)
        else:
            dictionary[key] = {value}

        return dictionary

    def add_piece(self, column):
        """
        The piece will "fall" to the lowest empty space in
        the given column. The first piece to be placed should
        be an "X". When you play a piece, the next player should
        automatically switch to the other player. After each
        piece is added, the attributes of the object will be updated.
        If the column is invalid (outside of the playing area),
        the column is already full, or if the game already is over,
        it will raise a ValueError and message.
        :param column: int|any int from 0 to 6 which represents
            the column to place the piece.
        :return:none
        """
        if column < 0 or column > len(self.board[0]) - 1:
            raise ValueError('Column is outside of the playing area')
        if self.board[0][column] != ' ':
            raise ValueError('The column is already full')
        if self.is_game_over() is True:
            raise ValueError('The game already is over')

        # The piece will "fall" to the lowest
        # empty space in the given column.
        for row in range(5, -1, -1):
            if self.board[row][column] == ' ':
                # Updated the board with the
                # first position of the player queue.
                self.board[row][column] = self.queue.pop(0)
                # Add the position information of the piece
                # added to the position_stack.
                self.position_stack.append((row, column))
                # Add the category information of the piece
                # added to the player_stack.
                self.player_stack.append(self.board[row][column])

                # Update the dictionaries respectively
                # according to the category of the piece added.
                if self.board[row][column] == 'X':
                    self.x_dict1 = self.update_dict(row, column, self.x_dict1)
                    self.x_dict2 = self.update_dict(column, row, self.x_dict2)
                    self.sum_x_dict = self.update_dict(
                        row + column, column, self.sum_x_dict
                    )
                    self.diff_x_dict = self.update_dict(
                        (row - column), column, self.diff_x_dict
                    )
                else:
                    self.o_dict1 = self.update_dict(row, column, self.o_dict1)
                    self.o_dict2 = self.update_dict(column, row, self.o_dict2)
                    self.sum_o_dict = self.update_dict(
                        row + column, column, self.sum_o_dict
                    )
                    self.diff_o_dict = self.update_dict(
                        (row - column), column, self.diff_o_dict
                    )
                break

    @ staticmethod
    def in_value_set_or_not(value_set, dictionary):
        """
        Check if the value of the dictionary
        is in the given value_set.
        :param value_set: set| any set.
        :param dictionary: dictionary|a dictionary whose key
            is an int and the corresponding value is a set.
        :return: boolean value| return true if the value
            of the dictionary is in the given value_set.
            Otherwise, return false.
        """
        boolean_value = False
        for key in dictionary:
            if dictionary[key] in value_set:
                boolean_value = True
                break
        return boolean_value

    def win_or_not(self, dict1, dict2, dict3, dict4):
        """
        Check if there exists a dictionary whose value
        is in the given set, which represents one player
        got 4 in a row, where "in a row" means
        a row, column, or diagonal.
        :param dict1: dictionary|a dictionary whose key
            is an int and the corresponding value is a set.
        :param dict2: dictionary|a dictionary whose key
            is an int and the corresponding value is a set.
        :param dict3: dictionary|a dictionary whose key
            is an int and the corresponding value is a set.
        :param dict4: dictionary|a dictionary whose key
            is an int and the corresponding value is a set.
        :return: boolean value| return true if there exists a
            dictionary whose value if in the given set.
        """
        a = frozenset(range(4))  # a = {0, 1, 2, 3}
        b = frozenset(range(1, 5))  # b = {1, 2, 3, 4}
        c = frozenset(range(2, 6))  # c = {2, 3, 4, 5}
        d = frozenset(range(3, 7))  # d = {3, 4, 5, 6}
        column_set = {a, b, c, d}
        row_set = {a, b, c}
        # Connect four in a row
        boolean_value1 = self.in_value_set_or_not(column_set, dict1)
        # Connect four in a column
        boolean_value2 = self.in_value_set_or_not(row_set, dict2)
        # Connect four in a diagonal(different directions)
        boolean_value3 = self.in_value_set_or_not(column_set, dict3)
        boolean_value4 = self.in_value_set_or_not(column_set, dict4)
        # Return true when a straight line of four in any direction
        boolean_value = boolean_value1 or boolean_value2 or \
            boolean_value3 or boolean_value4

        return boolean_value

    def is_game_over(self):
        """
        Returns a boolean that is True only if the
        game is over (the board is full or one
        player got 4 in a row, where "in a row"
        means a straight line of four in any direction)
        :return: boolean value| return true if the
            game is over. Otherwise, return false.
        """
        boolean_value = False
        # Check if the board is full.
        for column in range(7):
            if self.board[0][column] == ' ':
                break
        else:
            boolean_value = True
        # Check if player 'X' wins.
        if self.win_or_not(
                self.x_dict1, self.x_dict2, self.sum_x_dict, self.diff_x_dict
        ):
            boolean_value = True
        # Check if player 'O' wins.
        if self.win_or_not(
                self.o_dict1, self.o_dict2, self.sum_o_dict, self.diff_o_dict
        ):
            boolean_value = True

        return boolean_value

    def get_winner(self):
        """
        return None if there is not yet a winner, or if
        the game ends in a tie, otherwise it returns
        the player who got 4 in a row.
        :return: None or string| return none if there is
            no winner. Otherwise, return 'X' or 'O'.
        """
        # Player X constructs a straight line of four in any direction.
        if self.win_or_not(
                self.x_dict1, self.x_dict2, self.sum_x_dict, self.diff_x_dict
        ):
            return 'X'
        # Player O constructs a straight line of four in any direction.
        elif self.win_or_not(
                self.o_dict1, self.o_dict2, self.sum_o_dict, self.diff_o_dict
        ):
            return 'O'
        else:
            return None

    def undo(self):
        """
        Removes the last piece that was played in the board.
        Repeatedly calling this method will continue to
        step one play backwards. The corresponding attributes
        of the object will be updated. If there is nothing
        to undo you should raise a value error and message.
        :return: none.
        """
        if not self.position_stack:
            raise ValueError('There is nothing to undo')

        # Get the position which is undone.
        (row, column) = self.position_stack.pop()
        # The undone piece is added to the first
        # position of the player queue.
        self.queue = [self.player_stack.pop()] + self.queue

        # Clear the position information of the undone piece
        # in the corresponding dictionaries according to the specific piece.
        if self.board[row][column] == 'X':
            self.x_dict1[row].remove(column)
            self.x_dict2[column].remove(row)
            self.sum_x_dict[row + column].remove(column)
            self.diff_x_dict[row - column].remove(column)
        elif self.board[row][column] == 'O':
            self.o_dict1[row].remove(column)
            self.o_dict2[column].remove(row)
            self.sum_o_dict[row + column].remove(column)
            self.diff_o_dict[row - column].remove(column)

        # Clear the undone piece in the board.
        self.board[row][column] = ' '
