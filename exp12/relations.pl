parent(sudip, piyush).
parent(sudip, raj).
parent(sudip,sanshri).
parent(sudip,sabrina).
male(piyush).
male(raj).
female(sanshri).
female(sabrina).
brother(X,Y) :- parent(Z,X), parent(Z,Y),male(X), male(Y),dif(X,Y).
sister(X,Y) :- parent(Z,X), parent(Z,Y),female(X), female(Y),diff(X,Y).