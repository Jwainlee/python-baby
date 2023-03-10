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
tot = 0
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

for i in lst :
    print(lst[:i])

x = list(range(1,11))
print(x[::2])       # [1, 3, 5, 7, 9]
print(x[1::2])      # [2, 4, 6, 8, 10]
print(x[3::2])      # [4, 6, 8, 10]
print(x[0::3])      # [1, 4, 7, 10]
print(x[-6:])       # [5, 6, 7, 8, 9, 10]
a = ['a', 'b', 'c']
b = [10, 20, a, True, '신희훈']
print(b[4])
print(b[2])
print(b[2][1])
print(b[2][1:])
print(b[2][-2:])


# 리스트 수정
num = ['one', 'two', 'three', 'four']
len(num)


# 리스트 원소 추가
num.append('five')
print(num)


# 리스트 원소 삭제
num.remove('five')
print(num)


num[0]='1'
print(num)

num.insert(0, 'zero')

print(num)          # ['zero', '1', 'two', 'three', 'four']

num.remove('two')
print(num)

num.append('three')
print(num)

num.remove('three')
print(num)                  # ['zero', '1', 'four', 'three']
num.remove('three')
print(num)



# 리스트 연산
x = [1, 2, 3, 4]
y = [2.5, 4.2]
z = x + y
print(z)                # 원소끼리 더하는 거 아님


# 리스트 확장
x.extend(y)
print(x)


# 리스트 추가
x.append(y)
print(x)


# 리스트 확장 - 2
result = y * 2
print(result)               # [2.5, 4.2, 2.5, 4.2]
result2 = x + y * 2
print(result2)              # [1, 2, 3, 4, 2.5, 4.2, [2.5, 4.2], 2.5, 4.2, 2.5, 4.2]


# 리스트 내포
lst = [2,4,1,5,7]

lst2 = [i ** 2 for i in lst]
print(lst2)

lst3 = ['짝수' if i % 2 ==0 else '홀수' for i in lst2]
print(lst3)

lst4 = [i * 2 for i in lst if i % 2 == 0]
print(lst4)



# dict 객체
dic = dict(key1 = 100, key2 = 200)
print(dic)

dic2 = {'name' : '신희훈', 'age' : 23}
print(dic2)                       # 중괄호 dict 정의는 : 만 가능하다.

print(dic2['name'])


# dict 객체의 원소 수정, 삭제, 추가

dic2['age'] = 80

del dic2['age']
print(dic2)


# dict 객체의 요소 검사
print(dic2['name'])
print('name' in dic2)


# 요소 검사
for key in dic2.keys() :
    print(key)

for v in dic2.values() :
    print(v)


for i in dic2.items() :
   print(i)
 
# dict 사용 예시 - 단어 출현 빈도 수 구하기
charset = ['이재인', '이재인', '윤지민', '권하영', '신희훈']
wc = {}
for key in charset :
     wc[key] = wc.get(key, 0) + 1

print(wc)
