name = input("Enter your name: ")

#len() - function that returns the length of string*

if len(name) > 9: 
    print("Your name is way toooo long to remember. Can I use a nickname please?")
    print("This prints too")
elif len (name) <= 3: 
    print("That is very short - easy to remember!")
else:
    print("Oh, your name is pretty short!")
print("Nice to meet you anyway, {}!" .format(name))