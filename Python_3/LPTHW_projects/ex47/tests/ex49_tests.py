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
    print(test_lists)
    for i in range(list_len):
        test_list = test_lists[i]
        expected_word = test_types[i]
        assert_equal(peek(test_list), expected_word)


def test_match():
    test_lists = deepcopy(global_test_lists)
    print(test_lists[0][0][0], test_lists[1])
    for i in range(list_len):
        test_list = test_lists[i]
        test_type = test_types[i]
        if len(test_list) > 0:
            expected_word = test_list[0]
        else:
            None
        assert_equal(match(test_list, test_type), expected_word)


def test_skip():
    test_lists = deepcopy(global_test_lists)
    expected_lists1 = [
        scan("south"),
        scan("door"),
        scan("go"),
        [],
        scan("234"),
        scan("error123"),
        scan("east door"),
        scan("go to east"),
        scan("bear go to the door"),
        scan("princess kill 10 bears"),
        [],
    ]

    for i in range(list_len):
        test_list = test_lists[i]
        expected_list = expected_lists1[i]
        skip(test_list, "stop")
        assert_equal(test_list, expected_list)

    test_list2 = [("error", "error123")]
    expected_list2 = []
    skip(test_list2, "error")
    assert_equal(test_list2, expected_list2)


def test_parse_verb():
    """ test parse_verb function """
    test_lists_good = [scan("go"), scan("go to east"), scan("to error123 eat")]

    expected_lists = [scan("go"), scan("go"), scan("eat")]

    for i in range(len(test_lists_good)):
        test_list = test_lists_good[i]
        expected_list = expected_lists[i]
        assert_equal(parse_verb(test_list), *expected_list)

    # test bad situations
    test_lists_bad = [
        scan("south"),
        scan("door"),
        scan("234"),
        scan("east door"),
        scan("error123"),
        scan("to"),
        scan("bear go to the door"),
        scan("the princess kill 10 bear"),
        [],
    ]
    for i in range(len(test_lists_bad)):
        test_list = test_lists_bad[i]
        assert_raises(ParserError, parse_verb, test_list)