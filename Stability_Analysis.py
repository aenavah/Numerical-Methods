import matplotlib.pyplot as plt
import numpy as np

def plot_boundary(method):
  #plots boundary given the boundary function
  # note: need to plt.title and plt.show after calling this function
  plt.clf()
  thetas = np.linspace(0, 2*np.pi)

  real_vals = []
  imag_vals = []
  
  #plotting actual boundary
  for theta in thetas:
    y = method(theta) 
    real_part = y.real
    imag_part = y.imag
    real_vals.append(real_part)
    imag_vals.append(imag_part)
  plt.grid()
  plt.xlabel("Re(z)")
  plt.ylabel("Im(z)")
  plt.plot(real_vals, imag_vals)  
  plt.show()

#Compute the boundary algebraicly, here are some examples from AM213B HW2
def BDF3_boundary(theta):
  y = (11*np.e**(3j*theta) - 18*np.e**(2j*theta) + 9*np.e**(1j*theta) - 2)/(6*np.e**(3j*theta))
  return y

def AB3_boundary(theta):
  y = (12*np.e**(3j*theta) - 12*np.e**(2j*theta))/(5-16*np.e**(theta*1j)+23*np.e**(2j*theta)) 
  return y

if __name__ == "__main__":
# TO-DO - include formula in readme !!!
  plot_boundary(BDF3_boundary)
