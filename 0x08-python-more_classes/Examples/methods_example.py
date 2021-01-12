def hi(obj):
    print("Hi, I am " + obj.name + "!")

class Robot:
    say_hi = hi


x = Robot()
x.name = "marvin"
Robot.say_hi(x)
