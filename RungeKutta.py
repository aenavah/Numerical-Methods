import numpy as np

def f(A, y):
  f = A @ y
  return f 

def RK4(t, u0, dt, f):
  '''RK method from midterm'''
  K1 = f(t, u0)
  K2 = f(t + (1/2) * dt, u0 + ((1/2)*dt * K1))
  K3 = f(t + (1/2) * dt, u0 + ((1/2)*dt * K2))
  K4 = f(t + (1) * dt, u0 + dt*K3)

  u_next = u0 + (dt * (1/6)) * (K1 + 2*K2 + 2*K3 + K4)
  return u_next  

def RK3(t, u0, dt, f): 
    '''RK method from HW1'''
    K1 = f(t + (1/3)*dt, u0)
    K2 = f(t + (1/3)*dt, u0 + ((1/3) * dt * K1))
    K3 = f(t + (2/3)*dt, u0 + ((2/3) * dt * K2))
    u_next = u0 + (dt * (1/4)) * (K1 + 3 * K3)
    return u_next

def RK_Call(u0, t0, tn, dt, RK_method, A):
    n = int((tn-t0)/dt) #number steps

    ts = np.arange(t0, tn, dt)#t_{k+1}
    ts = ts[0:n]
    
    system_rows, system_columns = A.shape
    us = np.zeros((int(n), int(system_rows))) #solution vector

    us[0] = u0
    u_last = us[0]
    for i in range(1, int(n)):
      u_next = RK_method(ts[i], u_last, dt, f)
      us[i] = u_next
      u_last = u_next
    return ts, us

if __name__ == "__main__":
  A = np.array([[-1, 3],[-3, -1]])
  y0 = np.array([-3 , 1])
  dt = 0.01
  t0 = 0 
  tn = 10

  ts, us = RK_Call(y0, t0, tn, dt , RK3, A)    