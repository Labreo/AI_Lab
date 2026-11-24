% Expert system: identify possible nutritional deficiencies from reported symptoms.
% Start with:  ?- go.   and answer each question with yes. or no.

:- dynamic yes/1, no/1.

go :-
    undo,
    write('Nutritional Deficiency Expert System'), nl,
    write('Answer each question with yes. or no.'), nl, nl,
    (   hypothesis(Deficiency)
    ->  format('~nPossible deficiency: ~w~n', [Deficiency]),
        advice(Deficiency)
    ;   write('No deficiency identified from the symptoms given.'), nl
    ),
    write('Note: this is only a guide, please consult a doctor.'), nl,
    undo.

% Hypotheses: each deficiency needs all of its symptoms.
hypothesis(iron_deficiency) :-
    ask('Do you feel unusually tired or weak'),
    ask('Is your skin or the inside of your eyelids pale').
hypothesis(vitamin_c_deficiency) :-
    ask('Do your gums bleed easily'),
    ask('Do cuts and wounds heal slowly').
hypothesis(vitamin_d_deficiency) :-
    ask('Do you have bone or back pain'),
    ask('Do you have muscle weakness').
hypothesis(vitamin_b12_deficiency) :-
    ask('Do you have tingling or numbness in your hands or feet'),
    ask('Do you have memory problems or difficulty concentrating').
hypothesis(vitamin_a_deficiency) :-
    ask('Do you have difficulty seeing in dim light'),
    ask('Is your skin unusually dry').
hypothesis(calcium_deficiency) :-
    ask('Do you get frequent muscle cramps'),
    ask('Are your nails brittle').
hypothesis(iodine_deficiency) :-
    ask('Do you have noticeable swelling in the front of your neck'),
    ask('Do you experience unexpected weight gain and extreme cold sensitivity').
hypothesis(zinc_deficiency) :-
    ask('Have you experienced a loss of taste or smell'),
    ask('Are you having excessive hair loss or slow skin wound repair').
hypothesis(magnesium_deficiency) :-
    ask('Do you experience involuntary muscle twitches or eye spasms'),
    ask('Do you suffer from restless sleep, anxiety or irregular heartbeats').
hypothesis(potassium_deficiency) :-
    ask('Do you feel abnormal heart palpitations or fluttering'),
    ask('Do you suffer from persistent severe muscle cramps and abdominal bloating').
hypothesis(folate_deficiency) :-
    ask('Do you have painful mouth ulcers or a swollen red tongue'),
    ask('Do you experience persistent breathlessness and severe mental fatigue').
hypothesis(protein_deficiency) :-
    ask('Do you have swelling or fluid retention in your feet or legs'),
    ask('Are you experiencing visible muscle wasting and peeling skin').

% Dietary recommendation for each deficiency.
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
