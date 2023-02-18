# 연습문제

# 1
import pandas as pd

emp = pd.read_csv("C:/Users/JaeIn/Desktop/PythonStatistics/data/emp.csv")
print(emp)
print('관측치 길이: ', len(emp))
print('전체 평균 급여: ', emp['Pay'].mean())

mi = min(emp['Pay'])
ma = max(emp['Pay'])

for i in len(emp) :
    