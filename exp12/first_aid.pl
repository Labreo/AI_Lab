% Expert system: recommend first-aid measures from observed injuries and symptoms.
% Start with:  ?- go.   and answer each question with yes. or no.

:- dynamic yes/1, no/1.

go :-
    undo,
    write('First-Aid Expert System'), nl,
    write('Answer each question with yes. or no.'), nl, nl,
    (   hypothesis(Injury)
    ->  format('~nObserved condition: ~w~n', [Injury]),
        advice(Injury)
    ;   write('No matching condition found. Please consult a doctor.'), nl
    ),
    undo.

% Hypotheses, tried from the most serious to the least serious.
hypothesis(severe_bleeding) :-
    ask('Is there heavy bleeding that soaks through cloth'),
    ask('Does the bleeding continue after pressing on the wound').
hypothesis(burn) :-
    ask('Did the injury come from heat, fire or a hot liquid'),
    ask('Is the skin red, painful or blistered').
hypothesis(fracture) :-
    ask('Is there severe pain after a fall or a blow'),
    ask('Is the limb swollen or bent out of shape').
hypothesis(sprain) :-
    ask('Is there swelling or pain around a joint'),
    ask('Is it painful to move the joint or put weight on it').
hypothesis(minor_cut) :-
    ask('Is there a small cut or scrape on the skin'),
    ask('Is the bleeding light').
hypothesis(nosebleed) :-
    ask('Is blood coming from the nose').

% First-aid measures for each condition.
advice(severe_bleeding) :-
    step('Press firmly on the wound with a clean cloth and keep pressing.'),
    step('Raise the injured part above the level of the heart.'),
    step('Call emergency services immediately.').
advice(burn) :-
    step('Cool the burn under running tap water for at least 10 minutes.'),
    step('Do not apply ice, butter or toothpaste and do not burst blisters.'),
    step('Cover loosely with a clean non-stick dressing.').
advice(fracture) :-
    step('Keep the injured limb still and support it in the position found.'),
    step('Do not try to straighten the limb.'),
    step('Apply a cold pack and take the person to hospital.').
advice(sprain) :-
    step('Rest the joint and apply a cold compress for 15 to 20 minutes.'),
    step('Wrap it with an elastic bandage and keep it raised.'),
    step('See a doctor if the pain or swelling does not improve.').
advice(minor_cut) :-
    step('Wash the wound with clean water and mild soap.'),
    step('Apply an antiseptic and cover it with a band-aid.'),
    step('Change the dressing daily and keep it clean and dry.').
advice(nosebleed) :-
    step('Sit upright and lean slightly forward.'),
    step('Pinch the soft part of the nose for 10 minutes.'),
    step('Seek medical help if it lasts longer than 20 minutes.').

step(Text) :-
    format('  - ~w~n', [Text]).

% ask/1 uses stored answers first and asks the user only if the answer is unknown.
ask(Question) :-
    (   yes(Question) -> true
    ;   no(Question)  -> fail
    ;   format('~w? (yes/no)~n', [Question]),
        read(Reply),
        (   Reply == yes -> assertz(yes(Question))
        ;   assertz(no(Question)), fail
        )
    ).

undo :-
    retractall(yes(_)),
    retractall(no(_)).
