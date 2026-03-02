# python modules
# a module is a file containing python code
# it is reusable and can be used in other python files
# example 1
# add two numbers
# method 1
import lesson6a
# addition
lesson6a.addition(890,245)
# subtraction
lesson6a.subtraction(500,200)
# multiplication
lesson6a.multiply(700,80)
# division
lesson6a.division(856,487)
# method 2
from lesson6a import addition,subtraction,multiply,division
addition(40,60)
subtraction(500,60)
multiply(500,645)
division(630,30)
