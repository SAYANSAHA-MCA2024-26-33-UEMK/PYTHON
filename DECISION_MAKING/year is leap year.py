"Write a Java program to check whether a year is leap year or not."
year=int(input("enter the year:"))
if(year%100==0):
  if(year%400==0):
    print(year," is a leap year")
  else:
    print(year," is a not leap year")
else:
  if(year%4==0):
    print(year," is a leap year")
  else:
    print(year," is a not leap year")