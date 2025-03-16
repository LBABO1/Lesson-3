import math as m

n = int(input("Enter number: \n"))
x = []

for i in range(1,n+1):
    z = i
    x.append(z)

print(m.prod(x))