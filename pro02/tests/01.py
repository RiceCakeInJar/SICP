test = {
  'name': 'Problem 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> ps = ['short', 'really long', 'tiny']
          >>> s = lambda p: len(p) <= 5
          >>> choose(ps, s, 0) # remember to put quotes ('') around strings!
          'short'
          >>> choose(ps, s, 1)
          'tiny'
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['hi', 'how are you', 'fine']
          >>> s = lambda p: len(p) <= 4
          >>> choose(ps, s, 0)
          'hi'
          >>> choose(ps, s, 1)
          'fine'
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['VQwSwNX']
          >>> s = lambda p: p == 'VQwSwNX'
          >>> choose(ps, s, 0)
          'VQwSwNX'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['d', '6VXy', '9UtlGF3JvN', 'C']
          >>> s = lambda p: p == '6VXy' or p == '9UtlGF3JvN' or p == 'd'
          >>> choose(ps, s, 0)
          'd'
          >>> choose(ps, s, 1)
          '6VXy'
          >>> choose(ps, s, 2)
          '9UtlGF3JvN'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['nmLjTBQ']
          >>> s = lambda p: p == 'nmLjTBQ'
          >>> choose(ps, s, 0)
          'nmLjTBQ'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['LQa7i6tx', '7VNVwiz6', 'FiSMcoBy', 'CbkzHZd8Q', 'wTeIcJF', 'c5', '7qIhVzA']
          >>> s = lambda p: p == '7qIhVzA' or p == 'CbkzHZd8Q' or p == 'c5' or p == 'wTeIcJF'
          >>> choose(ps, s, 0)
          'CbkzHZd8Q'
          >>> choose(ps, s, 1)
          'wTeIcJF'
          >>> choose(ps, s, 2)
          'c5'
          >>> choose(ps, s, 3)
          '7qIhVzA'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = []
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = []
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['YSw2G9VmQ9', 'ER', 'r7ey5O', 'XO3sj', '2MWemTjKV1', 'ZZIaR', 'TIv0ZHG']
          >>> s = lambda p: p == '2MWemTjKV1'
          >>> choose(ps, s, 0)
          '2MWemTjKV1'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['0lQzW0tyg', 'yvW708v']
          >>> s = lambda p: p == 'yvW708v'
          >>> choose(ps, s, 0)
          'yvW708v'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = []
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['auPQIQ7', 'tk7FMoy', 'vNDPPf3d', '2LtT', 'ynsLz', 'frmxE', 'L', 'NKv']
          >>> s = lambda p: p == 'NKv' or p == 'tk7FMoy'
          >>> choose(ps, s, 0)
          'tk7FMoy'
          >>> choose(ps, s, 1)
          'NKv'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['Y', 'ENbBM', 'at4eksVN1', 'o8VT', 'x1a']
          >>> s = lambda p: p == 'ENbBM'
          >>> choose(ps, s, 0)
          'ENbBM'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['l0sZzF']
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import choose
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
