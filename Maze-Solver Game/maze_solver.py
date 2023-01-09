'''
Nan Chen
HW6

This ia a maze game. The program will ask user for which option 
they want to do. There are five opition for user to choose. 
Then the program will do that option. After finished it, the user will be 
asked to choose an option again.It can handle them selecting 
the option in any order, giving appropriate response. For example,
when user chooses 3 or 4 at first, it will prompt 'Please input 
the maze firstly.' message. So, the user must choose 1 or 2 to 
input maze at first if they want to continue playing game. 
The maze, the staring position or the path can be updated whenever. 
Each input maze and staring position will be varified to meet the guidlines.
Print maze would print the current maze to the screen. 
It will print the way to the exit if it has been calculated. 
The game will not quit until the user choose 5.
'''


def check_range(name, number, lower_bound, upper_bound):
    '''
    Function--Check if the number is in the range from 
        lower_bound to upper_bound. Return False if the number 
        of the name is in the range. Otherwise, return True.
    Parameter:
        name: string| any string to represent a variable name
        number: int|any int, the value of the name
        lower_bound: int| the minimum int of the number
        upper_bound: int| the maximum int of the number
    Return:
        boolean value|Return False if the number 
        of the name is in the range. Otherwise, return True.
    '''

    boolean_value = number not in range(lower_bound, upper_bound + 1)

    if boolean_value:
        message = 'The {} is out of range ({} <= {} <= {}). Please re-input: '
        print(message.format(name, lower_bound, name, upper_bound))

    return boolean_value


def input_qualified_number(name, lower_bound, upper_bound):
    '''
    Function--Keep prompting user to input an number until it is 
        an integer number which is in the range of the 
        given lower_bound and upper_bound. It might raise 
        ValueError if the input number is not an integer. 
        This error will be catched and prompt user to re-input.
    Parameters:
        name: string| any string to represent a variable name
        lower_bound: int| the minimum int of the number
        upper_bound: int| the maximum int of the number
    Returns:
        number: int|any integer number which is in the qualified range.
    '''

    done = True
    while done:
        try:
            message = 'The {} of the maze ({} <= {} <= {}): '
            number = input(
                message.format(name, lower_bound, name, upper_bound)
            )
            # Check if the input number is an integer number.
            if not float(number).is_integer():
                raise ValueError
            number = int(number)
            done = check_range(name, number, lower_bound, upper_bound)
        except ValueError:
            print('Please input an integer number.')

    return number


def check_character(maze_row, characters_list, message, row_number):
    '''
    Function: check if characters in the maze_row are all 
        in characters_list. If not, print error message and 
        return True. Otherwise, it will return False.
    Parameters:
        maze_row: string| a string contains any character
        characters_list: list of string| 
            the list of the required elements
        message: string|any string contains the prompt message
        row_number: int| an integer number which represents the 
            row number of the maze, which starts from 0.
    Return: boolean value| return False if characters in the 
        maze_row are all in characters_list,
        otherwise, return True.
    '''

    boolean_value = False
    for character in maze_row:
        if character not in characters_list:
            boolean_value = True
            print(message.format(row_number))
            break

    return boolean_value


