class Car:

    acceleration = 10

    def __init__(self, registration_number):
        self.registration_number = registration_number
        self.in_motion = False
        self.speed = 0

    def drive(self):
        self.in_motion = True

    def accelerate(self):
        self.speed += self.acceleration

    def stop(self):
        self.in_motion = False
        self.speed = 0


if __name__ == '__main__':
    my_old_nissan = Car('ERA39XV')
    print(my_old_nissan)
    print(my_old_nissan.registration_number, end='\n\n')

    print(my_old_nissan.in_motion)
    print(my_old_nissan.speed)

    my_old_nissan.drive()
    print(my_old_nissan.in_motion)
    print(my_old_nissan.speed)

    my_old_nissan.accelerate()
    print(my_old_nissan.in_motion)
    print(my_old_nissan.speed)

    my_old_nissan.stop()
    print(my_old_nissan.in_motion)
    print(my_old_nissan.speed)
