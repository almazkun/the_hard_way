from nose.tools import *
from ex48.lexicon import *
from ex49.parser import *


def test_peek():
    test_object = scan("go north bear to eat princess")
    print(test_object)
    assert_equal(peek(test_object), "verb")


def test_match():
    test_object = scan("go north bear to eat princess")
    print(test_object)
    assert_equal(match(test_object, "verb"), ("verb", "go"))


def test_skip():
    # deleting first element
    test_object_0 = scan("to go north")
    skip(test_object_0, "stop")
    assert_equal(test_object_0, scan("go north"))

    # deleting only one element
    test_object_1 = scan("asd")
    skip(test_object_1, "error")
    assert_equal(test_object_1, [])

    # only first element affected
    test_object_2 = scan("go to north")
    skip(test_object_2, "stop")
    assert_equal(test_object_2, scan("go to north"))

    # other types of words affected
    test_object_3 = scan("go to north")
    skip(test_object_3, "verb")
    assert_equal(test_object_3, scan("to north"))


def test_parse_verb():
    # test to find "verb"
    test_object_0 = scan("go north")
    assert_equal(parse_verb(test_object_0), *scan("go"))

    # test to skip "stop" and find "verb"
    test_object_1 = scan("to go north")
    assert_equal(parse_verb(test_object_1), *scan("go"))

    # rise error if "verb" not found
    test_object_2 = scan("to north")
    assert_raises(ParserError, parse_verb, test_object_2)


def test_parse_object():
    # test to find "noun"
    test_object_0 = scan("bear go")
    assert_equal(parse_object(test_object_0), *scan("bear"))

    # test to find "direction"
    test_object_1 = scan("north bear")
    assert_equal(parse_object(test_object_1), *scan("north"))

    # test to "skip" "stop" word
    test_object_2 = scan("to bear")
    assert_equal(parse_object(test_object_2), *scan("bear"))

    # test to raise and error
    test_object_3 = scan("to go")
    assert_raises(ParserError, parse_object, test_object_3)


def test_parse_subject():
    test_object_0 = scan("go bear")
    subj = match(scan("princess"), "noun")
    print(subj)
    a = parse_subject(test_object_0, subj)
    assert_equal(a.subject, ("princess"))
    assert_equal(a.verb, ("go"))
    assert_equal(a.object, ("bear"))


def test_parse_sentence():
    # if "noun", "verb", "object"
    test_object_0 = scan("bear go north")
    a = parse_sentence(test_object_0)
    assert_equal(a.subject, ("bear"))
    assert_equal(a.verb, ("go"))
    assert_equal(a.object, ("north"))

    # if "verb", "object"
    test_object_1 = scan("go north")
    b = parse_sentence(test_object_1)
    assert_equal(b.subject, ("player"))
    assert_equal(b.verb, ("go"))
    assert_equal(b.object, ("north"))

    # if "stop", "verb", "object"
    test_object_2 = scan("to go north")
    c = parse_sentence(test_object_2)
    assert_equal(c.subject, ("player"))
    assert_equal(c.verb, ("go"))
    assert_equal(c.object, ("north"))

    # if "stop", "noun", "verb", "object"
    test_object_3 = scan("to door go north")
    d = parse_sentence(test_object_3)
    assert_equal(d.subject, ("door"))
    assert_equal(d.verb, ("go"))
    assert_equal(d.object, ("north"))

    # if "error"
    test_object_4 = scan("tos door go north")
    assert_raises(ParserError, parse_sentence, test_object_4)
