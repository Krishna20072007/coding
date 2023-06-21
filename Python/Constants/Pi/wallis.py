pi = 2
max = 100000

for n in range(1, max):
    num = (8*pow(n, 2))/((8*pow(n, 2))-2)
    pi *= num
print(pi)
