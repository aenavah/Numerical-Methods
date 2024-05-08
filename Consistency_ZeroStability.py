import matplotlib.pyplot as plt
import numpy as np 
import math 

def ComputeCoefs(alphas, betas):
  C = []
  found = 0
  while found == 0:
    s = len(C)
    print("Working on C_" + str(s) + " coefficient...")
    summation = 0 
    for j in range (1, len(alphas)):
      tmp = ((j**s)*alphas[j]) - s*j**(s-1)*betas[j]
      print(tmp)
      summation += tmp
    C.append((1/math.factorial(s))*summation)
    print(C[s])
    if C[s] != 0:
      found = 1
if __name__ == "__main__":

  #use convention from AM213B HW2 (LecNote: Consistency)
  alphas = [1, -18/11, 9/11, -2/11]
  betas = [0, 0, 0, 6/11]

  ComputeCoefs(alphas, betas)