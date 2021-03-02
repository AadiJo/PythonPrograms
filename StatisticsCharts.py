import matplotlib.pyplot as plt
name = input("Hi, what's your name: ")
print("Hello,", name)
print("This program will allow you to make pie charts about your own data.\nLet's get started!")
NumOfLabels = int(input("How many pieces of data will you enter?  "))
labels = []
values = []
i = 1
print("Please name your pieces of data")
while i <= NumOfLabels:
    name2 = input("Please give the name for your data: ")
    labels.append(name2)
    i += 1
print("Please enter the values for your pieces of data")
i = 1
i2 = 0
while i <= NumOfLabels:
    print("Data name:", labels[i2])
    value = float(input("Please give the value for the data: "))
    values.append(value)
    i += 1
    i2 += 1
Title = input("What do you want your title to be?  ")
plt.figure(figsize=(5, 5))
plt.pie(values, labels=labels, autopct="%.2f%%", shadow=True)
plt.title(Title)
plt.show()
