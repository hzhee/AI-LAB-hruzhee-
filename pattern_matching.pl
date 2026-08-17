match([], _).

match([X|Xs], [X|Ys]) :-
    match(Xs, Ys).

match(Pattern, [_|Xs]) :-
    match(Pattern, Xs).