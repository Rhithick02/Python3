import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [2, 4, 6, 8]

# 'o', '--'
plt.plot(x, y, '--', color = "red")
plt.title("TESTING")
plt.xlabel("x")
plt.ylabel("y")
plt.show()