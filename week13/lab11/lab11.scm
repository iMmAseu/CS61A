(define (if-program condition if-true if-false)
  (cons 'if
        (cons condition
              (cons if-true (cons if-false nil)))))

(define (square n) (* n n))

(define (pow-expr base exp)
  (cond 
    ((= exp 0)
     1)
    ((= exp 1)
     (cons '* (cons base (cons 1 nil))))
    ((even? exp)
     (list 'square (pow-expr base (/ exp 2))))
    (else
     (cons '*
           (cons base (cons (pow-expr base (- exp 1)) nil))))))

(define-macro (repeat n expr)
  `(repeated-call ,n (lambda () ,expr)))

; Call zero-argument procedure f n times and return the final result.
(define (repeated-call n f)
  (if (= n 1)
      (f)
      (begin (f) (repeated-call (- n 1) f))))
