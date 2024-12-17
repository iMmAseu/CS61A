(define (caar x) (car (car x)))

(define (cadr x) (car (cdr x)))

(define (cdar x) (cdr (car x)))

(define (cddr x) (cdr (cdr x)))

; ; Problem 15
; ; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 15
  (begin (define (enum s index)
           (cond 
             ((null? s)
              '())
             (else
              (cons (cons index (cons (car s) nil))
                    (enum (cdr s) (+ index 1))))))
         (enum s 0)))

; END PROBLEM 15
; ; Problem 16
; ; Merge two lists S1 and S2 according to ORDERED? and return
; ; the merged lists.
(define (merge ordered? s1 s2)
  ; BEGIN PROBLEM 16
  (cond 
    ((null? s1)
     s2)
    ((null? s2)
     s1)
    ((ordered? (car s1) (car s2))
     (cons (car s1) (merge ordered? (cdr s1) s2)))
    (else
     (cons (car s2) (merge ordered? s1 (cdr s2))))))

; END PROBLEM 16
; ; Optional Problem 2
; ; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))

(define define? (check-special 'define))

(define quoted? (check-special 'quote))

(define let? (check-special 'let))

; ; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond 
    ((atom? expr)
     ; BEGIN OPTIONAL PROBLEM 2
     expr
     ; END OPTIONAL PROBLEM 2
    )
    ((quoted? expr)
     ; BEGIN OPTIONAL PROBLEM 2
     expr
     ; END OPTIONAL PROBLEM 2
    )
    ((or (lambda? expr) (define? expr))
     (let ((form (car expr))
           (params (cadr expr))
           (body (cddr expr)))
       ; BEGIN OPTIONAL PROBLEM 2
       (cons form (cons (map let-to-lambda params) (map let-to-lambda body)))
       ; END OPTIONAL PROBLEM 2
     ))
    ((let? expr)
     (let ((values (cadr expr))
           (body (cddr expr)))
       ; BEGIN OPTIONAL PROBLEM 2
       (cons (cons 'lambda (cons (car (zip (let-to-lambda values))) (let-to-lambda body))) (cadr (zip (let-to-lambda values))))
       ; END OPTIONAL PROBLEM 2
     ))
    (else
     ; BEGIN OPTIONAL PROBLEM 2
     (map let-to-lambda expr)
     ; END OPTIONAL PROBLEM 2
    )))

; Some utility functions that you may find useful to implement for let-to-lambda
(define (zip lst)
  (if (null? (car lst))
      '()
      (cons (map car lst) (zip (map cdr lst)))))
  
(define (open lst)
    (if (null? lst) '() ((car lst)))) 
  
