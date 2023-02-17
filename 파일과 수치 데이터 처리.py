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









