# definition
class Calculator:
    def __init__(self, number1, number2):
        self.num1 = number1
        self.num2 = number2

    def Add(self):
        answer = self.num1 + self.num2
        print(answer)

    def Subtract(self):
        if self.num1 > self.num2:
            answer = self.num1 - self.num2
            print(answer)
        if self.num2 > self.num1:
            answer = self.num2 - self.num1
        else:
            answer = 0
        print(answer)

    def Multiply(self):
        answer = int(self.num1) * int(self.num2)
        print(answer)

    def Divide(self):
        if self.num2 > self.num1:
            answer = float(self.num2) / float(self.num1)
        if self.num1 > self.num2:
            answer = float(self.num1) / float(self.num2)
        print(answer)


# main execution
print("Welcome to the calculator: updated version!")

num1 = float(input("What is the first number: "))
num2 = float(input("What is the second number: "))

operation = input("Welcome to the calculator: special version!\n\nWould you like to\n(1)Add\n(2)Subtract\n"
                  "(3)Multiply\n(4)Divide\n(5)Exit\n\nPlease enter the number beside the action you want to do: ")

cal = Calculator(num1, num2)
while operation != "5":
    if operation == "1":
        cal.Add()
    if operation == "2":
        cal.Subtract()
    if operation == "3":
        cal.Multiply()
    if operation == "4":
        cal.Divide()
    if operation == '5':
        print('Bye!')
    operation = input("Welcome to the calculator: special version!\n\nWould you like to\n(1)Add\n(2)Subtract\n"
                      "(3)Multiply\n(4)Divide\n(5)Exit\n"
                      "\nPlease enter the number beside the action you want to do: ")

print("Thank you for using the calculator!")
