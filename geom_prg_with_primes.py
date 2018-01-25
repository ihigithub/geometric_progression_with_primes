# geometric progression with primes
from geometric_progression.geometric_progression import calc_geom_prg
from prime.is_prime import is_prime


def geo_prg_primes(param):
    found_primes = []
    iteration = 0
    while len(found_primes) < param:
        iteration += 1
        if is_prime(iteration) == "prime":
            found_primes.append(iteration)
    print found_primes
    progression_of_primes = 1
    while len(found_primes)>0:
        progression_of_primes = calc_geom_prg(progression_of_primes, found_primes[0], 1)

        found_primes= found_primes[1:]

    return progression_of_primes


print geo_prg_primes(5)