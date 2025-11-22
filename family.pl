% --- Facts ---
male(john).
male(sam).
female(rita).
female(mary).

father(john, sam).
father(john, rita).
mother(mary, sam).
mother(mary, rita).

% --- Rules ---
brother(X, Y) :-
    father(F, X), father(F, Y),
    mother(M, X), mother(M, Y),
    X \= Y,
    male(X).

sister(X, Y) :-
    father(F, X), father(F, Y),
    mother(M, X), mother(M, Y),
    X \= Y,
    female(X).

grandfather(X, Y) :-
    father(X, Z),
    (father(Z, Y); mother(Z, Y)).

grandchild(X, Y) :-
    grandfather(Y, X).

uncle(X, Y) :-
    brother(X, P),
    (father(P, Y); mother(P, Y)).
