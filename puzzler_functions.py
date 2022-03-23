"""CSC108: Fall 2020 -- Assignment 1: Phrase Puzzler 

This code is provided solely for the personal and private use of students 
taking the CSC108 course at the University of Toronto. Copying for purposes 
other than this use is expressly prohibited. All forms of distribution of 
this code, whether as given or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2020 Mario Badr, Jennifer Campbell, Tom Fairgrieve, Diane Horton, 
Michael Liut, Jacqueline Smith, and Anya Tafliovich.
"""

# The next several lines contain 14 constants for you to use in your code.
# You must use these constants instead of the values they refer to. 
# E.g. Use HIDDEN instead of '^'. You may not need to use all of the 
# constants provided.

# points earned on each occurrence of a correctly guessed consonant
CONSONANT_POINTS = 1

# cost of buying a vowel, does not depend on the number of occurrences
VOWEL_PRICE = 1

# players' names
PLAYER_ONE = 'Player One'
PLAYER_TWO = 'Player Two'

# menu options
CONSONANT = 'C'  # guess a consonant
VOWEL = 'V'      # buy a vowel
SOLVE = 'S'      # try to solve the puzzle
QUIT = 'Q'       # quit the game

# symbol used for hidden characters
HIDDEN = '^'

# Game types
HUMAN = 'H-'             # one player, human
HUMAN_HUMAN = 'HH'       # two players, both human
HUMAN_COMPUTER = 'HC'    # two players, human and computer

# all consonants and all vowels
ALL_CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
ALL_VOWELS = 'aeiou'


# This function is complete and you must not change it.
def is_game_over(puzzle: str, view: str, move: str) -> bool:
    """Return True if and only if puzzle and view are a winning
    combination or move is QUIT.

    >>> is_game_over('apple', 'a^^le', 'V')
    False
    >>> is_game_over('apple', 'a^^le', 'Q')
    True
    >>> is_game_over('apple', 'apple', 'S')
    True
    """

    return move == QUIT or puzzle == view


def is_one_player_game(game_type: str) -> bool:
    """Return True if and only if game_type is a one-player game. 
        
    >>> is_one_player_game('H-')
    True
    >>> is_one_player_game('HH')
    False
    >>> is_one_player_game('HC')
    False
    """

    return bool(game_type == HUMAN)


def is_human(current_player: str, game_type: str) -> bool:
    """Return True if and only if current_player represents a human in a
    game of type game_type.

    >>> is_human('Player One', 'H-')
    True
    >>> is_human('Player One', 'HH')
    True
    >>> is_human('Player Two', 'HH')
    True
    >>> is_human('Player One', 'HC')
    True
    >>> is_human('Player Two', 'HC')
    False
    """
    if current_player == PLAYER_TWO and game_type == HUMAN_COMPUTER:
        return False
    else:
        return True

    
def current_player_score(player_one_score: int, player_two_score: int, 
                         current_player: str) -> int:
    """Return the score of the current_player.
    
    >>>current_player_score(1, 2, 'Player One')
    1
    >>>current_player_score(1, 3, 'Player Two')
    3
    """
    if current_player == PLAYER_ONE:
        return player_one_score
    elif current_player == PLAYER_TWO:
        return player_two_score
    return None

def is_bonus_letter(lowercase_letter: str, phrase_puzzle: str, 
                    current_view: str) -> bool:
    """Return True if and only if the first argument is a bonus letter that are 
    consonants that are currently hidden.
    
    >>>is_bonus_letter('p', 'apple', '^^^^^')
    True
    >>>is_bonus_letter('m', 'apple', '^^^^^')
    False
    >>>is_bonus_letter('a', 'apple', '^^^^^')
    False
    """
    
    return bool(lowercase_letter in phrase_puzzle and lowercase_letter in 
                ALL_CONSONANTS and lowercase_letter not in current_view)

def update_char_view(puzzle: str, view: str, index: int, guess: str) -> str:
    """Return what the updated view of the character should be: if the guess is
    correct, the character should be revealed; otherwise, the view should not 
    change.
    
    >>>update_char_view('apple', '^^^^^', 3, 'l')
    'l'
    >>>update_char_view('apple', '^^^^^', 3, 'm')
    '^'
    """
    if puzzle[index] == guess:
        return guess
    else:
        return view[index]
    return None

def calculate_score(current_score: int, occurences: int, 
                    current_move: str) -> int:
    """Return the new updated score.
    
    >>>calculate_score(1, 2, 'V')
    0
    >>>calculate_score(2, 1, 'C')
    3
    """
    if current_move == VOWEL:
        return current_score - VOWEL_PRICE
    elif current_move == CONSONANT:
        return current_score + occurences*CONSONANT_POINTS
    else:
        return None

def next_player(current_player: str, occurences: int, game_type: str) -> str:
    """Return the player to play in the next turn — player one or player two.
    
    >>>next_player('Player One', 1, 'H-')
    'Player One'
    >>>next_player('Player One', 0, 'HH')
    'Player Two'
    """
    if game_type == HUMAN:
        return current_player
    elif game_type == HUMAN_HUMAN or game_type == HUMAN_COMPUTER:
        if occurences > 0:
            return current_player
        elif occurences == 0:
            if current_player == PLAYER_ONE:
                return PLAYER_TWO
            elif current_player == PLAYER_TWO:
                return PLAYER_ONE
    return None

def is_hidden(index: int, puzzle: str, current_view: str) -> bool:
    """Return True if and only if the character at the given index is currently 
    hidden in the game.
    
    >>>is_hidden(0, 'apple', '^^^le')
    True
    >>>is_hidden(-1, 'aaple', '^^^le')
    False
    """
    return bool(puzzle[index] not in current_view)

def erase(letters: str, index: int) -> str:
    """Return the given letters with the character at the given index removed, 
    if the index is a valid index for that string of letters. Otherwise, it
    return the original string of letters unchanged. 
    
    >>>erase('apple', 2)
    aple
    >>>erase('apple', 3)
    appe 
    """
    if index >= 0:
        if len(letters) >= index + 1:
            return letters[:index]+letters[index+1:]
        else:
            return letters
    else:
        return letters

       
