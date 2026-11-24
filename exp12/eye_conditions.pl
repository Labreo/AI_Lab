% Expert system: identify possible eye conditions from the symptoms reported by the user.
% Start with:  ?- go.   and answer each question with yes. or no.

:- dynamic yes/1, no/1.

go :-
    undo,
    write('Eye Condition Expert System'), nl,
    write('Answer each question with yes. or no.'), nl, nl,
    (   hypothesis(Condition)
    ->  format('~nPossible condition: ~w~n', [Condition]),
        advice(Condition)
    ;   write('No eye condition identified from the symptoms given.'), nl
    ),
    write('Note: this is only a guide, please consult an eye doctor.'), nl,
    undo.

% Hypotheses: each condition needs all of its symptoms.
hypothesis(conjunctivitis) :-
    ask('Are your eyes red and itchy'),
    ask('Is there watery or sticky discharge from the eyes').
hypothesis(dry_eye_syndrome) :-
    ask('Do your eyes feel dry, gritty or burning'),
    ask('Do the symptoms get worse after screen use').
hypothesis(refractive_error) :-
    ask('Is your vision blurred'),
    ask('Do you get headaches or eye strain when reading').
hypothesis(cataract) :-
    ask('Is your vision cloudy or misty'),
    ask('Are you troubled by glare at night').
hypothesis(glaucoma) :-
    ask('Do you see coloured halos around lights'),
    ask('Do you have eye pain or loss of side vision').
hypothesis(stye) :-
    ask('Is there a red, painful lump on the eyelid'),
    ask('Is the eyelid swollen or tender to touch').
hypothesis(corneal_abrasion) :-
    ask('Did something scratch, hit or enter your eye'),
    ask('Do you experience intense eye pain and light sensitivity').
hypothesis(blepharitis) :-
    ask('Are your eyelid margins swollen, flaky or crusted with dandruff-like flakes'),
    ask('Do your eyelashes stick together upon waking').
hypothesis(subconjunctival_hemorrhage) :-
    ask('Is there a bright red patch of blood on the white of your eye'),
    ask('Is there no pain and no change in your vision').
hypothesis(diabetic_retinopathy) :-
    ask('Do you have a history of diabetes'),
    ask('Are you noticing fluctuating vision, dark spots or floating cobwebs').
hypothesis(color_blindness) :-
    ask('Do you have difficulty distinguishing between red and green or blue and yellow'),
    ask('Has this color confusion been present since childhood').
hypothesis(retinal_detachment) :-
    ask('Did you suddenly see a shower of floaters or flashes of light'),
    ask('Is there a dark curtain or shadow spreading across your visual field').

% Advice for each condition.
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
