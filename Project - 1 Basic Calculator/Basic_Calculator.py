#Build a basic calculator using python
#Steps involved
'''
1. Define the functions needed: add, sub, mul, div, mod
2. Print the options to be choose
3. Asking for values
4. Call the functions 
5. While loop to continue the program until the user wants to exit the program
'''
def add(a,b):
    answer=a+b
    print("___________")
    print( str(a)+ "+" +str(b)+ "=" +str(answer)  )
    print("___________")

def sub(a,b):
    answer=a-b
    print("___________")
    print(str(a)+ "-" +str(b)+ "=" +str(answer)  )
    print("___________")

def mul(a,b):
    answer=a*b
    print("___________")
    print(str(a)+ "*" +str(b)+ "=" +str(answer) )
    print("___________")

def div(a,b):
    answer=a/b
    print("___________")
    print(str(a)+ "/" +str(b)+ "=" +str(answer)  )
    print("___________")

def mod(a,b):
    answer=a%b
    print("___________")
    print(str(a)+ "%" +str(b)+ "=" +str(answer)  )
    print("___________")

while True:
    print("A.Addition")
    print("B.Subtraction")
    print("C.Multiplication")
    print("D.Division")
    print("E.Modulus")
    print("F.Exit")

    choice=input("Enter your choice:")

    if choice=="a" or choice=="A":
        print("Addition")
        a=int(input("Enter first number"))
        b=int(input("Enter second number"))
        add(a,b)
    elif choice=="b" or choice=="B":
        print("Subtraction")
        a=int(input("Enter first number"))
        b=int(input("Enter second number"))
        sub(a,b)
    elif choice=="c" or choice=="C":
        print("Multiplication")
        a=int(input("Enter first number"))
        b=int(input("Enter second number"))
        mul(a,b)
    elif choice=="d" or choice=="D":
        print("Division")
        a=int(input("Enter first number"))
        b=int(input("Enter second number"))
        div(a,b)
    elif choice=="e" or choice=="E":
        print("Modulus")
        a=int(input("Enter first number"))
        b=int(input("Enter second number"))
        mod(a,b)
    elif choice=="f" or choice=="F":
        print("Program ended")
        quit()

    