def check_maze_row(maze_row, row_number, width, height):
    '''
    Function--firstly, check if the length of the maze_row 
        is equal to the width. If not, return True. If they are 
        equal, then check if maze_row meet the special guidelines 
        according its row_number position. The first row(i = 0) 
        and the last row(i = height - 1) have the same guidelines 
        and the rows between them have the other guidelines. 
        Return False if the maze_row meets the guidelines. 
        Otherwise, return False.
    Parameters:
        maze_row: string|a string which is input by user.
        row_number: int| an integer number which represents the 
            row number of the maze, which starts from 0.
        width: int| an integer number which represents 
            the number of characters in one row of maze
        height: int| an integer number which represents 
            the total number of the rows of the maze.
    Returns:boolean value|return False if the maze_row 
        meets the guidelines. Otherwise, return False
    '''

    inner_space_character = [' ', 'X']
    outer_edge_character = ['X', 'E']
    boolean_value = True
    # Check whether the length of the maze_row
    # is equal to the width of the maze.
    if len(maze_row) != width:
        message = ('The length of row is wrong. '
                   'Please re-input the {} row.')
        print(message.format(row_number))
    else:
        # Check if the characters in the first row(i = 0) and 
        # the last row(i = height - 1) are capital letter 
        # X or capital letter E.
        if row_number == 0 or row_number == height - 1:
            message = ('Wrong input maze character. \n'
                       'They should be capital letter '
                       'X or capital letter E. \n'
                       'Please re-input the {} row.')

            boolean_value = check_character(
                maze_row, outer_edge_character, message, row_number
            )
        # Check whether the middle rows meet the guidelines.
        else:
            # The fist and the last character should be 
            # capital letter X or capital letter E.
            message = ('Wrong input maze character. \n'
                       'The fist and the last character should be capital '
                       'letter X or capital letter E. \n'
                       'Please re-input the {} row.')

            boolean_value1 = check_character(
                maze_row[0] + maze_row[-1], 
                outer_edge_character, message, row_number
            )
            # The characters in the middle should be 
            # capital letter X or the blank space.
            message = ('Wrong input maze character. \n'
                       'The characters except the fist and the last character '
                       'should be capital letter X or the blank space. \n'
                       'Please re-input the {} row.')
            boolean_value2 = check_character(
                maze_row[1:-1], inner_space_character, message, row_number
            )
            # Either the first and the last character or the 
            # characters in the middle of the maze_row don't 
            # meet the guideline will make the value of done True.
            boolean_value = (boolean_value1 or boolean_value2)
    return boolean_value


def input_maze_row(row_number, width, height):
    '''
    Function--Prompting user to input one specific row of maze 
        and check if it meets the guidelines according its position. 
        Keep prompting user to input until the input maze_row
        is varified as as a row of the maze.
    Parameter:
    row_number:int|any integer number in the range from 0 to height - 1
    width: int|an integer number which represents 
        the required number of the length of the maze_row.
    height:int|an integer number which represents the 
        required number of the total number of maze_row.
    Returns: string| a string which is input by user and 
        is varified as one row of the maze.
    '''

    done = True
    while done:
        # Prompt the user to input one specific row.
        row_message = 'The ' + str(row_number) + ' row: '
        maze_row = input(row_message)
        # Check whether the input row meets the requirements.
        # If not, the value of the done will be True and 
        # prompt the user to re-input this row.
        done = check_maze_row(maze_row, row_number, width, height)

    return maze_row


def check_maze_exit_number(maze_string):
    '''
    Function--check whether a maze_string which is constructed 
        by all varified maze_rows contains 1 or more capital letter E. 
        Return False if maze_string contains 1 or more 
        capital letter E. Otherwise, return True.
    Parameters:
        maze_string: string|a string which is constructed 
            by all varified maze_rows.
    Returns: boolean value|return False if maze_string contains 
        1 or more capital letter E. Otherwise, return True.
    '''
    result = False
    if maze_string.count('E') < 1:
        message = ('Wrong maze. Every maze needs' 
                   '1 or more exits. Please re-input.')
        print(message)
        result = True

    return result


def input_maze_dict(width, height):
    '''
    Function--Looping the program until the qualified maze is got.
        That is, the number of the maze_row is equal to 
        the height and each row meets its special requirments.
        The maze has 1 or more exits. If the maze is qualified, 
        using the row number(start from 0) as the key 
        and a list of the characters in the each maze_row 
        as its value to construct the maze_dict.
    Parameters:
        width: int|an integer number which represents 
            the required number of the length of the maze_row.
        height:int|an integer number which represents the 
            required number of the total number of maze_row.
    Returns:dictionary|key is the row_number from 0 to height -1,
        the corresponding value is a list of the 
        varified maze_row string which is input by user.
    '''

    result = True
    while result:
        maze_string = ''
        maze_dict = {}
        for row_number in range(height):
            maze_row = input_maze_row(row_number, width, height)
            maze_dict[row_number] = list(maze_row)
            # Construct maze_string using all varified input maze_row
            maze_string += maze_row
        # Check whether this maze has 1 or more exits.
        # If not, print message for user to input a new maze.
        result = check_maze_exit_number(maze_string)
    return maze_dict


