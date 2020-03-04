def collatz(number):
    """
    Collatz conjecture
    :param number:
    :return: collatz_lst
    """
    # or recursive
    #
    # print(number)
    # if number == 1:
    #     return 1
    # return collatz(number * 3 + 1) if number % 2 else collatz(number / 2)
    collatz_lst = [number]
    while number != 1:
        if number % 2:
            number = number * 3 + 1
            collatz_lst.append(number)
        else:
            number /= 2
            collatz_lst.append(number)

    return collatz_lst


def main():
    print(collatz(11))


if __name__ == '__main__':
    main()
