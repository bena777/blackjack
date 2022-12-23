import random
balance=1000
def blackjack():
    global balance
    # defines values in a dict while making a list out of 4 of each card (no suits)
    card_values = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10,'K': 10}
    deck = list(card_values.keys()) * 4
    # Player class sets bet amount and gives player their starting card values
    class Player():
        bet = int(input("How much would you like to bet?"))
        def __init__(self,name,bet):
            self.name=name
            self.bet=bet
            while self.bet>balance:
                print("Sorry, not enough money with current balance of $"+str(balance),"please pick a new amount.")
                self.bet=int(input("How much would you like to bet?"))
            self.hand=[]
            card1=random.choice(deck)
            deck.remove(card1)
            card2=random.choice(deck)
            deck.remove(card2)
            self.hand.append(card1)
            self.hand.append(card2)
            self.total=0
            self.total+=card_values[card1]+card_values[card2]
            print("Your cards are a",card1,"and a",card2,"for a total of",str(self.total))
        # hit function adds another card to players hand
        def hit(self):
            card=random.choice(deck)
            deck.remove(card)
            self.hand.append(card)
            self.total+=card_values[card]
            print("You drew a",card,"bringing your total to",str(self.total))
    # dealer class defines dealer's first card 
    class Dealer():
        def __init__(self):
            self.hand=[]
            card1=random.choice(deck)
            self.hand.append(card1)
            deck.remove(card1)
            self.total=0
            self.total+=card_values[card1]
            print("Dealer draws a",card1,"for a total of",str(self.total))
        # hit function is same as player hit function; would like to combine the two if possible 
        def hit(self):
            card=random.choice(deck)
            self.hand.append(card)
            deck.remove(card)
            self.total+=card_values[card]
            print("Dealer drew a",card,"bringing his total to",str(self.total))
    # makes variable out of player and dealer classes; 'Ben' is just a placeholder and can be changed
    player=Player('Ben',Player.bet)
    dealer=Dealer()
    hit='Yes'
    busted=False
    # While the player keeps inputting 'Yes' they will continue to recieve another card to their total
    # Loop will end when player decides he doesn't want to draw anymore or his score>21 
    # If score>21, player loses his original bet 
    while hit.lower()=='yes':
        hit=input("Would you like to hit?")
        if hit=='Yes':
            player.hit()
            # for loop changes players Ace card value from an 11 to a 1 if need be 
            if player.total>21:
                for i in player.hand:
                    if i=='A':
                        player.total-=10
                        player.hand.remove(i)
                        print("Changed A value to 1 bringing total to",str(player.total))
                if player.total>21:
                    hit='no'
                    balance-=player.bet
                    print("Sorry, your busted")
                    print("You lost $"+str(player.bet),"bringing your balance down to $"+str(balance))
                    # player.total=0
                    busted=True
    # only activates if player does not bust while drawing 
    # will continue drawing cards until dealer.total>=17
    while dealer.total<=17 and busted==False:
        if busted==False:
            dealer.hit()
            if dealer.total>21:
                for i in dealer.hand:
                    if i=='A':
                        dealer.total-=10
                        dealer.hand.remove(i)
                        print("Changed A value to 1 bringing total to",str(dealer.total))
                # if dealers score becomes >21 during the loop, player wins 1.5x his bet
                if dealer.total>21:
                    balance+=player.bet*1.5
                    print("Dealer busted!")
                    print("You win $"+str(player.bet*1.5),"bringing your balance up to $"+str(balance))
                    # dealer.total=0
                    busted=True
    # only activates if neither player busts
    if busted==False:
        if player.total>dealer.total:
            balance+=player.bet*1.5
            print(player.name+"'s total of",str(player.total),"is greater than the dealers total of",str(dealer.total))
            print("You win $" + str(player.bet * 1.5), "bringing your balance up to $" + str(balance))
        elif player.total==dealer.total:
            print("Tie game. No money is gained or lost. Your balance is still $"+str(balance))
        elif player.total<dealer.total:
            balance-=player.bet
            print("Dealers total of",str(dealer.total),"is greater than",player.name+"'s total of",str(player.total))
            print("You lose $"+str(player.bet),"bringing your balance down to $"+str(balance))
    play_again=input("Would you like to play again?")
    # allows player to play again if they want
    # only allowed if balance is positive
    if play_again.lower()=='yes':
        if balance<=0:
            print("Sorry, not enough funds. Your current balance is $"+str(balance))
            print("Thank you for playing! We hope to see you again soon.")
        else:
            blackjack()
    else:
        print("Thank you for playing",player.name,"! You ended with a total balance of $"+str(balance))
blackjack()