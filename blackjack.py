import random


def welcome():
    print("\nWelcome to the Blackjack Game! ")
    print("\nThe goal of the game is to get as close to 21 as possible without going over.")
    print("\nThe dealer will deal two cards to you and two cards to themselves. One of the dealer's cards will be face up and the other will be face down.")
    print("\nYou can choose to hit (get another card), stand (keep your current hand), double down (double your bet and get one more card), split (if you have two cards of the same value, you can split them into two hands), or surrender (give up half your bet and end the game).")
    print("\nIf you go over 21, you bust and lose the game. If the dealer goes over 21, they bust and you win. If neither of you busts, the hand with the higher total wins.")
    print("\nGood luck!")


def create_deck():
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suits = ["♠", "♥", "♦", "♣"]
    deck = [(rank, suit) for suit in suits for rank in ranks]
    return deck


def shuffle_deck(deck):
    random.shuffle(deck)
    return deck


def deal_card(deck):
    return deck.pop()


def display_hand(hand):
    return " ".join(f"{rank}{suit}" for rank, suit in hand)


def deal_initial_cards(deck):
    player_cards = [deal_card(deck), deal_card(deck)]
    dealer_cards = [deal_card(deck), deal_card(deck)]

    print(f"Player cards: {display_hand(player_cards)}")
    print(f"Dealer's cards: {dealer_cards[0][0]}{dealer_cards[0][1]} X")

    return player_cards, dealer_cards


def is_busted(cards):
    return calculate_hand(cards) > 21


def calculate_hand(cards):
    total = 0
    aces = 0

    for rank, _ in cards:
        if rank in ["J", "Q", "K"]:
            total += 10
        elif rank == "A":
            total += 11
            aces += 1
        else:
            total += int(rank)

    while total > 21 and aces:
        total -= 10
        aces -= 1

    return total


def get_player_choice():
    print("\n Choose what to do: ")
    while True:
        try:
            choice = int(input("\n1. Hit  2. Stand  3. Double Down  4. Split  5.Surrender\n")) 
            if 1 <= choice <= 5:
                return choice
        except ValueError:
            pass
        print('Invalid choice.')


def handle_hit(hand, deck):
    hand.append(deal_card(deck))
    return hand


def hand_double_down(hand, deck, bet, money):
    if money < bet * 2:
        print('Not enough money to double down!')
        return hand, bet
    bet *= 2
    hand.append(deal_card(deck))
    print(f"Bet: {bet}")
    print(f"Hand: {display_hand(hand)}")
    return hand, bet


def handle_split(player_cards, deck):
    # split validation
    if player_cards[0][0] != player_cards[1][0]:
        print("You can't split")
        return None
    
    hand1 = [player_cards[0], deal_card(deck)]
    hand2 = [player_cards[1], deal_card(deck)]
    return hand1, hand2


def play_split(player_cards, dealer_cards, player_bet, deck, money): 

    if money < player_bet * 2:
        print('Not enough money to play split.')
        return 
    
    split_hands = handle_split(player_cards, deck)

    if split_hands is None:
        return

    hand1, hand2 = split_hands
    hand1_bet = player_bet
    hand2_bet = player_bet

    print(f"\nHand 1: {display_hand(hand1)} ${hand1_bet}")
    print(f"\nHand 2: {display_hand(hand2)} ${hand2_bet}")


    print("\nPlaying Hand 1") 
    hand1, hand1_bet, _ = player_turn(hand1, hand1_bet, deck, money, allow_split=False, allow_surrender=False) 

    print("\nPlaying Hand 2") 
    hand2, hand2_bet, _ = player_turn(hand2, hand2_bet, deck, money, allow_split=False, allow_surrender=False) 

    dealer_cards = dealer_turn(dealer_cards, deck) 

    print("\nHand 1:")
    result1 = determine_winner(hand1, dealer_cards, was_split=True)

    print("\nHand 2:")
    result2 = determine_winner(hand2, dealer_cards, was_split=True)

    return result1, result2, hand1_bet, hand2_bet


def player_turn(player_cards, player_bet, deck, money, allow_split=True, allow_surrender=True):

    status = 'normal'

    while calculate_hand(player_cards) < 21:

        print(f"\nYour cards: {display_hand(player_cards)}")
        print(f"Total: {calculate_hand(player_cards)}")

        choice = get_player_choice()

        if choice == 1:
            player_cards = handle_hit(player_cards, deck)
            print(f"Player's cards: {display_hand(player_cards)}")
            print(f"Player's Hand: {calculate_hand(player_cards)}")

            # Check if player hand is busted:
            if is_busted(player_cards):
                print("\n You busted! Your hand is over 21.")
                break
        
        elif choice == 2:
            break

        elif choice == 3:
            if len(player_cards) != 2:
                print("You can only double down on your first two cards.")
                continue
            player_cards, player_bet = hand_double_down(player_cards, deck, player_bet, money)

            # Check if player hand is busted:
            if is_busted(player_cards):
                print("\n You busted! Your hand is over 21.")
            else:
                print(f"\nPlayer's Hand: {calculate_hand(player_cards)}")
            break  #Since the turn should end after doubling down.
    
        elif choice == 4:
            
            if not allow_split:
                print("Split is not available.")
                continue

            if len(player_cards) != 2:
                print("You can only split your initial two cards.")
                continue

            if player_cards[0][0] == player_cards[1][0]:
                status = 'split'
                return player_cards, player_bet, status
            else:
                print("You can't split these cards.")

        elif choice == 5: #Surrender

            if not allow_surrender:
                print("Surrender is not available.")
                continue

            print("You surrendered.")
            status = 'surrender'
            return player_cards, player_bet, status
        
    return player_cards, player_bet, status