def read_from_keyboard():
    '''
    Function--Given the range of the width and the height of the maze,
        get the qualified number of width and height of 
        the maze and the maze_dict from the keyboard 
        using input_qualified_number(), input_maze_dict() functions.
    Parameters:None.
    Returns:
        maze_dict:dictionary|key is the row_number from 0 
            to height -1,the corresponding value is a list of the 
            varified maze_row string which is input by user.
        width: int|an integer number which represents 
            the required number of the length of the maze_row.
        height:int|an integer number which represents the 
            required number of the total number of maze_row.
    '''

    width = input_qualified_number('width', 3, 120)
    height = input_qualified_number('height', 3, 40)
    message = 'Input maze:'
    print(message)
    maze_dict = input_maze_dict(width, height)

    return maze_dict, width, height


def check_file_data(file_data):
    '''
    Function--check a list of data which is read from file. 
        Each line is one element of the list. Check whether the 
        first element contains the qualified numbers which 
        represents the width and height of the maze. Check whether 
        the remaining elements meet the guidelines of maze one by 
        one. Any element in the list which is not qualified will 
        raise Valuerror to terminate the check. If all elements 
        pass the check, then it will return the width and height 
        of the maze and an dictionary in which key is the 
        row_number from 0 to height -1, the corresponding 
        value is a list of the varified maze_row string 
        which has qualified length and characters.
    Parameters:
        file_data: list|a list of data which is read from file. 
            Each line is one element of the list.
    Returns:
        maze_dict:dictionary|key is the row_number from 0 
            to height -1,the corresponding value is a list of the 
            varified maze_row string which is input by user.
        width: int|an integer number which represents 
            the required number of the length of the maze_row.
        height:int|an integer number which represents the 
            required number of the total number of maze_row.
    '''

    maze_string = ''
    maze_dict = {}
    key = 0

    for line_number in range(len(file_data)):
        file_data[line_number] = file_data[line_number].rstrip('\n')
        no_space_line = file_data[line_number].replace(' ', '')
        # The first line should contain integer numbers to 
        # specify the width and height of the maze.
        if line_number == 0:
            if no_space_line.isdigit():
                # Get the specified width and height of the maze.
                width, height = tuple(file_data[line_number].split())
                width, height = int(width), int(height)
                # Check if the number is in the right range.
                if check_range('width', width, 3, 120) or \
                   check_range('height', height, 3, 40):
                    raise ValueError

            else:
                print('The first line of the maze file should be integers.')
                raise ValueError

        elif line_number > 0:
            # Check if each line except the first digits 
            # line meet the guidlines of the maze. If not,
            # raise Valueerror for user to re-input
            if check_maze_row(file_data[line_number], key, width, height):
                raise ValueError

            # If the line is qualified, construct the maze_string.
            # Use the key(start from 0 and add 1 for each qualified line.)
            # and content of line as its corresponding 
            # value to construct the maze_dict.
            maze_string += file_data[line_number]
            maze_dict[key] = list(file_data[line_number])
            key += 1
    else:
        # Check if the maze_string contains 1 or more capital letter E.
        # If not, raise Valueerror for user to re-input.
        if check_maze_exit_number(maze_string):
            raise ValueError

    return maze_dict, width, height


def read_from_file():
    '''
    Function--Keep prompting user to input the filename until 
        the qualified data can be read from the file. 
        Opening file may raise FileNotFoundError 
        or PermissionError or OSError. Check the data in 
        file may raise Valuerror. Each error will be catched 
        and prompt user to input another filename.
    Parameters:None.
    Returns:
        maze_dict:dictionary|key is the row_number from 0 
            to height -1,the corresponding value is a list of the 
            varified maze_row string which is input by user.
        width: int|an integer number which represents 
            the required number of the length of the maze_row.
        height:int|an integer number which represents the 
            required number of the total number of maze_row.
    '''

    done = True
    while done:
        try:
            filename = input('Maze file: ')
            input_file = open(filename, 'r')
            file_data = input_file.readlines()
            # If get the qualified maze_dict, width and height 
            # data from the qualified maze_file, then teminate the loop
            maze_dict, width, height = check_file_data(file_data)
            done = False
            input_file.close()
        # Keep prompting user to input filename 
        # if the current file can't be read.
        except FileNotFoundError or PermissionError or OSError:
            print("Error occurred reading the maze file. Please re-input.")
        # Keep prompting user to input filename
        # if the data in current file is not qualified.
        except ValueError:
            print('Please re-input maze_file')

    return maze_dict, width, height


