% Expert system: recommend exercises from the user's fitness goal and physical capability.
% Start with:  ?- go.   and answer each question with yes. or no.

:- dynamic yes/1, no/1.

go :-
    undo,
    write('Fitness Expert System'), nl,
    write('Answer each question with yes. or no.'), nl, nl,
    (   setof(Exercise, exercise(Exercise), List)
    ->  nl, write('Recommended exercises:'), nl,
        forall(member(E, List), describe(E))
    ;   write('No exercise could be matched. Please consult a trainer.'), nl
    ),
    undo.

% Goals reported by the user.
goal(weight_loss)     :- ask('Is your goal to lose weight').
goal(muscle_gain)     :- ask('Is your goal to build muscle').
goal(flexibility)     :- ask('Is your goal to improve flexibility').
goal(endurance)       :- ask('Is your goal to improve stamina and endurance').
goal(core_stability)  :- ask('Is your goal to strengthen core and posture').
goal(stress_relief)   :- ask('Is your goal stress relief and mental relaxation').

% Physical capabilities reported by the user.
active        :- ask('Do you already exercise 3 or more times a week').
joint_problem :- ask('Do you have knee, back or joint pain').

% Rules: goal + capability -> exercise.
exercise(brisk_walking) :- goal(weight_loss), \+ active.
exercise(running)       :- goal(weight_loss), active, \+ joint_problem.
exercise(swimming)      :- ( goal(weight_loss) ; goal(endurance) ), joint_problem.
exercise(cycling)       :- goal(endurance), \+ joint_problem.
exercise(bodyweight_exercises) :- goal(muscle_gain), \+ active.
exercise(weight_training)      :- goal(muscle_gain), active, \+ joint_problem.
exercise(resistance_bands)     :- goal(muscle_gain), joint_problem.
exercise(yoga)       :- goal(flexibility).
exercise(stretching) :- goal(flexibility), joint_problem.
exercise(pilates)         :- goal(core_stability), \+ joint_problem.
exercise(chair_exercises) :- goal(core_stability), joint_problem.
exercise(tai_chi)         :- ( goal(flexibility) ; goal(stress_relief) ), joint_problem.
exercise(deep_breathing_meditation) :- goal(stress_relief), \+ joint_problem.
exercise(jump_rope)       :- goal(endurance), active, \+ joint_problem.
exercise(water_aerobics)  :- goal(weight_loss), joint_problem, \+ active.

describe(brisk_walking) :-
    step('Brisk walking: 30 minutes a day, 5 days a week.').
describe(running) :-
    step('Running or jogging: 20 to 30 minutes, 3 to 4 days a week.').
describe(swimming) :-
    step('Swimming: low-impact cardio, 30 minutes, 3 days a week.').
describe(cycling) :-
    step('Cycling: 30 to 45 minutes, 3 to 4 days a week.').
describe(bodyweight_exercises) :-
    step('Push-ups, squats and planks: 3 sets of 10, 3 days a week.').
describe(weight_training) :-
    step('Weight training: compound lifts, 3 to 4 days a week.').
describe(resistance_bands) :-
    step('Resistance band workouts: gentle on the joints, 3 days a week.').
describe(yoga) :-
    step('Yoga: 20 to 30 minutes daily.').
describe(stretching) :-
    step('Slow stretching: hold each stretch for 20 seconds, daily.').
describe(pilates) :-
    step('Pilates: mat workout for core and spine strength, 30 minutes, 3 days a week.').
describe(chair_exercises) :-
    step('Seated core exercises: seated leg raises and torso twists, 20 minutes daily.').
describe(tai_chi) :-
    step('Tai Chi: gentle flowing movements for joint flexibility and calm, 20 minutes daily.').
describe(deep_breathing_meditation) :-
    step('Mindful meditation and pranayama breathwork: 15 to 20 minutes daily.').
describe(jump_rope) :-
    step('Jump rope: high-intensity cardio intervals, 15 minutes, 3 days a week.').
describe(water_aerobics) :-
    step('Water aerobics: zero-impact resistance in pool, 30 to 40 minutes, 3 days a week.').

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
