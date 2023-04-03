a = "16325971932030867893153143345"
b = a[0:5] + a[9:15] + a[19:25]         # 번호 추출


abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# 3 -> ,
for i in range(len(b)) :                
    if b[i] == 3 :
        b.pop(i)
        b.insert(i, ',')
    

# 10의 자리
n = []
for i in b[::3] :
    n.append(int(i)*10)

# 1의 자리
m = []
for i in b[1::3] :
    m.append(int(i))

# 문자열 프린트
for i in range(len(n)) :
    print(abc[n[i] + m[i] - 1], end = '')







