test = {
  'name': 'Problem 10',
  'points': 100,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> picky_strategy(40, 51, threshold=7, num_rolls=2)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> picky_strategy(40, 53, threshold=7, num_rolls=2)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> picky_strategy(40, 51, threshold=12, num_rolls=5)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> picky_strategy(40, 52, threshold=7, num_rolls=2)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> picky_strategy(20, 0, threshold=1, num_rolls=4)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> from tests.check_strategy import check_strategy
          >>> check_strategy(picky_strategy)
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
