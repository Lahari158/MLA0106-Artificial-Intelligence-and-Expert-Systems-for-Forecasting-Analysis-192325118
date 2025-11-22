% Celsius to Fahrenheit
c_to_f(C, F) :-
    F is (C * 9/5) + 32.

% Freezing?
freezing(C) :-
    C =< 0.
