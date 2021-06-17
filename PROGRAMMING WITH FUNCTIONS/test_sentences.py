import pytest
from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase


def test_get_determiner():
    # Test the singular determiners.
    singular_determiners = ["the", "one"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(0,1):
        word = get_determiner('singular')
        # Verify that the word returned from get_determiner is
        # one of the words in the singular_determiners list.
        assert word in singular_determiners

    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.

    # Test the plural determiners.
    plural_determiners = ["some", "many"]
    for _ in range(0,1):
        word = get_determiner('plural')

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    singular_nouns = ["adult", "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]
    for _ in range(0, len(singular_nouns)-1):
        word = get_noun('singular')
        assert word in singular_nouns

    plural_nouns = ["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]
    for _ in range(0, len(plural_nouns)-1):
        word = get_noun('plural')
        assert word in plural_nouns


def test_get_verb():
    past_verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    for _ in range(0, len(past_verbs)-1):
        word = get_verb('singular', 'past')
        assert word in past_verbs

    future_verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    for _ in range(0, len(future_verbs)-1):
        word = get_verb('singular', 'future')
        assert word in future_verbs

    present_verbs_singular = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(0, len(present_verbs_singular)-1):
        word = get_verb('singular', 'present')
        assert word in present_verbs_singular

    present_verbs_plural = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    for _ in range(0, len(present_verbs_plural)-1):
        word = get_verb('plural', 'future')
        assert word in present_verbs_plural
    
def test_get_preposition():
    preposition_words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    for _ in range(0, len(preposition_words)-1):
        word = get_preposition()
    
    assert word in preposition_words

def test_get_prepositional_phrase():
    preposition_words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    singular_determiners = ["the", "one"]
    plural_determiners = ["some", "many"]
    singular_nouns = ["adult", "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]
    plural_nouns = ["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]

    #preposition word
    for _ in range(0, len(preposition_words)-1):
        phrase = get_prepositional_phrase('singular')
        phrase = phrase.split()
        assert phrase[0] in preposition_words

    #singular determiner
    for _ in range(0, len(singular_determiners)-1):
        phrase = get_prepositional_phrase('singular')
        phrase = phrase.split()
        assert phrase[1] in singular_determiners

    #singular nouns
    for _ in range(0, len(singular_nouns)-1):
        phrase = get_prepositional_phrase('singular')
        phrase = phrase.split()
        assert phrase[2] in singular_nouns

    #plural determiner
    for _ in range(0, len(plural_determiners)-1):
        phrase = get_prepositional_phrase('singular')
        phrase = phrase.split()
        assert phrase[1] in plural_determiners

    #plural nouns
    for _ in range(0, len(plural_nouns)-1):
        phrase = get_prepositional_phrase('plural')
        phrase = phrase.split()
        assert phrase[2] in plural_nouns


pytest.main(["-v", "--tb=line", "-rN", "test_sentences.py"])

