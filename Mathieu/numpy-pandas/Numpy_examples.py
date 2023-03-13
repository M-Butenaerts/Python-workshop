import numpy as np
import time
import matplotlib.pyplot as plt


np.random.seed(4)
###----------------------Basics---------------------

#create an array
arr1 = np.ones((2,3))
arr2 = np.zeros((2,2))
t_arr1 = np.linspace(0,5,50000)
t_arr2 = np.arange(0,5,0.01)
print(t_arr1.shape,t_arr1[-1])
print(t_arr2.shape,t_arr2[-1])


#indexing
arr1[0,2] = 3
print(arr1)
arr1[:,0:2] = arr2
print(arr1)

#operations (they have element wise operations generally)
arr3 = np.random.randint(1, 8, size=(2,3))
arr4 = np.random.randint(1, 8, size=(2,2))

print(arr3 - 2)
print(arr3*arr1)

#matrix operations
print(arr4 @ arr3)
print(arr3.T)
print(np.linalg.inv(arr4))

##This is deprecated!!! do not use it anymore
np.matrix(arr4)

###---------------------------------Why use this?-------------------------
#model distance vs time x=a t^2 + v0*t + x0
start = time.time()
acc = 2
v0 = 3
x_lst = []
t_lst = []
for t in range(0,50000,1):
    t /=10000
    t_lst.append(t)
    x_lst.append(acc*t**2+v0*t)

end = time.time()
dt_lst = end - start
print('timer:',end - start)

plt.plot(t_lst,x_lst)
plt.show()

start = time.time()
acc = 2
v0 = 3
x_arr = acc*t_arr1**2+v0*t_arr1

end = time.time()
dt_arr = end - start
print('timer:',end - start)
# print('Difference: ',round(dt_lst/dt_arr))
# plt.plot(t_lst,x_lst)
# plt.show()

###---------------Fotokes bewerken----------------
img = plt.imread('moeder delftsche.png')
# remove blue (RGBA and range is 0->1)
img_gray = 0.299*img[:,:,0]+0.587*img[:,:,1]+0.114*img[:,:,2] #0.299 * R' + 0.587 * G' + 0.114 * B'
img_blue = img[:,:,2]

# Select onbly the blue colors, So where B>0.5 and R,G<0.5
img_lightblue = np.where((img[:,:,2]>0.3) &(img[:,:,0]<0.7) & (img[:,:,1]<0.7) ,0,1)
#show the binary array
plt.imshow(img_lightblue,cmap='gray')
plt.show()

#change the colors in original image
img[:,:,2] *= img_lightblue #make the blue values zero at light blue places
img[:,:,1] += -img_lightblue+1 #Where light blue was present make it green
#show image
plt.imshow(img)
plt.show()

