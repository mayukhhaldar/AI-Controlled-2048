import random

# first create the basic structure of the game
# create a 4x4 board

gameBoard = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

gameFlags = [
    [False, False, False, False],
    [False, False, False, False],
    [False, False, False, False],
    [False, False, False, False]
]

validMove = False
score = 0
isLeftAllowed = True
isUpAllowed = True
isRightAllowed = True
leftHappened = False
upHappened = False


# Self-Playing Algorithm

def get_the_next_move():
    return corner_algorithm()


def blind_moves():
    global isLeftAllowed
    global isUpAllowed
    global isRightAllowed

    if isLeftAllowed:
        return "left"
    elif isUpAllowed:
        isLeftAllowed = True
        return "up"
    elif isRightAllowed:
        isLeftAllowed = True
        isUpAllowed = True
        return "right"
    else:
        isLeftAllowed = True
        isUpAllowed = True
        isRightAllowed = True
        return "down"


def corner_algorithm():
    global upHappened
    global leftHappened
    checkLeft = check_left(gameBoard)
    checkRight = check_right(gameBoard)
    checkUp = check_up(gameBoard)

    if checkLeft and not leftHappened:
        upHappened = False
        leftHappened = True
        return "left"
    elif checkUp and not upHappened:
        upHappened = True
        leftHappened = False
        return "up"
    elif checkUp:
        return "up"
    elif checkRight:
        return "right"
    else:
        return "down"


def check_left(board):
    numOfRows = len(board)
    numOfCols = len(board[0])
    for col in range(numOfCols):
        for row in range(numOfRows):
            if board[row][col] != 0 and col != 0:
                slideEnd = False
                tempCol = col
                while not slideEnd:
                    nextCol = tempCol - 1
                    if nextCol == 0:
                        slideEnd = True
                        if board[row][nextCol] == 0:
                            return True
                        elif board[row][nextCol] == board[row][col]:
                            return True
                        else:
                            if tempCol != col:
                                return True
                    elif board[row][nextCol] != 0:
                        slideEnd = True
                        if board[row][nextCol] == board[row][col]:
                            return True
                        else:
                            board[row][tempCol] = board[row][col]
                            if tempCol != col:
                                return True
                    else:
                        tempCol = nextCol


def check_right(board):
    numOfRows = len(board)
    numOfCols = len(board[0])

    for col in reversed(range(numOfCols)):
        for row in reversed(range(numOfRows)):
            if board[row][col] != 0 and col != numOfCols - 1:
                slideEnd = False
                tempCol = col
                while not slideEnd:
                    nextCol = tempCol + 1
                    if nextCol == numOfCols - 1:
                        slideEnd = True
                        if board[row][nextCol] == 0:
                            return True
                        elif board[row][nextCol] == board[row][col]:
                            return True
                        else:
                            if tempCol != col:
                                return True
                    elif board[row][nextCol] != 0:
                        slideEnd = True
                        if board[row][nextCol] == board[row][col]:
                            return True
                        else:
                            if tempCol != col:
                                return True
                    else:
                        tempCol = nextCol


def check_down(board):
    numOfRows = len(board)

    for row in reversed(range(numOfRows)):
        numOfCols = len(board[row])

        for col in reversed(range(numOfCols)):
            if board[row][col] != 0 and row != numOfRows - 1:
                slideEnd = False
                tempRow = row
                while not slideEnd:
                    nextRow = tempRow + 1
                    if nextRow == numOfRows - 1:
                        slideEnd = True
                        if board[nextRow][col] == 0:
                            return True
                        elif board[nextRow][col] == board[row][col]:
                            return True
                        else:
                            if tempRow != row:
                                return True
                    elif board[nextRow][col] != 0:
                        slideEnd = True
                        if board[nextRow][col] == board[row][col]:
                            return True
                        else:
                            if tempRow != row:
                                return True
                    else:
                        tempRow = nextRow


def check_up(board):
    numOfRows = len(board)
    for row in range(numOfRows):
        numOfCols = len(board[row])
        for col in range(numOfCols):
            if board[row][col] != 0 and row != 0:
                slideEnd = False
                tempRow = row
                while not slideEnd:
                    nextRow = tempRow - 1
                    if nextRow == 0:
                        slideEnd = True
                        if board[nextRow][col] == 0:
                            # just move the number (slide)
                            return True
                        elif board[nextRow][col] == board[row][col]:
                            # add the numbers (adding)
                            return True
                        else:
                            if tempRow != row:
                                return True
                    elif board[nextRow][col] != 0:
                        slideEnd = True
                        if board[nextRow][col] == board[row][col]:
                            return True
                        else:
                            # moving the number next to the different number
                            if tempRow != row:
                                return True
                    else:
                        tempRow = nextRow


