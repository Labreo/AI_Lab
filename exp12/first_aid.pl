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
hypothesis(choking) :-
    ask('Is the person unable to speak, breathe, or cough loudly'),
    ask('Is the person clutching their throat with their hands').
hypothesis(severe_bleeding) :-
    ask('Is there heavy bleeding that soaks through cloth'),
    ask('Does the bleeding continue after pressing on the wound').
hypothesis(electric_shock) :-
    ask('Did the person come into contact with a live electrical source'),
    ask('Is there numbness, difficulty breathing or visible entry and exit burns').
hypothesis(heat_stroke) :-
    ask('Has the person been exposed to extreme heat and has hot, dry skin or high fever'),
    ask('Is the person confused, dizzy or fainting').
hypothesis(snake_bite) :-
    ask('Was the person bitten by a snake or venomous reptile'),
    ask('Are there visible puncture marks, severe pain or spreading swelling').
hypothesis(burn) :-
    ask('Did the injury come from heat, fire or a hot liquid'),
    ask('Is the skin red, painful or blistered').
hypothesis(fracture) :-
    ask('Is there severe pain after a fall or a blow'),
    ask('Is the limb swollen or bent out of shape').
hypothesis(concussion) :-
    ask('Did the person receive a forceful blow or impact to the head'),
    ask('Is there dizziness, nausea, confusion or brief memory loss').
hypothesis(sprain) :-
    ask('Is there swelling or pain around a joint'),
    ask('Is it painful to move the joint or put weight on it').
hypothesis(chemical_eye_burn) :-
    ask('Did an acid, alkali or cleaning chemical splash into the eye'),
    ask('Is there acute burning pain, intense redness and constant tearing').
hypothesis(minor_cut) :-
    ask('Is there a small cut or scrape on the skin'),
    ask('Is the bleeding light').
hypothesis(nosebleed) :-
    ask('Is blood actively flowing from one or both nostrils'),
    ask('Did it start after trauma, nose picking or dry air').

% First-aid measures for each condition.
advice(choking) :-
    step('Deliver 5 firm back blows between shoulder blades with the heel of your hand.'),
    step('Perform 5 quick inward and upward abdominal thrusts (Heimlich maneuver).'),
    step('Call emergency services immediately if the airway remains obstructed.').
advice(severe_bleeding) :-
    step('Press firmly on the wound with a clean cloth and keep pressing.'),
    step('Raise the injured part above the level of the heart.'),
    step('Call emergency services immediately.').
advice(electric_shock) :-
    step('Do not touch the victim until the power source is turned off safely.'),
    step('Check breathing and pulse; begin CPR immediately if unresponsive.'),
    step('Call an ambulance and treat any electrical burns with sterile coverings.').
advice(heat_stroke) :-
    step('Move the person to a cool, shaded or air-conditioned area immediately.'),
    step('Rapidly cool the body by spraying cool water and fanning continuously.'),
    step('Call emergency medical services without delay; do not give hot fluids.').
advice(snake_bite) :-
    step('Keep the victim calm, still, and immobilize the bitten limb below heart level.'),
    step('Do NOT cut the wound, suck out venom, or apply an ice pack or tight tourniquet.'),
    step('Transport the patient immediately to the nearest hospital for antivenom.').
advice(burn) :-
    step('Cool the burn under running tap water for at least 10 minutes.'),
    step('Do not apply ice, butter or toothpaste and do not burst blisters.'),
    step('Cover loosely with a clean non-stick dressing.').
advice(fracture) :-
    step('Keep the injured limb still and support it in the position found.'),
    step('Do not try to straighten the limb.'),
    step('Apply a cold pack and take the person to hospital.').
advice(concussion) :-
    step('Have the person rest quietly and avoid physical exertion and screens.'),
    step('Apply an ice pack wrapped in a cloth to reduce swelling on the scalp.'),
    step('Seek medical evaluation; watch closely for worsening vomiting or drowsiness.').
advice(sprain) :-
    step('Rest the joint and apply a cold compress for 15 to 20 minutes.'),
    step('Wrap it with an elastic bandage and keep it raised.'),
    step('See a doctor if the pain or swelling does not improve.').
advice(chemical_eye_burn) :-
    step('Flush the eye continuously with clean, gentle running water for 15 to 20 minutes.'),
    step('Keep the eyelid held open during irrigation.'),
    step('Do not rub the eye; rush to the nearest emergency room immediately.').
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
