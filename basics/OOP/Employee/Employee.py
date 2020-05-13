import datetime


class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return f'{self.first}.{self.last}@company.pl'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split()

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay *= self.raise_amount

    @classmethod
    def set_raise_amount(cls, new_raise_amount):
        cls.raise_amount = new_raise_amount

    @staticmethod
    def is_work_day(day):
        return datetime.date.weekday(day) not in (5, 6)


if __name__ == '__main__':
    jan_kowalski = Employee('Jan', 'Kowalski', 6000)
    piotr_nowak = Employee('Piotr', 'Nowak', 4500)

    print(Employee.raise_amount)
    print(jan_kowalski.raise_amount)
    print(piotr_nowak.raise_amount)

    print("\n***Employee - set_raise_amount***")
    Employee.set_raise_amount(1.5)
    print(Employee.raise_amount)
    print(jan_kowalski.raise_amount)
    print(piotr_nowak.raise_amount)

    print("\n***Only jan_kowalski - set_raise_amount but all class objects have changed***")
    jan_kowalski.set_raise_amount(1.1)
    print(Employee.raise_amount)
    print(jan_kowalski.raise_amount)
    print(piotr_nowak.raise_amount)

    print("""\n***staticmethod***""")
    today = datetime.date.today()
    print(Employee.is_work_day(today))

    print("\n***Setters and Getters - property***")
    print(jan_kowalski.fullname)
    print(jan_kowalski.email)
    print("\n***Setters and Getters - setter***")
    jan_kowalski.fullname = 'Damian Kowalski'
    print(jan_kowalski.fullname)
    print(jan_kowalski.email)
    print("\n***Setters and Getters - deleter***")
    del jan_kowalski.fullname
    print(jan_kowalski.fullname)
    print(jan_kowalski.email)