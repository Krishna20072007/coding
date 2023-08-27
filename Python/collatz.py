arr = []

def collatz_conjecture(n):
    while n != 1:
        arr.append(n)
        if n % 2 == 0:
            n = n // 2

        else:
            n = 3 * n + 1
    arr.append(n)
    print(arr)

number = int(input("Enter a positive integer: "))
collatz_conjecture(number)
