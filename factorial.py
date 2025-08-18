def factorial(num):
   i = 1
   fact = 1
   while i <= num:
    fact *= i
    i += 1
   return fact 

print(factorial(5))
    