from itertools import combinations

def all_variants(text):
    for i in range(1,len(text)+1):
        combs = combinations(text, i)
        for combo in combs:
            yield "".join(combo)

a = all_variants("abc")
for i in a:
    print(i)