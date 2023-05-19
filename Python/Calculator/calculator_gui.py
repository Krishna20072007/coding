import tkinter as tk
from sympy import *
import math
from tkinter.font import Font

# Root
root = tk.Tk()
root.geometry("400x495")
root.configure(bg="#dddddd")
root.resizable(False, False)
root.title("Function Calculator")

equation = ""

# Formula Bar
formula_bar = tk.Label(root, text="", width=56, height=4, relief="groove", bg="#ddd", fg="#000")
formula_bar.grid(row=0, column=0, columnspan=6)

def add_to_equation(value):
    global equation
    equation += value
    formula_bar.config(text=equation)

def evaluate_equation():
    global equation
    try:
        result = eval_equation()
        formula_bar.config(text=result)
    except:
        formula_bar.config(text="Error")
    equation = ""

def eval_equation():
    global equation
    x = symbols('x')
    try:
        if 'derivative' in equation:
            eq = equation.replace('derivative(', 'diff(')
            result = eval(eq)
        elif 'integrate' in equation:
            eq = equation.replace('integrate(', 'integrate(')
            result = eval(eq)
        else:
            result = eval(equation)
        return result
    except:
        raise ValueError('Invalid equation')

# Clear function
def clear_equation():
    global equation
    equation = ""
    formula_bar.config(text="")

# Pi function
def add_pi():
    add_to_equation("pi")

# E function
def add_euler():
    add_to_equation("e")

# New buttons
addition_button = tk.Button(root, text='+', command=lambda: add_to_equation('+'), width=8, height=4, bg="#dddddd")
subtraction_button = tk.Button(root, text='-', command=lambda: add_to_equation('-'), width=8, height=4, bg="#dddddd")
multiplication_button = tk.Button(root, text='*', command=lambda: add_to_equation('*'), width=8, height=4, bg="#dddddd")
division_button = tk.Button(root, text='÷', command=lambda: add_to_equation('/'), width=8, height=4, bg="#dddddd")
modulo_button = tk.Button(root, text='%', command=lambda: add_to_equation('%'), width=8, height=4, bg="#dddddd")
power_button = tk.Button(root, text='power', command=lambda: add_to_equation('**'), width=8, height=4, bg="#dddddd")
logarithm_button = tk.Button(root, text='log', command=lambda: add_to_equation('log('), width=8, height=4, bg="#dddddd")
natural_logarithm_button = tk.Button(root, text='ln', command=lambda: add_to_equation('ln('), width=8, height=4, bg="#dddddd")
factorial_button = tk.Button(root, text='!', command=lambda: add_to_equation('factorial('), width=8, height=4, bg="#dddddd")
sine_button = tk.Button(root, text='sin', command=lambda: add_to_equation('math.sin('), width=8, height=4, bg="#dddddd")
cosine_button = tk.Button(root, text='cos', command=lambda: add_to_equation('math.cos('), width=8, height=4, bg="#dddddd")
tangent_button = tk.Button(root, text='tan', command=lambda: add_to_equation('math.tan('), width=8, height=4, bg="#dddddd")
arcsine_button = tk.Button(root, text='arcsin', command=lambda: add_to_equation('math.asin('), width=8, height=4, bg="#dddddd")
arccosine_button = tk.Button(root, text='arccos', command=lambda: add_to_equation('math.acos('), width=8, height=4, bg="#dddddd")
arctangent_button = tk.Button(root, text='arctan', command=lambda: add_to_equation('math.aran('), width=8, height=4, bg="#dddddd")
absolute_value_button = tk.Button(root, text='abs', command=lambda: add_to_equation('abs('), width=8, height=4, bg="#dddddd")
derivative_button = tk.Button(root, text='derivative', command=lambda: add_to_equation('derivative('), width=8, height=4, bg="#dddddd")
integration_button = tk.Button(root, text='integrate', command=lambda: add_to_equation('integrate('), width=8, height=4, bg="#dddddd")
x_button = tk.Button(root, text='x', command=lambda: add_to_equation('x'), width=8, height=4, bg="#dddddd")
y_button = tk.Button(root, text='y', command=lambda: add_to_equation('y'), width=8, height=4, bg="#dddddd")
zero_button = tk.Button(root, text='0', command=lambda: add_to_equation('0'), width=8, height=4, bg="#dddddd")
one_button = tk.Button(root, text='1', command=lambda: add_to_equation('1'), width=8, height=4, bg="#dddddd")
two_button = tk.Button(root, text='2', command=lambda: add_to_equation('2'), width=8, height=4, bg="#dddddd")
three_button = tk.Button(root, text='3', command=lambda: add_to_equation('3'), width=8, height=4, bg="#dddddd")
four_button = tk.Button(root, text='4', command=lambda: add_to_equation('4'), width=8, height=4, bg="#dddddd")
five_button = tk.Button(root, text='5', command=lambda: add_to_equation('5'), width=8, height=4, bg="#dddddd")
six_button = tk.Button(root, text='6', command=lambda: add_to_equation('6'), width=8, height=4, bg="#dddddd")
seven_button = tk.Button(root, text='7', command=lambda: add_to_equation('7'), width=8, height=4, bg="#dddddd")
eight_button = tk.Button(root, text='8', command=lambda: add_to_equation('8'), width=8, height=4, bg="#dddddd")
nine_button = tk.Button(root, text='9', command=lambda: add_to_equation('9'), width=8, height=4, bg="#dddddd")
point_button = tk.Button(root, text='.', command=lambda: add_to_equation('.'), width=8, height=4, bg="#dddddd")
equal_button = tk.Button(root, text='=', command=evaluate_equation, width=8, height=4, bg="#dddddd")
pi_button = tk.Button(root, text='pi', command=add_pi, width=8, height=4, bg="#dddddd")
euler_button = tk.Button(root, text='e', command=add_euler, width=8, height=4, bg="#dddddd")
clear_button = tk.Button(root, text='C', command=clear_equation, width=8, height=4, bg="#dddddd")
closebracket_button = tk.Button(root, text=')', command=lambda: add_to_equation(')'), width=8, height=4, bg="#dddddd")

