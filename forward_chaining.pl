fact(a).
fact(b).

rule(c) :-
    fact(a),
    fact(b).

forward :-
    rule(X),
    \+ fact(X),
    assertz(fact(X)),
    writeln(X),
    forward.

forward.