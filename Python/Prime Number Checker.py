from math import sqrt
n = int(input("Enter a number: "))
prime_flag = 0

if(n > 1):
    for i in range(2, int(sqrt(n)) + 1):
        if (n == 1):
            print("Undefined, one is neither prime nor composite")
        elif (n % i == 0):
            prime_flag = 1
            break
    if (prime_flag == 0):
        print(f"{n} is prime")
    else:
        print(f"{n} is composite")
else:
    print("Enter a positive number")
