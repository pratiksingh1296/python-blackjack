import random


dealer_hand = 0
player_hand = 0

def welcome():
       print("\nWelcome to the Blackjack Game! ")
       print("\nThe goal of the game is to get as close to 21 as possible without going over.")
       print("\nThe dealer will deal two cards to you and two cards to themselves. One of the dealer's cards will be face up and the other will be face down.")
       print("\nYou can choose to hit (get another card), stand (keep your current hand), double down (double your bet and get one more card), split (if you have two cards of the same value, you can split them into two hands), or surrender (give up half your bet and end the game).")
       print("\nIf you go over 21, you bust and lose the game. If the dealer goes over 21, they bust and you win. If neither of you busts, the hand with the higher total wins.")
       print("\nGood luck!")

welcome()


print("\nThe Dealer starts dealing cards: ")
card_delt1 = random.choice(range(1,12)) 
card_delt2 = random.choice(range(1,12)) 
dealer_card1 = random.choice(range(1,12))
dealer_card2 = random.choice(range(1,12))
print(f"\nThe two cards delt to player: {card_delt1} & {card_delt2} \n The Cards Delt to dealer are {dealer_card1} & X ")

player_hand = card_delt1 + card_delt2 
dealer_hand = dealer_card1 + dealer_card2

print(f"\nPlayer's Hand: {player_hand} ")
print(f"\nDealer's shows: {dealer_card1} ")

player_bet = int(input("\n Please enter bet amount: "))
                 

while player_hand < 21 and dealer_hand < 21:  #As long as player's & dealer's hands are less than 21.
        
        print("\n Choose what to do: ")
        choice = int(input("\n1. Hit  2. Stand  3. Double Down  4. Split  5.Surrender\n")) 
        
        if choice == 1:  #Hit
                card_delt = random.choice(range(1,12))
                player_hand += card_delt
                print(f"\nPlayer's Hand: {player_hand}")
            
                #Check if player has busted hand after hitting.           
                if player_hand > 21:
                 print("\n You busted! Your hand is over 21.")
                 break
        
        elif choice == 2: #Stand
                
                if dealer_hand < 17:
                       dealer_card = random.choice(range(1,12))
                       dealer_hand += dealer_card
                       print(f"\nDealer's Hand: {dealer_hand}")
                       if dealer_hand > 21:
                              print(f"\nDealer busted! Player wins!")
                       elif dealer_hand == 21:
                              break
                       
                elif dealer_hand >= 17:
                       print(f"\nDealer Stands: {dealer_hand}")  
                        
                
        elif choice == 3: #Double Down
                player_bet *= 2
                print(f"\nYou have doubled your bet to {player_bet}!")
    
                card_delt = random.choice(range(1,12))
                player_hand += card_delt

                if player_hand > 21:
                       print("\nYou busted! Your hand is over 21.")
                else:
                       print(f"\nPlayer's Hand: {player_hand}")
                break #Since the turn should end after doubling down.

        #Hand split logic  
        elif choice == 4:
                if card_delt1 == card_delt2:
                        print("You've split your hand: ")
        
                        #Dealing new cards for both hands
                        hand1 = card_delt1
                        hand2 = card_delt2
                        card_delt1 = random.choice(range(1,12))
                        card_delt2 = random.choice(range(1,12))
                        hand1 += card_delt1
                        hand2 += card_delt2      

                        print(f"1.First Hand: {hand1} , 2.Second Hand: {hand2}")

                        #Allow player to choose which hand to play first

                        play_hand = int(input(f"Which hand would you like to play first ? 1.First Hand: {hand1} , 2.Second Hand: {hand2}"))

                        if play_hand == 1:
                               current_hand = hand1
                               print(f"\nYou've chosen to play the first hand: {current_hand} ")

                        elif play_hand == 2:
                               current_hand = hand2
                               print(f"\nYou've chosen to play the second hand: {current_hand} ")
                        else:
                               print("Invalid Input.")      
                               continue        #Continue the loop but skip current

                        while current_hand < 21:
                               choice = int(input("\n1. Hit , 2. Stand:"))
                               
                               if choice == 1:
                                      card_delt = random.choice(range(1,12))
                                      current_hand += card_delt
                                      print(f"\nYour Hand: {current_hand}")

                                      if current_hand > 21:
                                             print(f"You busted! {current_hand} is over 21")
                                             break 
                                      
                               elif choice == 2:
                                      print(f"\nYou choose to stand with {current_hand}")
                                      break
                               
                               else:
                                      print("\nInvalid input, Please choose either 1 for Hit or 2 for Stand.")

                        if play_hand == 1:
                               current_hand = hand2
                        elif play_hand == 2:
                               current_hand = hand1
                                      
                        #Playing with other hand now
                                      
                        print(f"\nNow you are playing with other hand: {current_hand}")

                        while current_hand < 21:   
                               choice = int(input("\n1. Hit , 2. Stand:"))

                               if choice == 1:
                                      card_delt = random.choice(range(1,12))
                                      current_hand += card_delt
                                      print(f"\nYour Hand: {current_hand}")
                                      if current_hand > 21:
                                             print(f"You busted! {current_hand} is over 21")
                                             break
                               elif choice == 2:
                                      print(f"\nYou choose to stand with {current_hand}")
                                      break
                               else:
                                      print("\nInvalid input, Please choose either 1 for Hit or 2 for Stand.")
                else:
                       print("\n You can only split cards if both of them are the same.") #Error O/P
                                         

        elif choice == 5: #Surrender
                print("\n Thanks for playing. ")
                break #End the game


#Dealer moves after player has done with theirs & also checking win conditions

if player_hand <= 21:
       while dealer_hand < 17:
              dealer_card = random.choice(range(1,12))
              dealer_hand += dealer_card
              print(f"\nDealer's Hand: {dealer_hand}")
    
       if dealer_hand > 21:
              print(f"\nDealer busted! Player wins!")
       elif dealer_hand == player_hand:
              print(f"It's a tie.")
       elif dealer_hand < player_hand:
              print(f"Player wins with {player_hand}")
       elif dealer_hand > player_hand:
              print(f"Dealer wins with {dealer_hand}")