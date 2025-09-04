#Q1
'''def diff(n):
    if n > 17:
        return 2 * abs(n - 17)
    else:
        return 17 - n

print(diff(22))
print(diff(10))'''

#Q2
'''def in_range(n):
    return (100 <= n <= 1000) or (n == 2000)

print(in_range(500))
print(in_range(1500))'''

#Q3
'''def rev(s):
    return s[::-1]

print(rev("robot"))'''

#Q4
'''def count_case(s):
    d = {"UPPER": 0, "LOWER": 0}
    for ch in s:
        if ch.isupper():
            d["UPPER"] += 1
        elif ch.islower():
            d["LOWER"] += 1
    return d

print(count_case("RobOt"))'''

#Q5
'''def distinct(lst):
    return list(set(lst))

print(distinct([1,2,2,3,4,4,5]))'''

#Q6
'''def evens(lst):
    return [x for x in lst if x % 2 == 0]

print(evens([1,2,3,4,5,6,7,8,9]))'''

#Q7
'''def robot():
    def move():
        print("Robot is moving")
    move()

robot()'''

#Q8
'''def student(name, age, course):
    pass

print(student.__code__.co_varnames)'''

#Q9
'''def move_robot(x, y, direction):
    if direction == "up":
        y += 1
    elif direction == "down":
        y -= 1
    elif direction == "left":
        x -= 1
    elif direction == "right":
        x += 1
    return (x, y)

print(move_robot(0,0,"up"))
print(move_robot(2,3,"left"))'''

#Q10
'''def classify_temp(t):
    if t < 15:
        return "Cold"
    elif 15 <= t <= 30:
        return "Moderate"
    else:
        return "Hot"

print(classify_temp(10))
print(classify_temp(25))
print(classify_temp(35))'''

#Q11
'''def goal(path):
    x, y = 0, 0
    for m in path:
        if m == "up":
            y += 1
        elif m == "down":
            y -= 1
        elif m == "left":
            x -= 1
        elif m == "right":
            x += 1
    return (x, y) == (2, 0)

print(goal(["up","right","right","down"]))
print(goal(["up","up","right"]))'''

#Q12
'''class Student:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class
    def display(self):
        print("ID:", self.student_id)
        print("Name:", self.student_name)
        print("Class:", self.student_class)

s = Student(101, "Alice", "URA302")
s.display()'''

#Q13
'''class Student2:
    def __init__(self, sid, name, clas):
        self.sid = sid
        self.name = name
        self.clas = clas

st1 = Student2(1, "Alice", "A")
st2 = Student2(2, "Bob", "B")
print("Student1:", st1.sid, st1.name, st1.clas)
print("Student2:", st2.sid, st2.name, st2.clas)'''

#Q14
'''import math
class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r * self.r
    def perimeter(self):
        return 2 * math.pi * self.r

c = Circle(5)
print("Area:", c.area())
print("Perimeter:", c.perimeter())'''

#Q15
'''
class MyString:
    def __init__(self):
        self.s = ""
    def get_String(self):
        self.s = input("Enter string: ")
    def print_String(self):
        print(self.s.upper())

ms = MyString()
ms.get_String()
ms.print_String()
'''