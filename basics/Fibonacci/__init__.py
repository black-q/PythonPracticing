"""
Fibonacci
"""


import matplotlib.pyplot as plt


def fibonacci(n):
    """
    Fibonacci sequence
    :param n:
    :return:
    """
    fibonacci_digits = list()
    for i in range(n):
        if i <= 1:
            fibonacci_digits.append(i)
        else:
            fibonacci_digits.append(fibonacci_digits[i - 1] + fibonacci_digits[i - 2])

    return fibonacci_digits


def fibonacci_plot(lst, number):
    step = range(len(lst))
    plt.plot(step, lst, linestyle='-', marker='.', color='b')
    plt.grid(True)
    plt.xlabel("Step")
    plt.ylabel("Number")
    plt.title(f"The Fibonacci sequence for: {number}")
    plt.savefig("fibonacci.png", dpi=72)
    plt.show()


def main():
    try:
        number_of_digits = int(input("Enter number of Fibonacci digits: "))
        print(fibonacci(number_of_digits))
        fibonacci_plot(fibonacci(number_of_digits), number_of_digits)
    except ValueError:
        print("Input is not an int.")


if __name__ == '__main__':
    main()
