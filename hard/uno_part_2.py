"""
Uno (Part 2)

This problem is a continuation of Uno Part 1 (although you don't need to complete that problem to complete this one).

It's your turn to play again. Create a function that takes as its arguments (1) your hand (a list of cards), and (2) the face-up card. In Uno, you are able to play a card from your hand if either:

One of the card colors in your hand matches the face-up card's color.
One of the card numbers in your hand matches the face-up card's number.
Write a function that will return:

"Uno!" if after playing your card, you are left with a single card.
"You won!" if after playing your card, you are left with zero cards (an empty list).
"Keep going..." otherwise.
Examples
decision(["yellow 3", "red 3"], "red 10") ➞ "Uno!"

decision(["blue 1"], "blue 5") ➞ "You won!"

decision(["blue 1", "green 2", "yellow 4", "red 2"], "blue 5") ➞ "Keep going..."
Notes
There will not be more than one playable card in each hand.
"""

from unittest import TestCase


def decision(hand, face_up_card):
    face_up_color, face_up_number = face_up_card.split()
    playable_card = None

    for card in hand:
        color, number = card.split()
        if color == face_up_color or number == face_up_number:
            playable_card = card
            break

    if playable_card:
        hand.remove(playable_card)

    if len(hand) == 1:
        return "Uno!"
    elif len(hand) == 0:
        return "You won!"
    else:
        return "Keep going..."


TestCase().assertEqual(decision(['yellow 3', 'red 3'], 'red 10'), "Uno!")
TestCase().assertEqual(decision(['blue 1'], 'blue 5'), "You won!")
TestCase().assertEqual(decision(['red 1'], 'blue 5'), "Uno!")
TestCase().assertEqual(decision(['red 1', 'blue 10'], 'blue 5'), "Uno!")
TestCase().assertEqual(decision(['red 1', 'blue 10', 'green 7'], 'blue 5'), "Keep going...")
TestCase().assertEqual(decision(['red 1', 'green 7'], 'green 2'), "Uno!")
TestCase().assertEqual(decision(['green 7'], 'green 2'), "You won!")
TestCase().assertEqual(decision(['blue 7'], 'green 7'), "You won!")
TestCase().assertEqual(decision(['blue 1', 'green 2', 'yellow 4', 'red 2'], 'blue 5'), "Keep going...")
