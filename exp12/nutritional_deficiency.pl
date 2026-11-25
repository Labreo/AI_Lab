% Knowledge base: Nutritional Deficiency Expert System
% Start consultation: ?- go.

:- dynamic yes/1, no/1.

% Main entry point and consultation loop
go :-
    undo,
    write('Nutritional Deficiency Expert System'), nl,
    write('Enter your initial reported symptom (e.g. unusually tired, bleeding gums, bone pain, or list):'), nl,
    consult_loop.

consult_loop :-
    prompt_symptom(Symptom),
    (   Symptom == exit -> write('Consultation ended.'), nl, undo
    ;   Symptom == list -> show_symptoms, consult_loop
    ;   Symptom == none ->
        write('Unrecognized symptom. Type list to view options, or assert another symptom:'), nl,
        consult_loop
    ;   assertz(yes(Symptom)),
        format('Recorded initial symptom: ~w~n~n', [Symptom]),
        (   hypothesis(Deficiency)
        ->  format('~nPossible deficiency: ~w~n', [Deficiency]),
            advice(Deficiency),
            undo
        ;   format('~nNo deficiency could be confirmed with ~w.~n', [Symptom]),
            write('Please assert another symptom (or type exit):'), nl,
            consult_loop
        )
    ).

prompt_symptom(Symptom) :-
    write('|: '),
    read_line_to_string(user_input, Line),
    match_symptom(Line, Symptom).

show_symptoms :-
    nl, write('Available initial symptoms:'), nl,
    write('  1. tired_weak          (unusually tired, fatigue, weakness)'), nl,
    write('  2. bleeding_gums       (gums bleeding easily)'), nl,
    write('  3. bone_pain           (bone, joint or back pain)'), nl,
    write('  4. tingling_numbness   (tingling or numbness in hands/feet)'), nl,
    write('  5. dim_light_vision    (difficulty seeing in dim light)'), nl,
    write('  6. muscle_cramps       (frequent muscle cramps)'), nl,
    write('  7. neck_swelling       (swelling in the front of neck)'), nl,
    write('  8. loss_of_taste       (loss of taste or smell)'), nl,
    write('  9. muscle_twitches     (involuntary muscle or eye spasms)'), nl,
    write(' 10. heart_palpitations   (heart fluttering or palpitations)'), nl,
    write(' 11. mouth_ulcers        (painful mouth sores, red tongue)'), nl,
    write(' 12. feet_swelling       (swelling, fluid retention in legs/feet)'), nl, nl.

