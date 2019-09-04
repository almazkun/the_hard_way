def break_words(stuff):
    """This function divide sentences into words"""
    words = stuff.split(" ")
    return words


def sort_words(words):
    """Sort words"""
    return sorted(words)


def print_first_word(words):
    """Prints fist word"""
    word = words.pop(0)
    print(word)


def print_last_word(words):
    """Prints last word"""
    word = words.pop(-1)
    print(word)


def sort_sentence(sentence):
    """Return sorted sentence"""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last_words(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
