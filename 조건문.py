var1=100
print(id(var1))
print(type(var1))


# 실수-> 정수
a=int(10.5)
b=int(20.42)
add=a+b
print('add=', add)
add= 30

a=float(10)
b=float(20)
add2=a+b
print('add2=', add2)
add2= 30.0

a**2
100.0

#여러 줄 문자열
multiline=""" Hi
my name is
Jae In """
print(multiline)
 Hi
my name is
Jae In 

multiline2="Hi\nmy name is\nJae In"
print(multiline2)
Hi
my name is
Jae In

#문자열 색인
string = "PYTHON"
print(string[0])
P
print(string[1])
Y
print(string[-5])
Y

#문자열 연산
print("I am"+ str(24) + "years old")
I am24years old

print("가지마"*20)
가지마가지마가지마가지마가지마가지마가지마가지마가지마가지마가지마가지마가지마가지마가지마가지마가지마가지마가지마가지마

#나머지 계산
div1 = 10*3
print(div1)
30
# 이게 아닌데
div1 = 10%3
print(div1)
1

# 몫 계산
div2 = 10//3
print(div2)
3
10.3%2.5
0.3000000000000007


# 논리연산자
result1 = 30>50
print(result1)
False
result2 = 30>50 or 70>50
print(result2)
True

# 대입연산자
i = tot = 10
i += 1
tot += i
print(i, tot)
11 21

print('재인' '민지', end=',')
재인민지,
print('재인','민지', end=',')
재인 민지,
print('재인', end=',')
재인,
print('민지')
민지
print('출력1', end=',')
출력1,
print('출력2')
출력2
print('출력1', end=',')
출력1,

print(i, tot, end=',')
11 21,
print('재인''민지', end=',')
재인민지,
print('재인, ''민지')
재인, 민지

# 두 변수의 값 교체
v1, v2 = 100, 200
v2, v1 = v1, v2
print(v1, v2)
200 100
v3, v1 = v1, v2
print(v1,v2,v3)
100 100 200

# 패킹 할당 연산자
lst = [1,2,3,4,5]
v1, *v2 = lst
print(v1, v2)
1 [2, 3, 4, 5]
*v1, v2 = lst
print(v1, v2)
[1, 2, 3, 4] 5


# 조건문 - 단일 조건문
var = 10
if var >= 5 :
    print('var = ', var)
    print('var는 5보다 크다.')
    print('조건 만족')
print('항상 실행')
SyntaxError: invalid syntax
if var >= 5 :
    print('var = ', var)
    print('var는 5보다 크다.')
    print('조건 만족')
print('항상 실행')
SyntaxError: invalid syntax
if var >= 5 :
    print('var = ', var)
    print('var는 5보다 크다.')
    print('조건 만족')

    
var =  10
var는 5보다 크다.
조건 만족
if var >= 5 :
    print('var = ', var)
    print('var는 5보다 크다.')
    print('조건 만족')

    
var =  10
var는 5보다 크다.
조건 만족

# 100~85: 우수, 84~70: 보통, 69이하: 저조

score = int(input('점수 입력: '))
if score >= 85 and score <= 100
SyntaxError: incomplete input
if score >= 85 and score <= 100 :
    print('우수')
else :
    if score >= 70 :
        print('보통')
    else :
        print('저조')

저조
score = int(input('점수 입력: '))
점수 입력: 50
if score >= 85 and score <= 100 :
    print('우수')
else :
    if score >= 70 :
        print('보통')
    else :
        print('저조')

        
저조
score = int(input('점수 입력: '))
점수 입력: 90
if score >= 85 and score <= 100 :
    print('우수')
else :
    if score >= 70 :
        print('보통')
    else :
        print('저조')

        
우수
score = int(input('점수 입력: '))
점수 입력: 
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    score = int(input('점수 입력: '))
ValueError: invalid literal for int() with base 10: ''

# 중립조건문
grade = ''

if score >= 85 and score <= 100 :
    grade = 'A'
elif score >= 70 :
    grade = 'B'
else :
    grade = 'C'
print ('당신의 점수는 %d이고, 등급은 %s' %(score, grade))
SyntaxError: invalid syntax
if score >= 85 and score <= 100 :
    grade = 'A'
elif score >= 70 :
    grade = 'B'
else :
    grade = 'C'
print ('당신의 점수는 %d이고, 등급은 %s' %(score, grade))
SyntaxError: invalid syntax
if score >= 85 and score <= 100 :
    grade = 'A'
elif score >= 70 :
    grade = 'B'
else :
    grade = 'C'


score = int(input('점수 입력: '))
점수 입력: 90
if score >= 85 and score <= 100 :
    grade = 'A'
elif score >= 70 :
    grade = 'B'
else :
    grade = 'C'

    
print('너 점수는 %d, 등급은 %s임' %(score, grade))
너 점수는 90, 등급은 A임

# 한 줄 조건문
n = 9
result = 0

if num >= 5 :
    result = num * 2
... else :
...     result = num + 2
... print()
SyntaxError: invalid syntax
>>> if num >= 5 :
...     result = num * 2
... else :
...     result = num + 2
... 
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    if num >= 5 :
NameError: name 'num' is not defined. Did you mean: 'sum'?
>>> if n >= 5 :
...     result = n * 2
... else :
...     result = n + 2
... 
...     
>>> print('result:', result)
result: 18
>>> print('결과는 %d' %result)
결과는 18
>>> 
>>> result2 = n * 2 if n >= 5 else n + 2