def get_start_position(maze_dict, width, height):
    '''
    Function--Keep prompting user to input the start_row 
        and start_column. Both two numbers should be integer 
        and in the given range. And the location they represents 
        in the maze should not be in coincide with a wall.
        Then, the qualified location they represents in the maze
        will be 'S'.
    Parameters:
        maze_dict:dictionary|key is the row_number from 0 
            to height -1,the corresponding value is a list of the 
            varified maze_row string which is input by user.
        width: int|an integer number which represents 
            the required number of the length of the maze_row.
        height:int|an integer number which represents the 
            required number of the total number of maze_row.
    Returns:
        start_row: int|an integer number which represents 
            the row number in the maze, which is in the 
            range from 0 to height - 1.
        start_column: int|an integer number which represents 
            the column number in the maze, which is in the 
            range from 0 to width - 1.
    '''

    done = True
    while done:
        print('Input start location.')
        # Prompt user to input numbers as start_row and 
        # start_column and check if it is in the right 
        # range and give corresponding message.
        start_row = input_qualified_number('start_row', 0, height - 1)
        start_column = input_qualified_number('start_column', 0, width - 1)
        message = 'Start position is in coincide with a wall in {} row.'
        # Check if the start positon is in coincide with a wall.
        done = check_character(
                maze_dict[start_row][start_column], ' ', message, start_row
            )

    # If the starting positon is qualified, 
    # then change its value in the maze_dict as 'S'.
    # Otherwise, keep prompting user to input.
    maze_dict[start_row][start_column] = 'S'

    return start_row, start_column


def initialize_distance_direction(maze_dict):
    '''
    Function--initialize distance value and direction value for 
        all the spaces(blank space and exits) in the maze.
        Distance(s) is represented as a float and created 
        using float("inf"). Direction(s) is represented as None.
    Parameters:
        maze_dict:dictionary|key is the row_number from 0 
            to height -1,the corresponding value is a list of the 
            varified maze_row string which is input by user.
    Returns:
        distance_dict:dictionary|key is the tuple of (row, column) 
            which represents the blank space or the exit position 
            in the maze, the corresponding value is float("inf").
        direction_dict:dictionary|key is the tuple of (row, column) 
            which represents the blank space or the exit 
            position in the maze, the corresponding value is None.
    '''

    distance_dict = {}
    direction_dict = {}

    for row in range(0, len(maze_dict)):
        for column in range(0, len(maze_dict[row])):
            # All the spaces(blank space and exits) in 
            # the maze are initialized by a distance 
            # value and a direction value respectively.
            if maze_dict[row][column] != 'X':
                distance_dict[(row, column)] = float('inf')
                direction_dict[(row, column)] = None
    return distance_dict, direction_dict


def find_exits(maze_dict, start_row, start_column):
    '''
    Function--Calculating the distance and the direction 
        from the start position of the maze to each 
        space(blank spaces and exits) in the maze and 
        store the value in the distance_dict, direction_dict
        according to its (row, column) position.
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
    Returns:
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
    '''

    # Initialize distance value and direction value for 
    # all the spaces(blank space and exits) in the maze
    distance_dict, direction_dict = initialize_distance_direction(maze_dict)
    # Calculating the distance and the direction 
    # from the start position of the maze to each 
    # space(blank spaces and exits) in the maze   
    worklist = [(start_row, start_column)]
    distance_dict[(start_row, start_column)] = 0
    while worklist != []:
        current_row, current_column = worklist[0]
        worklist.remove(worklist[0])
        neighbors = {
            (current_row, current_column - 1): 'West', 
            (current_row, current_column + 1): 'East',
            (current_row - 1, current_column): 'North',
            (current_row + 1, current_column): 'South',
        }
        for neighbor in neighbors:
            if neighbor in distance_dict and \
               distance_dict[neighbor] == float('inf'):

                current_distance = distance_dict[(current_row, current_column)]
                distance_dict[neighbor] = current_distance + 1
                direction_dict[neighbor] = neighbors[neighbor]
                worklist += [neighbor]

    return distance_dict, direction_dict


