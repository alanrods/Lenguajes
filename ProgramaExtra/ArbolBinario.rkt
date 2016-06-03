;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-reader.ss" "lang")((modname ArbolBinario) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))

(define-struct nodo (valor izq der))

(define (crea-nodo valor) (make-nodo valor null null))

(define (inserta-nodo nodo-n ab)
  (cond
    [(< (nodo-valor nodo-n)(nodo-valor ab)) (cond
                                              [(null? (nodo-izq ab)) (make-nodo (nodo-valor ab) nodo-n (nodo-der ab))]
                                              [else
                                               (make-nodo
                                                (nodo-valor ab) (inserta-nodo nodo-n (nodo-izq ab)) (nodo-der ab))])]
    [(> (nodo-valor nodo-n)(nodo-valor ab)) (cond
                                              [(null? (nodo-der ab)) (make-nodo (nodo-valor ab) (nodo-izq ab) nodo-n)]
                                              [else
                                               (make-nodo
                                                (nodo-valor ab) (nodo-izq ab) (inserta-nodo nodo-n (nodo-der ab)))])]
    [else ab]))
 
(define (saca-nodo valor ab) (saca-aux valor ab (num-hijos (busca-nodo valor ab)) (maximo (busca-nodo valor ab))))

(define (saca-aux valor ab num-hijos-nodo nodo-max)
  (cond
    [(equal? num-hijos-nodo 0) (cond
                                 [(equal? valor (nodo-valor ab)) null]
                                 [(equal? (num-hijos ab) 2) (make-nodo (nodo-valor ab) (saca-aux valor (nodo-izq ab) num-hijos-nodo nodo-max) (saca-aux valor (nodo-der ab) num-hijos-nodo nodo-max))]
                                 [(equal? (num-hijos ab) 0) ab]
                                 [(and (equal? (nodo-izq ab) null) (equal? (num-hijos ab) 1)) (make-nodo (nodo-valor ab) null (saca-aux valor (nodo-der ab) num-hijos-nodo nodo-max))]
                                 [else (make-nodo (nodo-valor ab) (saca-aux valor (nodo-izq ab) num-hijos-nodo nodo-max) null)])]
    [(equal? num-hijos-nodo 1) (cond
                                 [(equal? valor (nodo-valor ab)) (cond
                                                                   [(equal? (nodo-izq ab) null) (nodo-der ab)]
                                                                   [else (nodo-izq ab)])]
                                 [(equal? (num-hijos ab) 2) (make-nodo (nodo-valor ab) (saca-aux valor (nodo-izq ab) num-hijos-nodo nodo-max) (saca-aux valor (nodo-der ab) num-hijos-nodo nodo-max))]
                                 [(equal? (num-hijos ab) 0) ab]
                                 [(and (equal? (nodo-izq ab) null) (equal? (num-hijos ab) 1)) (make-nodo (nodo-valor ab) null (saca-aux valor (nodo-der ab) num-hijos-nodo nodo-max))]
                                 [else (make-nodo (nodo-valor ab) (saca-aux valor (nodo-izq ab) num-hijos-nodo nodo-max) null)])]
    [else (cond
            [(equal? (nodo-valor nodo-max) (nodo-valor ab)) null]
            [(equal? valor (nodo-valor ab)) (make-nodo (nodo-valor (maximo ab)) (nodo-izq ab) (nodo-der ab))]
            [(equal? (num-hijos ab) 2) (make-nodo (nodo-valor ab) (saca-aux valor (nodo-izq ab) num-hijos-nodo nodo-max) (saca-aux valor (nodo-der ab) num-hijos-nodo nodo-max))]
            [(equal? (num-hijos ab) 0) ab]
            [(and (equal? (nodo-izq ab) null) (equal? (num-hijos ab) 1)) (make-nodo (nodo-valor ab) null (saca-aux valor (nodo-der ab) num-hijos-nodo nodo-max))]
            [else (make-nodo (nodo-valor ab) (saca-aux valor (nodo-izq ab) num-hijos-nodo nodo-max) null)])]))
  
(define (maximo ab)
  (cond
    [(equal? (nodo-der ab) null) ab]
    [else (maximo (nodo-der ab))]))

