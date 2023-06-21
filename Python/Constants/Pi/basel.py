num = 0
max = 1000000

for iteration in range(1, max):
    den = 1/pow(iteration, 2)
    num += den
    pi = pow(num*6, 1/2)

print(pi)
    
