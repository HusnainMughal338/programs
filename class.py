
def marks():
    marks = int(input("enter the marks: "))
    percentage = (marks/1100)*100
    print(percentage)
    if percentage >= 80:
       print("A grade")
    elif percentage >= 70:
        print("B grade")
    elif percentage >= 60:
        print("C grade")
    elif percentage >= 50:
        print("D grade")
        breakpoint
    else:
        print("fail")
    return marks
percentage = marks()
print(percentage)
