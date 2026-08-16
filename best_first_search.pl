edge(a, b, 1).
edge(a, c, 3).
edge(b, d, 2).
edge(c, d, 4).

heuristic(a, 5).
heuristic(b, 2).
heuristic(c, 3).
heuristic(d, 0).

best_first(Node, Goal, Path) :-
    bfs([[Node]], Goal, Path).

bfs([[Goal|Path]|_], Goal, [Goal|Path]).

bfs([[Current|Path]|Rest], Goal, FinalPath) :-
    findall(
        [Next, Current|Path],
        (
            edge(Current, Next, _),
            \+ member(Next, [Current|Path])
        ),
        NewPaths
    ),
    append(Rest, NewPaths, UpdatedPaths),
    sort_paths(UpdatedPaths, SortedPaths),
    bfs(SortedPaths, Goal, FinalPath).

sort_paths(Paths, Sorted) :-
    map_list_to_pairs(path_cost, Paths, Pairs),
    keysort(Pairs, SortedPairs),
    pairs_values(SortedPairs, Sorted).

path_cost([Node|_], Cost) :-
    heuristic(Node, Cost).