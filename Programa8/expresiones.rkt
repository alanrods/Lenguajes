;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname expresiones) (read-case-sensitive #t) (teachpacks ((lib "show-queen.ss" "teachpack" "htdp") (lib "image.ss" "teachpack" "2htdp") (lib "universe.ss" "teachpack" "2htdp") (lib "batch-io.ss" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "show-queen.ss" "teachpack" "htdp") (lib "image.ss" "teachpack" "2htdp") (lib "universe.ss" "teachpack" "2htdp") (lib "batch-io.ss" "teachpack" "2htdp")) #f)))
#|A. Definición de datos para la representación de expresiones 
|#

(define-struct sum (izq der))
(define-struct mul (izq der))

(define (evaluar en)
  (cond
    [(number? en) en]
    [(sum? en)(+(evaluar(sum-izq en))
                (evaluar(sum-der en)))]
    [(mul? en)(*(evaluar(mul-izq en))
                (evaluar(mul-der en)))]
    [(symbol? en)(substituir en)))

(check-expect (evaluar 5)5)
(check-expect (evaluar (make-sum 3 5))8)
(check-expect (evaluar (make-mul 3 5))15)
(check-expect (evaluar (make-sum(make-mul 5 5)(make-mul 4 4)))41)