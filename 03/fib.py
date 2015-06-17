seen_fibs = {}
def fib(nth):
    """
    Return the nth element of the Fibonacci squence
    """
    if nth == 0 or nth == 1:
        seen_fibs[nth] = 1
        return 1
    elif nth in seen_fibs:
        return seen_fibs[nth]

    this_fib = fib(nth - 1) + fib(nth - 2)
    seen_fibs[nth] = this_fib
    return this_fib

for num in xrange(1000):
    fib(num)
