#--------------Simple calculator------------
def Add(a,b):
    return a + b
def Sub(a,b):
    return a - b
def Mul(a,b):
    return a*b
def Div(a,b):
    return a/b
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice = int(input("Enter choice:"))
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
if choice == 1:
    print("result:",Add(a,b))
elif choice == 2:
    print("result:",Sub(a,b))
elif choice == 3:
    print("result:",Mul(a,b))
elif choice == 4:
    print("result:",Div(a,b))
else:
    print("invalid choice")                    