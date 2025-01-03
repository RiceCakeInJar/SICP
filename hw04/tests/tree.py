test = {
  'name': 'P4 (0pts)',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
          >>> preorder(numbers)
          [1, 2, 3, 4, 5, 6, 7]
          >>> preorder(tree(2, [tree(4, [tree(6)])]))
          [2, 4, 6]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ADT import tree
      >>> from hw04 import preorder
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
          >>> label_sum(t)
          15
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ADT import tree
      >>> from hw04 import label_sum
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> def has_int(tree, i):
          ...     def base_func(l):
          ...         return lambda i: l == i
          ...     def merge_func(l, bs):
          ...         return lambda i: l == i or any([b(i) for b in bs])
          ...     return fold_tree(tree, base_func, merge_func)(i)
          >>> has_int(tree(1, [tree(2, [tree(3)]), tree(4)]), 1)
          True
          >>> has_int(tree(1, [tree(2, [tree(3)]), tree(4)]), 5)
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ADT import tree
      >>> from hw04 import fold_tree
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> greetings = tree('h', [tree('i'),
          ...                        tree('e', [tree('l', [tree('l', [tree('o')])]),
          ...                                   tree('y')])])
          >>> print_tree(greetings)
          h
            i
            e
              l
                l
                  o
              y
          >>> has_path(greetings, 'h')
          True
          >>> has_path(greetings, 'i')
          False
          >>> has_path(greetings, 'hi')
          True
          >>> has_path(greetings, 'hello')
          True
          >>> has_path(greetings, 'hey')
          True
          >>> has_path(greetings, 'bye')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ADT import tree, print_tree
      >>> from hw04 import has_path
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
