"""
Created on Sat May  5 23:12:49 2018
@author: WYZ
"""
import random
import math
import numpy as np
import matplotlib.pyplot as plt

a = -0.03 # Annual return rate
D = 0.002 # Volatality
lamb = 100. # Yearly saving rate

def update(x,a,D,lamb):
  b = random.gauss(0,math.sqrt(2*D))
  return x*(1+a+b) + lamb

random.seed(None)
# Simulate for one case
'''T = [0]; X = [0]; x = 0
for t in range(1,500):
  x = update(x,a,D,lamb)
  X.append(x)
  T.append(t)'''
  
#plt.plot(T,X)

# Simulate for an ensemble
X_ens = np.zeros(20000)
T = 200
for t in range(0,T):
  for i in range(0,len(X_ens)):
    X_ens[i] = update(X_ens[i], a, D, lamb)
  
# Plot out density histogram  
plt.hist(X_ens, bins = 30, density = True)
# Plot theoretical pdf for stable, where annual return rate is negative
from scipy.special import gamma
X_theor = np.arange(0.1,max(X_ens),1)
Y_theor = np.zeros(len(X_theor))
a_adj = math.log(1+a)
D_adj = math.log(1+D)
for i in range(0,len(X_theor)):
  Y_theor[i] = X_theor[i]**((a_adj/D_adj)-1)*math.exp(-lamb/(D_adj*X_theor[i]))/(gamma(-a_adj/D_adj)*((lamb/D_adj)**(a_adj/D_adj)))
plt.plot(X_theor,Y_theor)

plt.xlabel('Amount of money')
plt.ylabel('Probability')
plt.show()

average = np.average(X_ens)
print(average) # Actual average

theoretical_avg = lamb*(math.exp((a_adj+D_adj)*T)-1)/(a_adj+D_adj)
print(theoretical_avg) # Theoretical average
print(theoretical_avg-average) # Evaluate difference