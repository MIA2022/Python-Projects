"""
Nan Chen
HW7

This is a Connect Four game. This game starts with the initial 
empty board, and prompting user to choose from three options.
After user chooses the option, the updated board will show
with the option menu for next choice. There might raise 
Value error when user chooses add piece or undo. Errors will 
be properly handled, and message will be given to the user.
The game continues until user quits. When you play a piece, 
the next player should automatically switch to the other player.
User can undo even when the game is over. The undone piece 
will be ready to be added as the next piece.
"""


from connect_four import ConnectFour


def check_input_cmd():
    '''
    Function--Show the user the option list and keep
        prompting user to input until a qualified character
        is input. If the input is not qualified,
        prompt message and compel user to re-input.
    Parameters: none.
    Returns:
        cmd: string| one of 'P', 'U', 'Q', 'p', 'u', 'q'.
    '''

    cmd_set = {'P', 'U', 'Q', 'p', 'u', 'q'}
    text_message = ('1. P)lay a piece\n'
                    '2. U)ndo the previous play\n'
                    '3. Q)uit game\nInput P/U/Q/p/u/q: ')
    done = True
    while done:
        cmd = input(text_message)
        if cmd in cmd_set:
            done = False
        else:
            print('Wrong option. Please input P/U/Q/p/u/q.')

    return cmd


def main():
    board = ConnectFour()
    # Print out the board, and then prompt
    # the user to choose the option.
    print(board.__str__())
    cmd = check_input_cmd()

    while cmd != 'Q' and cmd != 'q':

        if cmd == 'P' or cmd == 'p':
            done = True
            while done:
                try:
                    column = int(input('column number:'))
                    board.add_piece(column)
                    done = False
                except ValueError as e:
                    # Prompt user to choose another option
                    # if the game is already over. As for
                    # the column is invalid or already full,
                    # prompt user to input another column
                    if e.args[0] == 'The game already is over':
                        done = False
                    print(e)

        if cmd == 'U' or cmd == 'u':
            try:
                board.undo()
            except ValueError as e:
                # Print the error message to remind
                # user if there is no undo.
                print(e)

        print(board.__str__())
        cmd = check_input_cmd()
    # The input is Q or q, print out the final
    # state of the board and message.
    print(board.__str__())
    print('Game Over\nWinner is', board.get_winner())


if __name__ == '__main__':
    main()
