import random
random_extr = random.randint(0,9)

lotto = []
random_sel = []


for i in range(5):
    while random_extr in lotto:
        random_extr = random.randint(0,9)
    lotto.append(random_extr)
    
    random_sel.append(int(input('번호를 입력하세요(1~9): ')))

for i in range(5) :
    if random_sel[i] in lotto :
        print(random_sel[i])



