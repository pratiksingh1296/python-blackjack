# Blackjack Game (Python)

## Overview

This is a command-line Blackjack game written in Python. The game follows standard Blackjack rules and includes features such as betting, doubling down, splitting pairs, surrendering, and bankroll management.

## Features

* Standard 52-card deck
* Card shuffling before each game
* Player betting system
* Hit and Stand options
* Double Down
* Split pairs
* Surrender
* Automatic Ace value adjustment (1 or 11)
* Dealer follows standard rule of hitting until 17
* Blackjack detection
* Running balance that updates after each round

## Requirements

* Python 3.x

No external libraries are required. The game only uses Python's built-in `random` module.

## How to Run

1. Save the program as `blackjack.py`.
2. Open a terminal or command prompt.
3. Navigate to the project directory.
4. Run the program:

```bash
python blackjack.py
```

## How to Play

1. Start with a balance of **$100**.
2. Enter your bet for each round.
3. You and the dealer are dealt two cards.
4. Choose one of the following actions:

   * **Hit** – Draw another card.
   * **Stand** – Keep your current hand.
   * **Double Down** – Double your bet and receive one final card.
   * **Split** – Split matching cards into two separate hands.
   * **Surrender** – End the round and lose only half your bet.
5. The dealer reveals their hidden card and plays according to Blackjack rules.
6. Your balance is updated based on the outcome.
7. Continue playing until you choose to quit or your balance reaches $0.

## Project Structure

* `create_deck()` – Creates a standard deck of cards.
* `shuffle_deck()` – Randomizes the deck.
* `deal_card()` – Deals one card.
* `calculate_hand()` – Calculates the total value of a hand.
* `player_turn()` – Handles player actions.
* `dealer_turn()` – Handles dealer actions.
* `determine_winner()` – Determines the winner of each round.
* `main()` – Controls the overall game flow.

## Rules

* Number cards are worth their face value.
* Face cards (J, Q, K) are worth 10.
* Aces count as 11 unless doing so would cause a bust, in which case they count as 1.
* The dealer must hit until reaching at least 17.
* A natural Blackjack (Ace + 10-value card) wins unless the dealer also has Blackjack.

## Author

Developed as a Python command-line Blackjack game for practicing programming concepts such as functions, loops, conditional statements, and game logic.
