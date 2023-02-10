# dict 객체를 이용하는 단어 빈도수 구하기
char = ['jaein', 'jimin', 'jaein', 'jimin', 'dayeon']
bindo = {}

# get()
for key in char :
    bindo[key] = bindo.get(key, 0) + 1

print(bindo)



## 연습문제 ##
# 1
lst = [10, 1, 5, 2]
result = lst * 2
print(result)
result.append(result[0]*2)
print(result)
result2 = result[1::2]
print(result2)


# 2
size = int(input('vector 수: '))
lst = []
for i in range(size) :
    lst.append(int(input()))

print('vector 크기: ', len(lst))


# 3
size = int(input('vector 수: '))
lst = []
for i in range(size) :
    lst.append(int(input()))
a = int(input())
if a in lst :
    print('YES')
else :
    print('NO')


# 4
message = ['spam', 'ham', 'spam', 'ham', 'spam']
spam_list = ['spam' for i in message if i == 'spam']
print(spam_list)


# 5
message = ['spam', 'ham', 'spam', 'ham', 'spam']
dummy = [1 if i == 'spam' else 0 for i in message]
print(dummy)


# 6
position = ['과장', '부장', '대리', '사장', '대리', '과장']
bindo = {}
bindo_1 = []
for key in position :
    bindo[key] = bindo.get(key, 0) + 1
print(bindo)

# 6-1 : 빈도 수가 1인 직위 구하기    
for i in bindo.keys() :
    if bindo[i] == 1 :
        bindo_1.append(i)
print(bindo_1)

# 6-2 : 중복되지 않은 직위 구하기
posi = []
for i in bindo.keys() :
    posi.append(i)
print(posi)

