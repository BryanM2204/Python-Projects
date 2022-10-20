import random
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


x = []
y = []

fig = plt.figure(figsize=(15,15))
plot_point = int(input('Enter number of plots points to be graphed:'))

def animate(plot_point):
    for i in range(plot_point):
        x.append(range(plot_point))
        y.append(random.randint(0,10))
    
    plt.xlabel('Money')
    plt.ylabel('Bababooey')
    plt.title('Finnegan McSpeed and How He Relates to the Economy')
    plt.plot(x,y)

ani = FuncAnimation(fig, animate, interval= 300)
plt.show()