from inputNumber import inputNumber
import math

def output(num):
  quotient = math.floor(num / 2)
  last_remainder = num % 2

  binary = [str(last_remainder)]

  while quotient > 0:
    modulo = quotient % 2
    binary.insert(0, str(modulo))

    quotient = math.floor(quotient / 2)

  return "".join(binary)


if __name__ == '__main__':

  ## USER INPUT
  print("\n=============================")
  num = inputNumber("Enter Number(default is 50) : ", default=50)

  ## OUTPUT
  print(f"\nThe binary form of '{num}' is: {output(num)} ")
  print("=============================\n")