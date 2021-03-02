import matplotlib.pyplot as plt
plt.style.use("ggplot")

x = ['Nuclear', 'Gas', 'Oil', 'Coal']
energy = [5, 15, 22, 24]

x_pos = [i for i, _ in enumerate(x)]

plt.bar(x_pos, energy, color='green')
plt.xlabel("Energy Source")
plt.ylabel("Energy Output")
plt.title("Fuel Sources")

plt.xticks(x_pos, x)

plt.show()
