limite = int(input("Limite: "))
if limite <= 0:
 print "Debe de ser un entero positivo"
 exit()

def isPrime(number):
 if number % 2 == 0:
  return False
 count = 3
 while count < number:
  if number % count == 0:
   return False
  count = count + 1
 return True

number = 1
while number <= limite:
 if isPrime(number):
  print number
 number = number + 1
