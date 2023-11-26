% Constants
philosopher(socrates).
philosopher(plato).
philosopher(aristotle).

human(socrates).
human(plato).
human(aristotle).
human(suman).

% Propositions
p_socrates :- philosopher(socrates).
p_plato :- philosopher(plato).
p_aristotle :- philosopher(aristotle).
h_socrates :- human(socrates).
h_plato :- human(plato).
h_aristotle :- human(aristotle).
h_suman :- human(suman).

% Rules
w_socrates :- wise(socrates).
w_plato :- wise(plato).
w_aristotle :- wise(aristotle).

% p_socrates.   h_socrates.   w_socrates.