(define (num-hijos ab)
  (cond
    [(and (null? (nodo-izq ab)) (null? (nodo-der ab))) 0]
    [(and (not (null? (nodo-izq ab))) (not (null? (nodo-der ab)))) 2]
    [else 1]))

(define (num-hojas ab)
  (cond
    [(and (null? (nodo-izq ab)) (null? (nodo-der ab))) 1]
    [(nodo? ab)(+(num-hojas(nodo-izq ab))
                (num-hojas(nodo-der ab)))]))

(define (busca-nodo valor ab)
  (cond
    [(null? ab) #f]
    [(< valor (nodo-valor ab)) (busca-nodo valor (nodo-izq ab))]
    [(> valor (nodo-valor ab)) (busca-nodo valor (nodo-der ab))]
    [else ab]))

(define (pre-orden ab)
  (cond
    [(null? ab) empty]
    [else (append (list (nodo-valor ab)) (pre-orden (nodo-izq ab)) (pre-orden (nodo-der ab)))]))

(define (in-orden ab)
  (cond
    [(null? ab) empty]
    [else (append (in-orden (nodo-izq ab)) (list (nodo-valor ab)) (in-orden (nodo-der ab)))]))

(define (post-orden ab)
  (cond
    [(null? ab) empty]
    [else (append (post-orden (nodo-izq ab)) (post-orden (nodo-der ab)) (list (nodo-valor ab)))]))

(define arbol1 (crea-nodo 10))
;(define arbol2 (inserta-nodo (crea-nodo 8) arbol1))
;(define arbol3 (inserta-nodo (crea-nodo 9) arbol2))
;(define arbol4 (inserta-nodo (crea-nodo 2) arbol3))
(define arbol5 (inserta-nodo (crea-nodo 20) arbol1))
(define arbol6 (inserta-nodo (crea-nodo 15) arbol5))
(define arbol7 (inserta-nodo (crea-nodo 23) arbol6))
;(define arbol8 (inserta-nodo (crea-nodo 1) arbol7))
;(define a )
arbol7
;(num-hojas arbol7)
;(busca-nodo 2 arbol7)
;(pre-orden arbol7)
;(in-orden arbol7)
;(post-orden arbol7)
;(define arbol9 (saca-nodo 2 arbol8))
;arbol8
;arbol9
;(maximo arbol8)
;(saca-nodo 8 arbol8)

#|
(define (node-insert node-n arb)
  (cond
    [(< (node-valor node-n)(nodo-valor arb))(cond
                                              [(null? (nodo-izq arb))(make-nodo arb-valor node-n-valor null)]
                                              [(else
                                                (node-insert node-n arb-izq))])]
    [(>(node-valor node-n)(nodo-valor arb))(cond
                                             [(null? (nodo-der arb))(make-nodo arb-valor null node-n-valor)]
                                             [(else
                                               (node-insert node-n arb-der))])]
    ))
|#

#|
(struct nodo (valor izq der)#:transparent)

(define (crea-nodo valor) (nodo valor null null))

(define (inserta-nodo nodo-n ab)
  (cond
    [(< (nodo-valor nodo-n)(nodo-valor ab)) (cond
                                              [(null? (nodo-izq ab)) (struct-copy nodo ab [izq (crea-nodo (nodo-valor nodo-n))])]
                                              [else
                                               (nodo
                                                (nodo-valor ab) (inserta-nodo nodo-n (nodo-izq ab)) (inserta-nodo nodo-n (nodo-der ab)))])]
    [(> (nodo-valor nodo-n)(nodo-valor ab)) (cond
                                              [(null? (nodo-der ab)) (struct-copy nodo ab [der (crea-nodo (nodo-valor nodo-n))])]
                                              [else
                                               (nodo
                                                (nodo-valor ab) (inserta-nodo nodo-n (nodo-izq ab)) (inserta-nodo nodo-n (nodo-der ab)))])]))

(inserta-nodo (crea-nodo 10) (nodo 10 (nodo 8 '() '()) '()))
|#

#|
(struct posn (x y)#:transparent)
(struct-copy my-struct s [f2 200])
;;=> (my-struct 1 200 3 4)
(struct-copy my-struct s [f2 (* 100 (my-struct-f2 s))])
;;=> (my-struct 1 200 3 4)
|#