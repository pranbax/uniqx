from inputNumber import inputNumber

def magic_square(num):

  if (num % 2) == 0:
    return "Only odd numbers are allowed"
  elif num <= 1:
    return "Input must be greater than 1"

  
  square = [[0 for x in range(num)] for y in range(num)]
  
  #POSITION OF 1
  x = 0
  y = num / 2
  initial = True

  n = 1
  while n <= (num * num):
    if initial:
      square[int(x)][int(y)] = n
      n += 1
      x = x - 1
      y = y + 1
      initial = False
      continue

    if x < 0 and y == num:
      x = x + 2
      y = num - 1
    else:
      if x == -1:
          x = num - 1
        
      if y >= num:
        y = 0
    
    try:
      if square[int(x)][int(y)]:
        x = x + 2
        y = y - 1
        continue
      else:
        square[int(x)][int(y)] = n
        n += 1
    except:
      break

    x = x - 1
    y = y + 1

  for i in range(0, num):
      for j in range(0, num):
          print('%2d ' % (square[i][j]),
                end='')

          # To display output
          # in matrix form
          if j == num - 1:
              print()



## USER INPUT
print("\n=============================")
num = inputNumber("Enter Number(default is 9): ", default=9)
magic_square(num)
print("=============================\n")