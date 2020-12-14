from inputNumber import inputNumber

def squareRoot(num):

  if num <= 0:
    print("Number must be a real integer")
    return None

  n = None

  # WILD GUESS APPROX VALUE OF n FOR THE ROOT OF num
  # THEN COMPUTE RECURSIVELY ni+1 = (1/2)(ni + (num/ni))
  _n = num / 3 #this doesn't matter

  while True:
    n = _n
    _n = (n + (num / n)) / 2
    # print(_n)

    if n == _n: break
  
  return n


## USER INPUT
print("\n=============================")
num = inputNumber("Enter Number(default is 9): ", default=9)


## OUTPUT
output = squareRoot(num)
if not output: quit()
print(f"The square root of number '{num}' is {output}")
print("=============================\n")