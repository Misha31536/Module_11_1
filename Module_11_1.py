import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr1)
print(arr1.ndim)
a = np.array([0,30,45,60,90])
print ('Синус различных углов:')
# Преобразование в радианы, умножив на pi/180
print(np.sin(a*np.pi/180))
print('\n')
print('значения косинусов для углов в массиве:')
print(np.cos(a*np.pi/180))
print('\n')
print('значения тангенса для заданных углов:')
print(np.tan(a*np.pi/180))
