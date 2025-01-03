test = {
  'name': 'Problem 7',
  'points': 400,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> is_always_roll(always_roll_5)
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> is_always_roll(always_roll(3))
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> is_always_roll(catch_up)
          False
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
