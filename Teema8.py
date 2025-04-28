import matplotlib.pyplot as plt
import numpy as np
x=np.arange(-5, 10, 1) #0,1,2,3,4,5,6,7,8,9
y=x**2-5*x+6
plt.figure(facecolor='lightblue')
plt.title("Joonise pealkiri")
plt.xlabel("x telg")
plt.ylabel("y telg")
plt.grid(True)
plt.plot(x, y, color='blue', linestyle='-', marker='D', markersize=8, label="Joonise joon")
plt.show()

x = [0, 1, 2, 3, 4]
y1 = [0, 1, 4, 9, 16]
y2 = [16, 9, 4, 1, 0]

plt.plot(x, y1, linestyle='-', marker='o', color='blue',
         markersize=8, markerfacecolor='lightblue', label="Tõusev joon")
plt.plot(x, y2, linestyle='--', marker='x', color='green',
         markersize=8, label="Laskuv joon")

plt.title("Kahe joone näide")
plt.xlabel("x telg")
plt.ylabel("y telg")
plt.legend()
plt.grid(True)
plt.show()



plt.scatter(x, y1, color='blue', label="Tõusev joon")
plt.show()
plt.bar(x, y1, color='blue', label="Tõusev joon")
plt.show()
plt.barh(x, y1, color='red', label="Tõusev joon")
plt.show()
plt.hist(y1, bins=3, color='green', label="Tõusev joon")
plt.show()
plt.pie(y1, labels=x, autopct='%1.1f%%', startangle=140)
plt.show()