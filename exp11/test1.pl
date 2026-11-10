% Logical inference using Resolution in Prolog
% Knowledge base (Marcus problem) written as Horn clauses.

man(marcus).
pompeian(marcus).
ruler(caesar).
tryassassinate(marcus, caesar).

roman(X)         :- pompeian(X).
person(X)        :- man(X).
notloyalto(X, Y) :- person(X), ruler(Y), tryassassinate(X, Y).
hate(X, caesar)  :- roman(X), notloyalto(X, caesar).

% refute(Q): resolution refutation.
% Add the negated goal, then repeatedly resolve the first literal of the
% current resolvent with a clause whose head unifies with it.
% Deriving the empty clause [] proves Q.
refute(Query) :-
    format('Negated goal added to KB: ~~~w~n', [Query]),
    resolve([Query], 1).

resolve([], _) :-
    format('Empty clause [] derived -> contradiction, so the query is TRUE~n').
resolve([Goal|Rest], Step) :-
    clause(Goal, Body),
    body_to_list(Body, Literals),
    append(Literals, Rest, Resolvent),
    format('Step ~w: resolve ~~~w~n', [Step, Goal]),
    (   Body == true
    ->  format('        with fact : ~w~n', [Goal])
    ;   format('        with rule : ~w :- ~w~n', [Goal, Body])
    ),
    format('        resolvent : '), show(Resolvent), nl,
    Next is Step + 1,
    resolve(Resolvent, Next).

body_to_list(true, []) :- !.
body_to_list((A, B), [A|Rest]) :- !, body_to_list(B, Rest).
body_to_list(A, [A]).

show([]) :- write('[]').
show([L]) :- !, format('~~~w', [L]).
show([L|Ls]) :- format('~~~w v ', [L]), show(Ls).

query(Q) :-
    (   refute(Q)
    ->  true
    ;   format('No empty clause can be derived -> ~w cannot be proved~n', [Q])
    ).
