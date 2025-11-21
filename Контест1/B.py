import matplotlib.pyplot as plt
import numpy as np

# a, b = map(int, input().split())
a, b = 123, 456
x=0
while ((a+x)%b==0 and (b+x)%a==0)==False:
    x+=1
print(x)

plt.show()