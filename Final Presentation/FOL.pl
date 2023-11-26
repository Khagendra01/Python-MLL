% Constants
philosopher(socrates).
philosopher(plato).
philosopher(aristotle).

human(socrates). 
human(plato).     
human(aristotle). 
human(suman).

% Rules
wise(socrates).
wise(plato).
wise(aristotle).
% wise(X) :- human(X).

% Formulas
forall(X, philosopher(X)).
forall(X, wise(X) -> philosopher(X)).
