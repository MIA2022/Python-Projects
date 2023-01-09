'''
Nan Chen
HW6---Test file.

This is a program which test several functions 
in the maze_solver.py file.
'''


from maze_solver import *
import random


def test_check_range(name, number, lower_bound, upper_bound, expected):
    """
    Function--test check_range() function using 
        random input data. Testing whether 
        the number is in the right range.
    Parameters:
        name: string| any string to represent a variable name
        number: int|any int, the value of the name
        lower_bound: int| the minimum int of the number
        upper_bound: int| the maximum int of the number
        expected: boolean value|Return False if the number 
        of the name is in the range. Otherwise, return True
    Returns: none
    """
    actual = check_range(name, number, lower_bound, upper_bound)
    if actual != expected:
        print('Test_check_range failed:', name, number, lower_bound, upper_bound)
        print('Actual:', actual)
        print('Expected:', expected)
        return


def run_test_check_range():
    """
    Function--run test_check_range() function 
        using random input data.
    Parameters:none.
    Returns: none.
    """
    # Number is in the range.
    test_number = random.randint(1, 100)
    test_lower_bound = test_number - 1
    test_upper_bound = test_number + 1
    test_check_range(str(test_number), test_number, test_lower_bound, test_upper_bound, False)
    # Number is lower than the lower_bound.
    test_lower_bound = random.randint(1, 100)
    test_number = test_lower_bound - 1
    test_upper_bound = test_lower_bound + 1
    test_check_range(str(test_number), test_number, test_lower_bound, test_upper_bound, True)
    # Number is bigger than upper_bound.
    test_upper_bound = random.randint(1, 100)
    test_lower_bound = test_upper_bound - 1
    test_number = test_upper_bound + 1
    test_check_range(str(test_number), test_number, test_lower_bound, test_upper_bound, True)


def test_check_character(maze_row, characters_list, message, i, expected):
    """
    Function--test check_character() function using 
        random input data. Testing if characters 
        in the maze_row are all in characters_list.
    Parameters:
        maze_row: string| a string contains any character
        characters_list: list of string| 
            the list of the required elements
        message: string|any string contains the prompt message
        i: int| an integer number which represents the 
            row number of the maze, which starts from 0.
        expected: boolean value| return False if characters in the 
        maze_row are all in characters_list, otherwise, return True.
    Returns: none
    """
    actual = check_character(maze_row, characters_list, message, i)
    if actual != expected:
        print('Test_check_range failed:', maze_row, characters_list)
        print('Actual:', actual)
        print('Expected:', expected)
        return


def run_test_check_character():
    """
    Function--run test_check_character() function 
        using random input data.
    Parameters:none.
    Returns: none.
    """

    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    test_characters_list = []
    for i in range(random.randint(10, 20)):
        test_characters_list += characters[random.randint(0, 25)]
    length = int(len(test_characters_list) / 2)

    # All the characters in test_maze_row 
    # are in test_characters_list.
    test_maze_row = ''.join(test_characters_list[: length])
    message = test_maze_row + '{}'
    i = random.randint(0, 9)
    test_check_character(test_maze_row, test_characters_list, message, i, False)
    
    # No character in test_maze_row is in test_characters_list.
    test_maze_row = str(random.randint(0, 9)) * 5
    test_check_character(test_maze_row, test_characters_list, message, i, True)

    # Part of characters in test_maze_row are in test_characters_list.
    test_maze_row = ''.join(test_characters_list[: length]) + str(random.randint(0, 9)) * 5
    test_check_character(test_maze_row, test_characters_list, message, i, True)


def test_check_maze_row(maze_row, row_number, width, height, expected):
    """
    Function--test check_maze_row() function using 
        random input data. Testing if the length of the maze_row 
        is equal to the width. If not, return True. If they are 
        equal, then check if maze_row meet the special guidelines 
        according its row_number position.
    Parameters:
        maze_row: string|a string which is input by user.
        row_number: int| an integer number which represents the 
            row number of the maze, which starts from 0.
        width: int| an integer number which represents 
            the number of characters in one row of maze
        height: int| an integer number which represents 
            the total number of the rows of the maze.
        expected: boolean value|return False if the maze_row 
        meets the guidelines. Otherwise, return False
    Returns: none
    """

    actual = check_maze_row(maze_row, row_number, width, height)
    if actual != expected:
        print('Test_check_maze_row failed:', maze_row, row_number, width, height)
        print('Actual:', actual)
        print('Expected:', expected)
        return


