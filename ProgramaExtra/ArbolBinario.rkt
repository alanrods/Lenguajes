;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname ArbolBinario) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(define-struct nodo (valor izq der))

(define (numhojas ab)
  (cond
    [(number? ab) 1]
    [(nodo? ab)(+(numhojas(nodo-izq ab))
                (numhojas(nodo-der ab)))]))