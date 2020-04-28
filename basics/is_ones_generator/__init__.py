def is_ones(n_ones, ones_list):
    """
    Return True if in ones_list is n_ones next to each other and False if doesn't
    :param n_ones:
    :param ones_list:
    :return: Bool
    """

    gen = (sum(ones_list[i:i+n_ones]) for i in range(len(ones_list)))

    for element in gen:
        if element == n_ones:
            return True

    return False


def main():
    default_list = [0, 1, 1, 1, 0, 1, 1, 0, 0, 0]
    n_ones = int(input("How many ones is next to each other? : "))
    print(f"It's {is_ones(n_ones, default_list)}")


if __name__ == '__main__':
    main()
