"""
Fair Division under Ordinal Preferences:
Computing Envy-Free Allocations of Indivisible Goods

Sylvain Bouveret, Ulle Endriss and Jer´ ome Lang

2010

link:
https://books.google.co.il/books?hl=iw&lr=&id=cLqiEJVT3u8C&oi=fnd&pg=PA387&dq=Fair+Division+under+Ordinal+Preferences:+Computing+Envy-Free+Allocations+of+Indivisible+Goods&ots=GrWpDNui8t&sig=1VzhbXQpPSzGQbuGAC9Gf4S2tWI&redir_esc=y#v=onepage&q=Fair%20Division%20under%20Ordinal%20Preferences%3A%20Computing%20Envy-Free%20Allocations%20of%20Indivisible%20Goods&f=false

In this project I will implement the 1 main algorithm of this article: get PPE PEF allocation
The algorithm is propisition 4 and 5

Matan Hodadov
"""


def getPPE_PEF(m: int, n: int, preferences: dict) -> dict:
    unique_top_ranked = []
    for preference in preferences.values():
        if preference[0] not in unique_top_ranked:
            unique_top_ranked.append(preference[0])
    k = len(unique_top_ranked)
    if m < 2*n-k:
        raise Exception("m is lower then 2n-k")

    res = {}
    not_allocated = []
    not_fully_satisfied = []
    for pref in preferences.values():
        for char in pref:
            if char not in not_allocated:
                not_allocated.append(char)
    for N, pref in preferences.items():
        char = nextWantedGood(not_allocated, pref)
        not_allocated.remove(char)
        res[N] = char
        if char != pref[0]:
            not_fully_satisfied.append((N, char))
    while len(not_fully_satisfied) > 0 and len(not_allocated) > 0:
        not_fully_satisfied.reverse()
        temp = not_fully_satisfied.copy()
        for player in temp:
            char = nextWantedGood(not_allocated, preferences[player[0]])
            if char == "":
                not_fully_satisfied.remove(player)
                continue
            not_allocated.remove(char)
            res[player[0]] = res[player[0]] + char
            not_fully_satisfied.remove(player)
            player = list(player)
            player[1] = player[1] + char
            player = tuple(player)
            not_fully_satisfied.append(player)

    return res


def nextWantedGood(not_allocated: list, pref: str) -> str:
    for char in pref:
        if char in not_allocated:
            return char
    return ""


if __name__ == '__main__':

    answers = []
    answers.append({1: 'a', 2: 'df', 3: 'b', 4: 'ce'})
    answers.append({1: 'a', 2: 'df', 3: 'b', 4: 'ce'})
    answers.append({1: 'a', 2: 'df', 3: 'b', 4: 'ce'})
    answers.append({1: 'a', 2: 'df', 3: 'b', 4: 'ce'})
    answers.append({1: 'a', 2: 'def', 3: 'b', 4: 'c'})
    answers.append({1: 'a', 2: 'df', 3: 'b', 4: 'ce'})

    print(getPPE_PEF(6, 4, {1: "abcdef", 2: "adbcef", 3: "bacdfe", 4: "bacefd"}) == answers[0])
    print(getPPE_PEF(6, 4, {1: "abef", 2: "adbcef", 3: "bacdfe", 4: "bacefd"}) == answers[1])
    print(getPPE_PEF(6, 4, {1: "abef", 2: "adbf", 3: "bacdfe", 4: "bacefd"}) == answers[2])
    print(getPPE_PEF(6, 4, {1: "abef", 2: "adbcef", 3: "bacd", 4: "bacefd"}) == answers[3])
    print(getPPE_PEF(6, 4, {1: "abef", 2: "adbcef", 3: "bacdfe", 4: "bacd"}) == answers[4])
    print(getPPE_PEF(6, 4, {1: "abef", 2: "adbcef", 3: "bdfe", 4: "bacefd"}) == answers[5])
    try:
        print(getPPE_PEF(6, 4, {1: "abef", 2: "adbcef", 3: "adfe", 4: "acebfd"}))
        print(getPPE_PEF(6, 4, {1: "bacef", 2: "babcef", 3: "badfe", 4: "bafceb"}))
    except:
        print("Good. got m<2n-k exception as needed")

