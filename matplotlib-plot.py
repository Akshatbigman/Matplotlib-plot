import matplotlib.pyplot as plt
import numpy as np

plt.plot([1,2,3,4], [5,6,7,8], color = "red", linestyle = "dotted", lw = 10)
plt.plot([7,9,11,13], [15,17,19,21], color = "green", linestyle = "dashed", lw = 8)
plt.plot([9,12,15,18], [5,6,7,8], color = "yellow", linestyle = "dashdot", lw=5)

plt.plot([3,4,5,6,7],[85,95,87,90,92], color= "red")


grades = np.array([3,4,5,6,7])
percentage = np.array([85,95,87,90,92])

plt.plot(grades, percentage, color = "red", ls = "dotted")

plt.xlabel("Grades")
plt.ylabel("Percentage")
plt.title("Grades vs Percentage")

plt.show()


ypoints = np.array ([3,8,1,10])

plt.plot(ypoints, marker ="*")
plt.show()

a = [1,2,3,4,5,6]
b = [1,22,352,31,523,123]

a1 = [32,12,53,2,3,42]
b1 = [3,342,531,22,34,4210]

plt.scatter(a,b, color = "r")
plt.scatter(a1,b1, color = "b")
plt.show()

c = [1,2,3,4,5,6]
d = [1,22,352,31,523,123]

c1 = [32,12,53,2,3,42]
d1 = [3,342,531,22,34,4210]

plt.scatter(c,d, color = "r", s = 10, marker = '*')
plt.scatter(c1,d1, color = "b", s = 10, marker = '*')
plt.show()

x = [1,2,3,4,5,6]
y = [1,22,352,31,523,123]

x1 = [32,12,53,2,3,42]
y1 = [3,342,531,22,34,4210]


plt.scatter([x,y], [x1,y1], color = ['red'], s = 100, marker = '*')


plt.scatter([1,2,3],[4,5,6], color = ['green','red','blue'], s = 100, marker = '*')

o = np.array(['A','B','C','D'])
p = np.array([3,8,1,10])

plt.bar(o,p)
plt.show

x = np.array(['A','B','C','D'])
y = np.array([3,8,1,10])

plt.bar(x,y, color = 'r', width = 0.3)
plt.show    