def run_test_check_maze_row():
    """
    Function--run test_check_maze_row() function 
        using random input data.
    Parameters:none.
    Returns: none.
    """
    inner_space_character = [' ', 'X']
    outer_edge_character = ['X', 'E']
    width = random.randint(3, 100)
    height = random.randint(3, 100)
    # The length of the maze_row is not equal to width.
    # The row_number is 0 or height - 1.
    # The characters in the maze_row are all in the outer_edge_character list.
    # Return True directly.
    row_number = random.choice((0, height - 1))
    maze_row = ''
    for i in range(width - 1):
        maze_row += outer_edge_character[random.randint(0, 1)]
    test_check_maze_row(maze_row, row_number, width, height, True)

    # The length of the maze_row is not equal to width.
    # The row_number is between 0 and height - 1.
    # The first and the last characters in the maze_row are all in the outer_edge_character list.
    # The characters in the middle of the maze_row are all in the inner_space_character list.
    # Return True directly.
    maze_row = outer_edge_character[random.randint(0, 1)]
    for i in range(width - 3):
        maze_row += inner_space_character[random.randint(0, 1)]
    maze_row += outer_edge_character[random.randint(0, 1)]
    test_check_maze_row(maze_row, row_number, width, height, True)

    # The length of the maze_row is equal to width.
    # The row_number is 0 or height - 1.
    # The characters in the maze_row are all in the outer_edge_character list.
    row_number = random.choice((0, height - 1))
    maze_row = ''
    for i in range(width):
        maze_row += outer_edge_character[random.randint(0, 1)]
    test_check_maze_row(maze_row, row_number, width, height, False)

    # The length of the maze_row is equal to width.
    # The row_number is 0 or height - 1.
    # Part of characters in the maze_row are in the outer_edge_character list.
    number = int(width / 2)
    maze_row = maze_row[:number] + str(random.randint(0, 9)) * (width - number)
    test_check_maze_row(maze_row, row_number, width, height, True)

    # The length of the maze_row is equal to width.
    # The row_number is 0 or height - 1.
    # No character in the maze_row are not in the outer_edge_character list.
    maze_row = str(random.randint(0, 9)) * width
    test_check_maze_row(maze_row, row_number, width, height, True)

    # The length of the maze_row is equal to width.
    # The row_number is between 0 and height - 1.
    # The first and the last characters in the maze_row are all in the outer_edge_character list.
    # The characters in the middle of the maze_row are all in the inner_space_character list.
    row_number = random.randrange(1, height - 2)
    maze_row = outer_edge_character[random.randint(0, 1)]
    for i in range(width - 2):
        maze_row += inner_space_character[random.randint(0, 1)]
    maze_row += outer_edge_character[random.randint(0, 1)]
    test_check_maze_row(maze_row, row_number, width, height, False)

    # The length of the maze_row is equal to width.
    # The row_number is between 0 and height - 1.
    # The first and the last characters in the maze_row are not in the outer_edge_character list.
    # The characters in the middle of the maze_row are all in the inner_space_character list.
    maze_row = str(random.randint(0, 9))
    for i in range(width - 2):
        maze_row += inner_space_character[random.randint(0, 1)]
    maze_row += str(random.randint(0, 9))
    test_check_maze_row(maze_row, row_number, width, height, True)

    # The length of the maze_row is equal to width.
    # The row_number is between 0 and height - 1.
    # The first and the last characters in the maze_row are in the outer_edge_character list.
    # The characters in the middle of the maze_row are not in the inner_space_character list.
    maze_row = outer_edge_character[random.randint(0, 1)]
    maze_row += str(random.randint(0, 9)) * (width - 2)
    maze_row += outer_edge_character[random.randint(0, 1)]
    test_check_maze_row(maze_row, row_number, width, height, True)

    # The length of the maze_row is equal to width.
    # The row_number is between 0 and height - 1.
    # The first and the last characters in the maze_row are not in the outer_edge_character list.
    # The characters in the middle of the maze_row are not in the inner_space_character list.
    maze_row = str(random.randint(0, 9)) * width
    test_check_maze_row(maze_row, row_number, width, height, True)


def test_check_maze_exit_number(maze_string, expected):
    """
    Function--test check_character() function using 
        random input data. Testing if maze_string 
        contains 1 or more capital letter E.
    Parameters:
        maze_string: string|a string which is constructed 
            by all varified maze_rows.
        expected: boolean value|return False if maze_string contains 
            1 or more capital letter E. Otherwise, return True.
    Returns: none
    """

    actual = check_maze_exit_number(maze_string)
    if actual != expected:
        print('Test_check_maze_row failed:', maze_string)
        print('Actual:', actual)
        print('Expected:', expected)
        return


