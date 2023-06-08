import math
from sympy import *

while True:
    print("\nChoose the math operation.\n\n01 - Addition\n02 - Subtraction\n03 - Multiplication\n04 - Division\n05 - Modulo\n06 - Raising to a power\n07 - nth root\n08 - Logarithm\n09 - Natural Logarithm\n10 - Factorial\n11 - Sine\n12 - Cosine\n13 - Tangent\n14 - Arcsine\n15 - Arccos\n16 - Arctan\n17 - Absolute Value\n18 - Differentiation\n19 - Integration")
    operation = input("\nYour operation from the menu: ")
    
    #Addition
    if operation == "1":
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))
        print("\n" + str(val1 + val2))
        
        go_back = input('\nGo back to main menu? (y/n)')
        if go_back == 'y':
            continue
        else:
            print("\nThank You for using my Function Calculator!!")
            break
    
    # Subtraction
    elif operation == "2":
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))
        print("\n" + str(val1 - val2))
        
        go_back = input('\nGo back to main menu? (y/n) ')
        if go_back == 'y':
            continue
        else:
            print("\nThank You for using my Function Calculator!!")
            break
    
    # Multiplication
    elif operation == "3":
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))
        print("\n" + str(val1 * val2))
        
        go_back = input('\nGo back to main menu? (y/n) ')
        if go_back == 'y':
            continue
        else:
            print("\nThank You for using my Function Calculator!!")
            break
    
    # Division
    elif operation == "4":
        val1 = float(input("\nNumerator: "))
        val2 = float(input("\nDenominator: "))
        if val2 == 0:
            print("\nDivision by zero is not possible")
            break
        else:
            print("\n" + str(val1 / val2))
        
        go_back = input('\nGo back to main menu? (y/n) ')
        if go_back == 'y':
            continue
        else:
            print("\nThank You for using my Function Calculator!!")
            break

    # Modulo
    elif operation == "5":
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))
        if val2 == 0:
            print("\nDivision by zero is not possible")
            break
        else:
            print("\n" + str(val1 % val2))

        go_back = input('\nGo back to main menu? (y/n) ')
        if go_back == 'y':
            continue
        else:
            print("\nThank You for using my Function Calculator!!")
            break

    # Power
    elif operation == "6":
        val1 = float(input("\nBase: "))
        val2 = float(input("\nPower: "))
        print("\n" + str(pow(val1, val2)))
              
        go_back = input('\nGo back to main menu? (y/n) ')
        if go_back == 'y':
            continue
        else:
            print("\nThank You for using my Function Calculator!!")
            break

    # nth Root
    elif operation == "7":
        val1 = float(input("\nBase: "))
        val2 = float(input("\nn: "))
        print("\n" + str(pow(val1, 1/val2)))

        go_back = input('\nGo back to main menu? (y/n) ')
        if go_back == 'y':
            continue
        else:
            print("\nThank You for using my Function Calculator!!")
            break
    
    # Log
    elif operation == "8":
        val1 = float(input("\nEnter a value: "))
        base = float(input("\nEnter the Base: "))
        print("\n" + str(math.log(val1, base)))

        go_back = input('\nGo back to main menu? (y/n) ')
        if go_back == 'y':
            continue
        else:
            print("\nThank You for using my Function Calculator!!")
            break

    # ln
    elif operation == "9":
        val1 = float(input("\nEnter a value: "))
        print("\n" + str(math.log(val1, math.e)))

        go_back = input('\nGo back to main menu? (y/n) ')
        if go_back == 'y':
            continue
        else:
            print("\nThank You for using my Function Calculator!!")
            break

    # Factorial
    elif operation == "10":
        val1 = int(input("\nEnter a number: "))
        factorial = math.factorial(val1)
        print(factorial)

        go_back = input('\nGo back to main menu? (y/n)')
        if go_back == 'y':
            continue
        else:
            print("\nThank You for using my Function Calculator!!")
            break

    # sin
    elif operation == "11":
        deg = float(input("\nAngle(in degrees): "))
        rad = float(math.radians(deg))
        print("\n" + str(math.sin(rad)))
        
        go_back = input('\nGo back to main menu? (y/n)')
        if go_back == 'y':
            continue
        else:
            print("\nThank You for using my Function Calculator!!")
            break

    # cos
    elif operation == "12":
        deg = float(input("\nAngle(in degrees): "))
        rad = float(math.radians(deg))
        print("\n" + str(math.cos(rad)))
        
        go_back = input('\nGo back to main menu? (y/n)')
        if go_back == 'y':
            continue
        else:
            print("\nThank You for using my Function Calculator!!")
            break

    # tan
    elif operation == "13":
        deg = float(input("\nAngle(in degrees): "))
        rad = float(math.radians(deg))
        print("\n" + str(math.tan(rad)))
        
        go_back = input('\nGo back to main menu? (y/n)')
        if go_back == 'y':
            continue
        else:
            print("\nThank You for using my Function Calculator!!")
            break

    # arcsin
    elif operation == "14":
        val1 = float(input("\nEnter a value: "))
        arcsin = math.asin(val1)
        print("\n" + str(math.degrees(arcsin)))
        
        go_back = input('\nGo back to main menu? (y/n)')
        if go_back == 'y':
            continue
        else:
            print("\nThank You for using my Function Calculator!!")
            break

    # arccos
    elif operation == "15":
        val1 = float(input("\nEnter a value: "))
        arccos = math.acos(val1)
        print("\n" + str(math.degrees(arccos)))
        
        go_back = input('\nGo back to main menu? (y/n)')
        if go_back == 'y':
            continue
        else:
            print("\nThank You for using my Function Calculator!!")
            break

    # arctan
    elif operation == "16":
        val1 = float(input("\nEnter a value: "))
        arctan = math.atan(val1)
        print("\n" + str(math.degrees(arctan)))
        
        go_back = input('\nGo back to main menu? (y/n)')
        if go_back == 'y':
            continue
        else:
            print("\nThank You for using my Function Calculator!!")
            break

    # Absolute value
    elif operation == "17":
        val1 = int(input("Enter a value: "))
        print(abs(val1))

        go_back = input('\nGo back to main menu? (y/n) ')
        if go_back == 'y':
            continue
        else:
            print("\nThank You for using my Function Calculator!!")
            break

    # Differentiation
    elif operation == "18":
        x, y = symbols('x y')
        expr = input("Enter an expression: ")
        expr_diff = Derivative(expr, x) 
        print("Derivative of expression with respect to x : {}".format(expr_diff.doit()))

        go_back = input('\nGo back to main menu? (y/n) ')
        if go_back == 'y':
            continue
        else:
            print("\nThank You for using my Function Calculator!!")
            break

    # Integration
    elif operation == "19":
        x, y = symbols('x y')
        expr = input("Enter an expression: ")
        expr_intr = integrate(expr, x)
        print("Intergration of expression with respect to x : {}".format(expr_intr) + " + c")

        go_back = input('\nGo back to main menu? (y/n) ')
        if go_back == 'y':
            continue
        else:
            print("\nThank You for using my Function Calculator!!")
            break


    elif operation == "exit":
        print("Ok fine, exiting now")
        break

    # Invalid
    else:
        print("\nInvalid Number")
        continue
