class MyClass:
    def __init__(self, max_students):
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return "The student was added to your class"
        return "Your class is full. The student was not added."

    def view_class(self):
        return self.students


print("Welcome to Create a Class!")
Max_students = int(input("What is the limit of students in your new class: "))
myClass = MyClass(Max_students)
options = input("Would you like to\n(1) Add a student\n(2) View your class\n(3) Exit Create a Class\n\nPlease enter"
                " the number beside the action you want to do: ")

while options != "3":
    if options == "1":
        name = input("What is the name of your student: ")
        print(myClass.add_student(name))
    if options == "2":
        print(myClass.view_class())
    options = input("Would you like to\n(1) Add a student\n(2) View your class\n(3) Exit Create a Class\n\nPlease "
                    "enter the number beside the action you want to do: ")

print("Thank you for using Create a Class")
