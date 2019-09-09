from nose.tools import *
from ex48.lexicon import *
from copy import deepcopy
from ex49 import *


global_test_lists = [
    scan("south"),
    scan("door"),
    scan("go"),
    scan("to"),
    scan("234"),
    scan("error123"),
    scan("the east door"),
    scan("go to east"),
    scan("bear go to the door"),
    scan("the princess kill 10 bears"),
]

test_types = [
    "direction",
    "noun",
    "verb",
    "stop",
    "number",
    "error",
    "stop",
    "verb",
    "noun",
    "stop",
    None,
]


list_len = len(global_test_lists)


def test_peek():
    test_lists = deepcopy(global_test_lists)

    for i in range(list_len):
        test_list = test_lists[i]
        expected_word = test_types[i]
        assert_equal(peek(test_list), expected_word)


def test_match():
    test_lists = deepcopy(global_test_lists)

    for i in range(list_len):
        test_list = test_lists[i]
        test_type = test_types[i]
        if len(test_list) > 0:
            expected_word = test_list[0]
        else:
            None
        assert_equal(match(test_list, test_type), expected_word)
        print(
            i,
            "\ttest_list: >>",
            test_list,
            "<< test_type: >>",
            match(test_list, test_type),
            test_type,
            "<< \texpected_word >>",
            expected_word,
        )

    assert_equal(skip(test_objects, "direction"), "verb")


def test_skip():
    test_objects = deepcopy(global_test_lists)
    print(test_objects)
    a = skip(test_objects, "direction")
    print(a)
    assert_equal(skip(test_objects, "direction"), "verb")
