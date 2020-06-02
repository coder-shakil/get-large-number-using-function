#print large number by using function

def large_number (a,b,c):
  if a>b and a>c :
    print(a)

  elif b>c and b>a :
    print(b)

  else :
    print(c)

large_number(10,20,30)
large_number(30,10,20)
large_number(20,30,10)