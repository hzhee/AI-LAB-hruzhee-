initial_state([monkey_on_floor, banana_on_ceiling, box_in_room]).

action(grab,
       [monkey_on_box, banana_at_hand],
       [has_banana]).

action(climb_box,
       [at_box, monkey_on_floor],
       [monkey_on_box]).

action(push_box,
       [at(monkey,A), at(box,A)],
       [at(monkey,B), at(box,B)]) :-
    adjacent(A, B).

action(walk(A,B),
       [at(monkey,A)],
       [at(monkey,B)]).

adjacent(room, room).