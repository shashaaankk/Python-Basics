def factorial(n):
   factorial=1
   if(n==0):
       return factorial
   else:
       while n>=1:
           factorial*=n
           n=n-1
   return(factorial)

print(factorial(3))
