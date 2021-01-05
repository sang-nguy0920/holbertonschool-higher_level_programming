class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hi, my name is {}'.format(self.name))

p = Person('Swaroop')
p.say_hi()
# The previous 2 lines can also be written as
# Person('Swaroop').say_hi()
