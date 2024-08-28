#to solve the quardic equation find descriminent.
a:float = 10
b:float = 12
c:float = 3
d:float = (b**2)-(4*a*c)
print("The discriminant is",d)

def discriminent(a:float,b:float,c:float):
    d:float = (b**2)-(4*a*c)
    return d
result = discriminent(10,12,3)
print("The discriminent is",result)
