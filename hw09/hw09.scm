;;; Homework 09: Scheme List, Tail Recursion and Macro

;;; Required Problems

(define (make-change total biggest)
  (begin
    (define (make-change-helper total money so-far)
      (cond ((< total 0) (list))
            ((= money 0) (list))
            ((= total 0) (list so-far))
            (else 
              (append 
                (make-change-helper (- total money) money (append so-far (cons money nil)))
                (make-change-helper total (- money 1) so-far)
              )
            )
      )
    )
    (make-change-helper total biggest nil)
  )
)


(define (find n lst)
  (define (f n lst ans)
    (if (eq? n (car lst))
      ans
      (f n (cdr lst) (+ 1 ans))
    )
  )
  (f n lst 0)
)


(define (find-nest n sym)
  (define (f n sym-val so-far)
    (cond
      ((and (number? (car sym-val)) (null? (cdr sym-val)))
        (if (= n (car sym-val))
          `(car ,so-far)
          (list)
        )
      )
      ((and (number? (car sym-val)) (not (null? (cdr sym-val))))
        (if (= n (car sym-val))
          `(car ,so-far)
          (f n (cdr sym-val) `(cdr ,so-far))
        )
      )
      ((and (not (number? (car sym-val))) (null? (cdr sym-val)))
        (f n (car sym-val) `(car ,so-far))
      )
      (else
        (append (f n (cdr sym-val) `(cdr ,so-far)) (f n (car sym-val) `(car ,so-far)))
      )
    )
  )
  (f n (eval sym) sym)
)

(define-macro (my/or operands)
  (cond 
    ((null? operands) #f)
    ((null? (cdr operands)) (car operands))
    (else
      `(let ((t ,(car operands)))
        (if t
          t
          (my/or ,(cdr operands))
        )
      )
    )
  )  
)


(define-macro (k-curry fn args vals indices)
  
)


(define-macro (let* bindings expr)
  ''YOUR-CODE-HERE
)

;;; Just For Fun Problems


; Helper Functions for you
(define (cadr lst) (car (cdr lst)))
(define (cddr lst) (cdr (cdr lst)))
(define (caddr lst) (car (cdr (cdr lst))))
(define (cdddr lst) (cdr (cdr (cdr lst))))

(define-macro (infix expr)
  'YOUR-CODE-HERE
)


; only testing if your code could expand to a valid expression 
; resulting in my/and/2 and my/or/2 not hygienic
(define (gen-sym) 'sdaf-123jasf/a123)

; in these two functions you can use gen-sym function.
; assumption:
; 1. scm> (eq? (gen-sym) (gen-sym))
;    #f
; 2. all symbol generate by (gen-sym) will not in the source code before macro expansion
(define-macro (my/and/2 operands)
  'YOUR-CODE-HERE
)

(define-macro (my/or/2 operands)
  'YOUR-CODE-HERE
)