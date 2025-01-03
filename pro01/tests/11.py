test = {
  'name': 'Problem 11',
  'points': 100,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> swine_strategy(40, 51, threshold=10, num_rolls=5)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> swine_strategy(40, 53, threshold=10, num_rolls=6)
          6
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> swine_strategy(44, 35, threshold=7, num_rolls=7)
          7
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> swine_strategy(44, 53, threshold=8, num_rolls=2)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> from tests.check_strategy import check_strategy
          >>> check_strategy(swine_strategy)
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