def run_test_check_maze_exit_number():
    """
    Function--run test_check_maze_exit_number() function 
        using random input data.
    Parameters:none.
    Returns: none.
    """
    # Maze_string contains no capital letter E.
    maze_string = str(random.randint(0, 9)) * random.randint(10, 100)
    test_check_maze_exit_number(maze_string, True)
    # Maze_string contains 1 or more capital letter E.
    maze_string = 'E' * random.randint(1, 9) + maze_string
    test_check_maze_exit_number(maze_string, False)


def test_check_file_data(file_data, expected):
    """
    Function--test check_file_data() function using 
        random input data. Testing if a list of data 
        which is read from file meet the guidelines of maze.
        If the file_data meets the guidlines,then ecpect a 
        tuple which contains maze_dict, width, height.
        If the file_data doesn't meet the guidlines,
        then expect to raise Vallueerror, which will be cathed and 
        return a string which contains the error message.
    Parameters:
        file_data: list|a list of data which is read from file. 
            Each line is one element of the list.
        expected: if the file_data meets the guidlines,then ecpect a 
            tuple which contains maze_dict, width, height.
            maze_dict:dictionary|key is the row_number from 0 
                to height -1,the corresponding value is a list of the 
                varified maze_row string which is input by user.
            width: int|an integer number which represents 
                the required number of the length of the maze_row.
            height:int|an integer number which represents the 
                required number of the total number of maze_row.
            If the file_data doesn't meet the guidlines,
            then expect to raise Vallueerror, which will be cathed and 
            return a string which contains the error message.
    Returns: none
    """
    # if the file_data meets the guidlines,then ecpect a 
    # tuple which contains maze_dict, width, height.
    try:
        actual = check_file_data(file_data)
    # If the file_data doesn't meet the guidlines,
    # then expect to raise Vallueerror, which will be cathed and 
    # return a string which contains the error message.
    except ValueError:
        actual = 'Please re-input maze_file'
    
    if actual != expected:
        print('Test_check_maze_row failed:', file_data)
        print('Actual:', actual)
        print('Expected:', expected)
        return


def run_test_check_file_data():
    """
    Function--run test_check_file_data() function 
        using random input data.
    Parameters:none.
    Returns: none.
    """
    # The maze meets all requirements.
    expected_dict = {}
    inner_space_character = [' ', 'X']
    outer_edge_character = ['E', 'E']
    width = random.randint(3, 20)
    height = random.randint(3, 20)
    # The first row of maze.
    maze_row1 = outer_edge_character[random.randint(0, 1)] * width
    expected_dict[0] = list(maze_row1)
    # The row in the middle of the maze
    maze_row2 = outer_edge_character[random.randint(0, 1)]
    for i in range(width - 2):
        maze_row2 += inner_space_character[random.randint(0, 1)]
    maze_row2 += outer_edge_character[random.randint(0, 1)]
    # The first line which contains the number of 
    # the width and height of maze in the file.
    digit_line = str(width) + ' ' + str(height) 
    file_data = []
    file_data = [digit_line] + [maze_row1]
    for i in range(1, height - 1):
        file_data.append(maze_row2)
        expected_dict[i] = list(maze_row2)
    file_data.append(maze_row1)
    expected_dict[height - 1] = list(maze_row1)
    expected = expected_dict, width, height
    
    test_check_file_data(file_data, expected)

    expected = 'Please re-input maze_file'
    # The first line of the file contains string and float number.
    file_data = ['abc', '34.5']
    # The first line of the file contains number which is out of range.
    file_data = ['1', '45']
    test_check_file_data(file_data, expected)


    # The maze meets other requirements but contains no exit.
    inner_space_character = [' ', 'X']
    outer_edge_character = ['X', 'X']
    width = random.randint(3, 20)
    height = random.randint(3, 20)
    # The first row of maze.
    maze_row1 = outer_edge_character[random.randint(0, 1)] * width
    # The row in the middle of the maze
    maze_row2 = outer_edge_character[random.randint(0, 1)]
    for i in range(width - 2):
        maze_row2 += inner_space_character[random.randint(0, 1)]
    maze_row2 += outer_edge_character[random.randint(0, 1)]
    # The first line which contains the number of 
    # the width and height of maze in the file.
    digit_line = str(width) + ' ' + str(height) 
    file_data = []
    file_data = [digit_line] + [maze_row1]
    for i in range(1, height - 1):
        file_data.append(maze_row2)
    file_data.append(maze_row1)

    expected = 'Please re-input maze_file'

    test_check_file_data(file_data, expected)

    # The maze meets other requirements but the character 
    # in first and last row of the maze is not correct.
    inner_space_character = [' ', 'X']
    outer_edge_character = ['X', 'X']
    width = random.randint(3, 20)
    height = random.randint(3, 20)
    # The first row of maze.
    maze_row1 = str(random.randint(0, 9)) * width
    # The row in the middle of the maze
    maze_row2 = outer_edge_character[random.randint(0, 1)]
    for i in range(width - 2):
        maze_row2 += inner_space_character[random.randint(0, 1)]
    maze_row2 += outer_edge_character[random.randint(0, 1)]
    # The first line which contains the number of 
    # the width and height of maze in the file.
    digit_line = str(width) + ' ' + str(height) 
    file_data = []
    file_data = [digit_line] + [maze_row1]
    for i in range(1, height - 1):
        file_data.append(maze_row2)
    file_data.append(maze_row1)

    expected = 'Please re-input maze_file'
    
    test_check_file_data(file_data, expected)

    # The maze meets other requirements but the character 
    # in the middle row of the maze is not correct.
    inner_space_character = [' ', 'X']
    outer_edge_character = ['X', 'X']
    width = random.randint(3, 20)
    height = random.randint(3, 20)
    # The first row of maze.
    maze_row1 = outer_edge_character[random.randint(0, 1)] * width
    # The row in the middle of the maze
    maze_row2 = str(random.randint(0, 9))
    for i in range(width - 2):
        maze_row2 += inner_space_character[random.randint(0, 1)]
    maze_row2 += outer_edge_character[random.randint(0, 1)]
    # The first line which contains the number of 
    # the width and height of maze in the file.
    digit_line = str(width) + ' ' + str(height) 
    file_data = []
    file_data = [digit_line] + [maze_row1]
    for i in range(1, height - 1):
        file_data.append(maze_row2)
    file_data.append(maze_row1)

    expected = 'Please re-input maze_file'

    test_check_file_data(file_data, expected)


