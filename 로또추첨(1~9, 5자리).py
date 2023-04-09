import random
random_extr = random.randint(0,9)

lotto = []
user = []
random_sel = int(input('번호를 입력하세요(1~9): '))


for i in range(5):
    while random_extr in lotto:
        random_extr = random.randint(0,9)
    lotto.append(random_extr)

    while random_sel in user:
        random_sel = int(input('번호를 입력하세요(1~9): '))
    user.append(random_sel)
    
    
for i in range(5) :
    if user[i] in lotto :
        print(user[i])