def dealer_turn(dealer_cards, deck):
    # before hit
    print(f"\nDealer reveals: {display_hand(dealer_cards)}")
    print(f"Dealer total: {calculate_hand(dealer_cards)}")

    while calculate_hand(dealer_cards) < 17:
        dealer_cards = handle_hit(dealer_cards, deck)
        # after hit
        print(f"\nDealer's Hand: {display_hand(dealer_cards)}")
        print(f"Dealer total: {calculate_hand(dealer_cards)}")

    return dealer_cards


def is_blackjack(cards, was_split=False):
    return len(cards) == 2 and calculate_hand(cards) == 21 and not was_split


def determine_winner(player_cards, dealer_cards, was_split=False):

    player_blackjack = is_blackjack(player_cards, was_split)
    dealer_blackjack = is_blackjack(dealer_cards)

    player_total = calculate_hand(player_cards)
    dealer_total = calculate_hand(dealer_cards)

    # Both blackjack
    if player_blackjack and dealer_blackjack:
        print("Both have blackjack! Tie.")
        return "tie"
    
    # Player blackjack
    elif player_blackjack:
        print("Blackjack! Player wins!")
        return "blackjack"
    
    # Dealer blackjack
    elif dealer_blackjack:
        print("Dealer has blackjack! Dealer wins!")
        return "lose"

    # Normal
    if is_busted(player_cards):
        print("Player busted! Dealer wins!")
        return "lose"
    
    elif is_busted(dealer_cards):
        print(f"Dealer busted! Player wins!")
        return "win"
    
    elif dealer_total < player_total:
        print(f"Player wins with {player_total} !!")
        return "win"
    
    elif dealer_total > player_total:
        print(f"Dealer wins with {dealer_total} !!")
        return "lose"
    
    else:
        print("It's a tie.")
        return "tie"


def get_bet(money):
    while True:
        try:
            bet = int(input(f"Enter bet: "))
            if 1 <= bet <= money:
                return bet

        except ValueError:
            pass

        print("Invalid bet.")


def play_again():
    while True:
        choice = input("\nPlay again? (y/n): ").lower()

        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print("Invalid choice.")


def main():

    welcome()

    money = 100 # Default starting money

    while money > 0:

        print(f"\nBalance: ${money}")

        deck = create_deck()
        shuffle_deck(deck)

        player_bet = get_bet(money)
        player_cards, dealer_cards = deal_initial_cards(deck)
        
        # Check blackjack before player or dealer turn
        if is_blackjack(player_cards) or is_blackjack(dealer_cards):

            result = determine_winner(player_cards, dealer_cards)

            if result == "blackjack":
                money += player_bet * 1.5
            elif result == "lose":
                money -= player_bet

            print(f"\nNew balance: ${money}")

            if not play_again():
                print("Thanks for playing!")
                break

            continue

        player_cards, player_bet, status = player_turn(player_cards, player_bet, deck, money)

        if status == 'split':

            split_result = play_split(player_cards, dealer_cards, player_bet, deck, money)
            if split_result is None:
                continue

            result1, result2, hand1_bet, hand2_bet = split_result

            # Money Update
            print(f"Hand 1 result: {result1}")
            print(f"Hand 2 result: {result2}")

            if result1 == "win":
                money += hand1_bet
            elif result1 == 'lose':
                money -= hand1_bet

            if result2 == "win":
                money += hand2_bet
            elif result2 == 'lose':
                money -= hand2_bet

            # Print new balance
            print(f"\nNew balance: ${money}")

            # Ask" Play again?
            if not play_again():
                print("Thanks for playing!")
                break

            continue
        
        elif status == 'surrender':
            # Update money
            money -= player_bet // 2
            print(f"You lost half your bet. ${player_bet // 2}")
            # Print new balance
            print(f"New balance: ${money}")

            # Ask" Play again?
            if not play_again():
                print("Thanks for playing!")
                break
            continue
        
        # Don't play dealer if player busted
        if not is_busted(player_cards):
            dealer_cards = dealer_turn(dealer_cards, deck)
        else:
            print(f"\nDealer reveals: {display_hand(dealer_cards)}")

        result = determine_winner(player_cards, dealer_cards)

        # Money Update
        if result == "blackjack":
            money += player_bet * 1.5
        elif result == "win":
            money += player_bet
        elif result == "lose":
            money -= player_bet

        # Print Updated Balance
        print(f"\nNew balance: ${money}")

        # Ask: Play again?
        if not play_again():
            print("Thanks for playing!")
            break
    # Game Over Message
    print("Game over!")

main()
        