def test_initialize_distance_direction(maze_dict, expected):
    """
    Function--test initialize_distance_direction() function 
        using random input data. Testing whether initialize 
        distance value and direction value for all the 
        spaces(blank space and exits) in the maze.
    Parameters:
        maze_dict:dictionary|key is the row_number from 0 
            to height -1,the corresponding value is a list of the 
            varified maze_row string.
        expected: tuple| a tuple contains distance_dict and direction_dict.
        distance_dict:dictionary|key is the tuple of (row, column) 
            which represents the blank space or the exit position 
            in the maze, the corresponding value is float("inf").
        direction_dict:dictionary|key is the tuple of (row, column) 
            which represents the blank space or the exit 
            position in the maze, the corresponding value is None.
    Returns: none
    """
    actual = initialize_distance_direction(maze_dict)
    if actual != expected:
        print('Test_check_maze_row failed:', maze_dict)
        print('Actual:', actual)
        print('Expected:', expected)
        return


def run_test_initialize_distance_direction():
    """
    Function--run test_initialize_distance_direction() function 
        using random input data.
    Parameters:none.
    Returns: none.
    """
    # The maze_dict meets all requirements and all the 
    # spaces(blank space and exits) in the maze are initialized.
    maze_dict = {}
    expected_distance_dict = {}
    expected_direction_dict = {}
    inner_space_character = [' ', 'X']
    outer_edge_character = ['X', 'E']
    width = random.randint(3, 20)
    height = random.randint(3, 20)
    # The first and the last row of maze.
    maze_row1 = outer_edge_character[random.randint(0, 1)] * width
    for i in range(width):
        if maze_row1[i] == 'E':
            expected_distance_dict[(0, i)] = float('inf')
            expected_direction_dict[(0, i)] = None
            expected_distance_dict[(height - 1, i)] = float('inf')
            expected_direction_dict[(height - 1, i)] = None
    maze_dict[0] = list(maze_row1)
    
    # The row in the middle of the maze
    maze_row2 = outer_edge_character[random.randint(0, 1)]
    for i in range(width - 2):
        maze_row2 += inner_space_character[random.randint(0, 1)]
    maze_row2 += outer_edge_character[random.randint(0, 1)]
   
    for i in range(1, height - 1):
        maze_dict[i] = list(maze_row2)
        for j in range(width):
           if maze_row2[j] == 'E' or maze_row2[j] == ' ':
            expected_distance_dict[(i, j)] = float('inf')
            expected_direction_dict[(i, j)] = None 
    maze_dict[height - 1] = list(maze_row1)

    expected = expected_distance_dict, expected_direction_dict

    test_initialize_distance_direction(maze_dict, expected)
    

