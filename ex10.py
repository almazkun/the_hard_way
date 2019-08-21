d_artagnan = "\tMy name d'Artagnan"
athos = "this line\nis divided in half"
porthos = "I am \\ - \\ mushketire!"
aramis = """
Chose one:
\t* Graf
\t* Miledy
\t* Baron\n\t* General
"""

print(d_artagnan)
print(athos)
print(porthos)
print(aramis)


while True:
    for i in {"/", "- ", "|", "\\", "|"}:
        print(" {}\r".format(i))