% Keyword mapping for free-form user assertion
match_symptom(Line, Symptom) :-
    string_lower(Line, Lower),
    (   sub_string(Lower, _, _, _, 'exit')        -> Symptom = exit
    ;   sub_string(Lower, _, _, _, 'quit')        -> Symptom = exit
    ;   sub_string(Lower, _, _, _, 'list')        -> Symptom = list
    ;   sub_string(Lower, _, _, _, 'help')        -> Symptom = list
    ;   sub_string(Lower, _, _, _, 'tired')       -> Symptom = tired_weak
    ;   sub_string(Lower, _, _, _, 'fatigue')     -> Symptom = tired_weak
    ;   sub_string(Lower, _, _, _, 'weak')        -> Symptom = tired_weak
    ;   sub_string(Lower, _, _, _, 'gum')         -> Symptom = bleeding_gums
    ;   sub_string(Lower, _, _, _, 'bone')        -> Symptom = bone_pain
    ;   sub_string(Lower, _, _, _, 'back')        -> Symptom = bone_pain
    ;   sub_string(Lower, _, _, _, 'tingl')       -> Symptom = tingling_numbness
    ;   sub_string(Lower, _, _, _, 'numb')        -> Symptom = tingling_numbness
    ;   sub_string(Lower, _, _, _, 'dim')         -> Symptom = dim_light_vision
    ;   sub_string(Lower, _, _, _, 'night')       -> Symptom = dim_light_vision
    ;   sub_string(Lower, _, _, _, 'cramp')       -> Symptom = muscle_cramps
    ;   sub_string(Lower, _, _, _, 'neck')        -> Symptom = neck_swelling
    ;   sub_string(Lower, _, _, _, 'goiter')      -> Symptom = neck_swelling
    ;   sub_string(Lower, _, _, _, 'taste')       -> Symptom = loss_of_taste
    ;   sub_string(Lower, _, _, _, 'smell')       -> Symptom = loss_of_taste
    ;   sub_string(Lower, _, _, _, 'twitch')      -> Symptom = muscle_twitches
    ;   sub_string(Lower, _, _, _, 'spasm')       -> Symptom = muscle_twitches
    ;   sub_string(Lower, _, _, _, 'palpitat')    -> Symptom = heart_palpitations
    ;   sub_string(Lower, _, _, _, 'flutter')     -> Symptom = heart_palpitations
    ;   sub_string(Lower, _, _, _, 'ulcer')       -> Symptom = mouth_ulcers
    ;   sub_string(Lower, _, _, _, 'tongue')      -> Symptom = mouth_ulcers
    ;   sub_string(Lower, _, _, _, 'feet')        -> Symptom = feet_swelling
    ;   sub_string(Lower, _, _, _, 'leg')         -> Symptom = feet_swelling
    ;   sub_string(Lower, _, _, _, 'edema')       -> Symptom = feet_swelling
    ;   sub_string(Lower, _, _, _, '12')          -> Symptom = feet_swelling
    ;   sub_string(Lower, _, _, _, '11')          -> Symptom = mouth_ulcers
    ;   sub_string(Lower, _, _, _, '10')          -> Symptom = heart_palpitations
    ;   sub_string(Lower, _, _, _, '1')           -> Symptom = tired_weak
    ;   sub_string(Lower, _, _, _, '2')           -> Symptom = bleeding_gums
    ;   sub_string(Lower, _, _, _, '3')           -> Symptom = bone_pain
    ;   sub_string(Lower, _, _, _, '4')           -> Symptom = tingling_numbness
    ;   sub_string(Lower, _, _, _, '5')           -> Symptom = dim_light_vision
    ;   sub_string(Lower, _, _, _, '6')           -> Symptom = muscle_cramps
    ;   sub_string(Lower, _, _, _, '7')           -> Symptom = neck_swelling
    ;   sub_string(Lower, _, _, _, '8')           -> Symptom = loss_of_taste
    ;   sub_string(Lower, _, _, _, '9')           -> Symptom = muscle_twitches
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
hypothesis(iron_deficiency) :-
    verified(tired_weak),
    ask(pale_eyelids, 'Is your skin or the inside of your eyelids pale').
hypothesis(vitamin_c_deficiency) :-
    verified(bleeding_gums),
    ask(slow_wound_healing, 'Do cuts and wounds heal slowly').
hypothesis(vitamin_d_deficiency) :-
    verified(bone_pain),
    ask(muscle_weakness, 'Do you have muscle weakness').
hypothesis(vitamin_b12_deficiency) :-
    verified(tingling_numbness),
    ask(memory_issues, 'Do you have memory problems or difficulty concentrating').
hypothesis(vitamin_a_deficiency) :-
    verified(dim_light_vision),
    ask(unusual_dry_skin, 'Is your skin unusually dry').
hypothesis(calcium_deficiency) :-
    verified(muscle_cramps),
    ask(brittle_nails, 'Are your nails brittle').
hypothesis(iodine_deficiency) :-
    verified(neck_swelling),
    ask(cold_sensitivity, 'Do you experience unexpected weight gain and extreme cold sensitivity').
hypothesis(zinc_deficiency) :-
    verified(loss_of_taste),
    ask(hair_loss_slow_repair, 'Are you having excessive hair loss or slow skin wound repair').
hypothesis(magnesium_deficiency) :-
    verified(muscle_twitches),
    ask(restless_anxiety, 'Do you suffer from restless sleep, anxiety or irregular heartbeats').
hypothesis(potassium_deficiency) :-
    verified(heart_palpitations),
    ask(bloating_severe_cramps, 'Do you suffer from persistent severe muscle cramps and abdominal bloating').
hypothesis(folate_deficiency) :-
    verified(mouth_ulcers),
    ask(breathless_fatigue, 'Do you experience persistent breathlessness and severe mental fatigue').
hypothesis(protein_deficiency) :-
    verified(feet_swelling),
    ask(muscle_wasting_peeling, 'Are you experiencing visible muscle wasting and peeling skin').

% Dietary recommendations and nutritional guidance
advice(iron_deficiency) :-
    step('Eat spinach, lentils, beans, red meat and jaggery.'),
    step('Take vitamin C (lemon, orange) with meals to improve iron absorption.').
advice(vitamin_c_deficiency) :-
    step('Eat citrus fruits, amla, guava, tomatoes and bell peppers.').
advice(vitamin_d_deficiency) :-
    step('Get 15 to 20 minutes of morning sunlight daily.'),
    step('Eat eggs, fortified milk and fatty fish.').
advice(vitamin_b12_deficiency) :-
    step('Eat dairy products, eggs, fish and fortified cereals.'),
    step('A doctor may advise B12 supplements.').
advice(vitamin_a_deficiency) :-
    step('Eat carrots, sweet potato, papaya, leafy greens and eggs.').
advice(calcium_deficiency) :-
    step('Eat milk, curd, cheese, ragi and green leafy vegetables.'),
    step('Combine with vitamin D for better absorption.').
advice(iodine_deficiency) :-
    step('Use iodized salt in everyday cooking and meal preparation.'),
    step('Consume saltwater fish, seaweed, dairy products and eggs.').
advice(zinc_deficiency) :-
    step('Eat pumpkin seeds, nuts, chickpeas, lentils and whole grains.'),
    step('Include shellfish, lean poultry and zinc-fortified breakfast cereals.').
advice(magnesium_deficiency) :-
    step('Eat almonds, cashews, pumpkin seeds, dark chocolate and spinach.'),
    step('Consider drinking mineral-rich water and taking warm Epsom salt baths.').
advice(potassium_deficiency) :-
    step('Eat bananas, coconut water, sweet potatoes, avocados and oranges.'),
    step('Check with a physician regarding any diuretic medicines or electrolyte balance.').
advice(folate_deficiency) :-
    step('Eat dark green leafy vegetables, broccoli, asparagus, peas and kidney beans.'),
    step('Take folic acid supplements as prescribed, particularly during pregnancy.').
advice(protein_deficiency) :-
    step('Eat protein-dense foods: lentils, paneer, tofu, eggs, chicken and beans.'),
    step('Ensure an adequate protein portion is distributed across all daily meals.').

% Output formatting and working memory cleanup
step(Text) :-
    format('  - ~w~n', [Text]).

undo :-
    retractall(yes(_)),
    retractall(no(_)).
