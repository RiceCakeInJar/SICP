""" Project 1: The Game of Hog. """
from dice import six_sided, make_test_dice
from math import floor, sqrt

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.


######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome.
    """
    # BEGIN PROBLEM 1
    ans = 0
    i = 0
    condition = False
    while i < num_rolls:
        tr = dice()
        if tr == 1:
            condition = True
            i += 1
        else:
            ans += tr
            i += 1
    if condition:
        return 1
    else:
        return ans

    # END PROBLEM 1


def picky_piggy(opponent_score):
    """Return the points scored from rolling 0 dice accodring to Picky Piggy.

    opponent_score:  The total score of the other player.
    """
    # BEGIN PROBLEM 2
    num_gewei = opponent_score%10
    tr01 = opponent_score//10
    if opponent_score>=100:
        num_shiwei = tr01%10
    else:
        num_shiwei = tr01
    return 2*abs(num_shiwei-num_gewei)+1
    # END PROBLEM 2


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Return the points scored for the turn rolling NUM_ROLLS dices when the
    opponent has OPPONENT_SCORE points.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the other player.
    dice:            A function that simulates a single dice roll outcome.
    """
    # BEGIN PROBLEM 3
    if num_rolls == 0:
        return picky_piggy(opponent_score)
    else:
        return roll_dice(num_rolls, dice)
    # END PROBLEM 3


def swine_swap(score):
    """Return whether the players' scores will be swapped due to Swine Swap.

    score:           The total score of the current player.

    Hint: for this problem, you will find the math function sqrt useful.
    >>> sqrt(9)
    3.0
    >>> floor(sqrt(9))
    3
    >>> floor(sqrt(8))
    2
    """
    # BEGIN PROBLEM 4
    if sqrt(score) == floor(sqrt(score)):
        return True
    else:
        return False
    # END PROBLEM 4


def play(strategy0, strategy1,
         score0=0, score1=0, dice=six_sided, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with Player
    0's score first, and Player 1's score second.

    E.g., play(always_roll_5, always_roll_5) simulates a game in which both 
    players always choose to roll 5.

    A strategy function, such as always_roll_5, takes the current player's
    score and the opponent's score, and returns the number of dice that the
    corresponding player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first.
    strategy1:  The strategy function for Player 1, who plays second.
    score0:     Starting score for Player 0
    score1:     Starting score for Player 1
    dice:       A function of zero arguments that simulates a dice roll.
    goal:       The game ends and someone wins when this score is reached.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    while score0<goal and score1<goal:
        if who == 0:
            score0 += take_turn(strategy0(score0,score1),score1,dice)
            if swine_swap(score0):
                tr = score0
                score0 = score1
                score1 = tr
            who = 1
        if who == 1:
            score1 +=take_turn(strategy1(score1,score0),score0,dice)
            if swine_swap(score0):
                tr = score1
                score1 = score0
                score0 = tr
            who = 0
    return score0,score1
    # END PROBLEM 5


#######################
# Phase 2: Strategies #
#######################

def always_roll_5(score, opponent_score):
    """A strategy of always rolling 5 dice, regardless of the player's score or
    the oppononent's score.
    """
    return 5


def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    >>> strategy = always_roll(3)
    >>> strategy(0, 0)
    3
    >>> strategy(99, 99)
    3
    """
    assert n >= 0 and n <= 10
    # BEGIN PROBLEM 6
    def fool(a,b):
        return n
    return fool
    # END PROBLEM 6


def catch_up(score, opponent_score):
    """A player strategy that always rolls 5 dice unless the opponent
    has a higher score, in which case 6 dice are rolled.

    >>> catch_up(9, 4)
    5
    >>> strategy(17, 18)
    6
    """
    if score < opponent_score:
        return 6  # Roll one more to catch up
    else:
        return 5


def is_always_roll(strategy, goal=GOAL_SCORE):
    """Return whether strategy always chooses the same number of dice to roll.

    >>> is_always_roll(always_roll_5)
    True
    >>> is_always_roll(always_roll(3))
    True
    >>> is_always_roll(catch_up)
    False
    """
    # BEGIN PROBLEM 7
    a = 0
    b = 0
    condition = True
    while a<goal and b<goal:
        test0 = strategy(a,b)
        a +=1
        test1 = strategy(a,b)
        if test0 != test1:
            condition = False
            return condition
        elif a == goal-1:
            b+=1
            test2 = strategy(a,b)
            a = 0
            if test1 != test2:
                condition = False
                return condition
    return condition


    # END PROBLEM 7


def make_averaged(original_function, trials_count=1000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    called TOTAL_SAMPLES times.

    To implement this function, you will have to use *args syntax.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(roll_dice, 40)
    >>> averaged_dice(1, dice)  # The avg of 10 4's, 10 2's, 10 5's, and 10 1's
    3.0
    """
    # BEGIN PROBLEM 8
    def ans(*tmp):
        res = []
        i = 1
        while i <= trials_count:
            res.append(original_function(*tmp))
            i += 1
        tr = sum(res)
        return tr/trials_count
    return ans
    # END PROBLEM 8


def max_scoring_num_rolls(dice=six_sided, total_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn score
    by calling roll_dice with the provided DICE a total of TOTAL_SAMPLES times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    tr1=[]
    i = 1
    while i<=10:
        tr1.append(make_averaged(roll_dice, total_samples)(i,dice))
        i+=1
    return tr1.index(max(tr1))+1

    # END PROBLEM 9


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(6)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    six_sided_max = max_scoring_num_rolls(six_sided)
    print('Max scoring num rolls for six-sided dice:', six_sided_max)

    print('always_roll(6) win rate:',
          average_win_rate(always_roll(6)))  # near 0.5
    print('catch_up win rate:', average_win_rate(catch_up))
    print('always_roll(3) win rate:', average_win_rate(always_roll(3)))
    print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    print('picky_strategy win rate:', average_win_rate(picky_strategy))
    print('swine_strategy win rate:', average_win_rate(swine_strategy))
    print('final_strategy win rate:', average_win_rate(final_strategy))
    "*** You may add additional experiments as you wish ***"


def picky_strategy(score, opponent_score, threshold=8, num_rolls=6):
    """This strategy returns 0 dice if that gives at least THRESHOLD points,
    and returns NUM_ROLLS otherwise.
    """
    # BEGIN PROBLEM 10
    if picky_piggy(opponent_score)>=threshold:
        return 0
    return num_rolls
    # END PROBLEM 10


def swine_strategy(score, opponent_score, threshold=8, num_rolls=6):
    """This strategy returns 0 dice when this would gives the player at least
    THRESHOLD points in this turn. Otherwise, it returns NUM_ROLLS.
    """
    # BEGIN PROBLEM 11
    if swine_swap(score+picky_piggy(opponent_score)) and opponent_score-score>threshold:
        return 0
    elif picky_piggy(opponent_score)>threshold and not swine_swap(score+picky_piggy(opponent_score)):
        return 0
    return num_rolls
    # END PROBLEM 11


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    
    """
    # BEGIN PROBLEM 12
    return 6  # Remove this line once implemented.
    # END PROBLEM 12


##########################
# Command Line Interface #
##########################

# NOTE: Functions in this section do not need to be changed. They use features
# of Python not yet covered in the course.


if __name__ == '__main__':
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
