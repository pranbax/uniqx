def inputNumber(msg: str, default=None) -> int:
  """
  Get user input integer
  """
  while True:
    try:
      userInput = int(input(msg))
    except ValueError:
      if default is not None:
        return default
      else:
        print("Invalid input. Please Input a Number")
    else:
      return userInput