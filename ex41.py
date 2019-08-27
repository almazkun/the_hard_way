import random
from urllib.request import urlopen
import sys


WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []


PHRASES = {
    "class %%%(%%%):":
    "Creates class %%%, inherited from %%%.",
    "class %%%(object):\n\tdef __init__ (self, ***) ":
    "Class %%% combines __init__ with self, *** parameter.",
    "class %%%(object):\n\tdef ***(self, @@@) ":
    "Class %%% combines function *** with self, @@@ parameter.",
    "*** = %%%() ":
    "Initialize *** as %%% class instance.",
    "***.***(@@@) ":
    "From *** function *** taken and self, @@@ parameter.",
    "***.*** = '***'":
    "From *** attribute *** taken and set to '***'."
}


# training
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "russian":
    PHRASE_FIRST = True


# download words 
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip().decode("utf-8"))


def convert(snippet, phrase):
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(", ".join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        # class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # list of parameters
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


# end on CTRL + Z
try:
    while True:
        snippets = PHRASES.keys()
        random.shuffle(list(snippets))

        for snippet in snippets:
            phrase = PHRASES[snippet]

            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")

            print("ANSWER: {}\n\n".format(answer))

except EOFError:
    print("\n Saionara!")
