# Project 09
# Play some Blackjack!


import cards

def get_deck():
    # Create the deck of cards
    deck = cards.Deck()
    deck.shuffle()


    # Shuffle the deck, then display it in 13 columns
    deck.shuffle()

    return deck

def deal_cards(deck):
    """
    cards are dealt in proper order
    """
    
    player_list=[]
    dealer_list=[]
    
    player_list.append( deck.deal() )
    dealer_list.append( deck.deal() )
    player_list.append( deck.deal() )
    dealer_list.append( deck.deal() )

    return player_list, dealer_list


def hit(hand, deck):
    """
    adds one card to a hand
    """
    
    hand.append(deck.deal())


def calculate_hand(hand):
    """
    calculates value of hand
    assigns proper ace value
    """
    
    aces = []
    i = 0
    hand_values = []

    for card in hand:
        if card.get_value() != None:
            hand_values.append(card.get_value())

            # keeps track of aces
            if card.get_rank() == 1:
                aces.append(i)
            
            if sum(hand_values) <= 11:
                # reassign ace values
                if aces:
                    for ace in aces:
                        hand_values[ace] = 11
            elif sum(hand_values) > 21:
                # reassign ace values
                if aces:
                    for ace in aces:
                        hand_values[ace] = 1

        i+=1
      
    return sum(hand_values)


def player_turn(p1_cards, dealer_cards, deck):
    """
    prompt user to hit or stand
    say if user busts
    return hand total
    """
    while not deck.is_empty():
        try:
            print()
            usr_in = input('(H)it or (S)tand:')
            print()

            if usr_in.lower() != 'n' and usr_in.lower() != 'no' \
               and usr_in.lower() != 's' and usr_in.lower() != 'stand':
                
                hit(p1_cards, deck)

                print('Your hand: ',p1_cards)
                print('Dealer hand: [{}, xx]'.format(dealer_cards[0]))
                print('Current Player total:',calculate_hand(p1_cards))

                if calculate_hand(p1_cards) > 21:
                    print('Player has {}, busts.'.\
                          format(calculate_hand(p1_cards)))
                    
                    return calculate_hand(p1_cards)              

            else:
                return calculate_hand(p1_cards)
            
        except KeyboardInterrupt:
            continue
    else:
        return 'empty'


def dealer_turn(p1_score, dealer_cards, deck):
    """
    logic for dealer
    uses calculate_hand to get hand value
    hits or stands based on return value
    """
    while not deck.is_empty():
        if p1_score > 21:
            return 'noplay'
        if calculate_hand(dealer_cards) > 21:
            
            print('Dealer hand: ',dealer_cards)
            print('Dealer has {}, busts.'.\
                  format(calculate_hand(dealer_cards)))
            
            return calculate_hand(dealer_cards)
        
        elif calculate_hand(dealer_cards) >= 17:
            print('Dealer hand: ',dealer_cards)
            print('Dealer has {}. Dealer stands.'.\
                  format(calculate_hand(dealer_cards)))
            
            return calculate_hand(dealer_cards)

        elif calculate_hand(dealer_cards) < 17:
            print('Dealer takes a card..')
            hit(dealer_cards, deck)
    else:
        return 'empty'
       

def begin_game(deck, scoreboard):
    """
    deals cards
    starts players_turn
    gets players score
    finds winner with declare_winner
        uses dealer_turn
    """
    dealt_cards = deal_cards(deck)

    # assign players their cards
    p1_cards, dealer_cards = dealt_cards[0], dealt_cards[1]

    # start game
    if not deck.is_empty():
        print('Your hand: ',p1_cards)
        print('Dealer hand: [{}, xx]'.format(dealer_cards[0]))
        print('Current Player total:',calculate_hand(p1_cards))

    # user turn is first
    p1_score = player_turn(p1_cards, dealer_cards, deck)

    # pass p1_score and the dealers returned score 
    declare_winner(p1_score, dealer_turn(p1_score, dealer_cards, \
                                         deck),scoreboard)


def declare_winner(p1_score, dealer_score, scoreboard):
    """
    calculates the winner
    adds to the scoreboard
    """
        
    if p1_score == 'empty' or dealer_score == 'empty':
        print('Deck is empty')
        scoreboard['draw'] += 1
    elif dealer_score == 'noplay':
        print()
        print('Dealer is the winner!')
        scoreboard['dealer'] += 1
    elif dealer_score > 21:
        print()
        print('Player 1 is the winner!')
        scoreboard['player'] += 1
    elif p1_score == dealer_score:
        print()
        print('Game is a draw.')
        scoreboard['draw'] += 1
    elif p1_score > dealer_score:
        print()
        print('Player 1 is the winner!')
        scoreboard['player'] += 1
    elif p1_score < dealer_score:
        print()
        print('Dealer is the winner!')
        scoreboard['dealer'] += 1
    print()


def main():
    """
    Builds deck
    Initializes scoreboard
    Begins the game
    Prompts user to keep playing
    Prints scoreboard
    """
    # template for formatting
    format_template = \
                    "** wins:  {0:>3} **\n** losses:{1:>3} **\n** draw:  {2:>3} **"
    scoreboard = {'player':0,\
                  'dealer':0, 'draw':0}
    
    deck = get_deck()

    begin_game(deck, scoreboard)

    while not deck.is_empty():
        # print(deck.cards_count()) testing
        # get user input to begin_game
        try:
            usr_in = input('Play another round? (Y)es or (N)o:')

            # n or no to stop the game
            if usr_in.lower() != 'n' and usr_in.lower() != 'no':
                begin_game(deck, scoreboard)

            else:
                break

        except KeyboardInterrupt:
            print('User ended program.')
            break

    # print the scoreboard
    print()
    print('****************')
    print('**  Player 1  **')
    print('****************')
    print(format_template.format(scoreboard['player'], \
                                 scoreboard['dealer'], \
                                 scoreboard['draw']))
    print('****************')


main()