def find_closet_exit(distance_dict, maze_dict):
    '''
    Function--Look at the values in distance(s) to determine 
        which exit is the closest by determining which 
        exit has the smallest value stored in distance(s).
    Parameters:
        distance_dict:dictionary|key is the tuple of (row, column) 
            which represents the blank space or the exit position 
            in the maze, the corresponding value is the distance
            from each position to the start position.
        maze_dict:dictionary|key is the row_number from 0 
            to height -1,the corresponding value is a list of the 
            varified maze_row string which is input by user.
    Returns:
        exit_row: int|an integer which represents the 
            row position in the maze in which the 
            values in distance(s) is the smallest.
        exit_column: int|an integer which represents 
            the column position in the maze in which 
            the values in distance(s) is the smallest.
    '''

    exits_distance_dict = {}
    for row, column in distance_dict:
        if maze_dict[row][column] == 'E':
            exits_distance_dict[(row, column)] = distance_dict[(row, column)]

    # Interchange the position information with
    # its corresding value of distance for sorting.
    exits_distance_dict = {
        value: key for key, value in exits_distance_dict.items()
    }

    # sorting all the value of distance of exits
    exits_distance_list = sorted(exits_distance_dict)
    # choose the samallest value of distance and 
    # get its correspoding row and column of position of exit.
    exit_row, exit_column = exits_distance_dict[exits_distance_list[0]]

    return exit_row, exit_column


def get_path_to_exit(exit_row, exit_column, direction_dict):
    '''
    Function--Once we have identified closest exit, we can trace 
        backwards to the starting location by 
        using the information stored in direction(s).
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
    Returns:
        final_path:list|a list of elements, each element in it
            is (row, column) pair. The list contains the 
            exit positon in the maze and the position 
            in the path from exit to start position.
    '''

    final_path = []
    current_row, current_column = exit_row, exit_column
    # Loop until to the start position.
    while direction_dict[(current_row, current_column)] is not None:
        back_neighbors = {
            'West': (current_row, current_column + 1),
            'East': (current_row, current_column - 1),
            'North': (current_row + 1, current_column),
            'South': (current_row - 1, current_column),
        }

        position = direction_dict[(current_row, current_column)]
        next_row, next_column = back_neighbors[position]
        final_path += [(current_row, current_column)]
        current_row, current_column = next_row, next_column

    return final_path


def get_path_maze(maze_dict, final_path):
    '''
    Function-According to the position which 
        is stored in the fina_path list, change its 
        corresponding value of the maze_dict to
        "*" (asterisk) to denotes part of a path out.
    Parameters:
        maze_dict:dictionary|key is the row_number from 0 
            to height -1,the corresponding value is a list of the 
            varified maze_row string which is input by user.
        final_path:list|a list of elements, each element in it
            is (row, column) pair.
    Returns:
        maze_dict:dictionary|key is the row_number from 0 
            to height -1,the corresponding value is a list of the 
            varified maze_row string which is input by user. And modify 
            the value of the (row, column) pair which represents the position
            in the maze from blank space to "*" (asterisk).
    '''

    # If the final path is empty, 
    # then print prompt message.
    if final_path == []:
        print('The exit is unreachable.')
    # Find and change the value of the maze_dict according 
    # to the (row, column)pair which is stored 
    # in the fina_path list. The first element is 
    # the exit position, so, there is no change.
    else:
        for row, column in final_path[1:]:
            maze_dict[row][column] = '*'

    return maze_dict