# Game Control and Functionality


def print_board(board):
    length = len(board)
    largestLength = find_largest_length(gameBoard)
    for row in range(length):
        colLength = len(board[row])
        for col in range(colLength):
            numOfDigits = len(str(board[row][col]))
            numOfSpaces = largestLength - numOfDigits
            for i in range(numOfSpaces):
                print(" ", end='')
            print(board[row][col], end='')
            print("  ", end='')
        print("\n", end='')


def reset_flags():
    rowLength = len(gameFlags)
    for row in range(rowLength):
        colLength = len(gameFlags)
        for col in range(colLength):
            gameFlags[row][col] = False


def initializing_board():
    firstNumber = random.randint(2, 4)
    while firstNumber == 3:
        firstNumber = random.randint(2, 4)

    row = random.randint(0, 3)
    col = random.randint(0, 3)
    gameBoard[row][col] = firstNumber

    secondNumber = random.randint(2, 4)
    while secondNumber == 3:
        secondNumber = random.randint(2, 4)

    rowNext = random.randint(0, 3)
    colNext = random.randint(0, 3)

    while rowNext == row and colNext == col:
        rowNext = random.randint(0, 3)
        # colNext = random.randint(0, 3)

    gameBoard[rowNext][colNext] = secondNumber


def find_largest_length(board):
    length = 0
    rowLength = len(board)
    for row in range(rowLength):
        colLength = len(board[row])
        for col in range(colLength):
            numOfDigits = len(str(board[row][col]))
            if numOfDigits > length:
                length = numOfDigits

    return length


def move_up(board):
    global validMove
    global score
    numOfRows = len(board)
    for row in range(numOfRows):
        numOfCols = len(board[row])
        for col in range(numOfCols):
            if board[row][col] != 0 and row != 0:
                slideEnd = False
                tempRow = row
                while not slideEnd:
                    nextRow = tempRow - 1
                    if nextRow == 0:
                        slideEnd = True
                        if board[nextRow][col] == 0:
                            # just move the number (slide)
                            validMove = True
                            board[nextRow][col] = board[row][col]
                            board[row][col] = 0
                        elif board[nextRow][col] == board[row][col]:
                            # add the numbers (adding)
                            if not gameFlags[nextRow][col]:
                                validMove = True
                                board[nextRow][col] = board[row][col] * 2
                                gameFlags[nextRow][col] = True
                                score = score + board[nextRow][col]
                                board[row][col] = 0
                            else:
                                # perform a slide
                                board[tempRow][col] = board[row][col]
                                if tempRow != row:
                                    validMove = True
                                    board[row][col] = 0
                        else:
                            # if the number is different then just move the piece upto it (slide)
                            board[tempRow][col] = board[row][col]
                            if tempRow != row:
                                validMove = True
                                board[row][col] = 0
                    elif board[nextRow][col] != 0:
                        slideEnd = True
                        if board[nextRow][col] == board[row][col]:
                            # add the numbers (adding)
                            if not gameFlags[nextRow][col]:
                                validMove = True
                                board[nextRow][col] = board[row][col] * 2
                                gameFlags[nextRow][col] = True
                                score = score + board[nextRow][col]
                                board[row][col] = 0
                            else:
                                # perform a slide
                                board[tempRow][col] = board[row][col]
                                if tempRow != row:
                                    validMove = True
                                    board[row][col] = 0
                        else:
                            # moving the number next to the different number
                            board[tempRow][col] = board[row][col]
                            if tempRow != row:
                                validMove = True
                                board[row][col] = 0
                    else:
                        tempRow = nextRow


