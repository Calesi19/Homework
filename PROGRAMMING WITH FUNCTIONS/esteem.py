

def main():
    print("This program is an implementaiton of the Rosenberg Self-Esteem Scale.\n This program will show you ten statements that you could possibly\napply to yourself. Please rate how much you agree with each of the\nstatements by responding with one of these four letters:")
    print("\nD means you strongly disagree with the statement.\nd means you disagree with the statement.\na means you agree with the statement. \nA means you strongly agree with the statement.\n")
    
    NEGATIVE = -1
    POSITIVE = 1

    score = 0
    score += survey("1. I feel that I am a person of worth, at least on an equal plane with others.", POSITIVE)
    score += survey("2. I feel that I have a number of good qualities.", POSITIVE)
    score += survey("3. All in all, I am inclined to feel that I am a failure.", NEGATIVE)
    score += survey("4. I am able to do things as well as most other people.", POSITIVE)
    score += survey("5. I feel I do not have much to be proud of.", NEGATIVE)
    score += survey("6. I take a positive attitude toward myself.", POSITIVE)
    score += survey("7. On the whole, I am satisfied with myself.", POSITIVE)
    score += survey("8. I wish I could have more respect for myself.", NEGATIVE)
    score += survey("9. I certainly feel useless at times.", NEGATIVE)
    score += survey("10. At times I think I am no good at all.", NEGATIVE)

    print(f"\nYour score is {score}.\nA score below 15 may indicate problematic low self-esteem.")


def survey(statement, pos_or_neg):
    print(statement)
    answer = input("Enter D, d, a, or A: ")
    score = 0
    if answer == 'D':
        score = 0
    elif answer == 'd':
        score = 1
    elif answer == 'a':
        score = 2
    elif answer == 'A':
        score = 3

    if pos_or_neg == NEGATIVE:
        score = 3 - score

    return score


