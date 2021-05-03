n = int(input())
stalenN = n
print(n, "=", end=' ')

potenca = 0
while n % 2 == 0:
        n /= 2
        potenca += 1
skupaj = 2 ** potenca
print("2^" + str(potenca), end='*')
relevantPrastevila = [2]
while True:
    i = 1
    dodanoPraSt = True
    while dodanoPraSt:
        i += 1
        for j in relevantPrastevila:
            if i%j==0:
                break
            if j == relevantPrastevila[-1]:
                relevantPrastevila.append(i)
                dodanoPraSt = False

    i = relevantPrastevila[-1]
    potenca = 0

    while n % i == 0:
        n /= i
        potenca += 1
    if potenca == 1:
        print(i, end='*')
    elif potenca > 1:
        print(str(i) + "^" + str(potenca), end='*')
    skupaj *= i ** potenca
    if skupaj == stalenN:
        break

print(end='\b')
print(" ")