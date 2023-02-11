# builtin 함수와 import 사용 예
help(len)
dataset = list(range(1, 6))
print(dataset)

print('\nbuiltin 함수')
print('len=', len(dataset))
print('sum=', sum(dataset))
print('max=', max(dataset))
print('min=', min(dataset))


# import 함수
import statistics
from statistics import variance, stdev

print('평균=', statistics.mean(dataset))
print('중위수=', statistics.median(dataset))
print('표본 분산=', variance(dataset))                # from 방식
print('표본 표준편차=', stdev(dataset))               # from 방식               


# 내장클래스와 내장함수 목록 보기
import builtins
dir(builtins)


# builtins 내장함수
print(abs(-10))

print(all([1, True, 10, -15]))             # 모든 원소가 0(False)이 아닐 때 True 반환
print(all([1, True, 0, -15]))
print(all([1, True, False, -15]))

print(any([1, True, 0, -15]))             # 어느 한 원소라도 0(False)이 아닐 때 True 반환
print(any([0, False]))

print(bin(8))                                     # 2진수로 변환
print(bin(10))

print(hex(10))                                  # 16진수로 변환
print(oct(10))                                   # 8진수로 변환

print(eval('100 + 200'))                    # 수식으로 이루어진 문자열을 계산
print(eval('100 + 200') * 30)

print(ord('A'))                                 # 아스키 값 반환

print(pow(10, 2))                             # x**y 반환

print(round(3.14159, 3))                 # 반올림, 3자리까지 나타내기

print(sorted([3, 2, 1, 5]))                 # 오름차순, 내림차순 정렬
print(sorted([3, 2, 1, 5], reverse= True))

print(zip([1, 3, 5], [2, 4, 6]))
print(list(zip([1, 3, 5], [2, 4, 6])))      # 튜플은 읽기 전용, 결과 확인은 list 써야 함


# 사용자정의함수
def jae() :
    print('아무고토 없어요')
    print('jae')

jae()


def jae1(x, y) :
    print('jae1')
    z = x * y
    print('z=', z)

jae1(10, 10)


def jae2(x, y) :
    print('jae2')
    tot = x + y
    sub = x - y
    mul = x * y
    div = x / y
    
    return tot, sub, mul, div

x = int(input('x 입력: '))
y = int(input('y 입력: '))

t, s, m, d = jae2(x, y)
print('tot = ', t)
print('sub = ', s)
print('mul = ', m)
print('div = ', d)


# 지역변수
x = 50
def local(x) :
    x += 50

local(x)
print('x = ', x)                                # 지역변수이므로 x = 50 이 출력됨

# 전역변수
def global_x() :
    global x                                     # 함수내부에서 전역변수 x 사용
    x += 50

global_x()
print('x = ', x)

# 몬테카를로 시뮬레이션
import random

def coin(n) :
    result = []
    for i in range(n) :
        r = random.randint(0, 1)
        if r == 1 :
            result.append(1)
        else :
            result.append(0)

    return result

def mont(n) :
    cnt = 0
    for i in range(n) :
        cnt += coin(1)[0]

    result = cnt / n
    return result
