
def func1():
   print("Hello in func1")


func1()   

# RECURSION

def fac(n):
   if n==0 or n==1:
      return 1
   return n* fac(n-1) 

print(fac(5))