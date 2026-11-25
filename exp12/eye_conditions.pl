% Knowledge base: Eye Condition Expert System
% Start consultation: ?- go.

:- dynamic yes/1, no/1.

% Main entry point and consultation loop
go :-
    undo,
    write('Eye Condition Expert System'), nl,
    write('Enter your initial reported ocular symptom (e.g. red itchy eyes, dry burning, blurred vision, or list):'), nl,
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
        (   hypothesis(Condition)
        ->  format('~nPossible condition: ~w~n', [Condition]),
            advice(Condition),
            undo
        ;   format('~nNo eye condition could be confirmed with ~w.~n', [Symptom]),
            write('Please assert another symptom (or type exit):'), nl,
            consult_loop
        )
    ).

prompt_symptom(Symptom) :-
    write('|: '),
    read_line_to_string(user_input, Line),
    match_symptom(Line, Symptom).

show_symptoms :-
    nl, write('Available initial eye symptoms:'), nl,
    write('  1. red_itchy             (red, irritated and itchy eyes)'), nl,
    write('  2. dry_eyes              (dry, gritty or burning eyes)'), nl,
    write('  3. blurred_vision        (fuzzy or out of focus vision)'), nl,
    write('  4. cloudy_vision         (cloudy, misty or dim vision)'), nl,
    write('  5. halos_lights          (rainbow or coloured halos around lights)'), nl,
    write('  6. eyelid_lump           (red, tender or painful lump on eyelid)'), nl,
    write('  7. eye_injury            (scratched, hit or foreign body in eye)'), nl,
    write('  8. crusted_eyelids       (swollen, flaky or crusted eyelid margins)'), nl,
    write('  9. red_blood_patch       (bright red blood patch on white of eye)'), nl,
    write(' 10. diabetic_floaters     (dark spots, floating cobwebs with diabetes)'), nl,
    write(' 11. color_confusion       (trouble telling red from green or blue)'), nl,
    write(' 12. shower_of_floaters    (sudden flashes of light or floater shower)'), nl, nl.

