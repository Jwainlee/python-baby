# for 문과 if 문의 in
words = ['재인', '승희', '채원', '하영']
if '하영' in words :
    print('광대하마')
else :
    print('하영 없다')

    
# 1
x = 2
y = 2.5 * x ** 2 + 3.3 * x + 6
print('2차 방정식 결과 = ', y)


#2
while True :
    fat = int(input('지방의 그램을 입력하세요 : '))
    if fat == 80000 :                           # 탈출 조건
        break
    car = int(input('탄수화물의 그램을 입력하세요 : '))
    pro = int(input('단백질의 그램을 입력하세요 : '))

    tot_cal = fat * 9 + pro * 4 + car * 4
    print('총 칼로리는 %d입니다' %tot_cal)



# 3
while True :
    kg = int(input('수하물의 무게는 얼마입니까? '))

    if kg == 0 :
        break                                       # 탈출 조건
    
    fee = kg // 10 * 10000
    if fee == 0 :
        print('수수료는 없습니다.')
    else :
        print('수수료는 %d원 입니다.' %fee)


        
# 4
lst = range(1,101)
lst2 = []
for e in lst :
    if e % 3 == 0 and e % 2 != 0 :
        lst2.append(e)
        tot += e

        
print('수열 = ', lst2)
print('누적합 = ', tot)




# list 객체의 색인
for i in lst2 :
    print(lst2[:i])

    
[3, 9, 15]
[3, 9, 15, 21, 27, 33, 39, 45, 51]
[3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87]
[3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99]
[3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99]
[3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99]
[3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99]
[3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99]
[3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99]
[3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99]
[3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99]
[3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99]
[3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99]
[3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99]
[3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99]
[3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99]
[3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99]
lst = [1,2,3,4,5]
for i in lst :
    print(lst[:i])

    
[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 3, 4, 5]
lst = [0, 2, 4, 4, 5, 4]
for i in lst :
    print(lst[:i])

    
[]
[0, 2]
[0, 2, 4, 4]
[0, 2, 4, 4]
[0, 2, 4, 4, 5]
[0, 2, 4, 4]
x = list(range(1,11))
print(x[::2])
[1, 3, 5, 7, 9]
print(x[1::2])
[2, 4, 6, 8, 10]
print(x[3::2])
[4, 6, 8, 10]
print(x[0::3])
[1, 4, 7, 10]
print(x[-6:])
[5, 6, 7, 8, 9, 10]
a = ['a', 'b', 'c']
b = [10, 20, a, True, '신희훈']
print(b[4])
신희훈
print(b[2])
['a', 'b', 'c']
print(b[2][1])
b
print(b[2][1:])
['b', 'c']
print(b[2][-2:])
['b', 'c']

# 리스트 수정
num = ['one', 'two', 'three', 'four']
len(num)
4
# 리스트 원소 추가
num.append('five')
print(num)
['one', 'two', 'three', 'four', 'five']
# 리스트 원소 삭제
num.remove('five')
print(num)
['one', 'two', 'three', 'four']
num[0]='1'
print(num)
['1', 'two', 'three', 'four']
num.insert(0, 'zero')

print(num)
['zero', '1', 'two', 'three', 'four']
num.remove('two')
print(num)
['zero', '1', 'three', 'four']
num.append('three')
print(num)
['zero', '1', 'three', 'four', 'three']
num.remove('three')
print(num)
['zero', '1', 'four', 'three']
num.remove('three')
print(num)
['zero', '1', 'four']

# 리스트 연산
x = [1,2,3,4]
y = [2.5, 4.2]
z = x + y
print(z)
[1, 2, 3, 4, 2.5, 4.2]

# 리스트 확장
x.extend(y)
print(x)
[1, 2, 3, 4, 2.5, 4.2]

# 리스트 추가
x.append(y)
print(x)
[1, 2, 3, 4, 2.5, 4.2, [2.5, 4.2]]

# 리스트 확장 - 2
result = y * 2
print(result)
[2.5, 4.2, 2.5, 4.2]
result2 = x + y * 2
print(result2)
[1, 2, 3, 4, 2.5, 4.2, [2.5, 4.2], 2.5, 4.2, 2.5, 4.2]

# 리스트 내포
lst = [2,4,1,5,7]
lst2 = [i ** 2 for i in lst]
print(lst2)
[4, 16, 1, 25, 49]
lst3 = ['짝수' if i % 2 ==0 else '홀수' for i in lst2]
print(lst3)
['짝수', '짝수', '홀수', '홀수', '홀수']
lst4 = [i * 2 for i in lst if i % 2 == 0 else i]
SyntaxError: invalid syntax
lst4 = [i * 2 for i in lst if i % 2 == 0]
print(lst4)
[4, 8]
lovely Jae In♥[4, 8]
SyntaxError: invalid character '♥' (U+2665)
# dict 객체
dic = dict(key1 = 100, key2 = 200)
print(dic)
{'key1': 100, 'key2': 200}
dic2 = {'name' = '신희훈', 'age' = 23}
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
dic2 = {'name' : '신희훈', 'age' : 23}
dic2 = {'name' == '신희훈', 'age' == 23}
print(dic2)
{False}
dic2 = {'name' : '신희훈', 'age' : 23}
print(dic2)
{'name': '신희훈', 'age': 23}
# 중괄호 dict 정의는 : 만 가능하다.

print(dic2['name'])
신희훈
print(type(dic2))
<class 'dict'>

# dict 객체의 원소 수정, 삭제, 추가

dic2['age'] = 80
print(dic2)
{'name': '신희훈', 'age': 80}
del dic2['age']
print(dic2)
{'name': '신희훈'}
dic2['gf'] = '이재인'
print(dic2)
{'name': '신희훈', 'gf': '이재인'}

# dict 객체의 요소 검사
print(dic2['gf'])
이재인
print('gf' in dic2)
True

# 요소 검사
for key in dic2.keys() :
    print(key)

    
name
gf
for v in dic2.values() :
    print(v)

...     
신희훈
이재인
>>> for i in dic2.items() :
...     print(i)
... 
...     
('name', '신희훈')
('gf', '이재인')
>>> 
>>> # dict 사용 예시 - 단어 출현 빈도 수 구하기
>>> charset = ['이재인', '이재인', '윤지민', '권하영', '신희훈']
>>> wc = {}
>>> for key in charset :
...     wc[key] = wc.get(key, 0) + 1
... print(wc)
SyntaxError: invalid syntax
>>> for key in charset :
...     wc[key] = wc.get(key, 0) + 1
... 
...     
>>> print(wc)
{'이재인': 2, '윤지민': 1, '권하영': 1, '신희훈': 1}
