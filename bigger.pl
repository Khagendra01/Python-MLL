% Define symptoms
symptom(fever).
symptom(cough).
symptom(runny_nose).
symptom(sneezing).
symptom(headache).
symptom(fatigue).

% Define rules for diagnosis
diagnosis(prolog_fever) :-
    symptom(fever),
    symptom(headache),
    symptom(fatigue),
    not(symptom(cough)),
    not(symptom(runny_nose)),
    not(symptom(sneezing)).

diagnosis(cold) :-
    symptom(cough),
    symptom(runny_nose),
    symptom(sneezing),
    not(diagnosis(prolog_fever)).

diagnosis(unknown) :-
    not(diagnosis(prolog_fever)),
    not(diagnosis(cold)).

% Query the expert system
diagnose_condition :-
    write('Enter symptoms separated by commas (e.g., fever, cough, headache): '),
    read_line_to_string(user_input, Input),
    atomic_list_concat(Symptoms, ', ', Input), % Split the input string into a list
    list_to_set(Symptoms, UniqueSymptoms), % Remove duplicates
    check_diagnosis(UniqueSymptoms, Diagnosis),
    format('Diagnosis: ~w.~n', [Diagnosis]).

check_diagnosis(Symptoms, Diagnosis) :-
    member(Symptom, Symptoms),
    symptom(Symptom),
    once(diagnosis(Diagnosis)),
    format('Patient may have ~w.~n', [Diagnosis]).

% Example usage:
% ?- diagnose_condition.
