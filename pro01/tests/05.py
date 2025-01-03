test = {
  'name': 'Problem 5',
  'points': 400,
  'suites': [
    {
      'cases': [
        {
          'answer': 'While score0 and score1 are both less than goal',
          'choices': [
            'While score0 and score1 are both less than goal',
            'While at least one of score0 or score1 is less than goal',
            'While score0 is less than goal',
            'While score1 is less than goal'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': r"""
          The variables score0 and score1 are the scores for Player 0
          and Player 1, respectively. Under what conditions should the
          game continue?
          """
        },
        {
          'answer': 'A function that returns the number of dice a player will roll',
          'choices': [
            'The number of dice a player will roll',
            'A function that returns the number of dice a player will roll',
            "A player's desired turn outcome"
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'What is a strategy in the context of this game?'
        },
        {
          'answer': 'strategy1(score1, score0)',
          'choices': [
            'strategy1(score1, score0)',
            'strategy1(score0, score1)',
            'strategy1(score1)',
            'strategy1(score0)'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': r"""
          If strategy1 is Player 1's strategy function, score0 is
          Player 0's current score, and score1 is Player 1's current
          score, then which of the following demonstrates correct
          usage of strategy1?
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=69484, score0=15, score1=10, goal=27)
          >>> print(turns[0])
          Start scores = (15, 10).
          Player 0 rolls 8 dice and gets outcomes [2, 1, 6, 6, 6, 5, 4, 4].
          End scores = (10, 16)
          >>> print(turns[1])
          Start scores = (10, 16).
          Player 1 rolls 3 dice and gets outcomes [4, 2, 4].
          End scores = (10, 26)
          >>> print(turns[2])
          Start scores = (10, 26).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (19, 26)
          >>> print(turns[3])
          Start scores = (19, 26).
          Player 1 rolls 10 dice and gets outcomes [6, 2, 1, 1, 5, 5, 2, 6, 1, 4].
          End scores = (19, 27)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=42415, score0=3, score1=3, goal=18)
          >>> print(turns[0])
          Start scores = (3, 3).
          Player 0 rolls 3 dice and gets outcomes [5, 5, 4].
          End scores = (17, 3)
          >>> print(turns[1])
          Start scores = (17, 3).
          Player 1 rolls 8 dice and gets outcomes [3, 1, 3, 3, 2, 3, 1, 5].
          End scores = (4, 17)
          >>> print(turns[2])
          Start scores = (4, 17).
          Player 0 rolls 3 dice and gets outcomes [1, 6, 4].
          End scores = (5, 17)
          >>> print(turns[3])
          Start scores = (5, 17).
          Player 1 rolls 7 dice and gets outcomes [5, 2, 5, 3, 6, 4, 1].
          End scores = (5, 18)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=1568, score0=3, score1=29, goal=50)
          >>> print(turns[0])
          Start scores = (3, 29).
          Player 0 rolls 1 dice and gets outcomes [4].
          End scores = (7, 29)
          >>> print(turns[1])
          Start scores = (7, 29).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (7, 44)
          >>> print(turns[2])
          Start scores = (7, 44).
          Player 0 rolls 9 dice and gets outcomes [4, 1, 4, 6, 3, 2, 6, 3, 6].
          End scores = (8, 44)
          >>> print(turns[3])
          Start scores = (8, 44).
          Player 1 rolls 1 dice and gets outcomes [2].
          End scores = (8, 46)
          >>> print(turns[4])
          Start scores = (8, 46).
          Player 0 rolls 9 dice and gets outcomes [3, 4, 1, 4, 5, 2, 3, 6, 1].
          End scores = (46, 9)
          >>> print(turns[5])
          Start scores = (46, 9).
          Player 1 rolls 8 dice and gets outcomes [2, 3, 6, 1, 6, 1, 4, 3].
          End scores = (46, 10)
          >>> print(turns[6])
          Start scores = (46, 10).
          Player 0 rolls 1 dice and gets outcomes [3].
          End scores = (10, 49)
          >>> print(turns[7])
          Start scores = (10, 49).
          Player 1 rolls 5 dice and gets outcomes [3, 1, 5, 5, 4].
          End scores = (10, 50)
          >>> print(turns[8])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=72434, score0=8, score1=45, goal=67)
          >>> print(turns[0])
          Start scores = (8, 45).
          Player 0 rolls 8 dice and gets outcomes [6, 1, 6, 6, 6, 3, 5, 4].
          End scores = (45, 9)
          >>> print(turns[1])
          Start scores = (45, 9).
          Player 1 rolls 9 dice and gets outcomes [3, 3, 4, 4, 3, 2, 5, 5, 1].
          End scores = (45, 10)
          >>> print(turns[2])
          Start scores = (45, 10).
          Player 0 rolls 7 dice and gets outcomes [6, 4, 3, 3, 5, 6, 6].
          End scores = (78, 10)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=53739, score0=54, score1=50, goal=58)
          >>> print(turns[0])
          Start scores = (54, 50).
          Player 0 rolls 9 dice and gets outcomes [4, 3, 5, 6, 3, 2, 3, 4, 2].
          End scores = (86, 50)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=63941, score0=1, score1=44, goal=73)
          >>> print(turns[0])
          Start scores = (1, 44).
          Player 0 rolls 6 dice and gets outcomes [2, 1, 1, 5, 1, 6].
          End scores = (2, 44)
          >>> print(turns[1])
          Start scores = (2, 44).
          Player 1 rolls 9 dice and gets outcomes [5, 2, 3, 5, 1, 1, 5, 5, 1].
          End scores = (2, 45)
          >>> print(turns[2])
          Start scores = (2, 45).
          Player 0 rolls 8 dice and gets outcomes [5, 4, 3, 4, 3, 1, 2, 2].
          End scores = (3, 45)
          >>> print(turns[3])
          Start scores = (3, 45).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (3, 52)
          >>> print(turns[4])
          Start scores = (3, 52).
          Player 0 rolls 5 dice and gets outcomes [2, 6, 5, 5, 2].
          End scores = (23, 52)
          >>> print(turns[5])
          Start scores = (23, 52).
          Player 1 rolls 7 dice and gets outcomes [2, 3, 2, 1, 4, 3, 6].
          End scores = (23, 53)
          >>> print(turns[6])
          Start scores = (23, 53).
          Player 0 rolls 2 dice and gets outcomes [6, 4].
          End scores = (33, 53)
          >>> print(turns[7])
          Start scores = (33, 53).
          Player 1 rolls 1 dice and gets outcomes [5].
          End scores = (33, 58)
          >>> print(turns[8])
          Start scores = (33, 58).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (40, 58)
          >>> print(turns[9])
          Start scores = (40, 58).
          Player 1 rolls 7 dice and gets outcomes [3, 3, 4, 3, 2, 6, 5].
          End scores = (40, 84)
          >>> print(turns[10])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hog, importlib
      >>> import tests.play_utils
      """,
      'teardown': r"""
      
      """,
      'type': 'doctest'
    }
  ]
}
