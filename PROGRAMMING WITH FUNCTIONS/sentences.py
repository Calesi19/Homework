import random

def get_determiner(quantity):
    
    if quantity == 'singular':
        words = ["The", "One"]
    else:
        words = ["Some", "Many"]

    return random.choice(words)

def get_noun(quantity):

    if quantity == 'singular':
        words = ["adult", "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]
    else:
        words = ["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]
    
    return random.choice(words)


def get_verb(quantity, tense):

    if tense == 'past':
        words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == 'future':
        words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    elif tense == 'present' and quantity == 'singular':
        words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == 'present' and quantity == 'plural':
        words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    
    return random.choice(words)

def get_preposition():
    words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    return random.choice(words)

def get_prepositional_phrase(quantity):
    return f'{get_preposition()} {get_determiner(quantity).lower()} {get_noun(quantity)}'


def main():
    closing_prompt = ' '
    while closing_prompt.lower() != 'q':
        quantities = ['singular', 'plural', 'singular', 'plural', 'singular', 'plural']
        tenses = ['past', 'past', 'present', 'present', 'future', 'future']
        print()
        for i in range(0,6):
            print(f'{i + 1}. {get_determiner(quantities[i])} {get_noun(quantities[i])} {get_verb(quantities[i], tenses[i])}.')
        print()
        for i in range(0,6):
            print(f'{i + 1}. {get_determiner(quantities[i])} {get_noun(quantities[i])} {get_verb(quantities[i], tenses[i])} {get_prepositional_phrase(quantities[i])}.')
        closing_prompt = input("\nEnter 'q' to quit. ")


main()
