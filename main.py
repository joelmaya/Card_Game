from random import *


def showHelp():
    instructions = """\nPlayers simply guess if the next card is going to be lower or higher than previous one
and win or loose they bet according to if they were right or not.\n"""
    print(instructions)


def specialInput(prompt):
    action = input(prompt)
    if action == '--help':
        print("You need help")
        # Go to help screen
        showHelp()
        return specialInput(prompt)
    elif action == "--resume":
        print("You want to resume")
        # You can decide whether or not to do anything else here
        return specialInput(prompt)
    else:
        return action


def cardDeck():  # create deck of the cards
    cardDeck = []
    for value in range(4):  # four sets of cards
        for i in range(2, 11):  # for number values
            if value == 0:
                cardDeck.append(str(i) + '♠')
            if value == 1:
                cardDeck.append(str(i) + '♣')
            if value == 2:
                cardDeck.append(str(i) + '♦')
            if value == 3:
                cardDeck.append(str(i) + '♥')
    figures = ['J', 'Q', 'K', 'A']
    for figure in figures:  # for four set of figures
        cardDeck.append(str(figure) + '♠')
        cardDeck.append(str(figure) + '♣')
        cardDeck.append(str(figure) + '♦')
        cardDeck.append(str(figure) + '♥')
    shuffle(cardDeck)
    return cardDeck


class Player:  # define player class
    def __init__(self, nickname='Player', bankroll=100, value=0):
        self.nick = nickname
        self.bankroll = int(bankroll)
        self.value = value
        self.BetKind = ''
        self.amount = 0

    def __str__(self):
        return self.nick + ' plays'

    def win(self):

        self.bankroll += 2 * int(self.amount)

    def MassBet(self):

        for i in range(1000):
            self.amount = int(specialInput('how much do you want to bet? '))
            if self.amount <= self.bankroll:
                break
            else:
                print('You can bet only your current bank!')
        for i in range(1000):
            self.BetKind = specialInput('higher/lower [h/l] ')
            if self.BetKind == 'h' or self.BetKind == 'l':
                break
            else:
                print("Please enter only 'h' or 'l' ")
        self.bankroll -= int(self.amount)

    def GetValue(self, card):
        self.value = Values[card[0:-1]]


Deck = cardDeck()
Values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
          '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}  # define value of each card

PlayerList = []
NPlayers = int(specialInput('How many players are going to play? '))  # Here you can define players
for i in range(NPlayers):
    print('Inicialization, player ', i + 1)
    nickname = specialInput('What is your nickname? ')
    bankroll = specialInput('What is your bank? ')
    player = Player(nickname, bankroll)
    PlayerList.append(player)

oldCardsValues = [Deck[-1]]
Deck.pop()
print(Deck[45:])
round = 0
while True:
    print('You bet againts: ', oldCardsValues[-1])
    for player in PlayerList:  # define kind of the bet for each player
        print(player.nick + ', ', end='')
        player.MassBet()
    DrawCard = Deck.pop()
    if NPlayers == 1:
        print('You draw: ', DrawCard)
    else:
        print('All players bet! Draw is: ', DrawCard)
    for player in PlayerList:  # define if player won or lost
        player.GetValue(DrawCard)
        if player.BetKind == 'l':
            if Values[oldCardsValues[-1][0:-1]] > player.value:
                player.win()
                print(player.nick, 'won! New bankroll: ', player.bankroll)
            elif Values[oldCardsValues[-1][0:-1]] < player.value:
                print(player.nick, 'lost! New bankroll: ', player.bankroll)
            else:
                print('Same card', player.nick, 'lost')
        elif player.BetKind == 'h':
            if Values[oldCardsValues[-1][0:-1]] < player.value:
                player.win()
                print(player.nick, 'won! New bankroll: ', player.bankroll)
            elif Values[oldCardsValues[-1][0:-1]] > player.value:
                print(player.nick, 'lost! New bankroll: ', player.bankroll)
            else:
                print('Same card', player.nick, 'lost')
        print(player.bankroll)
        if player.bankroll <= 0:  # if player run out of cash he is out
            print(player.nick, 'I am sorry, you run out of your cash. You are out.')
            PlayerList.remove(player)
    if len(PlayerList) == 0:  # if there are no remaining players game is over
        print('No more players left. Game Over!')
        break

    round += 1
    print('current deck len: ', len(Deck), 'current round: ', round)
    MixCoeficcient = randrange(25, 35)
    if len(Deck) < MixCoeficcient:  # create new deck in random interval of the remaining cards
        Deck = cardDeck()

    oldCardsValues.append(DrawCard)
    print('-' * 40)
