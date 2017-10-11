from random import shuffle
import os
import sys
clear = lambda : os.system('cls')

class Player(object):
    def __init__(self,name,bal):
        self.name = name
        self.count = 0
        self.bal = bal
        self.bet = 0
        self.busted = False
        self.stand = False
        self.double = False
        self.card = []
        self.blackjack = False
    def double_bet(self):
        self.double = True
        self.bal -= self.bet
        self.bet = self.bet*2
    def player_stand(self):
        self.stand = True
    def player_busted(self):
        self.busted = True
    def __str__(self):
        return "Player:%s\tCard:%s\tCount:%s\tBal:%s"%(self.name,self.card,self.count,self.bal)

class Dealer(object):
    def __init__(self,name,bal):
        self.name = name
        self.count = 0
        self.bal = bal
        self.stand = False
        self.busted = False
        self.card = []
        self.blackjack = False
    def dealer_stand(self):
        self.stand =True
    def dealer_busted(self):
        self.busted = True
    def __str__(self):
        return "Dealer:%s\tCard:%s\tCount:%s\tBal:%s"%(self.name,self.card,self.count,self.bal)

def play_game():

    def print_player(player_list):
            for player in player_list:
                print(player)

    def generate_deck():
        deck = {}
        suits = ('C','S','D','H')
        ranks = [('A',1),('2',2),('3',3),('4',4),('5',5),('6',6),('7',7),('8',8),('9',9),('J',10),('Q',10),('K',10)]
        for suit in suits:
            for rank,value in ranks:
                deck[suit+"-"+rank]=value
        return deck

    def draw_card(deck):
        keys = list(deck.keys())
        shuffle(keys)
        shuffle(keys)
        shuffle(keys)
        lst = [(key,deck[key]) for key in keys]
        return lst.pop()

    #Initialize player and dealer
    player_list = []
    dealer = None
    replay = 'Y'
    first_time = True

    if len(sys.argv) < 2:
        print("1.Usage : <script_name.py> player_count player1_name=player1_bal player2_name=player2_bal .. playerN_name=playerN_bal dealer_name=dealer_balance")
        sys.exit(1)

    try:
        if len(sys.argv) == int(sys.argv[1])+2:
            for i in range(2,len(sys.argv)-1):
                try:
                    lst = sys.argv[i].split("=")
                    player_list.append(Player(lst[0],int(lst[1])))
                except:
                    print("2.Usage : <script_name.py> player_count player1_name=player1_bal player2_name=player2_bal .. playerN_name=playerN_bal dealer_name=dealer_balance")
                    sys.exit(1)
            try:
                temp = sys.argv[i+1].split("=")
                dealer = Dealer(temp[0],int(temp[1]))
            except:
                print("3.Usage : <script_name.py> player_count player1_name=player1_bal player2_name=player2_bal .. playerN_name=playerN_bal dealer_name=dealer_balance")
                sys.exit(1)
        else:
            print("4.Usage : <script_name.py> player_count player1_name=player1_bal player2_name=player2_bal .. playerN_name=playerN_bal dealer_name=dealer_balance")
            sys.exit(1)
    except:
        print("Player Count is invaild or not specified : 5.Usage : <script_name.py> player_count player1_name=player1_bal player2_name=player2_bal .. playerN_name=playerN_bal dealer_name=dealer_balance")

    try:
        num_of_player = int(sys.argv[1])
    except:
        print("5.Enter valid count (Integer Required)\nUsage : <script_name.py> player_count player1_name=player1_bal player2_name=player2_bal .. playerN_name=playerN_bal dealer_name=dealer_balance")
        sys.exit(1)

    for player in player_list:
        player.bet = int(input("Enter Player %s's Bet:"%player.name))
        player.bal -= player.bet

    deck = generate_deck()

    while (replay == 'Y' or replay == 'y') and not player_list == []:
        clear()

        if not first_time:
            for player in player_list:
                player.bet = int(input("Enter new bet %s:"%player.name))
                player.bal -= player.bet
            print_player(player_list)
            print(dealer)
        #serve first time
        for i in range(0,2):
            for player in player_list:
                card = draw_card(deck)
                deck.pop(card[0])
                if card[1] == 1:
                    if player.count + 11 < 21:
                        player.card.append(card[0])
                        player.count += 11
                    else:
                        player.card.append(card[0])
                        player.count += 1
                else:
                    player.card.append(card[0])
                    player.count += int(card[1])
        for player in player_list:
            if player.count == 21:
                print("------->Player %s has blackjack<----"%player.name)
                player.blackjack = True
                player.stand = True
        dealercard = draw_card(deck)
        deck.pop(dealercard[0])
        if dealercard[1] == 1:
            if dealer.count + 11 < 21:
                dealer.card.append(dealercard[0])
                dealer.count += 11
            else:
                dealer.card.append(dealercard[0])
                dealer.count += 1
        else:
            dealer.card.append(dealercard[0])
            dealer.count += int(dealercard[1])

        print("------------------:Card status after First dealing:---------------")
        print_player(player_list)
        input("---Press Enter to see dealer status-->")
        print("------------------:Dealer's Card Status---------------------------")
        print(dealer)
        input("---Press Enter to Start game--->")
        #dealing starts
        for player in player_list:
            print("-----------------------:",player.name,"'s chance:---------------------")
            print(player)
            if player.blackjack == True:
                print("----------Player has blackjack-------------")
                continue
            while not player.double and not player.stand and not player.busted:
                choice = input("1.hit,2.double,3.stand: ")
                if choice == '1':
                    card = draw_card(deck)
                    deck.pop(card[0])
                    if card[1] == 1:
                        if player.count + 11 < 21:
                            player.card.append(card[0])
                            player.count += 11
                        else:
                            player.card.append(card[0])
                            player.count += 1
                    else:
                        player.card.append(card[0])
                        player.count += int(card[1])
                    if player.count > 21:
                        player.player_busted()
                        print(player.name," is busted")
                    if player.count == 21:
                        player.player_stand()
                        print(player.name," is standing")
                elif choice == '2':
                    if player.bal - player.bet > 0:
                        card = draw_card(deck)
                        deck.pop(card[0])
                        if card[1] == 1:
                            if player.count + 11 < 21:
                                player.card.append(card[0])
                                player.count += 11
                            else:
                                player.card.append(card[0])
                                player.count += 1
                        else:
                            player.card.append(card[0])
                            player.count += int(card[1])
                        player.double_bet()
                        if player.count > 21:
                            player.player_busted()
                            print(player.name," is busted")
                        if player.count == 21:
                            player.player_stand()
                            print(player.name," is standing")
                    else:
                        print(player.name," can not bet double (Not sufficient Balance)")
                        continue
                elif choice == '3':
                    player.player_stand()
                print(player)
        #dealer opens second card
        dealercard = draw_card(deck)
        deck.pop(dealercard[0])
        if dealercard[1] == 1:
            if dealer.count + 11 < 21:
                dealer.card.append(dealercard[0])
                dealer.count += 11
            else:
                dealer.card.append(dealercard[0])
                dealer.count += 1
        else:
            dealer.card.append(dealercard[0])
            dealer.count += int(dealercard[1])
        print("--------------------Dealer's Card status------------------------")
        print(dealer)
        while not dealer.stand and not dealer.busted:
            print("------------------Dealer ",dealer.name,"'s chance----------------------")
            choice = input("1.hit,2.stand :")
            if choice == '1':
                dealercard = draw_card(deck)
                deck.pop(dealercard[0])
                if dealercard[1] == 1:
                    if dealer.count + 11 < 21:
                        dealer.card.append(dealercard[0])
                        dealer.count += 11
                    else:
                        dealer.card.append(dealercard[0])
                        dealer.count += 1
                else:
                    dealer.card.append(dealercard[0])
                    dealer.count += int(dealercard[1])
                if dealer.count > 21:
                    print(dealer)
                    dealer.dealer_busted()
                    print("Dealer  is busted")
                if dealer.count == 21:
                    dealer.dealer_stand()
                    print("Dealer is standing")
            elif choice == '2':
                dealer.dealer_stand()
            print(dealer)
        #check who wins or lose
        print("--------------------Final Status:----------------------")
        for player in player_list:
            win_amount = 0
            if player.busted:
                print(player.name,"lost")
                dealer.bal += player.bet
                continue
            if dealer.busted:
                if player.blackjack == True:
                    win_amount += player.bet /2
                    dealer.bal -= player.bet /2
                win_amount += player.bet*2
                dealer.bal -= player.bet
                print(player.name," wins ",win_amount," Rs")
                player.bal += win_amount
                continue
            if player.count > dealer.count:
                if player.blackjack == True:
                    win_amount += player.bet /2
                    dealer.bal -= player.bet /2
                win_amount += player.bet*2
                dealer.bal -= player.bet
                print(player.name," wins ",win_amount," Rs")
                player.bal += win_amount
                continue
            if player.count == dealer.count:
                if player.blackjack == True:
                    win_amount += player.bet /2
                    dealer.bal -= player.bet /2
                print(player.name," has draw")
                player.bal += player.bet + win_amount
                continue
            else:
                print(player.name," is lost")
                dealer.bal += player.bet
                continue
        print_player(player_list)
        print(dealer)
        #reinitialize player object for next play
        for player in player_list:
            if player.bal < 1:
                print("Player %s can not play again"%player.name)
                player_list.remove(player)
            else:
                player.stand = False
                player.busted = False
                player.double = False
                player.count = 0
                player.card = []
        dealer.stand = False
        dealer.busted = False
        dealer.card = []
        dealer.count = 0

        first_time = False
        replay = input("Replay?(Y/N):")

play_game()
