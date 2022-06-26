import math


def count_find_num(primes_l, limit):
    prod = math.prod(primes_l)
    result = [prod] if prod <= limit else []
    for el in primes_l:
        for r in result:
            result = list(set(result))
            res = [r * el**i for i in range(prod) if r * el**i <= limit]
            result.extend(res)

    qty = len(set(result))
    max_value = max(result) if result else None

    print([qty, max_value] if max_value else [])

    return [qty, max_value] if max_value else []


if __name__ == "__main__":
    count_find_num([17, 31, 79], 1434589)  # [3, 1290623]
    #
    # primesL = [2, 3]
    # limit = 200
    # assert count_find_num(primesL, limit) == [13, 192]
    #
    # primesL = [2, 5]
    # limit = 200
    # assert count_find_num(primesL, limit) == [8, 200]
    #
    # primesL = [2, 3, 5]
    # limit = 500
    # assert count_find_num(primesL, limit) == [12, 480]
    #
    # primesL = [2, 3, 5]
    # limit = 1000
    # assert count_find_num(primesL, limit) == [19, 960]
    #
    # primesL = [2, 3, 47]
    # limit = 200
    # assert count_find_num(primesL, limit) == []
