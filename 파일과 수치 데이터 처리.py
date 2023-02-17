# csv 파일 입출력
import pandas as pd
import os
os.chdir('C:/Users/JaeIn/Desktop/PythonStatistics/data')

st = pd.read_csv('student.csv', header = None)
print(st)

col_names = ['sno', 'name', 'height', 'weight']
st.columns = col_names
print(st)

BMI = st['weight'] / (st['height'] * 0.01) ** 2
print(BMI)

st['BMI'] = BMI.round(2)
print(st)

labels = []
for i in st.BMI :
    if i >= 18 and i <= 23 :
        labels.append('정상')
    elif i > 23 :
        labels.append('비만')
    else :
        labels.append('저체중')
        
st['label'] = labels
print(st)


# excel 파일 읽기
import pandas as pd
import os
os.chdir('C:/Users/JaeIn/Desktop/PythonStatistics/data')
sam = pd.ExcelFile('sam_kospi.xlsx')

kospi = sam.parse('sam_kospi')
print(kospi.info())

# 칼럼 추출
high = kospi['High']
low = kospi['Low']
print(high.mean())
print(low.mean())


# array()
import numpy as np

lst = [1, 2, 3, 4, 5]
arr1 = np.array(lst)
print(arr1.shape)
print(arr1.mean())
print(arr1.std())
print(arr1.var())

lst2 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
arr2 = np.array(lst2)
print(arr2.shape)

# 브로드캐스팅 연산
print(arr1 + arr2)
print(arr1 * arr2)


# zeros()
zer = np.zeros((3, 5))
print(zer)

# arange()
# print(range(-1.0, 10.5)) : range는 실수 불가
x = np.arange(-1.0, 2, 0.1)
y = x ** 2 + 2 * x + 3

import matplotlib.pyplot as plt
plt.plot(x, y)
plt.show()

cnt = 0
for i in np.arange(3) :
    for j in np.arange(5) :
        cnt += 1
        zer[i, j] = cnt
print(zer)


# 유니버설 함수
data = np.random.randn(5)
print('data = ', data)
print(np.abs(data))
print(np.sqrt(data))
print(np.square(data))
print(np.sign(data))
print(np.var(data))
print(np.std(data))

print(np.power(data, 2))
print(np.maximum(data, 1))
print(np.mod(data, 2))
op1 = np.greater_equal(data, 0.1)
op2 = np.less_equal(data, 0.4)
print(data[np.logical_and(op1, op2)])

data = np.random.randn(3, 4)
print(data)
print(np.mean(data))
print(data.mean())
print(data.max())
print(data.sum())


# 색인 참조
ldata = [0, 1, 2, 3, 4, 5]
print(ldata[:])
print(ldata[3])
print(ldata[:3])        # 0 ~ 2

arr = np.arange(10)
print(arr[3])

# 슬라이싱 - 리스트
ldata_obj = ldata[1:4]
print(ldata_obj)

ldata_obj[0] = 100
print(ldata_obj)
print(ldata)                    # 전체는 수정 안 됨

# 슬라이싱 - 다차원 배열
arr_obj = arr[1:4]
print(arr_obj)

arr_obj[:] = 100
print(arr)                      # 1 ~ 3이 100으로 수정됨


# 고차원 색인
ar2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(ar2)
print(ar2[::2])                 # 홀수행 선택

ar3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(ar3.shape)
print(ar3[0, 1])
print(ar3[1, 1, 1:])


# 난수
data = np.random.rand(5, 3)
print(data)
print(data.mean())
print(data.min())

data = np.random.randint(165, 175, size = 10)
dataa = np.random.randint(165, 175, size = (2, 5))
print(data)
print(dataa)


# 정규분포 난수, 균등분포 난수
normal = np.random.normal(0, 1, 1000)   # N(0, 1)
print(normal)

plt.hist(normal)
plt.show()

unif = np.random.uniform(0, 1, 1000)
print(unif)

plt.hist(unif)
plt.show()
