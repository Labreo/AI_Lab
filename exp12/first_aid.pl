% Knowledge base: First Aid Diagnostic Expert System
% Start consultation: ?- go.

:- dynamic yes/1, no/1.

% Main entry point and consultation loop
go :-
    undo,
    write('First-Aid Expert System'), nl,
    write('Enter your initial observed symptom or condition (e.g. Cough unable to speak, heavy bleeding, burn, or list):'), nl,
    consult_loop.

consult_loop :-
    prompt_symptom(Symptom),
    (   Symptom == exit -> write('Consultation ended.'), nl, undo
    ;   Symptom == list -> show_symptoms, consult_loop
    ;   Symptom == none ->
        write('Unrecognized symptom. Type list to view options, or assert another condition:'), nl,
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

prompt_symptom(Symptom) :-
    write('|: '),
    read_line_to_string(user_input, Line),
    match_symptom(Line, Symptom).

show_symptoms :-
    nl, write('Available initial symptoms / conditions:'), nl,
    write('  1. unable_to_speak      (cough, choking, cannot breathe)'), nl,
    write('  2. heavy_bleeding       (bleeding through cloth)'), nl,
    write('  3. electric_contact     (electrical wire, outlet contact)'), nl,
    write('  4. extreme_heat         (heat stroke, hot dry skin)'), nl,
    write('  5. snake_bite           (venomous reptile or snake bite)'), nl,
    write('  6. heat_injury          (burn from fire, hot liquid, iron)'), nl,
    write('  7. severe_pain_fall     (bone fracture after fall or blow)'), nl,
    write('  8. head_impact          (blow to head, concussion)'), nl,
    write('  9. joint_swelling       (sprain, twisted ankle or joint)'), nl,
    write(' 10. chemical_splash      (cleaning chemical or acid in eye)'), nl,
    write(' 11. small_cut            (minor cut, scrape on skin)'), nl,
    write(' 12. nose_bleeding        (blood flowing from nostrils)'), nl, nl.

% Keyword mapping for free-form user assertion
match_symptom(Line, Symptom) :-
    string_lower(Line, Lower),
    (   sub_string(Lower, _, _, _, 'exit')        -> Symptom = exit
    ;   sub_string(Lower, _, _, _, 'quit')        -> Symptom = exit
    ;   sub_string(Lower, _, _, _, 'list')        -> Symptom = list
    ;   sub_string(Lower, _, _, _, 'help')        -> Symptom = list
    ;   sub_string(Lower, _, _, _, 'nose')        -> Symptom = nose_bleeding
    ;   sub_string(Lower, _, _, _, 'chemical')    -> Symptom = chemical_splash
    ;   sub_string(Lower, _, _, _, 'concussion')  -> Symptom = head_impact
    ;   sub_string(Lower, _, _, _, 'head')        -> Symptom = head_impact
    ;   sub_string(Lower, _, _, _, 'fracture')    -> Symptom = severe_pain_fall
    ;   sub_string(Lower, _, _, _, 'broken')      -> Symptom = severe_pain_fall
    ;   sub_string(Lower, _, _, _, 'bone')        -> Symptom = severe_pain_fall
    ;   sub_string(Lower, _, _, _, 'sprain')      -> Symptom = joint_swelling
    ;   sub_string(Lower, _, _, _, 'joint')       -> Symptom = joint_swelling
    ;   sub_string(Lower, _, _, _, 'ankle')       -> Symptom = joint_swelling
    ;   sub_string(Lower, _, _, _, 'snake')       -> Symptom = snake_bite
    ;   sub_string(Lower, _, _, _, 'bite')        -> Symptom = snake_bite
    ;   sub_string(Lower, _, _, _, 'burn')        -> Symptom = heat_injury
    ;   sub_string(Lower, _, _, _, 'fire')        -> Symptom = heat_injury
    ;   sub_string(Lower, _, _, _, 'scald')       -> Symptom = heat_injury
    ;   sub_string(Lower, _, _, _, 'heat_stroke') -> Symptom = extreme_heat
    ;   sub_string(Lower, _, _, _, 'sun')         -> Symptom = extreme_heat
    ;   sub_string(Lower, _, _, _, 'electric')    -> Symptom = electric_contact
    ;   sub_string(Lower, _, _, _, 'shock')       -> Symptom = electric_contact
    ;   sub_string(Lower, _, _, _, 'speak')       -> Symptom = unable_to_speak
    ;   sub_string(Lower, _, _, _, 'cough')       -> Symptom = unable_to_speak
    ;   sub_string(Lower, _, _, _, 'chok')        -> Symptom = unable_to_speak
    ;   sub_string(Lower, _, _, _, 'cut')         -> Symptom = small_cut
    ;   sub_string(Lower, _, _, _, 'scrape')      -> Symptom = small_cut
    ;   sub_string(Lower, _, _, _, 'heavy_bleed') -> Symptom = heavy_bleeding
    ;   sub_string(Lower, _, _, _, 'bleed')       -> Symptom = heavy_bleeding
    ;   sub_string(Lower, _, _, _, 'blood')       -> Symptom = heavy_bleeding
    ;   sub_string(Lower, _, _, _, '12')          -> Symptom = nose_bleeding
    ;   sub_string(Lower, _, _, _, '11')          -> Symptom = small_cut
    ;   sub_string(Lower, _, _, _, '10')          -> Symptom = chemical_splash
    ;   sub_string(Lower, _, _, _, '1')           -> Symptom = unable_to_speak
    ;   sub_string(Lower, _, _, _, '2')           -> Symptom = heavy_bleeding
    ;   sub_string(Lower, _, _, _, '3')           -> Symptom = electric_contact
    ;   sub_string(Lower, _, _, _, '4')           -> Symptom = extreme_heat
    ;   sub_string(Lower, _, _, _, '5')           -> Symptom = snake_bite
    ;   sub_string(Lower, _, _, _, '6')           -> Symptom = heat_injury
    ;   sub_string(Lower, _, _, _, '7')           -> Symptom = severe_pain_fall
    ;   sub_string(Lower, _, _, _, '8')           -> Symptom = head_impact
    ;   sub_string(Lower, _, _, _, '9')           -> Symptom = joint_swelling
    ;   Symptom = none
    ).

% Working memory verification and interactive questions
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

% Diagnostic rules and hypotheses
hypothesis(choking) :-
    verified(unable_to_speak),
    ask(clutching_throat, 'Is the person clutching their throat with their hands').
hypothesis(severe_bleeding) :-
    verified(heavy_bleeding),
    ask(continuous_bleeding, 'Does the bleeding continue after pressing on the wound').
hypothesis(electric_shock) :-
    verified(electric_contact),
    ask(shock_symptoms, 'Is there numbness, difficulty breathing or visible entry and exit burns').
hypothesis(heat_stroke) :-
    verified(extreme_heat),
    ask(heat_fainting, 'Is the person confused, dizzy or fainting').
hypothesis(snake_bite) :-
    verified(snake_bite),
    ask(bite_swelling, 'Are there visible puncture marks, severe pain or spreading swelling').
hypothesis(burn) :-
    verified(heat_injury),
    ask(blistered_skin, 'Is the skin red, painful or blistered').
hypothesis(fracture) :-
    verified(severe_pain_fall),
    ask(deformed_limb, 'Is the limb swollen or bent out of shape').
hypothesis(concussion) :-
    verified(head_impact),
    ask(concussion_dizziness, 'Is there dizziness, nausea, confusion or brief memory loss').
hypothesis(sprain) :-
    verified(joint_swelling),
    ask(joint_movement_pain, 'Is it painful to move the joint or put weight on it').
hypothesis(chemical_eye_burn) :-
    verified(chemical_splash),
    ask(eye_burning_pain, 'Is there acute burning pain, intense redness and constant tearing').
hypothesis(minor_cut) :-
    verified(small_cut),
    ask(light_bleeding, 'Is the bleeding light').
hypothesis(nosebleed) :-
    verified(nose_bleeding),
    ask(nose_trauma, 'Did it start after trauma, nose picking or dry air').

% Treatment recommendations and procedural advice
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

% Output formatting and working memory cleanup
step(Text) :-
    format('  - ~w~n', [Text]).

undo :-
    retractall(yes(_)),
    retractall(no(_)).
