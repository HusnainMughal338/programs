#write a progrm to find the percentage of a student and print the grade.
print("enter the marks of the student\n")
def marks():
    marks = int(input("enter the marks: "))
    total_marks = int(input("enter the total marks: "))
    percentage = (marks/total_marks)*100
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
