def is_ones(n_ones, ones_list):
    count = 0
    for element in ones_list:
        if element == 1:
            count += 1
        else:
            count = 0

        if count == n_ones:
            return True

    return False


def main():
    default_list = [0, 1, 1, 1, 0, 1, 1, 0, 0, 0]
    n_ones = int(input("How many ones is next to each other? : "))
    print(f"It's {is_ones(n_ones, default_list)}")


if __name__ == '__main__':
    main()
