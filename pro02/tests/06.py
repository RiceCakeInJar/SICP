test = {
  'name': 'Problem 6',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> big_limit = 10
          >>> sphinx_fixes("car", "cad", big_limit)
          1
          >>> sphinx_fixes("this", "that", big_limit)
          2
          >>> sphinx_fixes("one", "two", big_limit)
          3
          >>> sphinx_fixes("from", "form", big_limit)
          2
          >>> sphinx_fixes("awe", "awesome", big_limit)
          4
          >>> sphinx_fixes("someawe", "awesome", big_limit)
          6
          >>> sphinx_fixes("awful", "awesome", big_limit)
          5
          >>> sphinx_fixes("awful", "awesome", 3) > 3
          True
          >>> sphinx_fixes("awful", "awesome", 4) > 4
          True
          >>> sphinx_fixes("awful", "awesome", 5) > 5
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> big_limit = 10
          >>> sphinx_fixes("nice", "rice", big_limit)    # Substitute: n -> r
          1
          >>> sphinx_fixes("range", "rungs", big_limit)  # Substitute: a -> u, e -> s
          2
          >>> sphinx_fixes("pill", "pillage", big_limit) # Don't substitute anything, length difference of 3.
          3
          >>> sphinx_fixes("roses", "arose", big_limit)  # Substitute: r -> a, o -> r, s -> o, e -> s, s -> e
          5
          >>> sphinx_fixes("rose", "hello", big_limit)   # Substitute: r->h, o->e, s->l, e->l, length difference of 1.
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> big_limit = 10
          >>> sphinx_fixes("goodbye", "good", big_limit)
          3
          >>> sphinx_fixes("pront", "print", big_limit)
          1
          >>> sphinx_fixes("misspollid", "misspelled", big_limit)
          2
          >>> sphinx_fixes("worry", "word", big_limit)
          2
          >>> sphinx_fixes("first", "flashy", big_limit)
          4
          >>> sphinx_fixes("hash", "ash", big_limit)
          4
          >>> sphinx_fixes("ash", "hash", big_limit)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> big_limit = 0
          >>> sphinx_fixes("baste", "bastion", big_limit) > big_limit
          True
          >>> sphinx_fixes("awesome", "awesome", big_limit)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> small_words_list = ["spell", "nest", "test", "pest", "best", "bird", "wired",
          ...                     "abstraction", "abstract", "peeling", "gestate", "west",
          ...                     "spelling", "bastion"]
          >>> autocorrect("speling", small_words_list, sphinx_fixes, 10)
          'peeling'
          >>> autocorrect("abstrction", small_words_list, sphinx_fixes, 10)
          'abstract'
          >>> autocorrect("wird", small_words_list, sphinx_fixes, 10)
          'bird'
          >>> autocorrect("gest", small_words_list, sphinx_fixes, 10)
          'nest'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Check that the recursion stops when the limit is reached
          >>> import trace, io
          >>> from contextlib import redirect_stdout
          >>> with io.StringIO() as buf, redirect_stdout(buf):
          ...     trace.Trace(trace=True).runfunc(sphinx_fixes, "someaweqwertyuio", "awesomeasdfghjkl", 3)
          ...     output = buf.getvalue()
          >>> len([line for line in output.split('\n') if 'funcname' in line]) < 10
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sphinx_fixes('rut', 'ruhw', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sphinx_fixes('yo', 'yo', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([sphinx_fixes('slurp', 'slurpn', k) > k for k in range(6)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import sphinx_fixes, autocorrect
      >>> import tests.construct_check as test
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
