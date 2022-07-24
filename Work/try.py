portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]

from collections import Counter 
number_of_shares = Counter()
for name, shares, price in portfolio:
    number_of_shares[name] += shares

from collections import defaultdict
holdings = defaultdict(list)
for name, shares, price in portfolio:
    try:
        holdings[name].append((shares,price))
    except KeyError:
        print("Exception on", name)

print(number_of_shares)
print(type(number_of_shares))
print(holdings)