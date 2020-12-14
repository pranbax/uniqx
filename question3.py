from inputNumber import inputNumber
import math


def primeFactors(num):
  factors = []
  i = 2

  if num < 2:
    while num < 2:
      print("Invalid Input. Enter number equal or more than 2\n")
      num = inputNumber("Enter Number(default is 10): ", default=10)
    
  while i <= num:
    if (num % i) == 0:
      factors.append(i)
      num = num / i
    else:
      i += 1

  return factors

## USER INPUT
print("\n=============================")
num = inputNumber("Enter Number(default is 10): ", default=10)


## OUTPUT
output = primeFactors(num)
print(f"\nPrime factors of number '{num}' is/are: {output} ")
print("=============================\n")