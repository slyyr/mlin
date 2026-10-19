import numpy as np
import seaborn as sns

arr = np.array([2,3,4,6,7,8,9,12,13,16,17,23,25,27,34,37,201])

Q1 = np.percentile(arr, 25)
Q2 = np.percentile(arr, 50)
Q3 = np.percentile(arr, 75)
Q4 = np.percentile(arr, 100)

IQR = Q3 - Q1

UF = Q3 + (1.5*IQR)
LF = Q1 - (1.5*IQR)

l = []

for i in arr:
    if i >= LF and i <= UF:
        l.append(i)

arr2 = np.array(l)
print(arr2)

sns.boxplot(x = arr2, color="yellow")