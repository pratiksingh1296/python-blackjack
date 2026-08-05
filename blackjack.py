import random

def welcome():
    print("\nWelcome to the Blackjack Game! ")
    print("\nThe goal of the game is to get as close to 21 as possible without going over.")
    print("\nThe dealer will deal two cards to you and two cards to themselves. One of the dealer's cards will be face up and the other will be face down.")
    print("\nYou can choose to hit (get another card), stand (keep your current hand), double down (double your bet and get one more card), split (if you have two cards of the same value, you can split them into two hands), or surrender (give up half your bet and end the game).")
    print("\nIf you go over 21, you bust and lose the game. If the dealer goes over 21, they bust and you win. If neither of you busts, the hand with the higher total wins.")
    print("\nGood luck!")


def deal_card():
    return random.choice(range(1,12))


def deal_initial_cards():
    player_cards = [deal_card(), deal_card()]
    dealer_cards = [deal_card(), deal_card()]

    print(f"Player cards: {player_cards[0]}, {player_cards[1]}")
    print(f"Dealer's cards: {dealer_cards[0]}, X")

    return player_cards, dealer_cards


def is_busted(cards):
    return sum(cards) > 21


def calculate_hand(cards):
    return sum(cards)


def get_player_choice():
    print("\n Choose what to do: ")
    return int(input("\n1. Hit  2. Stand  3. Double Down  4. Split  5.Surrender\n")) 


def handle_hit(hand):
    hand.append(deal_card())
    return hand


def hand_double_down(hand, bet):
    bet *= 2
    hand.append(deal_card())
    print(f"Bet: {bet}")
    print(f"Hand: {hand}")
    return hand, bet


def handle_split(player_cards):
    if player_cards[0] != player_cards[1]:
        print("You can't split")
        return None
    hand1 = [player_cards[0], deal_card()]
    hand2 = [player_cards[1], deal_card()]
    return hand1, hand2


def play_split(player_cards, dealer_cards, player_bet): 

    split_hands = handle_split(player_cards)

    if split_hands is None:
        return

    hand1, hand2 = split_hands

    print("\nPlaying Hand 1") 
    hand1, player_bet = player_turn(hand1, player_bet) 

    print("\nPlaying Hand 2") 
    hand2, player_bet = player_turn(hand2, player_bet) 

    dealer_cards = dealer_turn(dealer_cards) 

    print("\nHand 1:")
    determine_winner(hand1, dealer_cards)

    print("\nHand 2:")
    determine_winner(hand2, dealer_cards)


def player_turn(player_cards, player_bet):

    while calculate_hand(player_cards) < 21:

        print(f"\nYour cards: {player_cards}")
        print(f"Total: {calculate_hand(player_cards)}")

        choice = get_player_choice()

        if choice == 1:
            player_cards = handle_hit(player_cards)
            print(f"Player's cards: {player_cards}")
            print(f"Player's Hand: {calculate_hand(player_cards)}")

            # Check if player hand is busted:
            if is_busted(player_cards):
                print("\n You busted! Your hand is over 21.")
                break
        
        elif choice == 2:
            break

        elif choice == 3:
            player_cards, player_bet = hand_double_down(player_cards, player_bet)

            # Check if player hand is busted:
            if is_busted(player_cards):
                print("\n You busted! Your hand is over 21.")
            else:
                print(f"\nPlayer's Hand: {calculate_hand(player_cards)}")
            break  #Since the turn should end after doubling down.
    
        elif choice == 4:
            return player_cards, player_bet, True

        elif choice == 5: #Surrender
                        print("\n Thanks for playing. ")
                        break #End the game

    return player_cards, player_bet, False

def dealer_turn(dealer_cards):

    while calculate_hand(dealer_cards) < 17:
        dealer_cards = handle_hit(dealer_cards)
        print(f"\nDealer's Hand: {dealer_cards}")

    return dealer_cards

def determine_winner(player_cards, dealer_cards):

    if is_busted(dealer_cards):
        print(f"\nDealer busted! Player wins!")
    elif calculate_hand(dealer_cards) == calculate_hand(player_cards):
        print(f"It's a tie.")
    elif calculate_hand(dealer_cards) < calculate_hand(player_cards):
        print(f"Player wins with {calculate_hand(player_cards)}")
    elif calculate_hand(dealer_cards) > calculate_hand(player_cards):
        print(f"Dealer wins with {calculate_hand(dealer_cards)}")
    

def main():

    welcome()

    player_cards, dealer_cards = deal_initial_cards()

    player_bet = int(input("\nPlease enter bet amount: "))

    player_cards, player_bet, split_requested = player_turn(player_cards, player_bet)

    if split_requested:
        play_split(player_cards, dealer_cards, player_bet)
        return
    
    # Don't play dealer if player busted
    if not is_busted(player_cards):
        dealer_cards = dealer_turn(dealer_cards)

    determine_winner(player_cards, dealer_cards)

main()
    
