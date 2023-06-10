import sys
sys.set_int_max_str_digits(1000000)

def collatz(num):
    while num != 1:
        print(num)
        if num % 2 == 0:
            num = int(num / 2)
        else:
            num = int(3 * num + 1)
    else:
        print(num)


def main():
    num = int(input("Enter a Number: "))
    collatz(num)


main()
