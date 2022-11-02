import random
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


x = []
y = []

fig = plt.figure(figsize=(15,15))
plot_point = int(input('Enter number of plots points to be graphed:'))

def animate(plot_point):
    x = []
    y = []
    for i in range(plot_point):
        x.append(i)
        y.append(random.randint(0,10))
    
    plt.xlabel('Money')
    plt.ylabel('Bababooey')
    plt.title('Finnegan McSpeed and How He Relates to the Economy')
    plt.plot(x,y)

ani = FuncAnimation(fig, animate(plot_point), interval= 300)
plt.show()