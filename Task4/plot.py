import matplotlib
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
f = open("output.txt", "r")

#Plot points here
pointStr = f.readlines()
points = [list(map(int, i[:-1].split(","))) for i in pointStr]
plt.scatter(*zip(*points))

ax.set(xlabel='x-axis', ylabel='y-axis',
       title='Some data that was outputted by the C++ program')
ax.grid()

plt.show()
