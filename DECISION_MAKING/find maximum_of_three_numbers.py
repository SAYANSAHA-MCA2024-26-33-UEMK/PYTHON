a=int(input("enter the 1st number:"))
b=int(input("enter the 2nd number:"))
c=int(input("enter the 3rd number:"))
if(a>b):
  if(a>c):
    print(a," 1st value is a maximum value")
  else:
    print(c," 3rd value is a maximum value")
else:
  if(b>c):
    print(b," 2nd value is a maximum value")
  else:
    print(c," 3rd value is a maximum value")