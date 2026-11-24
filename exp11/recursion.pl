% Recursion: a predicate defined in terms of itself.
% Each predicate has a base case and a recursive case.

% factorial(N, F): F = N!
factorial(0, 1).
factorial(N, F) :-
    N > 0,
    N1 is N - 1,
    factorial(N1, F1),
    F is N * F1.

% fibonacci(N, F): F is the N-th Fibonacci number
fibonacci(0, 0).
fibonacci(1, 1).
fibonacci(N, F) :-
    N > 1,
    N1 is N - 1,
    N2 is N - 2,
    fibonacci(N1, F1),
    fibonacci(N2, F2),
    F is F1 + F2.

% sum_to(N, S): S = 1 + 2 + ... + N
sum_to(0, 0).
sum_to(N, S) :-
    N > 0,
    N1 is N - 1,
    sum_to(N1, S1),
    S is S1 + N.
