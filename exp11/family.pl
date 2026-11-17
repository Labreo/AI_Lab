parent(pam,bob).
parent(tom,bob).
parent(tom,liz).
parent(bob,ann).
parent(bob,pat).
parent(pat,jim).

male(bob).
female(pam).
male(tom).
female(liz).
male(pat).
female(ann).
male(jim).

father(X,Y):- parent(X,Y), male(X).
mother(X,Y):- parent(X,Y), female(X).
child(X,Y):- parent(Y,X).
sibling(X,Y):- parent(Z,X), parent(Z,Y).
grandfather(X,Y):- parent(X,Z), parent(Z,Y), male(X).
grandmother(X,Y):- parent(X,Z), parent(Z,Y), female(X).
ancestor(X,Y):- parent(X,Y).
ancestor(X,Y):- parent(X,Z), ancestor(Z,Y).