% Keyword mapping for free-form user assertion
match_symptom(Line, Symptom) :-
    string_lower(Line, Lower),
    (   sub_string(Lower, _, _, _, 'exit')        -> Symptom = exit
    ;   sub_string(Lower, _, _, _, 'quit')        -> Symptom = exit
    ;   sub_string(Lower, _, _, _, 'list')        -> Symptom = list
    ;   sub_string(Lower, _, _, _, 'help')        -> Symptom = list
    ;   sub_string(Lower, _, _, _, 'curtain')     -> Symptom = shower_of_floaters
    ;   sub_string(Lower, _, _, _, 'flash')       -> Symptom = shower_of_floaters
    ;   sub_string(Lower, _, _, _, 'floater')     -> Symptom = shower_of_floaters
    ;   sub_string(Lower, _, _, _, 'color')       -> Symptom = color_confusion
    ;   sub_string(Lower, _, _, _, 'colour')      -> Symptom = color_confusion
    ;   sub_string(Lower, _, _, _, 'diabet')      -> Symptom = diabetic_floaters
    ;   sub_string(Lower, _, _, _, 'blood')       -> Symptom = red_blood_patch
    ;   sub_string(Lower, _, _, _, 'crust')       -> Symptom = crusted_eyelids
    ;   sub_string(Lower, _, _, _, 'flake')       -> Symptom = crusted_eyelids
    ;   sub_string(Lower, _, _, _, 'scratch')     -> Symptom = eye_injury
    ;   sub_string(Lower, _, _, _, 'foreign')     -> Symptom = eye_injury
    ;   sub_string(Lower, _, _, _, 'lump')        -> Symptom = eyelid_lump
    ;   sub_string(Lower, _, _, _, 'stye')        -> Symptom = eyelid_lump
    ;   sub_string(Lower, _, _, _, 'halo')        -> Symptom = halos_lights
    ;   sub_string(Lower, _, _, _, 'cloud')       -> Symptom = cloudy_vision
    ;   sub_string(Lower, _, _, _, 'mist')        -> Symptom = cloudy_vision
    ;   sub_string(Lower, _, _, _, 'blur')        -> Symptom = blurred_vision
    ;   sub_string(Lower, _, _, _, 'dry')         -> Symptom = dry_eyes
    ;   sub_string(Lower, _, _, _, 'grit')        -> Symptom = dry_eyes
    ;   sub_string(Lower, _, _, _, 'itch')        -> Symptom = red_itchy
    ;   sub_string(Lower, _, _, _, 'red')         -> Symptom = red_itchy
    ;   sub_string(Lower, _, _, _, '12')          -> Symptom = shower_of_floaters
    ;   sub_string(Lower, _, _, _, '11')          -> Symptom = color_confusion
    ;   sub_string(Lower, _, _, _, '10')          -> Symptom = diabetic_floaters
    ;   sub_string(Lower, _, _, _, '1')           -> Symptom = red_itchy
    ;   sub_string(Lower, _, _, _, '2')           -> Symptom = dry_eyes
    ;   sub_string(Lower, _, _, _, '3')           -> Symptom = blurred_vision
    ;   sub_string(Lower, _, _, _, '4')           -> Symptom = cloudy_vision
    ;   sub_string(Lower, _, _, _, '5')           -> Symptom = halos_lights
    ;   sub_string(Lower, _, _, _, '6')           -> Symptom = eyelid_lump
    ;   sub_string(Lower, _, _, _, '7')           -> Symptom = eye_injury
    ;   sub_string(Lower, _, _, _, '8')           -> Symptom = crusted_eyelids
    ;   sub_string(Lower, _, _, _, '9')           -> Symptom = red_blood_patch
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
hypothesis(conjunctivitis) :-
    verified(red_itchy),
    ask(sticky_discharge, 'Is there watery or sticky discharge from the eyes').
hypothesis(dry_eye_syndrome) :-
    verified(dry_eyes),
    ask(screen_worse, 'Do the symptoms get worse after screen use').
hypothesis(refractive_error) :-
    verified(blurred_vision),
    ask(reading_headaches, 'Do you get headaches or eye strain when reading').
hypothesis(cataract) :-
    verified(cloudy_vision),
    ask(night_glare, 'Are you troubled by glare at night').
hypothesis(glaucoma) :-
    verified(halos_lights),
    ask(side_vision_loss, 'Do you have eye pain or loss of side vision').
hypothesis(stye) :-
    verified(eyelid_lump),
    ask(tender_eyelid, 'Is the eyelid swollen or tender to touch').
hypothesis(corneal_abrasion) :-
    verified(eye_injury),
    ask(intense_pain_light, 'Do you experience intense eye pain and light sensitivity').
hypothesis(blepharitis) :-
    verified(crusted_eyelids),
    ask(eyelashes_stick, 'Do your eyelashes stick together upon waking').
hypothesis(subconjunctival_hemorrhage) :-
    verified(red_blood_patch),
    ask(no_pain_clear_vision, 'Is there no pain and no change in your vision').
hypothesis(diabetic_retinopathy) :-
    verified(diabetic_floaters),
    ask(fluctuating_vision, 'Are you noticing fluctuating vision, dark spots or floating cobwebs').
hypothesis(color_blindness) :-
    verified(color_confusion),
    ask(childhood_present, 'Has this color confusion been present since childhood').
hypothesis(retinal_detachment) :-
    verified(shower_of_floaters),
    ask(dark_curtain, 'Is there a dark curtain or shadow spreading across your visual field').

% Advice and clinical guidance
advice(conjunctivitis) :-
    step('Wash hands often and do not touch or rub the eyes.'),
    step('Use a clean, warm compress and see a doctor for eye drops.').
advice(dry_eye_syndrome) :-
    step('Use lubricating eye drops and blink often.'),
    step('Follow the 20-20-20 rule: every 20 minutes look 20 feet away for 20 seconds.').
advice(refractive_error) :-
    step('Get an eye test; glasses or contact lenses may be needed.'),
    step('Read in good light and take regular breaks.').
advice(cataract) :-
    step('See an ophthalmologist; surgery is the usual treatment.'),
    step('Avoid night driving until the eyes are examined.').
advice(glaucoma) :-
    step('See an eye doctor urgently; high eye pressure can damage the nerve.'),
    step('Treatment is with eye drops, laser or surgery.').
advice(stye) :-
    step('Apply a warm compress for 10 minutes, 3 to 4 times a day.'),
    step('Do not squeeze it; see a doctor if it does not clear in a week.').
advice(corneal_abrasion) :-
    step('Do not rub the eye and avoid wearing contact lenses.'),
    step('Rinse gently with saline solution and consult an eye specialist promptly.').
advice(blepharitis) :-
    step('Clean eyelid margins daily with diluted baby shampoo or eyelid wipes.'),
    step('Apply a warm compress for 5 to 10 minutes to unblock eyelid oil glands.').
advice(subconjunctival_hemorrhage) :-
    step('Reassure yourself: this usually resolves spontaneously in 1 to 2 weeks.'),
    step('Check blood pressure and see a doctor if it recurs frequently.').
advice(diabetic_retinopathy) :-
    step('Maintain tight control over blood glucose and blood pressure levels.'),
    step('Schedule an immediate dilated fundus examination with a retina specialist.').
advice(color_blindness) :-
    step('Undergo formal Ishihara color testing with an optometrist.'),
    step('Consider color-filtering lenses or digital assistive accessibility tools.').
advice(retinal_detachment) :-
    step('Emergency: seek hospital ophthalmic casualty care immediately.'),
    step('Keep head posture stable and avoid strenuous physical activity.').

% Output formatting and working memory cleanup
step(Text) :-
    format('  - ~w~n', [Text]).

undo :-
    retractall(yes(_)),
    retractall(no(_)).
