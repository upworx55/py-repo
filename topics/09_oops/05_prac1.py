
# Q: Create student class that takes name & marks of 3 subjects as arguments in constructor. 
# Then create a method to print the average marks of the student.

class Student:
    def __init__(self, name, marks):
        self.name = name  # instance attribute
        self.marks = marks  # instance attribute (list of marks)

    def get_avg(self):  # instance method to calculate average marks
        sum = 0
        for val in self.marks:
            sum += val
        print("Average marks of", self.name, "is:", sum / len(self.marks))

s1 = Student("Ram", [90, 85, 95])  # creating an object of class Student with name and marks
s1.get_avg()  # calling the instance method get_avg() using the object s1

s1.name = "Shyam"  # changing the name of the student
s1.get_avg()  # calling the instance method get_avg() using the object s1 after changing the name

s1.name = "Hari"  # changing the name of the student again
s1.marks = [80, 75, 85]  # changing the marks of the student
s1.get_avg()  # calling the instance method get_avg() using the object s1


