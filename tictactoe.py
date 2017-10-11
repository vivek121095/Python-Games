import os
def clear():
    os.system( 'cls' )
def print_board():
    global tttboard
    for row in tttboard:
        print(row)

def update_board_pos(pos,player):
    global tttboard
    if player == '1':
        tttboard[pos[0]][pos[1]] = 'O'
    else:
        tttboard[pos[0]][pos[1]] = 'X'
    clear()
    print_board()

def win_check():
    global tttboard
    return ((tttboard[0][0]==tttboard[0][1]==tttboard[0][2]!='-')or
            (tttboard[0][0]==tttboard[1][0]==tttboard[2][0]!='-')or
            (tttboard[0][0]==tttboard[1][1]==tttboard[2][2]!='-')or
            (tttboard[0][1]==tttboard[1][1]==tttboard[2][1]!='-')or
            (tttboard[0][2]==tttboard[1][2]==tttboard[2][2]!='-')or
            (tttboard[0][2]==tttboard[1][1]==tttboard[2][0]!='-')or
            (tttboard[1][0]==tttboard[1][1]==tttboard[1][2]!='-')or
            (tttboard[2][0]==tttboard[2][1]==tttboard[2][2]!='-'))

def board_full():
    global avail_pos
    if avail_pos == []:
        return True
    else:
        return False

tttboard = [['-','-','-'],['-','-','-'],['-','-','-']]
avail_pos = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
player = '1'
def play_game():
    global player
    global tttboard
    global avail_pos
    print_board()
    print("Who want to play first Player(1 or 2)?:")
    if input() == '1':
        player = '1'
    else:
        player = '2'
    while True:
        print("player",player," chance: (type 99,99 to quit)")
        inp = tuple(int(x.strip()) for x in input().split(','))
        if inp == (99,99):
            break
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
