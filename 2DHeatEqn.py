import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

print("2D heat equation solver")


def Initialize(length = 4, height = 3, n = 5, dx = 1, dt = 0.001, u_top = 100, u_bottom = 2, u_left = 0, u_right = 0):

    alpha = 2 #thermal diffusivity constant

    #gamma = (alpha * dt) / (dx ** 2)
    x_nodes = length # length of plate
    y_nodes = height # height of plate

    us_over_time = np.empty((n, x_nodes, y_nodes))

    for k in range(0, n): #for each timestep
        us = np.empty((x_nodes, y_nodes))
        u_0 = 0 
        us.fill(u_0)

        us[0, :] = u_top
        us[-1, :] = u_bottom
        us[1:-2, 0] = u_left
        us[1:-2, -1] = u_right
        #us_over_time[k, :, :] = us
    return us_over_time
def Calculate(us, method = 1, dx = 1):
    n, x_nodes, y_nodes = np.shape(us)
    print("number of timesteps: " + str(n))
    print("number of x nodes: " + str(x_nodes))
    print("number of y nodes: " + str(y_nodes))
    us_last = us[0, :, :]
    for k in range(1, n - 1, 1):
        
        us_next = np.zeros_like(us_last)
        print(us)
        for i in range(1, x_nodes - 1, delta_x):
            for j in range(1, y_nodes - 1, delta_x):
                u[k + 1, i, j] = gamma * (u[k,i+1,j] + u[k,i-1,j] + u[k,i,j+1] + u[k,i,j-1] - 4*u[k,i,j]) + u[k,i,j]
    return u

def plotheatmap(u_k, k):
    # Clear the current plot figure
    plt.clf()

    plt.title(f"Temperature at t = {k*delta_t:.3f} unit time")
    plt.xlabel("x")
    plt.ylabel("y")

    # This is to plot u_k (u at time-step k)
    plt.pcolormesh(u_k, cmap=plt.cm.jet, vmin=0, vmax=100)
    plt.colorbar()

    return plt

# Do the calculation here

u = Initialize()
u = Calculate(u)

#def animate(k):
    #plotheatmap(u[k], k)

#anim = animation.FuncAnimation(plt.figure(), animate, interval=1, frames=n, repeat=False)
#plt.show()
#anim.save("heat_equation_solution.gif")

print("Done!")


#adapting https://gist.github.com/corvasto/c6d9dba1b1dbcde1ddeee5eff3f8209a#file-fdm_2d_heat_equation-py