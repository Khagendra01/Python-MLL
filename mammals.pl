% mammals.pl

:- discontiguous animal/1.

mammal(X) :- animal(X), has_hair(X), gives_birth_to_live_young(X).
warm_blooded(X) :- mammal(X).

% Some example facts
animal(dog).
has_hair(dog).
gives_birth_to_live_young(dog).

animal(bird).
has_feathers(bird).
lays_eggs(bird).
