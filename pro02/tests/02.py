test = {
  'name': 'Problem 2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> dogs = about(['dogs', 'hounds'])
          >>> dogs('A paragraph about cats.')
          False
          >>> dogs('A paragraph about dogs.')
          True
          >>> dogs('Release the Hounds!')
          True
          >>> dogs('"DOGS" stands for Department Of Geophysical Science.')
          True
          >>> dogs('Do gs and ho unds don\'t count')
          False
          >>> dogs("AdogsParagraph")
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
          >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
          'Cute Dog!'
          >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
          'Nice pup.'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import about
      >>> from cats import choose
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> ab = about(['neurine', 'statutably', 'quantivalent', 'intrarachidian', 'itinerantly', 'cloaklet'])
          >>> ab('unhollow simsim dcloakletB itinerantly cloakLet dQUaNtivalentJ gnEurinE fissiparity Mneurinel')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['unsimilar', 'conditioning', 'crystallogenical', 'mennom', 'foreannouncement', 'neomorph'])
          >>> ab('#crystallogenIcalW podded reorganizationist neomorPhf hneomorphj')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['smopple', 'modernizer'])
          >>> ab('tongsman smopplek ASmoppleg Bsm(<opPLeF SMopPlES')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['equalizing', 'phrymaceous', 'fluidimeter', 'seeds', 'bridgemaking'])
          >>> ab('xph+rymaceous hobbledehoyism zphrymaceousy ofluidimeter Lseeds?\\ interbank DsEe)dS consumer iatromathematical')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['seeingly', 'essexite'])
          >>> ab('essexite clupeine habeas disrupture faceable phototypography LseeIngly seeingly')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['probatively', 'unabatedly', 'reundergo', 'unweld', 'handgun', 'hydrometra', 'recessionary', 'grippotoxin'])
          >>> ab('DreuNdergo reundergo unabAtedlYM grippotoxin Lre<und!ergoy')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['elysia'])
          >>> ab('hewlett el=ysiA` pamphletic elysia te#Lysiac')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['entomical'])
          >>> ab('obduction polyacid en\\tomical{w entoMicAlP entO[m]icalP befrill zentom[icalr centomi_CAl')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['choirwise', 'uncircumstantial', 'glassine', 'supplies', 'underivedly', 'henter', 'undeserving', 'uncope'])
          >>> ab('tazia uncope glassine glassineW eChoirwis<e& uncircumstaNTIal uninventiveness pentahexahedral')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import about
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
