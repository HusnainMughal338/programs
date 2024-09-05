#write a python program to find the discriminant of a quadratic equation.
print("question no #1: write a python program to find the discriminant of a quadratic equation.")
def discriminent():
    a = float(input("Enter the value of a:"))
    b = float(input("Enter the value of b:"))
    c = float(input("Enter the value of c:"))
    print((b**2)-(4*a*c))
    return a,b,c
result = discriminent()


print("\n||-----------------Question End------------------||\n")


#write a python program to find the square of a number.
print("question no #2: write a python program to find the square of a number.\n")
def square():
    num = int(input("Enter a number: "))
    power = int(input("Enter the power: "))
    print(num**power)
    return num
num = square()



print("\n||-----------------Question End------------------||\n")