def move_down(board):
    global validMove
    global score
    numOfRows = len(board)

    for row in reversed(range(numOfRows)):
        numOfCols = len(board[row])

        for col in reversed(range(numOfCols)):
            if board[row][col] != 0 and row != numOfRows - 1:
                slideEnd = False
                tempRow = row
                while not slideEnd:
                    nextRow = tempRow + 1
                    if nextRow == numOfRows - 1:
                        slideEnd = True
                        if board[nextRow][col] == 0:
                            validMove = True
                            board[nextRow][col] = board[row][col]
                            board[row][col] = 0
                        elif board[nextRow][col] == board[row][col]:
                            if not gameFlags[nextRow][col]:
                                validMove = True
                                board[nextRow][col] = board[row][col] * 2
                                gameFlags[nextRow][col] = True
                                score = score + board[nextRow][col]
                                board[row][col] = 0
                            else:
                                board[tempRow][col] = board[row][col]
                                if tempRow != row:
                                    validMove = True
                                    board[row][col] = 0
                        else:
                            board[tempRow][col] = board[row][col]
                            if tempRow != row:
                                validMove = True
                                board[row][col] = 0
                    elif board[nextRow][col] != 0:
                        slideEnd = True
                        if board[nextRow][col] == board[row][col]:
                            if not gameFlags[nextRow][col]:
                                validMove = True
                                board[nextRow][col] = board[row][col] * 2
                                gameFlags[nextRow][col] = True
                                score = score + board[nextRow][col]
                                board[row][col] = 0
                            else:
                                board[tempRow][col] = board[row][col]
                                if tempRow != row:
                                    validMove = True
                                    board[row][col] = 0
                        else:
                            board[tempRow][col] = board[row][col]
                            if tempRow != row:
                                validMove = True
                                board[row][col] = 0
                    else:
                        tempRow = nextRow


def move_left(board):
    global validMove
    global score
    numOfRows = len(board)
    numOfCols = len(board[0])

    for col in range(numOfCols):
        for row in range(numOfRows):
            if board[row][col] != 0 and col != 0:
                slideEnd = False
                tempCol = col
                while not slideEnd:
                    nextCol = tempCol - 1
                    if nextCol == 0:
                        slideEnd = True
                        if board[row][nextCol] == 0:
                            validMove = True
                            board[row][nextCol] = board[row][col]
                            board[row][col] = 0
                        elif board[row][nextCol] == board[row][col]:
                            if not gameFlags[row][nextCol]:
                                validMove = True
                                board[row][nextCol] = board[row][col] * 2
                                gameFlags[row][nextCol] = True
                                score = score + board[row][nextCol]
                                board[row][col] = 0
                            else:
                                # perform a slide
                                board[row][nextCol] = board[row][col]
                                if tempCol != col:
                                    validMove = True
                                    board[row][col] = 0
                        else:
                            board[row][tempCol] = board[row][col]
                            if tempCol != col:
                                validMove = True
                                board[row][col] = 0
                    elif board[row][nextCol] != 0:
                        slideEnd = True
                        if board[row][nextCol] == board[row][col]:
                            if not gameFlags[row][nextCol]:
                                validMove = True
                                board[row][nextCol] = board[row][col] * 2
                                gameFlags[row][nextCol] = True
                                score = score + board[row][nextCol]
                                board[row][col] = 0
                            else:
                                board[row][nextCol] = board[row][col]
                                if tempCol != col:
                                    validMove = True
                                    board[row][col] = 0
                        else:
                            board[row][tempCol] = board[row][col]
                            if tempCol != col:
                                validMove = True
                                board[row][col] = 0
                    else:
                        tempCol = nextCol


def move_right(board):
    global validMove
    global score
    numOfRows = len(board)
    numOfCols = len(board[0])

    for col in reversed(range(numOfCols)):
        for row in reversed(range(numOfRows)):
            if board[row][col] != 0 and col != numOfCols - 1:
                slideEnd = False
                tempCol = col
                while not slideEnd:
                    nextCol = tempCol + 1
                    if nextCol == numOfCols - 1:
                        slideEnd = True
                        if board[row][nextCol] == 0:
                            validMove = True
                            board[row][nextCol] = board[row][col]
                            board[row][col] = 0
                        elif board[row][nextCol] == board[row][col]:
                            if not gameFlags[row][nextCol]:
                                validMove = True
                                board[row][nextCol] = board[row][col] * 2
                                gameFlags[row][nextCol] = True
                                score = score + board[row][nextCol]
                                board[row][col] = 0
                            else:
                                # perform a slide
                                board[row][nextCol] = board[row][col]
                                if tempCol != col:
                                    validMove = True
                                    board[row][col] = 0
                        else:
                            board[row][tempCol] = board[row][col]
                            if tempCol != col:
                                validMove = True
                                board[row][col] = 0
                    elif board[row][nextCol] != 0:
                        slideEnd = True
                        if board[row][nextCol] == board[row][col]:
                            if not gameFlags[row][nextCol]:
                                validMove = True
                                board[row][nextCol] = board[row][col] * 2
                                gameFlags[row][nextCol] = True
                                score = score + board[row][nextCol]
                                board[row][col] = 0
                            else:
                                # perform a slide
                                board[row][nextCol] = board[row][col]
                                if tempCol != col:
                                    validMove = True
                                    board[row][col] = 0
                        else:
                            board[row][tempCol] = board[row][col]
                            if tempCol != col:
                                validMove = True
                                board[row][col] = 0
                    else:
                        tempCol = nextCol


