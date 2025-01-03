;;; Lab08: Scheme

(define (over-or-under a b)
  (if (> a b)
    1
    (if (= a b)
      0
      -1
    )
  )
)


(define (make-adder n)
  (lambda (x) (+ x n))
)


(define (composed f g)
  (lambda (x) (f (g x)))
)


(define (remainder a b)
  (- a (* b (quotient a b))))

(define (gcd a b)
  (if (= b 0)
    a
    (gcd b (modulo a b))
  )
)


(define lst
  (list (list 1) 2 (list 3 4) 5)
)
 
(define (ordered s)
  (if (or (null? s) (null? (cdr s)))
    #t
    (if (> (- (car s) (car (cdr s))) 0)
      #f
      (ordered (cdr s))
    )
  )
)
