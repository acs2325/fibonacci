import argparse

def fib(n,ics, verbose = False):
    """Given k initial conditions, return fibonacci_k sum Nth element.

    n = nth term of fibonnaci seq
    ics = list of initial conditions
    """

    k = len(ics)
    i = 0

    if n < k:
        return(ics[n])

    while i < n:

        if verbose: print(ics)
        fib = sum(ics)
        ics.pop(0)
        ics.append(fib)
        i+=1

    return fib

if __name__ == '__main__':

    p = argparse.ArgumentParser()
    p.add_argument('-N', type=int)
    p.add_argument('-ics', nargs="+", type=int)
    p.add_argument("-v","--verbose", help="increase output verbosity",
                    action="store_true")
    args = p.parse_args()

    solution = fib(args.N,args.ics,args.verbose)

    print("The {}th fibonacci_{} term given ics {} is {}".format(args.N,len(args.ics),args.ics,solution))
