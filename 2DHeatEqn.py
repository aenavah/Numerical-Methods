import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

print("2D heat equation solver")


def Initialize(Length, t_n, dt):
  pass



alpha = 2 #thermal diffusivity constant
delta_x = 1 

delta_t = 0.001
gamma = (alpha * delta_t) / (delta_x ** 2)
n = 1000
x_nodes = 50 # length of plate
y_nodes = 50 # height of plate


# Initialize solution: number of frames, rows, columns, and fill with zeros 
u = np.empty((n, x_nodes, y_nodes)) 
u_initial = 0
u.fill(u_initial)

# Boundary conditions
u_top = 100.0 
u_left = 0.0
u_bottom = 0.0
u_right = 0.0

# Set the initial condition

# Set the boundary conditions
u[:, (x_nodes - 1):, :] = u_top
u[:, :, :1] = u_left
u[:, :1, 1:] = u_bottom
u[:, :, (x_nodes - 1):] = u_right

def calculate(u):
    for k in range(0, n - 1, 1):
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
u = calculate(u)

def animate(k):
    plotheatmap(u[k], k)

anim = animation.FuncAnimation(plt.figure(), animate, interval=1, frames=n, repeat=False)
plt.show()
#anim.save("heat_equation_solution.gif")

print("Done!")


#adapting https://gist.github.com/corvasto/c6d9dba1b1dbcde1ddeee5eff3f8209a#file-fdm_2d_heat_equation-py