'''Write a Java program for following grading system.
Note: Percentage>=90% : Grade A
Percentage>=80% : Grade B
Percentage>=70% : Grade C
Percentage>=60% : Grade D
Percentage>=40% : Grade E
Percentage < 40% : Grade F'''
marks=int(input("enter the marks:"))
if(marks<=100 and marks>=90):
  print(marks," Grade A")
elif(marks<=90 and marks>=80):
  print(marks," Grade B")
elif(marks<=80 and marks>=70):
  print(marks," Grade C")
elif(marks<=70 and marks>=60):
  print(marks," Grade D")
elif(marks<=60 and marks>=40):
  print(marks," Grade E")
elif(marks<=40 and marks>=0):
  print(marks," Grade F")