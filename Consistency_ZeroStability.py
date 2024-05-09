import matplotlib.pyplot as plt
import numpy as np 
import math 
import sympy as sp

def FirstChar(alphas):
  z = sp.symbols('z')
  q = len(alphas)
  rho = 0 
  for j in range(q):
    rho += alphas[j]*(z**j)
  return rho

def SecondChar(betas):
  z = sp.symbols('z')
  q = len(betas)
  sigma = 0 
  for j in range(q):
    sigma += betas[j]*(z**j)
  return sigma

def SecondCharPrime(alphas):
  z = sp.symbols('z')
  q = len(alphas)
  sigma_prime = 0
  for j in range(1, q):


    sigma_prime += j * alphas[j]* (z**(j-1))
  return sigma_prime 

def ComputeCoefs(alphas, betas):
  z = sp.symbols("z")
  rho = FirstChar(alphas)
  sigma = SecondChar(betas)
  rho_prime = SecondCharPrime(alphas)

  C_0 = rho.subs(z, 1)
  C_1 = rho_prime.subs(z, 1) - sigma.subs(z, 1)
  Coefficients = [C_0, C_1]
  
  q = len(alphas) 
  s = 2

  while Coefficients[-1] == 0:
    #print("Coefficient: " + str(s))
    summation = 0
    for j in range(1, q):
      summation +=  (j**s)*alphas[j] - s*(j**(s-1))*betas[j]
    C_s = 1/math.factorial(s)*(summation)
    Coefficients.append(C_s)
    s += 1

  order = s - 2
  return order

def ZeroStability(rho):
  z = sp.symbols("z")
  rho_roots = sp.solve(rho, z)
  Zero_Stable = False 
  for root in rho_roots:
    if root.is_real < 1:
      Zero_Stable = True
  return Zero_Stable

if __name__ == "__main__":

  alphas = [sp.Rational(-2, 11), sp.Rational(9, 11), sp.Rational(-18, 11), 1]  # Example coefficients for FirstChar
  betas = [0, 0, 0, sp.Rational(6, 11)]  # Example coefficients for SecondChar and SecondCharPrime

  ConsistencyOrder = ComputeCoefs(alphas, betas)
  Zero_Stable = ZeroStability(FirstChar(alphas))
  
  print("Order of Consistency: " + str(ConsistencyOrder))
  print("Zero-Stable = " + str(Zero_Stable))