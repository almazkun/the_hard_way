import ex25


print("Давайте попрактикуемся!")
print(
    "Вы должны знать об управляющих последовательностях с символом \\, которые \n управляют переносом строк и \t отступами."
)


poem = """
\tДля счастья
мне совсем немного надо.
Хочу тебя \n я нежно обнимать,
Хочу всегда
я быть с тобою рядом
\n\t\tИ никогда не отпускать!
"""


print("--------------")
print(poem)
print("--------------")


five = 10 - 2 + 3 - 6
print("Здесь должна быть пятерка: {}".format(five))


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)


print("Начиная с: {}".format(start_point))
print("У нас есть {} бобров, {} банок и {} ящиков.".format(beans, jars, crates))


start_point = start_point / 10


print("Также можно поступить следующим образом:")
print("У нас есть %d бобов, %d банок и %d коробков." % secret_formula(start_point))


sentence = "All good things come to those who weight."


words = ex25.break_words(sentence)
sorted_words = ex25.sort_words(words)

ex25.print_first_word(words)
ex25.print_last_word(words)
ex25.print_first_word(sorted_words)
ex25.print_last_word(sorted_words)
sorted_words = ex25.sort_sentence(sentence)
print(sorted_words)
ex25.print_first_and_last_words(sentence)
ex25.print_first_and_last_sorted(sentence)
