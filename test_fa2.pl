
:- dynamic yes/1, no/1.

go :-
    undo,
    write('First-Aid Expert System'), nl,
    write('Enter your initial observed symptom or condition:'), nl,
    consult_loop.

consult_loop :-
    prompt_initial_symptom(Symptom),
    (   Symptom == exit -> write('Consultation ended.'), nl, undo
    ;   Symptom == none ->
        write('Unrecognized symptom. Please assert another symptom or condition:'), nl,
        consult_loop
    ;   assertz(yes(Symptom)),
        format('Recorded initial symptom: ~w~n~n', [Symptom]),
        (   hypothesis(Injury)
        ->  format('~nObserved condition: ~w~n', [Injury]),
            advice(Injury),
            undo
        ;   format('~nNo condition could be confirmed with ~w.~n', [Symptom]),
            write('Please assert another symptom or condition (or type exit):'), nl,
            consult_loop
        )
    ).

prompt_initial_symptom(Symptom) :-
    write('|: '),
    read_line_to_string(user_input, Line),
    match_symptom(Line, Symptom).

match_symptom(Line, Symptom) :-
    string_lower(Line, Lower),
    (   sub_string(Lower, _, _, _, 'exit')  -> Symptom = exit
    ;   sub_string(Lower, _, _, _, 'quit')  -> Symptom = exit
    ;   sub_string(Lower, _, _, _, 'speak') -> Symptom = unable_to_speak
    ;   sub_string(Lower, _, _, _, 'cough') -> Symptom = unable_to_speak
    ;   sub_string(Lower, _, _, _, 'chok')  -> Symptom = unable_to_speak
    ;   sub_string(Lower, _, _, _, 'bleed') -> Symptom = heavy_bleeding
    ;   sub_string(Lower, _, _, _, 'burn')  -> Symptom = heat_injury
    ;   Symptom = none
    ).

verified(Key) :- yes(Key).

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
    verified(unable_to_speak),
    ask(clutching_throat, 'Is the person clutching their throat with their hands').

hypothesis(severe_bleeding) :-
    verified(heavy_bleeding),
    ask(continuous_bleeding, 'Does the bleeding continue after pressing on the wound').

hypothesis(burn) :-
    verified(heat_injury),
    ask(blistered_skin, 'Is the skin red, painful or blistered').

advice(choking) :-
    write('  - Perform 5 back blows and 5 abdominal thrusts (Heimlich maneuver).'), nl.
advice(severe_bleeding) :-
    write('  - Press firmly on the wound with a clean cloth.'), nl.
advice(burn) :-
    write('  - Cool the burn under running tap water for at least 10 minutes.'), nl.

undo :-
    retractall(yes(_)),
    retractall(no(_)).
