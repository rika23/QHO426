print("What type of cover does the book have?")
answer = input()
if answer == "soft cover":
    print("Is the book perfect-bound?")
    answer = input()
    if answer == "yes":
      print("Soft cover, perfect bound books are very popular!")
    else:
      print("Soft covers with coils or stitches are great for short books")
elif answer == "hard cover":
      print("Books with hard covers can be more expensive!")