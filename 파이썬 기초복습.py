Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# for 문과 if 문의 in
words = ['재인', '승희', '채원', '하영']
if '하영' in words :
    print('광대하마')
else :
    print('하영 없다')

    
광대하마
# 1
x = 2
y = 2.5 * x ** 2 + 3.3 * x + 6
print('2차 방정식 결과 = ', y)
2차 방정식 결과 =  22.6

#2
fat = int(input('지방의 그램을 입력하세요 : '))
지방의 그램을 입력하세요 : 25
fat = car = pro = 0
fat = int(input('지방의 그램을 입력하세요 : '))
지방의 그램을 입력하세요 : 
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    fat = int(input('지방의 그램을 입력하세요 : '))
ValueError: invalid literal for int() with base 10: ''
fat = car = pro = 0
while True :
    fat = int(input('지방의 그램을 입력하세요 : '))
    car = int(input('탄수화물의 그램을 입력하세요 : '))
    pro = int(input('단백질의 그램을 입력하세요 : '))
    tot_cal = fat * 9 + pro * 4 + car * 4
    if fat == 80000
    
SyntaxError: incomplete input
while True :
    fat = int(input('지방의 그램을 입력하세요 : '))
    car = int(input('탄수화물의 그램을 입력하세요 : '))
    pro = int(input('단백질의 그램을 입력하세요 : '))
    tot_cal = fat * 9 + pro * 4 + car * 4
    print('총 칼로리는 %d입니다' %tot_cal)
    if fat == 80000 :
        break

    
지방의 그램을 입력하세요 : 25
탄수화물의 그램을 입력하세요 : 520
단백질의 그램을 입력하세요 : 45
총 칼로리는 2485입니다
지방의 그램을 입력하세요 : 80000
탄수화물의 그램을 입력하세요 : 9
단백질의 그램을 입력하세요 : 8
총 칼로리는 720068입니다
while True :
    fat = int(input('지방의 그램을 입력하세요 : '))
        if fat == 80000 :
        break
    car = int(input('탄수화물의 그램을 입력하세요 : '))
    pro = int(input('단백질의 그램을 입력하세요 : '))
    
    tot_cal = fat * 9 + pro * 4 + car * 4
    print('총 칼로리는 %d입니다' %tot_cal)
    
SyntaxError: unexpected indent
while True :
    fat = int(input('지방의 그램을 입력하세요 : '))
    if fat == 80000 :
        break
    car = int(input('탄수화물의 그램을 입력하세요 : '))
    pro = int(input('단백질의 그램을 입력하세요 : '))

    tot_cal = fat * 9 + pro * 4 + car * 4
    print('총 칼로리는 %d입니다' %tot_cal)

    
지방의 그램을 입력하세요 : 25
탄수화물의 그램을 입력하세요 : 520
단백질의 그램을 입력하세요 : 45
총 칼로리는 2485입니다
지방의 그램을 입력하세요 : 80000

# 3
fee = int(input('수하물의 무게는 얼마입니까?'))
수하물의 무게는 얼마입니까?8
while True L
SyntaxError: incomplete input
while True :
    kg = int(input('수하물의 무게는 얼마입니까? '))
    fee = kg // 10 * 10000
    if fee = 0 :
        
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
while True :
    kg = int(input('수하물의 무게는 얼마입니까? '))

    if kg == 0 :
        break                                       # 탈출 조건
    
    fee = kg // 10 * 10000
    if fee == 0 :
        print('수수료는 없습니다.')
    else :
        print('수수료는 %d원 입니다.' %fee)

        
수하물의 무게는 얼마입니까? 8
수수료는 없습니다.
수하물의 무게는 얼마입니까? 15
수수료는 10000원 입니다.
수하물의 무게는 얼마입니까? 21
수수료는 20000원 입니다.
수하물의 무게는 얼마입니까? 30
수수료는 30000원 입니다.
수하물의 무게는 얼마입니까? 80
수수료는 80000원 입니다.
수하물의 무게는 얼마입니까? 0

# 4
cnt = tot = 0

lst = range(1,101)
for e in lst :
    lst2 = []
    if e % 3 == 0 and e % 2 != 0 :
        lst2.append(e)
        tot += e
        print('수열 = ', lst2)
        print('누적합 = ', tot)

        
수열 =  [3]
누적합 =  3
수열 =  [9]
누적합 =  12
수열 =  [15]
누적합 =  27
수열 =  [21]
누적합 =  48
수열 =  [27]
누적합 =  75
수열 =  [33]
누적합 =  108
수열 =  [39]
누적합 =  147
수열 =  [45]
누적합 =  192
수열 =  [51]
누적합 =  243
수열 =  [57]
누적합 =  300
수열 =  [63]
누적합 =  363
수열 =  [69]
누적합 =  432
수열 =  [75]
누적합 =  507
수열 =  [81]
누적합 =  588
수열 =  [87]
누적합 =  675
수열 =  [93]
누적합 =  768
수열 =  [99]
누적합 =  867
for e in lst :
    lst2 = []
    if e % 3 == 0 and e % 2 != 0 :
        lst2.append(e)
        tot += e
    print('수열 = ', lst2)
    print('누적합 = ', tot)

    
