""""Validate PESEL number and returning birth date, gender and age"""

from datetime import date, datetime, timedelta

def dead():
    """
    Escape
    :return:
    """
    print("Bye!")
    exit(0)


def pesel_validation(pesel_number):
    """
    Validation
    :param pesel_number:
    :return: bool
    """
    # or with regular expression:
    #   import re
    #   regular = r'^\d{11}$'
    #   reg = re.match(regular, pesel_number)
    #   if reg: ...
    # but I prefer shorter version with len :)
    if len(pesel_number) == 11:
        factor = (9, 7, 3, 1, 9, 7, 3, 1, 9, 7)
        sum = 0
        for i in range(0, 10):
            sum += int(pesel_number[i]) * factor[i]
        if sum % 10 == int(pesel_number[10]):
            return True
        else:
            return False
    else:
        return False


def get_gender(pesel_number):
    """
    The PESEL number determines gender
    :param pesel_number:
    :return: gender in string
    """
    if int(pesel_number[9]) % 2:
        return 'Man'

    return 'Woman'


def get_birth_date(pesel_number):
    """
    The PESEL number determines the date of birth
    :param pesel_number:
    :return: date of birth
    """
    year = int(pesel_number[0:2]) + 1900
    month = int(pesel_number[2:4])
    day = int(pesel_number[4:6])

    if 20 < month < 40:
        year += 100
        month -= 20
    elif 40 < month < 60:
        year += 200
        month -= 40
    elif 60 < month < 80:
        year += 300
        month -= 60
    elif month > 80:
        year -= 100
        month -= 80

    if month < 10:
        month = f'0{month}'

    if day < 10:
        day = f'0{day}'

    return f'{year}-{month}-{day}'


def get_age(pesel_number):
    """
    The PESEL number determines age
    :param pesel_number:
    :return: age
    """
    today = date.today()
    birth_date = datetime.strptime(get_birth_date(pesel_number), '%Y-%m-%d').date()
    age = (today - birth_date) // timedelta(days=365.2425)

    return age


def main():
    """
    Prints data from pesel number
    :return:
    """

    pesel_information = dict()

    while True:
        pesel = input('Please provide PESEL number: \n> ')
        if pesel_validation(pesel):
            pesel_information['Gender'] = get_gender(pesel)
            pesel_information['Birth date'] = get_birth_date(pesel)
            pesel_information['Age'] = get_age(pesel)

            print(pesel_information)
            dead()
        else:
            print('The PESEL number is not valid')
            escape = input('Quit? y/n \n> ')

            if escape != 'n':
                dead()


if __name__ == '__main__':
    main()
