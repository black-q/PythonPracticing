"""
BMI Calculator
"""


def compute_bmi(weight, height):
    """
    Calculate BMI and return category
    :param weight:
    :param height:
    :return: result
    """
    bmi = weight / height ** 2
    if bmi < 18.5:
        result = 'underweight'
    elif bmi > 25:
        result = 'overweight'
    else:
        result = 'normal'

    return result


def main():
    user_weight = float(input("Your weight [kg]: "))
    user_height = float(input("Your height [m]: "))
    user_result = compute_bmi(user_weight, user_height)

    print(f'You are {user_result}')


if __name__ == '__main__':
    main()
