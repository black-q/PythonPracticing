"""
An Isogram is a word in which no letter occurs more than once
"""


def is_isogram(word):
    """
    Check if the word is an isogram
    :param word:
    :return:
    """
    letters = set()
    for letter in word.lower():
        if letter in letters:
            return False
        letters.add(letter)

    return True


def dead():
    """
    Escape
    :return:
    """
    print("Bye!")
    exit(0)


def main():
    """
    Prints result
    :return:
    """
    while True:
        user_word = input("Please provide the word: ").strip()
        answer = 'is' if is_isogram(user_word) else 'is not'
        print(f'Word {user_word} {answer} an isogram.')
        escape = input("Do you want to check another word (y / n)?")

        if escape != 'n':
            dead()


if __name__ == '__main__':
    main()