수열 =  []
누적합 =  867
수열 =  []
누적합 =  867
수열 =  [3]
누적합 =  870
수열 =  []
누적합 =  870
수열 =  []
누적합 =  870
수열 =  []
누적합 =  870
수열 =  []
누적합 =  870
수열 =  []
누적합 =  870
수열 =  [9]
누적합 =  879
수열 =  []
누적합 =  879
수열 =  []
누적합 =  879
수열 =  []
누적합 =  879
수열 =  []
누적합 =  879
수열 =  []
누적합 =  879
수열 =  [15]
누적합 =  894
수열 =  []
누적합 =  894
수열 =  []
누적합 =  894
수열 =  []
누적합 =  894
수열 =  []
누적합 =  894
수열 =  []
누적합 =  894
수열 =  [21]
누적합 =  915
수열 =  []
누적합 =  915
수열 =  []
누적합 =  915
수열 =  []
누적합 =  915
수열 =  []
누적합 =  915
수열 =  []
누적합 =  915
수열 =  [27]
누적합 =  942
수열 =  []
누적합 =  942
수열 =  []
누적합 =  942
수열 =  []
누적합 =  942
수열 =  []
누적합 =  942
수열 =  []
누적합 =  942
수열 =  [33]
누적합 =  975
수열 =  []
누적합 =  975
수열 =  []
누적합 =  975
수열 =  []
누적합 =  975
수열 =  []
누적합 =  975
수열 =  []
누적합 =  975
수열 =  [39]
누적합 =  1014
수열 =  []
누적합 =  1014
수열 =  []
누적합 =  1014
수열 =  []
누적합 =  1014
수열 =  []
누적합 =  1014
수열 =  []
누적합 =  1014
수열 =  [45]
누적합 =  1059
수열 =  []
누적합 =  1059
수열 =  []
누적합 =  1059
수열 =  []
누적합 =  1059
수열 =  []
누적합 =  1059
수열 =  []
누적합 =  1059
수열 =  [51]
누적합 =  1110
수열 =  []
누적합 =  1110
수열 =  []
누적합 =  1110
수열 =  []
누적합 =  1110
수열 =  []
누적합 =  1110
수열 =  []
누적합 =  1110
수열 =  [57]
누적합 =  1167
수열 =  []
누적합 =  1167
수열 =  []
누적합 =  1167
수열 =  []
누적합 =  1167
수열 =  []
누적합 =  1167
수열 =  []
누적합 =  1167
수열 =  [63]
누적합 =  1230
수열 =  []
누적합 =  1230
수열 =  []
누적합 =  1230
수열 =  []
누적합 =  1230
수열 =  []
누적합 =  1230
수열 =  []
누적합 =  1230
수열 =  [69]
누적합 =  1299
수열 =  []
누적합 =  1299
수열 =  []
누적합 =  1299
수열 =  []
누적합 =  1299
수열 =  []
누적합 =  1299
수열 =  []
누적합 =  1299
수열 =  [75]
누적합 =  1374
수열 =  []
누적합 =  1374
수열 =  []
누적합 =  1374
수열 =  []
누적합 =  1374
수열 =  []
누적합 =  1374
수열 =  []
누적합 =  1374
수열 =  [81]
누적합 =  1455
수열 =  []
누적합 =  1455
수열 =  []
누적합 =  1455
수열 =  []
누적합 =  1455
수열 =  []
누적합 =  1455
수열 =  []
누적합 =  1455
수열 =  [87]
누적합 =  1542
수열 =  []
누적합 =  1542
수열 =  []
누적합 =  1542
수열 =  []
누적합 =  1542
수열 =  []
누적합 =  1542
수열 =  []
누적합 =  1542
수열 =  [93]
누적합 =  1635
수열 =  []
누적합 =  1635
수열 =  []
누적합 =  1635
수열 =  []
누적합 =  1635
수열 =  []
누적합 =  1635
수열 =  []
누적합 =  1635
수열 =  [99]
누적합 =  1734
수열 =  []
누적합 =  1734
for e in lst :
    lst2 = []
    if e % 3 == 0 and e % 2 != 0 :
        lst2.append(e)
        tot += e
print('수열 = ', lst2)
print('누적합 = ', tot)
SyntaxError: invalid syntax
for e in lst :
    lst2 = []
    if e % 3 == 0 and e % 2 != 0 :
        lst2.append(e)
        tot += e
        print('수열 = ', lst2)
        print('누적합 = ', tot)

        
수열 =  [3]
누적합 =  1737
수열 =  [9]
누적합 =  1746
수열 =  [15]
누적합 =  1761
수열 =  [21]
누적합 =  1782
수열 =  [27]
누적합 =  1809
수열 =  [33]
누적합 =  1842
수열 =  [39]
누적합 =  1881
수열 =  [45]
누적합 =  1926
수열 =  [51]
누적합 =  1977
수열 =  [57]
누적합 =  2034
수열 =  [63]
누적합 =  2097
수열 =  [69]
누적합 =  2166
수열 =  [75]
누적합 =  2241
수열 =  [81]
누적합 =  2322
수열 =  [87]
누적합 =  2409
수열 =  [93]
누적합 =  2502
수열 =  [99]
누적합 =  2601
lst = range(1,101)
lst2 = []
for e in lst :
    if e % 3 == 0 and e % 2 != 0
    
SyntaxError: incomplete input
lst = range(1,101)lst2 = []
SyntaxError: invalid syntax
lst = range(1,101)
lst2 = []
for e in lst :
    if e % 3 == 0 and e % 2 != 0 :
        lst2.append(e)

        
print('수열 = ',  lst2)
수열 =  [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99]
lst = range(1,101)
lst2 = []
for e in lst :
    if e % 3 == 0 and e % 2 != 0 :
        lst2.append(e)
        tot += e

        
print('수열 = ', lst2)
수열 =  [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99]
print('누적합 = ', tot)
누적합 =  3468
lst = range(1,101)
lst2 = []
tot = 0
for e in lst :
    if e % 3 == 0 and e % 2 != 0 :
        lst2.append(e)
        tot += e

        
print('수열 = ', lst2)
수열 =  [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99]
누적합 =  3468
print('누적합 = ', tot)
누적합 =  867


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
