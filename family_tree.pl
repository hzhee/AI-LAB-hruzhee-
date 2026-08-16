parent(john, mary).
parent(john, david).
parent(mary, susan).
parent(david, tom).

sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).