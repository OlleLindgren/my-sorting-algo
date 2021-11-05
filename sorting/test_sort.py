import random

from sort import sort_list

def uniform_random_numbers(n=100):
    return [random.random() for _ in range(n)]

def normal_random_numbers(n=100):
    return [random.normalvariate(0., 1.) for _ in range(n)]

def random_integers(n=100):
    return [random.randint(0, 10000) for _ in range(n)]

if __name__ == '__main__':

    assert sort_list([]) == sorted([])
    print('Empty list OK')

    assert sort_list(iter([])) == sorted(iter([]))
    print('Empty generator OK')

    random_numbers = uniform_random_numbers(1)
    assert sort_list(random_numbers) == sorted(random_numbers)
    print('Single number OK')

    random_numbers = [1 for _ in range(100)]
    assert sort_list(random_numbers) == sorted(random_numbers)
    print('100 ones OK')

    random_numbers = normal_random_numbers(100)
    assert sort_list(random_numbers) == sorted(random_numbers)
    print('100 Normal random numbers OK')

    random_numbers = uniform_random_numbers(1000)
    assert sort_list(random_numbers) == sorted(random_numbers)
    print('1000 Uniform random numbers OK')

    random_numbers = normal_random_numbers(1000)
    assert sort_list(random_numbers) == sorted(random_numbers)
    print('1000 Normal random numbers OK')

    random_numbers = random_integers(1000)
    assert sort_list(random_numbers) == sorted(random_numbers)
    print('Random integers OK')

    random_numbers = random_integers(1000)
    assert sort_list(iter(random_numbers)) == sorted(iter(random_numbers))
    print('Sort generator OK')
