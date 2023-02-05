import sys
sys.set_int_max_str_digits(1000000)


arr = []


def collatz(num):
    while num != 1:
        arr.append(num)
        if num % 2 == 0:
            num = num / 2
        else:
            num = 3 * num + 1
    else:
        arr.append(num)
        print(arr)
        print('\n')
        print(len(arr))



def main():
    num = int(input("Enter a Number: "))

    collatz(num)
 
main()
