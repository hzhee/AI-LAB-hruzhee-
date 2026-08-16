fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grape, purple).
fruit_color(orange, orange).

list_fruits :-
    fruit_color(Fruit, Color),
    format('~w is ~w~n', [Fruit, Color]),
    fail.

list_fruits.