def print_maze(maze_dict):
    '''
    Function--The key in the maze_dict as the number of 
        the row of the maze, which starts from 0. 
        Convert the corresponding value from a list to a string.
        Then the maze can be shown on the screen.
    Parameter:
        maze_dict:dictionary|key is the row_number from 0 
            to height -1,the corresponding value is a list of the 
            varified maze_row string which is input by user 
            or is modified by the cloest path.
    Returns: string|a string which represents all characters 
        in the maze.each row is seperated by a new line character
    '''

    maze = ''
    for value in maze_dict.values():
        maze += ''.join(str(item) for item in value) + '\n'

    return maze[:-1]


def check_input_cmd():
    '''
    Function--Show the user the option list and keep 
        prompting user to input until an integer number 
        which is in the range from 1 to 5. This function 
        might raise Valuerror when the input is not an 
        integer or not in the right range. The error will 
        be catched and print prompt message and 
        compel user to re-input.
    Parameters: none.
    Returns:
        cmd: int|any integer number from 1 to 5.
    '''

    cmd_set = {1, 2, 3, 4, 5}
    text_message = ('\n1. Read maze from keyboard\n'
                    '2. Read maze from file\n3. Find exit\n'
                    '4. Print maze \n5. Quit game\n'
                    'Input the number of the option: ') 

    done = True
    while done:
        try:
            cmd = int(input(text_message))
            if cmd not in cmd_set:
                raise ValueError
            done = False
        except ValueError:
            print('Wrong option number. Please input an integer from 1 to 5.')

    return cmd


def clear_path(maze_dict):
    '''
    Function--Clear up the start position and path of the last game
        in the original maze to ensure the maze is the original.
    Parameter:
        maze_dict:dictionary|key is the row_number from 0 
            to height -1,the corresponding value is a list of the 
            varified maze_row string which is input by user 
            or is modified by the cloest path.
    Returns:
        maze_dict:dictionary|key is the row_number from 0 
            to height -1,the corresponding value is a list of the 
            varified maze_row string which is input by user.
    '''

    # Clear up the start position and path of the last game
    # in the original maze to ensure the maze is the original.
    old_path_characters = ['S', '*']
    for value in maze_dict.values():
        for i in range(len(value)):
            if value[i] in old_path_characters:
                value[i] = ' '

    return maze_dict


def main():
    cmd = check_input_cmd()

    while cmd != 5:
        if cmd == 1 or cmd == 2:
            # Intialize all the variables of the maze or 
            # clear up the datas of the last game to begin a new game.
            width = height = start_row = 0
            start_column = exit_row = exit_column = 0
            maze_dict = distance_dict = direction_dict = {}
            final_path = []
            maze = ''

            if cmd == 1:
                # Get the width, height and the 
                # specific datas of maze from the keyboard.
                maze_dict, width, height = read_from_keyboard()

            else:
                # Get the width, height and the 
                # specific datas of maze from the keyboard.         
                maze_dict, width, height = read_from_file()

        elif cmd == 3:
            try:
                # Clear up the data of the last game 
                # to have the original maze for next game.
                maze_dict = clear_path(maze_dict)
                # Find closet exit of the maze 
                # for the start_row, start_column.
                start_row, start_column = get_start_position(
                    maze_dict, width, height
                )
                distance_dict, direction_dict = find_exits(
                    maze_dict, start_row, start_column
                )
                exit_row, exit_column = find_closet_exit(
                    distance_dict, maze_dict
                )
                print('Already find the closet exit.')
            # If there is no maze, print the error message.
            except UnboundLocalError:
                print('Please input the maze firstly.')

        elif cmd == 4: 
            try:
                # Print the way to the exit if it has been calculated.
                try:
                    final_path = get_path_to_exit(
                        exit_row, exit_column, direction_dict
                    )
                    maze_dict = get_path_maze(maze_dict, final_path)
                    maze = print_maze(maze_dict)
                    print('The solved maze.')
                    print(maze)
                # If there is no way to the exit, 
                # then print the current maze to the screen.
                except KeyError:
                    maze = print_maze(maze_dict)
                    print('The original maze.')
                    print(maze)
            # If there is no maze, print the error message.
            except UnboundLocalError:
                print('Please input the maze firstly.')

        # Prompt user to input another option.
        cmd = check_input_cmd()

    print('Game over.')


if __name__ == '__main__':
    main()
