input_tuple=final_tuple=()
flag=False
n=int(input("Enter the number of student "))
print"Enter the number, roll no and average mark of 5 subjects of ",n,"student"
for i in range(0,n):
    name=raw_input("Enter the name ")
    roll_no=input("Enter the roll no ")
    marks=int(input("Enter student average marks "))
    per_marks=(int(marks)*100)/500
    input_tuple=(name,roll_no,marks,per_marks,)
    final_tuple=final_tuple+(input_tuple,)
input_roll=input("Please enter the student roll no for results ")
for x in final_tuple:
    if(x[1]==input_roll):
        flag=True
        if(x[3]>=0 and x[3]<=34):
            print("Name ",x[0],"Roll No ",x[1],"Fail ")
        elif(x[3]>=35 and x[3]<=49):
            print("Name ",x[0],"Roll No ",x[1],"Pass class ")
        elif(x[3]>=50 and x[3]<=59):
            print("Name ",x[0],"Roll No ",x[1],"Second class ")
        elif(x[3]>=60 and x[3]<=69):
            print("Name ",x[0],"Roll No ",x[1],"First class ")
        elif(x[3]>=70 and x[3]<=100):
            print("Name ",x[0],"Roll No ",x[1],"First class with distinction ")
if flag==False:
    print("Record not found ")
