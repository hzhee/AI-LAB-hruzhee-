can_fly(sparrow).
can_fly(eagle).
can_fly(parrot).
cannot_fly(penguin).
cannot_fly(ostrich).

bird_can_fly(Bird) :-
    can_fly(Bird),
    format('~w can fly.~n', [Bird]).

bird_can_fly(Bird) :-
    cannot_fly(Bird),
    format('~w cannot fly.~n', [Bird]).