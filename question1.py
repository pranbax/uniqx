from inputNumber import inputNumber

def output_1(num1, num2):
  x = num1
  y = num2
  output = [x, y]

  while len(output) < 10:
    last_index = len(output)-1
    last_num = output[last_index]
    prev_num = output[last_index - 1]

    next_num = prev_num + last_num

    output.append(next_num)
  
  return output


if __name__ == '__main__':
  defaults = [0, 1]

  ## QUESTION 1 INPUT:
  print("\n=============================")
  print("QUESTION 2 INPUT")
  num1 = inputNumber(f"Enter First Number(default: {defaults[0]}) : ", defaults[0])
  num2 = inputNumber(f"Enter Second Number(default: {defaults[1]}) : ", defaults[1])

  ## OUTPUT:
  print(output_1(num1, num2), "\n")
  print("=============================\n")