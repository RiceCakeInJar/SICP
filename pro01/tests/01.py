test = {
  'name': 'Problem 1',
  'points': 300,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> roll_dice(2, make_test_dice(4, 6, 1))
          10
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> roll_dice(3, make_test_dice(4, 6, 1))
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> roll_dice(4, make_test_dice(2, 2, 3))
          9
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> a = roll_dice(4, make_test_dice(1, 2, 3))
          >>> a # check that the value is being returned, not printed
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> counted_dice = make_test_dice(4, 1, 2, 6)
          >>> roll_dice(3, counted_dice)
          1
          >>> # Make sure you call dice exactly num_rolls times!
          >>> # If you call it fewer or more than that, it won't be at the right spot in the cycle for the next roll
          >>> # Note that a return statement within a loop ends the loop
          >>> roll_dice(1, counted_dice)
          6
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> roll_dice(9, make_test_dice(6))
          54
          >>> roll_dice(7, make_test_dice(2, 2, 2, 2, 2, 2, 1))
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
