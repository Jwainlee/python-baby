# 연습문제

# 1
import pandas as pd

emp = pd.read_csv("C:/Users/JaeIn/Desktop/PythonStatistics/data/emp.csv")
print(emp)
print('관측치 길이: ', len(emp))
print('전체 평균 급여: ', emp['Pay'].mean())

p = emp['Pay']
n = emp['Name']
mi = min(p)
ma = max(p)


for idx in range(len(emp)) :
    if  p[idx] == mi :
        print('최저 급여: %d, 이름: %s' %(p[idx], n[idx]))
    elif p[idx] == ma :
        print('최고 급여: %d, 이름: %s' %(p[idx], n[idx]))


# 2
import numpy as np
arr2 = np.random.randn(5, 4)
arr2


for i in range(len(arr2[:,])) :
    idx = i + 1
    a = arr2[i,]
    print('%d행 합계: %d' %(idx, sum(a)))
    print('%d행 최대값: %d' %(idx, max(a)))
    print('%d행 최소값: %d' %(idx, min(a)))


# 3






