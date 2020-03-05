import matplotlib.pyplot as plt
import numpy as np

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


def collatz_plot(lst, number):
    step = range(len(lst))
    plt.plot(step, lst, linestyle='-', marker='.', color='b')
    plt.grid(True)
    plt.xlabel("Step")
    plt.ylabel("Number")
    plt.title(f"Collatz conjecture for: {number}")
    plt.savefig("collatz.png", dpi=72)
    plt.show()


def main():
    user_number = int(input("Please, provide number: "))
    result_lst = collatz(user_number)
    print(f'Collatz sequence for {user_number} is: {result_lst}')
    collatz_plot(result_lst, user_number)


if __name__ == '__main__':
    main()
