test = {
  'name': 'Problem 9',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> p = [[1, 4, 6, 7], [0, 4, 6, 9]]
          >>> words = ['This', 'is', 'fun']
          >>> game = time_per_word(words, p)
          >>> get_all_words(game)
          ['This', 'is', 'fun']
          >>> get_all_times(game)
          [[3, 2, 1], [4, 2, 3]]
          >>> p = [[0, 2, 3], [2, 4, 7]]
          >>> game = time_per_word(['hello', 'world'], p)
          >>> get_word(game, word_index=1)
          'world'
          >>> game["times"]
          [[2, 1], [2, 3]]
          >>> time(game, player_num=0, word_index=1)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[49, 53, 57, 58, 61, 63], [57, 61, 65, 69, 74, 76], [58, 61, 62, 65, 69, 72]]
          >>> game = time_per_word(['gonalgia', 'smopple', 'modernizer', 'posticum', 'undiscernible'], p)
          >>> game['words']
          ['gonalgia', 'smopple', 'modernizer', 'posticum', 'undiscernible']
          >>> game['times']
          [[4, 4, 1, 3, 2], [4, 4, 4, 5, 2], [3, 1, 3, 4, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[47, 50, 54, 55, 58], [88, 90, 91, 96, 97], [91, 95, 99, 101, 103]]
          >>> game = time_per_word(['equalizing', 'phrymaceous', 'fluidimeter', 'seeds'], p)
          >>> game['words']
          ['equalizing', 'phrymaceous', 'fluidimeter', 'seeds']
          >>> game['times']
          [[3, 4, 1, 3], [2, 1, 5, 1], [4, 4, 2, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[91, 95, 99, 100, 103, 108, 113], [73, 75, 77, 80, 85, 89, 90]]
          >>> game = time_per_word(['unsupposable', 'seeingly', 'essexite', 'policemanism', 'havenet', 'ammonionitrate'], p)
          >>> game['words']
          ['unsupposable', 'seeingly', 'essexite', 'policemanism', 'havenet', 'ammonionitrate']
          >>> game['times']
          [[4, 4, 1, 3, 5, 5], [2, 2, 3, 5, 4, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[58, 62, 66, 67, 69, 72, 76]]
          >>> game = time_per_word(['unsanitariness', 'probatively', 'unabatedly', 'reundergo', 'unweld', 'handgun'], p)
          >>> game['words']
          ['unsanitariness', 'probatively', 'unabatedly', 'reundergo', 'unweld', 'handgun']
          >>> game['times']
          [[4, 4, 1, 2, 3, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[35, 36, 39, 43, 45, 50, 52]]
          >>> game = time_per_word(['extort', 'elysia', 'cungeboi', 'cams', 'plagueproof', 'overdeeming'], p)
          >>> game['words']
          ['extort', 'elysia', 'cungeboi', 'cams', 'plagueproof', 'overdeeming']
          >>> game['times']
          [[1, 3, 4, 2, 5, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[46]]
          >>> game = time_per_word([], p)
          >>> game['words']
          []
          >>> game['times']
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import *
      """,
      'teardown': r"""
      
      """,
      'type': 'doctest'
    }
  ]
}
