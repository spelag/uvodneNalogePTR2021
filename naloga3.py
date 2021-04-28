n = int(input())

relevantPrastevila = []
for i in range(2, n//2):
    for j in range(2, i):
        if(i%j==0):
            break
    else:
        relevantPrastevila.append(i)

for i in relevantPrastevila:
    potenca = 0
    while n % i == 0:
        n /= i
        potenca += 1
    if potenca == 1:
        print(i, end='*')
    elif potenca > 1:
        print(str(i) + str(potenca), sep='^', end='*')
print(end='\b')
print(" ")