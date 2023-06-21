pi = 4
max = 1000000

for iteration in range(max):
    den = 4 / (iteration * 2 + 3)
    if (iteration % 2 == 0):
        pi -= den
    else:
        pi += den
        
print(pi)