from itertools import combinations


def is_prime(num):
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


def find_prime_sum_pairs(lst):
    return [pair for pair in combinations(lst, 2) if is_prime(sum(pair))]


print(find_prime_sum_pairs([2, 5, 1, 3, 7, 9]))
