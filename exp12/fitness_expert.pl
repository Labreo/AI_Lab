% Knowledge base: Fitness and Exercise Recommendation Expert System
% Start consultation: ?- go.

:- dynamic yes/1, no/1.

% Main entry point and consultation loop
go :-
    undo,
    write('Fitness Expert System'), nl,
    write('Enter your primary fitness goal (e.g. weight loss, muscle gain, endurance, flexibility, core stability, stress relief, or list):'), nl,
    consult_loop.

consult_loop :-
    prompt_goal(Goal),
    (   Goal == exit -> write('Consultation ended.'), nl, undo
    ;   Goal == list -> show_goals, consult_loop
    ;   Goal == none ->
        write('Unrecognized goal. Type list to view available options, or assert another goal:'), nl,
        consult_loop
    ;   assertz(yes(Goal)),
        format('Recorded primary goal: ~w~n~n', [Goal]),
        (   setof(Exercise, exercise(Exercise), List)
        ->  nl, write('Recommended exercises:'), nl,
            forall(member(E, List), describe(E)),
            undo
        ;   format('~nNo exercise could be matched for ~w.~n', [Goal]),
            write('Please assert another goal (or type exit):'), nl,
            consult_loop
        )
    ).

prompt_goal(Goal) :-
    write('|: '),
    read_line_to_string(user_input, Line),
    match_goal(Line, Goal).

show_goals :-
    nl, write('Available fitness goals:'), nl,
    write('  1. weight_loss     (lose weight, burn fat, slim down)'), nl,
    write('  2. muscle_gain     (build muscle, hypertrophy, strength)'), nl,
    write('  3. endurance       (cardio stamina, aerobic capacity)'), nl,
    write('  4. flexibility     (mobility, stretching, range of motion)'), nl,
    write('  5. core_stability  (strengthen core, posture, spinal support)'), nl,
    write('  6. stress_relief   (mental relaxation, calm, meditation)'), nl, nl.

% Keyword mapping for free-form user assertion
match_goal(Line, Goal) :-
    string_lower(Line, Lower),
    (   sub_string(Lower, _, _, _, 'exit')       -> Goal = exit
    ;   sub_string(Lower, _, _, _, 'quit')       -> Goal = exit
    ;   sub_string(Lower, _, _, _, 'list')       -> Goal = list
    ;   sub_string(Lower, _, _, _, 'help')       -> Goal = list
    ;   sub_string(Lower, _, _, _, 'weight')     -> Goal = weight_loss
    ;   sub_string(Lower, _, _, _, 'fat')        -> Goal = weight_loss
    ;   sub_string(Lower, _, _, _, 'slim')       -> Goal = weight_loss
    ;   sub_string(Lower, _, _, _, 'muscle')     -> Goal = muscle_gain
    ;   sub_string(Lower, _, _, _, 'strength')   -> Goal = muscle_gain
    ;   sub_string(Lower, _, _, _, 'endur')      -> Goal = endurance
    ;   sub_string(Lower, _, _, _, 'stamina')    -> Goal = endurance
    ;   sub_string(Lower, _, _, _, 'cardio')     -> Goal = endurance
    ;   sub_string(Lower, _, _, _, 'flex')       -> Goal = flexibility
    ;   sub_string(Lower, _, _, _, 'stretch')    -> Goal = flexibility
    ;   sub_string(Lower, _, _, _, 'core')       -> Goal = core_stability
    ;   sub_string(Lower, _, _, _, 'posture')    -> Goal = core_stability
    ;   sub_string(Lower, _, _, _, 'stress')     -> Goal = stress_relief
    ;   sub_string(Lower, _, _, _, 'relax')      -> Goal = stress_relief
    ;   sub_string(Lower, _, _, _, 'calm')       -> Goal = stress_relief
    ;   sub_string(Lower, _, _, _, '1')          -> Goal = weight_loss
    ;   sub_string(Lower, _, _, _, '2')          -> Goal = muscle_gain
    ;   sub_string(Lower, _, _, _, '3')          -> Goal = endurance
    ;   sub_string(Lower, _, _, _, '4')          -> Goal = flexibility
    ;   sub_string(Lower, _, _, _, '5')          -> Goal = core_stability
    ;   sub_string(Lower, _, _, _, '6')          -> Goal = stress_relief
    ;   Goal = none
    ).

% Working memory verification and interactive questions
goal(G) :- yes(G).

active :-
    ask(is_active, 'Do you already exercise 3 or more times a week').

joint_problem :-
    ask(has_joint_pain, 'Do you have knee, back or joint pain').

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

% Recommendation rules: goal + capability -> exercise
exercise(brisk_walking)             :- goal(weight_loss), \+ active.
exercise(running)                   :- goal(weight_loss), active.
exercise(water_aerobics)            :- goal(weight_loss), joint_problem.
exercise(bodyweight_exercises)      :- goal(muscle_gain), \+ active.
exercise(weight_training)           :- goal(muscle_gain), active.
exercise(resistance_bands)          :- goal(muscle_gain), joint_problem.
exercise(swimming)                  :- goal(endurance), joint_problem.
exercise(cycling)                   :- goal(endurance), \+ joint_problem.
exercise(jump_rope)                 :- goal(endurance), active.
exercise(yoga)                      :- goal(flexibility), \+ joint_problem.
exercise(stretching)                :- goal(flexibility), joint_problem.
exercise(pilates)                   :- goal(core_stability), \+ joint_problem.
exercise(chair_exercises)           :- goal(core_stability), joint_problem.
exercise(tai_chi)                   :- goal(stress_relief), joint_problem.
exercise(deep_breathing_meditation) :- goal(stress_relief), \+ joint_problem.

% Exercise descriptions and workout guidelines
describe(brisk_walking) :-
    step('Brisk walking: 30 minutes a day, 5 days a week.').
describe(running) :-
    step('Running or jogging: 20 to 30 minutes, 3 to 4 days a week.').
describe(water_aerobics) :-
    step('Water aerobics: zero-impact resistance in pool, 30 to 40 minutes, 3 days a week.').
describe(bodyweight_exercises) :-
    step('Push-ups, squats and planks: 3 sets of 10, 3 days a week.').
describe(weight_training) :-
    step('Weight training: compound lifts, 3 to 4 days a week.').
describe(resistance_bands) :-
    step('Resistance band workouts: gentle on the joints, 3 days a week.').
describe(swimming) :-
    step('Swimming: low-impact cardio, 30 minutes, 3 days a week.').
describe(cycling) :-
    step('Cycling: 30 to 45 minutes, 3 to 4 days a week.').
describe(jump_rope) :-
    step('Jump rope: high-intensity cardio intervals, 15 minutes, 3 days a week.').
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

% Output formatting and working memory cleanup
step(Text) :-
    format('  - ~w~n', [Text]).

undo :-
    retractall(yes(_)),
    retractall(no(_)).
