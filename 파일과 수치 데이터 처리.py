# csv 파일 입출력
import pandas as pd
import os
os.chdir('C:/Users/JaeIn/Desktop/PythonStatistics/data')

st = pd.read_csv('student.csv', header = None)
print(st)

col_names = ['sno', 'name', 'height', 'weight']
st.columns = col_names
print(st)

