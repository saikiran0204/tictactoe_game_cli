board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
count = 0
def show():
    print("|---|----|----|")
    for i in board:
        print("",end='|')
        for j in i:
            print("",j,end = " | ")
        print()
        print("|---|----|----|")

def checkrow(j):
    for i in range(0,3):
        if board[i][0] == j and board[i][1] == j and board[i][2] == j:
            return True
    return False

def checkcol(j):
    for i in range(0,3):
        if board[0][i] == j and board[1][i] == j and board[2][i] == j:
            return True
    return False

def checkdiag(c):
    if (board[0][0] == c and board[1][1] == c and board[2][2] == c) or (board[2][0] == c and board[1][1] == c and board[0][2] == c):
        return True
    else:
        return False


def checkwin(c):
    if c == 0:
        j='x'
    else:
        j='o'
    if checkrow(j) or checkcol(j) or checkdiag(j):
        return True
    else:
        return False


while count <= 8:
    show()
    position = input("enter position").split('.')
    try:
        position[0], position[1] = int(position[0]), int(position[1])
        if board[position[0]][position[1]] != 0:
            print('spot already taken')
        else:
            c = count%2
            if c == 0:
                board[position[0]][position[1]] = 'x'
            else:
                board[position[0]][position[1]]='o'
            if checkwin(c):
                show()
                if c == 0:
                    print('X wins')
                    break
                else:
                    print('o wins')
                    break
            count += 1
    except IndexError:
        print("out of range")
    except ValueError:
        print("please enter integer")
    finally:
        pass
if count >= 9:
    print("Draw match")