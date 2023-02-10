# dict 객체를 이용하는 단어 빈도수 구하기

char = ['jaein', 'jimin', 'jaein', 'jimin', 'dayeon']
bindo = {}

# get()

for key in char :
    bindo[key] = bindo.get(key, 0) + 1

print(bindo)




