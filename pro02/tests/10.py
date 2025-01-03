test = {
  'name': 'Problem 10',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> p0 = [2, 2, 3]
          >>> p1 = [6, 1, 2]
          >>> fastest_words(game(['What', 'great', 'luck'], [p0, p1]))
          [['What'], ['great', 'luck']]
          >>> p0 = [2, 2, 3]
          >>> p1 = [6, 1, 3]
          >>> fastest_words(game(['What', 'great', 'luck'], [p0, p1]))  # with a tie, choose the first player
          [['What', 'luck'], ['great']]
          >>> p2 = [4, 3, 1]
          >>> fastest_words(game(['What', 'great', 'luck'], [p0, p1, p2]))
          [['What'], ['great'], ['luck']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p0 = [5, 1, 3]
          >>> p1 = [4, 1, 6]
          >>> fastest_words(game(['Just', 'have', 'fun'], [p0, p1]))
          [['have', 'fun'], ['Just']]
          >>> p0  # input lists should not be mutated
          [5, 1, 3]
          >>> p1
          [4, 1, 6]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3], [5]]
          >>> fastest_words(game(['smopple'], p))
          [['smopple'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[]]
          >>> fastest_words(game([], p))
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5], [2], [4]]
          >>> fastest_words(game(['seeingly'], p))
          [[], ['seeingly'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 1, 2, 3, 4], [1, 5, 3, 4, 1], [5, 1, 5, 2, 3]]
          >>> fastest_words(game(['reundergo', 'unweld', 'handgun', 'hydrometra', 'recessionary'], p))
          [['unweld', 'handgun'], ['reundergo', 'recessionary'], ['hydrometra']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[], [], []]
          >>> fastest_words(game([], p))
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 1, 2]]
          >>> fastest_words(game(['prebeleve', 'upanishadic', 'ftp'], p))
          [['prebeleve', 'upanishadic', 'ftp']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 3, 5, 2, 4], [2, 4, 5, 1, 2], [1, 5, 2, 1, 3]]
          >>> fastest_words(game(['supplies', 'underivedly', 'henter', 'undeserving', 'uncope'], p))
          [['underivedly'], ['undeserving', 'uncope'], ['supplies', 'henter']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import game, fastest_words
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> test.swap_implementations(cats) # Make sure the abstraction barrier isn't crossed!
          >>> p0 = [2, 2, 3]
          >>> p1 = [6, 1, 2]
          >>> cats.fastest_words(cats.game(['What', 'great', 'luck'], [p0, p1]))
          [['What'], ['great', 'luck']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import cats
      >>> import tests.abstraction_check as test # Make sure the abstraction barrier isn't crossed!
      """,
      'teardown': r"""
      >>> test.restore_implementations(cats)
      """,
      'type': 'doctest'
    }
  ]
}
