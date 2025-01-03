test = {
  'name': 'wwsd',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define (has-even? s)
          ....        (cond ((null? s) #f)
          ....              ((even? (car s)) #t)
          ....              (else (has-even? (cdr-stream s)))))
          has-even?
          scm> (define (f x) (* 3 x))
          f
          scm> (define nums (cons-stream 1 (cons-stream (f 3) (cons-stream (f 5) nil))))
          nums
          scm> nums
          (1 . #[promise (not forced)])
          scm> (cdr nums)
          #[promise (not forced)]
          scm> (cdr-stream nums)
          (9 . #[promise (not forced)])
          scm> nums
          (1 . #[promise (forced)])
          scm> (define (f x) (* 2 x))
          f
          scm> (cdr-stream nums)
          (9 . #[promise (not forced)])
          scm> (cdr-stream (cdr-stream nums))
          (10 . #[promise (not forced)])
          scm> (has-even? nums)
          #t
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': False,
      'setup': r"""
      
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