def test_get_path_maze(maze_dict, final_path, expected):
    """
    Function--test initialize_distance_direction() function 
        using random input data. Testing if the position which 
        is stored in the fina_path list, change its 
        corresponding value of the maze_dict to
        "*" (asterisk) to denotes part of a path out.
    Parameters:
        maze_dict:dictionary|key is the row_number from 0 
            to height -1,the corresponding value is a list of the 
            varified maze_row string.
        final_path:list|a list of elements, each element in it
            is (row, column) pair.
        expected: maze_dict:dictionary|key is the row_number from 0 
            to height -1,the corresponding value is a list of the 
            varified maze_row string which is input by user. And modify 
            the value of the (row, column) pair which represents the position
            in the maze from blank space to "*" (asterisk).
    Returns: none
    """
    actual = get_path_maze(maze_dict, final_path)
    if actual != expected:
        print('Test_check_maze_row failed:', maze_dict, final_path)
        print('Actual:', actual)
        print('Expected:', expected)
        return


def run_test_get_path_maze():
    """
    Function--run test_get_path_maze() function 
        using random input data.
    Parameters:none.
    Returns: none.
    """
    # The exit is reachable.
    # The maze meets all requirements.
    maze_dict = {}
    expected = {}
    inner_space_character = [' ', 'X']
    outer_edge_character = ['E', 'E']
    width = random.randint(3, 20)
    height = random.randint(3, 20)
    # The first row of maze.
    maze_row1 = outer_edge_character[random.randint(0, 1)] * width
    maze_dict[0] = list(maze_row1)

    # The row in the middle of the maze
    maze_row2 = outer_edge_character[random.randint(0, 1)]
    for i in range(width - 2):
        maze_row2 += inner_space_character[random.randint(0, 1)]
    maze_row2 += outer_edge_character[random.randint(0, 1)]
    
    for i in range(1, height - 1):
        maze_dict[i] = list(maze_row2)
        expected[i] = list(maze_row2)

    maze_dict[height - 1] = list(maze_row1)
    expected[height - 1] = list(maze_row1)

    final_path = [(0, width - 2), (0, width - 1)]
    maze_row1 = maze_row1[:-1] + '*'
    expected[0] = list(maze_row1)

    test_get_path_maze(maze_dict, final_path, expected)

    # The exit is unreachable.
    # The fianl path is an empty list.
    maze_dict = {}
    width = random.randint(3, 20)
    height = random.randint(3, 20)
    # The first row of maze is wall
    maze_row1 = 'X' * width
    maze_dict[0] = list(maze_row1)
    # The second row of maze has blank space and an Exit.
    maze_row2 = 'X' + ' ' * (width - 3) + 'X' + 'E'
    maze_dict[1] = list(maze_row2)
    # The remaining rows of maze are wall.
    for i in range(2, height - 1):
        maze_dict[i] = list(maze_row1)
    
    expected = maze_dict
    final_path = []

    test_get_path_maze(maze_dict, final_path, expected)


def test_print_maze(maze_dict, expected):
    """
    Function--test print_maze() function using random 
        input data. Testing whether the corresponding 
        value of the maze_dict is converted from a list to a string
    Parameters:
        maze_dict:dictionary|key is the row_number from 0 
            to height -1,the corresponding value is a list of the 
            varified maze_row string which is input by user 
            or is modified by the cloest path.
        expected: string|a string which represents all characters 
            in the maze.each row is seperated by a new line character
    Returns: none
    """
    actual = print_maze(maze_dict)
    if actual != expected:
        print('Test_check_maze_row failed:', maze_dict)
        print('Actual:', actual)
        print('Expected:', expected)
        return


