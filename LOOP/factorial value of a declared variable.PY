"Write a Java Program to calculate factorial value of a declared variable."
a=int(input("enter the number:"))
fact=1
for i in range(1,a+1):
  fact=fact*i
print("the factorial is:",fact)