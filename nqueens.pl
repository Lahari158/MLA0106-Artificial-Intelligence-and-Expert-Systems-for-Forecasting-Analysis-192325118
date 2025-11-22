% Check if two queens attack each other
% 4-Queens Problem in Prolog

% Main predicate
solve_4queens(Solution) :-
    Solution = [Q1, Q2, Q3, Q4],
    permutation([1,2,3,4], Solution),
    safe(Solution).

% Check all queens are safe
safe([Q1, Q2, Q3, Q4]) :-
    no_attack(Q1, Q2, 1),
    no_attack(Q1, Q3, 2),
    no_attack(Q1, Q4, 3),
    no_attack(Q2, Q3, 1),
    no_attack(Q2, Q4, 2),
    no_attack(Q3, Q4, 1).

% Attack condition for diagonals
no_attack(X, Y, D) :-
    Diff is abs(X - Y),
    Diff =\= D.
