class Person:
    def __init__(self, weight, hight):
        self.weight = weight
        self.hight = hight

    def say(self, string):
        print ("Hello, my name is {}".format(string))

class Student(Person):
    def __init__(self, weight, height):
        super().__init__(weight, height)

    def course(self, course):
        self.course = course


Eugene = Student(65, 175)
Eugene.course = 2

Eugene.say("Eugene")
print("My height is: {}\nMy weight is: {}\nMy cousrse is: {}".format(Eugene.hight, Eugene.weight, Eugene.course))