# .grid
addition_button.grid(row=3,column=4)
subtraction_button.grid(row=4,column=4)
multiplication_button.grid(row=5,column=4)
division_button.grid(row=6,column=4)
modulo_button.grid(row=6,column=0)
power_button.grid(row=1,column=4)
logarithm_button.grid(row=1,column=5)
natural_logarithm_button.grid(row=2,column=5)
factorial_button.grid(row=3,column=5)
sine_button.grid(row=1,column=1)
cosine_button.grid(row=1,column=2)
tangent_button.grid(row=1,column=3)
arcsine_button.grid(row=2,column=1)
arccosine_button.grid(row=2,column=2)
arctangent_button.grid(row=2,column=3)
absolute_value_button.grid(row=4,column=5)
derivative_button.grid(row=5,column=5)
integration_button.grid(row=6,column=5)
x_button.grid(row=2,column=0)
y_button.grid(row=3,column=0)
zero_button.grid(row=6,column=2)
one_button.grid(row=5,column=1)
two_button.grid(row=5,column=2)
three_button.grid(row=5,column=3)
four_button.grid(row=4,column=1)
five_button.grid(row=4,column=2)
six_button.grid(row=4,column=3)
seven_button.grid(row=3,column=1)
eight_button.grid(row=3,column=2)
nine_button.grid(row=3,column=3)
point_button.grid(row=6,column=1)
equal_button.grid(row=6,column=3)
pi_button.grid(row=4,column=0)
euler_button.grid(row=5,column=0)
clear_button.grid(row=2,column=4)
closebracket_button.grid(row=1, column=0)

root.mainloop()
