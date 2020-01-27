class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello my name is {}".format(self.name))

    def sayage(self):
        print("I am {} years old".format(self.age))


p = Person("Calvin Raveenthran", 27)
p.greet()
p.sayage()