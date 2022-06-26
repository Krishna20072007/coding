def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def percent(x, y):
    return x / y * 100


def power(x, y):
    return x**y


print("Please select operator -\n"
      "1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide\n"
      "4. Percentage\n"
      "6. Exponent\n")


select = int(input("Select operations form 1, 2, 3, 4, 5, 6:"))
number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))

if select == 1:
    print(number_1, "+", number_2, "=", add(number_1, number_2))


elif select == 2:
    print(number_1, "-", number_2, "=", subtract(number_1, number_2))


elif select == 3:
    print(number_1, "*", number_2, "=", multiply(number_1, number_2))


elif select == 4:
    print(number_1, "/", number_2, "=", divide(number_1, number_2))


elif select == 5:
    print(number_1, "is", percent(number_1, number_2), "%", "of", number_2)

elif select == 6:
    print(number_2, "to the power of", number_1,
          "is", power(number_1, number_2))

else:
    print("Invalid input")
