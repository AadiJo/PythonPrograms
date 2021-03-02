import matplotlib.pyplot as plt
import time
values = []
labels = []
file = open(r"C:\Users\Simmi\Downloads\Pie Chart - Sheet1-1.txt", "r")
for x in file:
    List1 = str(x)
    List = List1.rsplit(",")
    labels.append(List[0])
    values.append(List[1])

plt.figure(figsize=(5, 5))
plt.pie(values, labels=labels, autopct="%.2f%%", shadow=True)
plt.title("Your Graph")
print("Creating pie chart....")
time.sleep(1.5)
plt.show()
