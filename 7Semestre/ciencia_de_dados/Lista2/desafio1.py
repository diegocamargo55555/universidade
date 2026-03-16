import numpy as np
#1
arr1 = np.arange(0, 10, 1)
#print(arr1)



#2
arr33 = ([False, True, False],
                 [True, True, True],
                 [False, False, False])


#3
impares = arr1[arr1 % 2 == 1]
print("impares", impares)

#4
arr1[::] = -1
#print(arr1)


#5
arr55 = np.random.randint(1, 100, size=(25))
arr55 = arr55.reshape((5,5))
#print(arr55)

#6
#print("soma total: ", arr55.sum())

#7
#print("valor maximo", arr55.max())


#8
a = np.array([1, 2, 3, 4, 5]) 
#print(a + 2)


#9
a= np.array([1, 2, 3]) 
b = np.array([4, 5, 6])
c = np.array([a,b])
#print(c.reshape(-1))


#10
arr10 = np.array([10, 20, 30, 40])
arr10.T
print(arr10)