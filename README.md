# fibonacci
Calculate the $Nth$ term of $F_{k}$, a generalized fibonacci  sequence. $F_{k,N} \equiv F_{N-1} + F_{N-2} + ... + F_{N-k}$ 

#### To Run:
just specify a term number `N` (0-indexed) and a list of initial conditions `ics` as integers separated by spaces:

`python fib.py -N 16 -ics 1 1`

The function implements a queue data structure via a list of `len(ics)` integers as it calculates. To see the queue in action, one can run in verbose mode:

`python fib.py -N 16 -ics 1 1 -v`
