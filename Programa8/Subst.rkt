;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname Subst) (read-case-sensitive #t) (teachpacks ((lib "show-queen.ss" "teachpack" "htdp") (lib "image.ss" "teachpack" "2htdp") (lib "universe.ss" "teachpack" "2htdp") (lib "batch-io.ss" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "show-queen.ss" "teachpack" "htdp") (lib "image.ss" "teachpack" "2htdp") (lib "universe.ss" "teachpack" "2htdp") (lib "batch-io.ss" "teachpack" "2htdp")) #f)))
#|A. Definición de datos para la representación de expresiones 
|#

(define-struct sum (izq der))
(define-struct mul (izq der))

(define (evaluar en)
  (cond
    [(number? en)en]
    [(conSimbolo en) "No se puede evaluar"]
    [(sum? en)(+(evaluar(sum-izq en))
                (evaluar(sum-der en)))]
    [(mul? en)(*(evaluar(mul-izq en))
                 (evaluar(mul-der en)))]))
#|
(check-expect (evaluar 5) 5)
(check-expect (evaluar (make-sum 5 5))10)
(check-expect (evaluar (make-mul 5 5))25)
(check-expect (evaluar 'x)"No se puede evaluar")
(check-expect (evaluar (make-sum (make-mul 4 4)(make-sum 1 0)))17)
|#

(define (conSimbolo en)
  (cond
    [(number? en) (not (number? en))]
    [(symbol? en) (symbol? en)]
    [(sum? en)(or (conSimbolo(sum-izq en))
                (conSimbolo(sum-der en)))]
    [(mul? en)(or (conSimbolo(mul-izq en))
                 (conSimbolo(mul-der en)))]))
;(check-expect (conSimbolo (make-sum(make-mul 3 'x)(make-mul 4 4))) #t)

(define (subst en var n)
  (cond
    [(and (symbol? en)(equal? en var))n]
    [(number? en)en]
    [(sum? en)(make-sum (subst(sum-izq en) var n)
                (subst(sum-der en) var n))]
    [(mul? en)(make-mul(subst(mul-izq en) var n)
                 (subst(mul-der en) var n))]
    [else "No se puede substituir"]))
#|
(check-expect (subst empty empty 2)"No se puede substituir")
(check-expect (subst "hola" "hola" 2) "No se puede substituir")
(check-expect (subst 'x 'x 10)10)
(check-expect (subst 5 'x 2) 5)
(check-expect (subst 'x 'x 2) 2)
(check-expect (subst (make-sum 3 5) 'x 2) (make-sum 3 5))
(check-expect (subst (make-sum (make-mul 3 'x) (make-mul 4 'x)) 'x 2)
            (make-sum (make-mul 3 2) (make-mul 4 2)))
(check-expect (subst (make-sum (make-mul 'x 'y) (make-mul 'x 'z)) 'x 2)
             (make-sum (make-mul 2 'y) (make-mul 2 'z)))
|#