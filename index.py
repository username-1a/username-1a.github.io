import numpy as np
import matplotlib.pyplot as plt
iter_func=lambda z,c:(z**2+c)

def calc_steps(z,c,max_iter_num=128):
  num=0
  while abs(z)<2 and num<max_iter_num:
    z=iter_func(z,c)
    num=num+1
    return num

def display_julia(x_num=100,y_num=100):
  X,Y=np.meshgrid(np.linspace(-2,2,x_num+1),np.linspace(-2,2,y_num+1)
  C=X+Y*1j
  result=np.zeros((y_num+1,x_num+1))
  c=complex(round(random.uniform(-2,2),5))
  for i in range(y_num+1):
    for j in range(x_num+1):
      result[i,j]=calc_steps(C[i,j],c)
  plt.imshow(result,interpolation="bilinear",cmap=plt.cm.bone,
           vmax=abs(result).max(),vmin=abs(result).min(),
           extent=[-2,2,-2,2]
  plt.show()