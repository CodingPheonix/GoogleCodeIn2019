import matplotlib
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
f = open("output.txt", "r")

#Plot points here
pointStr = f.readlines()
for i in pointStr:
    tmp = [int(x) for x in i if x != ',' and x != '\n']
    ax.plot(tmp[0], tmp[1], 'o', color='black')

ax.set(xlabel='x-axis', ylabel='y-axis',
       title='Some data that outputted by the C++ program')
ax.grid()

plt.show()
