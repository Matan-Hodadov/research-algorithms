
from typing import Iterable


# bounded subset as iterator
def bounded_subset_i(S: Iterable, C: int):
    temp_S = []
    for i in S:
        if i <= C:
            temp_S.append(i)
    S = temp_S
    S.sort()
    subsets = {(): S}
    counter = 0
    while counter < len(subsets):
        origin = list(subsets.keys())[counter]
        arr = subsets[origin]
        for i in arr:
            if sum(origin) + i <= C:
                temp_key = list(origin) + [i]
                temp_key.sort()
                temp_key = tuple(temp_key)
                temp_value = arr.copy()
                temp_value.remove(i)
                subsets[temp_key] = temp_value
        counter += 1
    return iter([list(i) for i in subsets.keys()])


# bounded subset as generator
def bounded_subset_g(S: Iterable, C: int):
    S.sort()
    for i in range(len(S)):
        if S[i] > C:
            S.remove(S[i])
    subsets = {(): S}
    counter = 0
    while counter < len(subsets):
        origin = list(subsets.keys())[counter]
        arr = subsets[origin]
        for i in arr:
            if sum(origin) + i < C:
                temp_key = list(origin) + [i]
                temp_key.sort()
                temp_key = tuple(temp_key)
                temp_value = arr.copy()
                temp_value.remove(i)
                subsets[temp_key] = temp_value
        counter += 1
        yield list(origin)


for subset in bounded_subset_i([1, 2, 3, 4, 5, 6, 7], 5):
    print(subset)


