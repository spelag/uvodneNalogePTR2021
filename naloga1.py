zacetneTocke = int(input())
stIger = int(input())
spremembeTock = []
for i in range(stIger):
    spremembeTock.append(int(input()))

maxZap = []
zapIgre = 0
vsota = zacetneTocke - 3200
for i in spremembeTock:
    vsota += i
    if vsota < 0:
        maxZap.append(zapIgre)
        zapIgre = 0
    else:
        zapIgre += 1

print(max(maxZap))