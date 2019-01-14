from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt


x_data = [-7,-4,-1,0,2,5,7]
y_data = [20,14,5,3,-2,-10,-15]

#reg = [a,b], y=ax+b
def d2(reg, x,y):
    distance = 0
    for i in range(0,len(y_data)):
        distance += (y[i]-(reg[0]*x[i]+reg[1]))**2
        
    return distance


result = optimize.minimize(d2, [1,0] , args=(x_data,y_data))



print(result)

print(np.corrcoef(x_data,y_data))

plt.plot(x_data, y_data, 'ro')
plt.axis([min(x_data)-1, max(x_data)+1, min(y_data)-1, max(y_data)+1])
plt.show()