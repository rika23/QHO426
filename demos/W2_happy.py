h = input("Are you happy?")
k = input("Do you know it?")
if h.lower() == "yes" and k.lower() == "yes":
  print("Clap your hands!")
elif h == "yes" and k == "no":
  print("Show your happiness")
else:
  print("Help is available. Talk to me!")
