print("Program started!")

print("Please enter a standard character:")
character = input()

if (len(character) == 1):
  print("The ASCII code for {} is {}".format(character, ord(character)))
else:
  print("Error with entry")

print("Program ended!")
