from sys import argv


script, user_name = argv
prompt = "> "


print("Hi {}, I am a {} script.".format(user_name, script))
print("I want to ask you 2 questions.")
print("Do you like me, {}".format(user_name))
likes = input(prompt)

print("Where do you live, {}?".format(user_name))
lives = input(prompt)

print("What computer do you use, {}".format(user_name))
computer = input(prompt)

print(
    """
So, you said that you {} me.
You live in some nevewhere called {}.
And you have something called {}. Wonderfull!
""".format(
        likes, lives, computer
    )
)