def run_test_print_maze():
    """
    Function--run test_print_maze() function 
        using random input data.
    Parameters:none.
    Returns: none.
    """
    # The maze meets all requirements.
    maze_dict = {}
    expected = ''
    inner_space_character = [' ', 'X']
    outer_edge_character = ['E', 'E']
    width = random.randint(3, 20)
    height = random.randint(3, 20)
    # The first row of maze.
    maze_row1 = outer_edge_character[random.randint(0, 1)] * width
    maze_dict[0] = list(maze_row1)
    expected += maze_row1 + '\n'

    # The row in the middle of the maze
    maze_row2 = outer_edge_character[random.randint(0, 1)]
    for i in range(width - 2):
        maze_row2 += inner_space_character[random.randint(0, 1)]
    maze_row2 += outer_edge_character[random.randint(0, 1)]
    
    for i in range(1, height - 1):
        maze_dict[i] = list(maze_row2)
        expected += maze_row2 + '\n'

    maze_dict[height - 1] = list(maze_row1)
    expected += maze_row1

    test_print_maze(maze_dict, expected)


def test_clear_path(maze_dict, expected):
    """
    Function--test clear_path() function using random 
        input data. Testing whether clearing up the 
        start position and path of the last game
        in the original maze.
    Parameters:
        maze_dict:dictionary|key is the row_number from 0 
            to height -1,the corresponding value is a list of the 
            varified maze_row string which is input by user 
            or is modified by the cloest path.
        expected: maze_dict:dictionary|key is the row_number from 0 
            to height -1,the corresponding value is a list of the 
            varified maze_row string which is input by user.
    Returns: none
    """
    actual = clear_path(maze_dict)
    if actual != expected:
        print('Test_check_maze_row failed:', maze_dict)
        print('Actual:', actual)
        print('Expected:', expected)
        return


def run_test_clear_path():
    """
    Function--run test_clear_path() function 
        using random input data.
    Parameters:none.
    Returns: none.
    """
    # Maze_dict is modified by finding the cloest exits
    # the expected is the original maze_dict.
    expected = {}
    maze_dict = {}
    inner_space_character = ' '
    outer_edge_character = ['X', 'E']
    width = random.randint(3, 20)
    height = random.randint(3, 20)
    # The first row of maze.
    maze_row1 = outer_edge_character[random.randint(0, 1)] * width
    expected[0] = list(maze_row1)

    expected_maze_row2 = ''
    # The row in the middle of the maze
    maze_row2 = outer_edge_character[random.randint(0, 1)]
    
    for i in range(width - 3):
        maze_row2 += inner_space_character
    expected_maze_row2 = maze_row2 + ' '
    maze_row2 += '*'
    
    last_character = outer_edge_character[random.randint(0, 1)]
    maze_row2 += last_character
    expected_maze_row2 += last_character
    
    for i in range(1, height - 1):
        expected[i] = list(expected_maze_row2)
        maze_dict[i] = list(maze_row2)

    expected[height - 1] = list(maze_row1)
    maze_dict[height - 1] = list(maze_row1)

    maze_row1 = maze_row1
    maze_dict[0] = list(maze_row1)

    test_clear_path(maze_dict, expected)


def test_find_exits(maze_dict, start_row, start_column, expected):
    """
    Function--test find_exits() function using random 
        input data. 
    Parameters:
        maze_dict:dictionary|key is the row_number from 0 
            to height -1,the corresponding value is a list of the 
            varified maze_row string which is input by user.
        start_row: int|an integer number which represents 
            the row number in the maze, which is in the 
            range from 0 to height - 1.
        start_column: int|an integer number which represents 
            the column number in the maze, which is in the 
            range from 0 to width - 1.
        expected: 
            distance_dict:dictionary|key is the tuple of (row, column) 
                which represents the blank space or the exit position 
                in the maze, the corresponding value is the distance
                from each position to the start position.
            direction_dict:dictionary|key is the tuple of (row, column) 
                which represents the blank space or the exit 
                position in the maze, the corresponding value 
                is the direction from which the player moved 
                to get to the space s from the starting 
                location of the playe, which is one of 'North',
                'East', 'South', 'West'.
    Returns: none
    """
    actual = find_exits(maze_dict, start_row, start_column)
    if actual != expected:
        print('Test_check_maze_row failed:', maze_dict, start_row, start_column)
        print('Actual:', actual)
        print('Expected:', expected)
        return


