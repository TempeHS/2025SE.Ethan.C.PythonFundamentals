print("What's your name?")  # initial prompt to user
name = input()  # store user's name on seperate line

# (All changes) remove any whitespace + capitalise name
name = name.strip().title()

print("Hello,", name)  # reply to user
