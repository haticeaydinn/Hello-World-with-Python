# class Point:
#     # constructor init method:
#     def __init__(self, x, y):
#         self.x = x  # point.x = 10
#         self.y = y  # point.y = 20
#
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
#
# # point1.draw()  --> method
# # point1.x = 10  -->  attribute
# point1 = Point(10, 20)
# point1.draw()
# print(point1.x)
# print(point1.y)
#

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hi, I am {self.name} !')


my_person = Person("Hatice")
my_person.talk()