def run_test_find_exits():
    """
    Function--run test_find_exits() function 
        using random input data.
    Parameters:none.
    Returns: none.
    """
    # The exit is reachable.
    # The maze meets all requirements.
    maze_dict = {}
    width = random.randint(3, 20)
    height = random.randint(3, 20)
    # The first row of maze is wall
    maze_row1 = 'X' * width
    maze_dict[0] = list(maze_row1)
    # The second row of maze has blank space and an Exit.
    maze_row2 = 'X' + ' ' * (width - 2) + 'E'
    maze_dict[1] = list(maze_row2)
    # The remaining rows of maze are wall.
    for i in range(2, height - 1):
        maze_dict[i] = list(maze_row1)
    
    start_row = 1
    start_column = width - 3

    distance_dict, direction_dict = initialize_distance_direction(maze_dict)
    # Change the value of the distance_dict.
    # {(1, width - 3): 0, (1, width -2): 1, (1, width - 1): 2}
    for i in range(width - 3, width):
        distance_dict[1, i] = i - (width - 3)
    for i in range(width - 4, 0, -1):
        distance_dict[1, i] = width - 3 - i
    # Change the value of the direction_dict.
    for i in range(width - 2, width):
        direction_dict[1, i] = 'East'
    for i in range(1, width - 3):
        direction_dict[1, i] = 'West'
    
    expected = distance_dict, direction_dict
    
    test_find_exits(maze_dict, start_row, start_column, expected)

    # The exit is unreachable.
    # The maze meets all requirements.
    maze_dict = {}
    width = random.randint(3, 20)
    height = random.randint(3, 20)
    # The first row of maze is wall
    maze_row1 = 'X' * width
    maze_dict[0] = list(maze_row1)
    # The second row of maze has blank space and an Exit.
    maze_row2 = 'X' + ' ' * (width - 3) + 'X' + 'E'
    maze_dict[1] = list(maze_row2)
    # The remaining rows of maze are wall.
    for i in range(2, height - 1):
        maze_dict[i] = list(maze_row1)
    
    start_row = 1
    start_column = width - 3

    distance_dict, direction_dict = initialize_distance_direction(maze_dict)
    # Change the value of the distance_dict.
    for i in range(width - 3, 0, -1):
        distance_dict[(1, i)] = width - 3 - i
    # Change the value of the direction_dict.
    for i in range(1, width - 3):
        direction_dict[(1, i)] = 'West'
    
    expected = distance_dict, direction_dict
    
    test_find_exits(maze_dict, start_row, start_column, expected)


def test_find_closet_exit(distance_dict, maze_dict, expected):
    """
    Function--test find_closet_exit() function using random 
        input data. Testing whether if the exit is the closest 
        by determining which exit has the smallest 
        value stored in distance(s).
    Parameters:
        distance_dict:dictionary|key is the tuple of (row, column) 
            which represents the blank space or the exit position 
            in the maze, the corresponding value is the distance
            from each position to the start position.
        maze_dict:dictionary|key is the row_number from 0 
            to height -1,the corresponding value is a list of the 
            varified maze_row string which is input by user.
        expected: 
            exit_row: int|an integer which represents the 
                row position in the maze in which the 
                values in distance(s) is the smallest.
            exit_column: int|an integer which represents 
                the column position in the maze in which 
                the values in distance(s) is the smallest.
    Returns: none
    """
    actual = find_closet_exit(distance_dict, maze_dict)
    if actual != expected:
        print('Test_check_maze_row failed:', distance_dict, maze_dict)
        print('Actual:', actual)
        print('Expected:', expected)
        return


def run_test_find_closet_exit():
    """
    Function--run test_find_closet_exit() function 
        using random input data.
    Parameters:none.
    Returns: none.
    """
    # The second row of maze has two Exits.
    # The right exit in the second row is the cloest.
    # The maze meets all requirements.
    maze_dict = {}
    width = random.randint(5, 20)
    height = random.randint(3, 20)
    # The first row of maze is wall
    maze_row1 = 'X' * width
    maze_dict[0] = list(maze_row1)
    # The second row of maze has two Exits.
    maze_row2 = 'E' + ' ' * (width - 2) + 'E'
    maze_dict[1] = list(maze_row2)
    # The remaining rows of maze are wall.
    for i in range(2, height - 1):
        maze_dict[i] = list(maze_row1)

    distance_dict, direction_dict = initialize_distance_direction(maze_dict)
    # The right exit in the second row is the cloest.
    for i in range(width - 2, width):
        distance_dict[(1, i)] = i - (width - 2)
    for i in range(width - 3, 0, -1):
        distance_dict[(1, i)] = width - 2 - i

    exit_row = 1
    exit_column = width - 1

    expected = exit_row, exit_column

    test_find_closet_exit(distance_dict, maze_dict, expected)
  
    # The second row of maze has two Exits.
    # The left exit in the second row is the cloest.
    # The maze meets all requirements.
    maze_dict = {}
    width = random.randint(5, 20)
    height = random.randint(3, 20)
    # The first row of maze is wall
    maze_row1 = 'X' * width
    maze_dict[0] = list(maze_row1)
    # The second row of maze has two Exits.
    maze_row2 = 'E' + ' ' * (width - 2) + 'E'
    maze_dict[1] = list(maze_row2)
    # The remaining rows of maze are wall.
    for i in range(2, height - 1):
        maze_dict[i] = list(maze_row1)

    distance_dict, direction_dict = initialize_distance_direction(maze_dict)
    # The left exit in the second row is the cloest.
    for i in range(1, width):
        distance_dict[(1, i)] = i - 1
    
    distance_dict[(1, 0)] = 1

    exit_row = 1
    exit_column = 0

    expected = exit_row, exit_column

    test_find_closet_exit(distance_dict, maze_dict, expected)


