diet(diabetes, 'Avoid sugar, prefer vegetables').
diet(hypertension, 'Low salt, high fiber').
diet(obesity, 'Low fat, more fruits').

suggest_diet(Disease) :-
    diet(Disease, Recommendation),
    format('Recommended diet: ~w~n', [Recommendation]).