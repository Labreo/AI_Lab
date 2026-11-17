% To identify possible diseases based on symptoms.

% Patient symptoms
has_symptom(amit, fever).
has_symptom(amit, cough).
has_symptom(amit, body_pain).

has_symptom(rahul, sneezing).
has_symptom(rahul, runny_nose).
has_symptom(rahul, cough).

has_symptom(john, vomiting).
has_symptom(john, stomach_pain).
has_symptom(john, diarrhea).

% Diagnosis rules
disease(X, flu) :-
has_symptom(X, fever),
has_symptom(X, cough),
has_symptom(X, body_pain).

disease(X, common_cold) :-
has_symptom(X, sneezing),
has_symptom(X, runny_nose),
has_symptom(X, cough).

disease(X, food_poisoning) :-
has_symptom(X, vomiting),
has_symptom(X, stomach_pain),
has_symptom(X, diarrhea).

has_injury(amit, burn).
has_injury(amit, fever).
has_injury(amit, hot).

has_injury(johnithon, acl_tear).
has_injury(johnithon, strained_muscle).
has_injury(johnithon, cramp).

has_injury(sam, cut).
has_injury(sam, bleeding).
has_injury(sam, minor_pain).

first_aid(X, ors_or_oral) :-
has_injury(amit, burn),
has_injury(amit, fever),
has_injury(amit, hot).

first_aid(X, cold_compress) :-
has_injury(johnithon, acl_tear),
has_injury(johnithon, strained_muscle),
has_injury(johnithon, cramp).

first_aid(X, band_aid) :-
has_injury(sam, cut),
has_injury(sam, bleeding),
has_injury(sam, minor_pain).

has_symptom(amit, fatigue).
has_symptom(amit, pale_skin).
has_symptom(rahul, bleeding_gums).
has_symptom(rahul, slow_wound_healing).
has_symptom(john, bone_pain).
has_symptom(john, muscle_weakness).
has_symptom(john, pale_skin).
has_symptom(john, bone_pain).

disease(X, anemia) :-
    has_symptom(X, fatigue),
    has_symptom(X, pale_skin).

disease(X, scurvy) :-
    has_symptom(X, bleeding_gums),
    has_symptom(X, slow_wound_healing).

disease(X, leukemia) :-
    has_symptom(X, bone_pain),
    has_symptom(X, pale_skin).

disease(X, vitamin_d_deficiency) :-
    has_symptom(X, bone_pain),
    has_symptom(X, muscle_weakness).

fitness_goal(amit, weight_loss).
fitness_goal(rahul, muscle_gain).
fitness_goal(john, flexibility).

fitness_recommendation(X, running) :-
fitness_goal(X, weight_loss).

fitness_recommendation(X, weight_training) :-
fitness_goal(X, muscle_gain).

fitness_recommendation(X, yoga) :-
fitness_goal(X, flexibility).

has_eye_symptom(amit, itchy_eyes).
has_eye_symptom(amit, redness).
has_eye_symptom(rahul, blurred_vision).
has_eye_symptom(rahul, eye_strain).
has_eye_symptom(john, dry_eyes).
has_eye_symptom(john, burning_sensation).

eye_condition(X, allergic_conjunctivitis) :-
has_eye_symptom(X, itchy_eyes),
has_eye_symptom(X, redness).

eye_condition(X, refractive_error) :-
has_eye_symptom(X, blurred_vision),
has_eye_symptom(X, eye_strain).

eye_condition(X, dry_eye_syndrome) :-
has_eye_symptom(X, dry_eyes),
has_eye_symptom(X, burning_sensation).
