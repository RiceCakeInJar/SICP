test = {
  'name': 'Question 3: A, B, and X',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> a = lambda x: x * 2 + 1
          >>> def b(b, x):
          ...     return b(x + a(x))
          >>> x = 3
          >>> b(a, x)
          21
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
