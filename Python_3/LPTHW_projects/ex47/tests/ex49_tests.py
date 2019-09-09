from nose.tools import *
from ex48.lexicon import *
from ex49 import peek, match, skip


test_sentence = "North go to the bear"
test_objects = scan(test_sentence)

def test_peek():
    assert_equal(peek(test_objects), ("direction"))


def test_match():
    assert_equal(match(test_objects, "direction"), ("direction", "North"))


def 

def skip (word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)


