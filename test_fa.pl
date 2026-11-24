
:- dynamic yes/1, no/1.

go :-
    undo,
    write('First-Aid Expert System'), nl,
    write('Enter your initial observed symptom or condition:'), nl,
    consult_loop.

consult_loop :-
    prompt_initial_symptom(Symptom),
    (   Symptom == none -> write('No initial symptom provided.'), nl
    ;   assertz(yes(Symptom)),
        format('Initial symptom recorded: ~w~n~n', [Symptom]),
        (   hypothesis(Injury)
        ->  format('~nObserved condition: ~w~n', [Injury]),
            advice(Injury),
            undo
        ;   format('~nNo condition could be confirmed with ~w.~n', [Symptom]),
            write('Would you like to assert another symptom? (yes/no): '),
            read_reply(R),
            (   R == yes -> consult_loop
            ;   write('Please consult emergency services or a doctor.'), nl, undo
            )
        )
    ).

prompt_initial_symptom(Symptom) :-
    write('|: '),
    read_line_to_string(user_input, Line),
    match_symptom(Line, Symptom).

match_symptom(Line, Symptom) :-
    string_lower(Line, Lower),
    (   sub_string(Lower, _, _, _, 'speak') -> Symptom = unable_to_speak
    ;   sub_string(Lower, _, _, _, 'cough') -> Symptom = unable_to_speak
    ;   sub_string(Lower, _, _, _, 'chok')  -> Symptom = unable_to_speak
    ;   sub_string(Lower, _, _, _, 'bleed') -> Symptom = heavy_bleeding
    ;   sub_string(Lower, _, _, _, 'burn')  -> Symptom = heat_injury
    ;   Symptom = none
    ).

ask(Key, Question) :-
    (   yes(Key) -> true
    ;   no(Key)  -> fail
    ;   format('~w? (yes/no)~n|: ', [Question]),
        read_reply(Reply),
        (   Reply == yes -> assertz(yes(Key))
        ;   assertz(no(Key)), fail
        )
    ).

read_reply(Reply) :-
    read_line_to_string(user_input, Line),
    string_lower(Line, Lower),
    (   sub_string(Lower, _, _, _, 'y') -> Reply = yes
    ;   Reply = no
    ).

hypothesis(choking) :-
    ask(unable_to_speak, 'Is the person unable to speak, breathe, or cough loudly'),
    ask(clutching_throat, 'Is the person clutching their throat with their hands').

hypothesis(severe_bleeding) :-
    ask(heavy_bleeding, 'Is there heavy bleeding that soaks through cloth'),
    ask(continuous_bleeding, 'Does the bleeding continue after pressing on the wound').

advice(choking) :-
    write('  - Perform 5 back blows and 5 abdominal thrusts (Heimlich maneuver).'), nl.
advice(severe_bleeding) :-
    write('  - Press firmly on the wound with a clean cloth.'), nl.

undo :-
    retractall(yes(_)),
    retractall(no(_)).
