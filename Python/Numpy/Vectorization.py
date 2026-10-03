import numpy as np

# Let's say we have prices of 5 items, and we want to add a $2 tax to each.
prices = np.array([10, 15, 20, 25, 30])

# BAD (The standard Python way using loops):
taxed_prices_loop = []
for price in prices:
    taxed_prices_loop.append(price + 2)
print(taxed_prices_loop)

# GOOD (The NumPy Vectorized way):
taxed_prices_numpy = prices + 2 
print("Vectorized Output:", taxed_prices_numpy)

a=np.array([10,20,30,40])
b=a+5
print(b)