def game_end_check(board):
    checkBoard = board.copy()
    empty = 0
    rowLength = len(checkBoard)
    for row in range(rowLength):
        colLength = len(checkBoard[row])
        for col in range(colLength):
            if checkBoard[row][col] == 0:
                empty = empty + 1

    if empty == 0:
        global validMove
        canUp = False
        canDown = False
        canRight = False
        canLeft = False

        validMove = False
        move_up(checkBoard)
        if validMove:
            canUp = True

        validMove = False
        move_down(checkBoard)
        if validMove:
            canDown = True

        validMove = False
        move_right(checkBoard)
        if validMove:
            canRight = True

        validMove = False
        move_left(checkBoard)
        if validMove:
            canLeft = True

        if not canUp and not canDown and not canLeft and not canRight:
            exit_game()


def find_largest_tile(board):
    largestTile = 0
    rowLength = len(board)
    for row in range(rowLength):
        colLength = len(board[row])
        for col in range(colLength):
            tile = board[row][col]
            if tile > largestTile:
                largestTile = tile

    return largestTile


def exit_game():
    print("Thank you for playing!")
    print("Your final score is: ", end='')
    print(score)
    largestTile = find_largest_tile(gameBoard)
    print("Your largest tile was: ", end='')
    print(largestTile)
    print_board(gameBoard)
    exit()


def spawn_new_number():
    newNumber = random.randint(2, 4)
    while newNumber == 3:
        newNumber = random.randint(2, 4)

    row = random.randint(0, 3)
    col = random.randint(0, 3)

    while gameBoard[row][col] != 0:
        row = random.randint(0, 3)
        col = random.randint(0, 3)

    gameBoard[row][col] = newNumber


def user_plays():
    global validMove
    print("Enter Next Move: ")

    while True:
        game_end_check(gameBoard)
        reset_flags()
        validMove = False
        validInput = True
        move = input()
        if move == "up":
            move_up(gameBoard)
        elif move == "down":
            move_down(gameBoard)
        elif move == "left":
            move_left(gameBoard)
        elif move == "right":
            move_right(gameBoard)
        elif move == "exit":
            exit_game()
        else:
            print("Sorry your input was not understood. Please try again!")
            validInput = False

        if validInput:
            if not validMove:
                print("Move is not valid. Try a different move!")
            else:
                spawn_new_number()
                print("Your score is: ", end='')
                print(score)
                print_board(gameBoard)

        print("Enter Next Move: ")


def ai_plays():
    global validMove
    global isLeftAllowed
    global isRightAllowed
    global isUpAllowed
    isLeftAllowed = True
    isUpAllowed = True
    isRightAllowed = True
    while True:
        game_end_check(gameBoard)
        reset_flags()
        validMove = False
        print_board(gameBoard)
        move = get_the_next_move()
        print(move)
        print(score)
        if move == "up":
            move_up(gameBoard)
            if not validMove:
                isUpAllowed = False
        elif move == "down":
            move_down(gameBoard)
        elif move == "left":
            move_left(gameBoard)
            if not validMove:
                isLeftAllowed = False
        elif move == "right":
            move_right(gameBoard)
            if not validMove:
                isRightAllowed = False
        elif move == "exit":
            exit_game()

        if validMove:
            spawn_new_number()


# main game start and loop
initializing_board()
reset_flags()
print_board(gameBoard)
print("Who will play: 1. You or 2. AI")
whoPlays = input()

if whoPlays == "1":
    user_plays()
elif whoPlays == "2":
    ai_plays()
else:
    exit()
