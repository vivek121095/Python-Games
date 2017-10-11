import os,sys

def clear():
    os.system( 'cls' )

def print_board():
    global tttboard
    for row in tttboard:
        print(row)

def update_board_pos(pos,player):
    global tttboard
    board_pos = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    if player == '1':
        tttboard[board_pos[pos-1][0]][board_pos[pos-1][1]] = 'O'
    else:
        tttboard[board_pos[pos-1][0]][board_pos[pos-1][1]] = 'X'
    clear()
    print_board()

def win_check():
    global tttboard
    return ((tttboard[0][0]==tttboard[0][1]==tttboard[0][2])or
            (tttboard[0][0]==tttboard[1][0]==tttboard[2][0])or
            (tttboard[0][0]==tttboard[1][1]==tttboard[2][2])or
            (tttboard[0][1]==tttboard[1][1]==tttboard[2][1])or
            (tttboard[0][2]==tttboard[1][2]==tttboard[2][2])or
            (tttboard[0][2]==tttboard[1][1]==tttboard[2][0])or
            (tttboard[1][0]==tttboard[1][1]==tttboard[1][2])or
            (tttboard[2][0]==tttboard[2][1]==tttboard[2][2]))

def board_full():
    global avail_pos
    if avail_pos == []:
        return True
    else:
        return False

tttboard = []
avail_pos = []
player = '0'

def play_game():
    global player
    global tttboard
    global avail_pos
    player = '1'
    tttboard = [['1','2','3'],['4','5','6'],['7','8','9']]
    avail_pos = [1,2,3,4,5,6,7,8,9]
    print_board()
    print("Who want to play first Player(1 or 2)?:")
    if input() == '1':
        player = '1'
    else:
        player = '2'
    while True:
        inp = int(input("player %s chance: (type 99 to quit)"%player))
        clear()
        if inp == 99 :
            sys.exit(0)
        if inp in avail_pos:
            update_board_pos(inp,player)
            avail_pos.pop(avail_pos.index(inp))
        else:
            print("position already taken")
            continue
        if win_check():
            print("player ",player," won!!")
            break
        if board_full():
            print("Draw!!")
            break
        if player == '1':
            player = '2'
        else:
            player = '1'
while True:
    play_game()
    print("Want to Play again?(Y/N):")
    replay = input()
    if replay == 'N' or replay == 'n':
        break
