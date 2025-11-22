boy(jim).
girl(lisa).

child(jim).
child(lisa).

good_child(jim).
good_child(lisa).

gets_gift(X) :-
    child(X),
    good_child(X).

gets_bike(X) :-
    boy(X),
    good_child(X).

gets_doll(X) :-
    girl(X),
    good_child(X).
