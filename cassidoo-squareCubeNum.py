def squareCubeNum(num: int):
  if num < 0: # validates the input. i could've just returned out, but figured to feature the functionality of the code.
    print(str(num) + " is negative, so it cannot have a perfect square. However, if it was " + str(abs(num)) + ":")
    
  posNum = abs(num) # takes the absolute value of the input, making it positive.
  
  highestCubeRoot = round(pow(posNum, 1/3)) # lets the application quickly iterate through the closest cubed numbers to the input
  
  for i in range(1, highestCubeRoot, 1):
    perfectCube = pow(i, 3) # we know this is a perfect cube
    if ((pow(perfectCube, 1/2) == round(pow(perfectCube, 1/2)))): # check if the perfect cube has a perfect square
      print(str(perfectCube))