def test_get_path_to_exit(exit_row, exit_column, direction_dict, expected):
    """
    Function--test get_path_to_exit() function using random 
        input data. 
    Parameters:
        exit_row: int|an integer which represents the 
            row position in the maze in which the 
            values in distance(s) is the smallest.
        exit_column: int|an integer which represents 
            the column position in the maze in which 
            the values in distance(s) is the smallest.
        direction_dict:dictionary|key is the tuple of (row, column) 
            which represents the blank space or the exit 
            position in the maze, the corresponding value 
            is the direction from which the player moved 
            to get to the space s from the starting 
            location of the playe, which is one of 'North',
            'East', 'South', 'West'.
        expected: 
            final_path:list|a list of elements, each element in it
                is (row, column) pair. The list contains the 
                exit positon in the maze and the position 
                in the path from exit to start position.
    Returns: none
    """
    actual = get_path_to_exit(exit_row, exit_column, direction_dict)
    if actual != expected:
        print('Test_check_maze_row failed:', exit_row, exit_column, direction_dict)
        print('Actual:', actual)
        print('Expected:', expected)
        return


def run_test_get_path_to_exit():
    """
    Function--run test_get_path_to_exit() function 
        using random input data.
    Parameters:none.
    Returns: none.
    """
    # The exit is unreachable.
    # The final path is an empty list.
    # The maze meets all requirements.
    maze_dict = {}
    width = random.randint(5, 20)
    height = random.randint(3, 20)
    # The first row of maze is wall
    maze_row1 = 'X' * width
    maze_dict[0] = list(maze_row1)
    # The second row of maze has blank space and an Exit.
    maze_row2 = 'X' + ' ' * (width - 3) + 'X' + 'E'
    maze_dict[1] = list(maze_row2)
    # The remaining rows of maze are wall.
    for i in range(2, height - 1):
        maze_dict[i] = list(maze_row1)

    distance_dict, direction_dict = initialize_distance_direction(maze_dict)
    # Change the value of the direction_dict.
    for i in range(1, width - 3):
        direction_dict[(1, i)] = 'West'

    expected = []
    exit_row = 1
    exit_column = width - 1

    test_get_path_to_exit(exit_row, exit_column, direction_dict, expected)

    # The exit is reachable.
    # The maze meets all requirements.
    maze_dict = {}
    width = random.randint(5, 20)
    height = random.randint(3, 20)
    # The first row of maze is wall
    maze_row1 = 'X' * width
    maze_dict[0] = list(maze_row1)
    # The second row of maze has blank space and an Exit.
    maze_row2 = 'X' + ' ' * (width - 2) + 'E'
    maze_dict[1] = list(maze_row2)
    # The remaining rows of maze are wall.
    for i in range(2, height - 1):
        maze_dict[i] = list(maze_row1)
    

    distance_dict, direction_dict = initialize_distance_direction(maze_dict)
    
    # Change the value of the direction_dict.
    for i in range(width - 2, width):
        direction_dict[1, i] = 'East'
    for i in range(1, width - 3):
        direction_dict[1, i] = 'West'
    
    expected = [(1, width - 1), (1, width - 2)]
    exit_row = 1
    exit_column = width - 1

    test_get_path_to_exit(exit_row, exit_column, direction_dict, expected)


def main():
    for test_number in range(1000):
        run_test_check_range()
        run_test_check_character()
        run_test_check_maze_row()
        run_test_check_maze_exit_number()
        run_test_check_file_data()
        run_test_initialize_distance_direction()
        run_test_get_path_maze()
        run_test_print_maze()
        run_test_clear_path()
        run_test_find_exits()
        run_test_find_closet_exit()
        run_test_get_path_to_exit()

    print('Done.')


if __name__ == '__main__':
    main()
