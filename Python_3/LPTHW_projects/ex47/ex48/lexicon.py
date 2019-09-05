def scan(line):
    words = line.split(" ")
    result = []
    for word in words:
        type = analise(word.lower())
        result.append((type, word))
    print(words, result)
    return result


def analise(word):
    rules = {
        "direction": [
            "north",
            "south",
            "east",
            "west",
            "down",
            "up",
            "left",
            "right",
            "back",
        ],
        "verb": ["go", "run", "stop", "kill", "eat"],
        "stop": ["the", "in", "a", "of", "from", "to", "at", "it"],
        "noun": ["door", "bear", "princess", "cabinet"],
    }

    if word.isdigit():
        return "number"
    for rule, rule_list in rules.items():
        if word in rule_list:
            return rule
    return "error"
