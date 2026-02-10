# functions with parameters
# example 1
def greeting(name):
    print("Good morning",name)
# call the function
greeting("Smith")
# example 2
def addition(number1,number2):
    answer=number1+number2
    print("the sum is",answer)
# call the function
addition(40,60)
# NB: a function is usable block of code that perfoms a specific task
addition(900,700)
addition(1500,400)
addition(-160,-40)
# assignment
# subtraction
def subtraction(number1,number2):
    answer=number1-number2
    print("the difference is",answer)
# call the function
subtraction(900,400)
# division 
def division(number1,number2):
    answer=number1/number2
    print("the quotient is",answer)
# call the function
division(4000,60)
# multiplication 
def multiplication(number1,number2):
    answer=number1*number2
    print("the product is",answer)
# call the function
multiplication(420,630)
# simple interest 
def  interest(principle,rate,time):
    answer=(principle*rate*time)/100
    print("the interest is",answer)
# call the function
interest(1000,5,2)
# area of a triangle 
def area(base,height):
    answer=(base*height*1/2)
    print("the areais",answer)
# call the function
area(50,90)
# BMI
def calculatebmi(weight,height):
    bmi = weight / (height ** 2) 
    print("the bmi is",bmi)
# call the function
calculatebmi(80,5)

