move(1, Source, Target, _) :-
    format('Move disk from ~w to ~w~n', [Source, Target]).

move(N, Source, Target, Auxiliary) :-
    N > 1,
    N1 is N - 1,
    move(N1, Source, Auxiliary, Target),
    move(1, Source, Target, _),
    move(N1, Auxiliary, Target, Source).