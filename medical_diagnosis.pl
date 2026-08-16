has_fever(john).
has_cough(john).
has_body_pain(john).

diagnosis(Patient, flu) :-
    has_fever(Patient),
    has_cough(Patient),
    has_body_pain(Patient).