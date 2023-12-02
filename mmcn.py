import math
lmda = 2.4
mu = 1
c = 3
N = 20

rho = lmda / (c * mu)
a = lmda / mu



#P0
P0 = 1
for n in range(1, c):
    P0 = P0 + (pow(a, n) / math.factorial(n))
P0temp = 0
for n in range (c+1, N):
    P0temp = P0temp + pow(rho, n-c)
P0temp = P0temp * (pow(a, c) / math.factorial(c))
P0 = P0 + P0temp
P0 = 1 / P0


#Pn
Pn = (pow(a, N) * P0) / (math.factorial(c) * pow(c, N-c))

#Lq
Lq = ((rho * pow(a, c) * P0) / (math.factorial(c) * pow((1 - rho), 2))) * (1 - pow(rho, N - c) - (N - c) * pow(rho, N - c) * (1 - rho))

#lmdae
lmdae = lmda * (1 - Pn)

#Wq
Wq = Lq / lmdae

#W
W = Wq + 1/mu

#L
L = lmdae * W

print("L = ", L)
print("Lq = ", Lq)
print("W = ", W)
print("Wq = ", Wq)
print("rho = ", rho)
print("Pn = ", Pn * 100)