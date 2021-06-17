import random
def append_random_numbers(numbers_list, quantity):
    for i in range(0, quantity):
        numbers_list.append(random.randint(1, 1000))
    
def append_random_words(words_list, quantity):
    words = ['join', 'love', 'smile', 'love', 'cloud', 'head']
    for i in range(0, quantity):
        words_list.append(random.choice(words))

def main():
    randnums = []
    closing_prompt = ' '
    while closing_prompt.lower() != 'q':
        if randnums:
            print(randnums)
        append_random_numbers(randnums, 1)
        print(randnums)
        append_random_numbers(randnums, 2)
        print(randnums)
        randwords = []
        append_random_words(randwords, 1)
        print(randwords)
        append_random_words(randwords, 2)
        print(randwords)
        closing_prompt = input("\nPress 'q' to exit. ")

main()