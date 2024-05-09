import numpy as np
import matplotlib.pyplot as plt


def RK4(t, u0, dt, f):
  '''RK method from midterm'''
  K1 = f(A, u0)
  K2 = f(A, u0 + ((1/2)*dt * K1))
  K3 = f(A, u0 + ((1/2)*dt * K2))
  K4 = f(A, u0 + dt*K3)

  u_next = u0 + (dt * (1/6)) * (K1 + 2*K2 + 2*K3 + K4)
  return u_next  

def RK3(t, u0, dt, f): 
    '''RK method from HW1'''
    K1 = f(A, u0)
    K2 = f(A, u0 + ((1/3) * dt * K1))
    K3 = f(A, u0 + ((2/3) * dt * K2))
    u_next = u0 + (dt * (1/4)) * (K1 + 3 * K3)
    return u_next

def RK_Call(u0, t0, tn, dt, RK_method, f):
    n = int((tn-t0)/dt) #number steps

    ts = np.arange(t0, tn, dt)#t_{k+1}
    ts = ts[0 : n]
    
    system_rows, system_columns = A.shape
    us = np.zeros((int(n), int(system_rows))) #solution vector

    us[0] = u0
    u_last = us[0]
    for i in range(1, int(n)):
      u_next = RK_method(ts[i], u_last, dt, f)
      us[i] = u_next
      u_last = u_next
    plt.title("Numerical Solution using RK Method")
    plt.plot(ts, us)
    plt.grid()
    plt.xlabel("Time")
    plt.ylabel("y(t)")
    plt.legend()
    plt.show()
    return ts, us

def f(A, y):
    f = A @ y
    return f 

def RK3_S(A, b, h, x, y):
  A = np.copy(A)
  z = complex(x,y)

  size = np.shape(A)
  I = np.eye(size[0])
  num = np.linalg.det(I - z*A + z*(h@(b.T)))
  den = np.linalg.det(I - z*A)
  S = abs(num/den)

  return S

def RK3_AbsoluteStabilityRegion(A, b, h, xa, xb, ya, yb):
  #xa is left x, xb is right x, ya is top, yb is bottom
  nx, ny = (200+1, 200+1)
  real = np.linspace(xa, xb, ny)
  imag = np.linspace(yb, ya, nx)
  real_v, imag_v = np.meshgrid(real, imag)

  S_grid = np.ones((nx, ny))

  #iterate through y values for each fixed x
  for x_i in range(nx):
    for y_i in range(ny):
      boundary= RK3_S(A, b, h, real_v[x_i, y_i], imag_v[x_i, y_i])
      S_grid[x_i, y_i] = boundary 
  plt.xlabel("Re(z)")
  plt.ylabel("Im(z)")
  contour = plt.contourf(real_v, imag_v, S_grid)
  plt.colorbar()
  plt.grid()
  plt.title("Contours of RK3 Method")
  plt.show()
  #plt.savefig("Q2b_RK3_Contours.jpg")

if __name__ == "__main__":
  '''Example Call for computing numerical solution'''
  A = np.array([[-1, 3],[-3, -1]])
  y0 = np.array([-3 , 1])
  dt = 0.01
  t0 = 0 
  tn = 10
  method = RK3

  ts, us = RK_Call(y0, t0, tn, dt , method, f)    

  '''Example call for stability region'''
  #From Midterm 213B
  A = np.array([[0, 0, 0],
                [1/4, 1/4, 0],
                [0, 1, 0]])
  b = np.array(([1/6],[2/3],[1/6]))
  
  h = np.ones_like(b)
  RK3_AbsoluteStabilityRegion(A, b, h, -6, 2, 4, -4)