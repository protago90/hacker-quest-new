# by protago90

from time import time
from timeit import timeit
from typing import Callable, List
from functools import partial

MSG = '  >> {}∎'


# Utils

def promptify(f: Callable) -> Callable:
    '''
    Handler of euler's problem dedicated [f]unc to print solution and computing time.
    '''
    def f_n(*args, **kwargs) -> None:
        n = int(''.join(filter(str.isdigit, f.__name__)))
        t = time()
        m = (f'the anwser for the #{n} euler problem is >{f(*args, **kwargs)}<; '
             f'computed in {round(time() - t, 4):.4f}s ')
        print(MSG.format(m))
    return f_n


def timeitfy(fs: List[Callable], args, i: int=10) -> None:
    '''
    Tester of time performance of proposed [f]unc[s] with euler's solutions.
    '''
    assert len(fs) > 0
    m = f'the times of test solutions: '
    for f in fs:
        m += f'{f.__name__}={round(timeit(partial(f, *args), number=i), 2):.2f}s '
    print(MSG.format(m))


# Commons

def sieve_primes(x: int) -> list:
    '''
    Produce first [x] primes list based on ~Eratosthenes recipe.
    '''
    rec = []
    for n in range(2, x+1):
        for prime in rec:
            if n % prime == 0: break
        else:
            rec.append(n)
    return rec

def sieve_primes_gen(x: int) -> list:
    '''
    Generate first [x] primes list based on ~Eratosthenes recipe.
    '''
    rec = []
    for n in range(2, x+1):            
        for prime in rec:              
            if n % prime == 0: break   
        else:
            rec.append(n)
            yield n                     

def prime_factors(x: int) -> list: # of lists
    '''
    Produce prime factors aka prime decomposition of [x] numb.
    '''
    primes: list = sieve_primes(x)
    rec = []
    while x != 1:
        for p in primes:
            if x % p == 0:
                rec.append(p); x = int(x/p)
    return rec

def factors(x: int):
    '''
    Produce all factors of considered [x] numb.
    '''
    rec = []
    for n in range(1, x+1):
        if x % n == 0:
            rec.append(n)
    return rec

def is_prime(x: int):
    '''
    Test if given [x] numb belongs to the primes.
    '''
    return True if factors(x) == [1, x] else False
