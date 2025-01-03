;;; Lab 10: Stream

;;; Required Problems

(define (filter-stream f s)
  (if (null? s) nil
      (let ((rest (cdr-stream s)))
        (if (f (car s))
            (cons-stream (car s) (filter-stream f rest))
            (filter-stream f rest)))))


(define (slice s start end)
  (if (eq? nil s)
    nil
    (if (eq? 0 start)
      (if (eq? 0 end)
        nil
        (cons (car s) (slice (cdr-stream s) 0 (- end 1)))
      )
      (slice (cdr-stream s) (- start 1) (- end 1))
    )
  )
)



(define (naturals n)
  (cons-stream n (naturals (+ n 1))))


(define (combine-with f xs ys)
  (if (or (null? xs) (null? ys))
      nil
      (cons-stream
        (f (car xs) (car ys))
        (combine-with f (cdr-stream xs) (cdr-stream ys)))))


(define factorials
  (cons-stream 1 (combine-with * (naturals 1) factorials))
)


(define fibs
  (cons-stream 0 (cons-stream 1 (combine-with + fibs (cdr-stream fibs))))
)

(define (exp x)
  (define xx (cons-stream x xx))
  (cons-stream 1 (combine-with + (exp x) (combine-with / (combine-with expt xx (naturals 1)) (cdr-stream factorials))))
)


(define (list-to-stream lst)
  (if (null? lst) nil
      (cons-stream (car lst) (list-to-stream (cdr lst)))))


(define (nondecrease s)
  (define (finder s)
    (cond
      ((null? s) nil)
      ((null? (cdr-stream s)) (cons (car s) nil))
      ((<= (car s) (car (cdr-stream s))) (cons (car s) (finder (cdr-stream s))))
      (else (cons (car s) nil))
    )
  )
  (define (returner s)
    (cond
      ((null? s) nil)
      ((null? (cdr-stream s)) nil)
      ((<= (car s) (car (cdr-stream s))) (returner (cdr-stream s)))
      (else (cdr-stream s))
    )
  )
  (if (eq? nil s)
    nil
    (cons-stream (finder s) (nondecrease (returner s)))
  )
)

;;; Just For Fun Problems

(define (my-cons-stream first second) ; Does this line need to be changed?
  'YOUR-CODE-HERE
)

(define (my-car stream)
  'YOUR-CODE-HERE
)

(define (my-cdr-stream stream)
  'YOUR-CODE-HERE
)


(define (sieve s)
  'YOUR-CODE-HERE
)

(define primes (sieve (naturals 2)))
