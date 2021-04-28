vse = []
vse.append(list(input().replace(" ", "")))
for i in range(len(vse[0])-1):
    vse.append(list(input().replace(" ", "")))
vse.reverse()

a = 2
indexVecje = 0
sestevek = 0
for i in vse:
    sestevek += int(i[indexVecje])
    if vse.index(i) + 1 != len(vse):
        indexVecje = vse[vse.index(i)+1].index(max(vse[vse.index(i)+1][indexVecje:indexVecje+a]))
        if vse[vse.index(i)+1].count(max(vse[vse.index(i)+1][indexVecje:indexVecje+a])) > 1:
            temp = vse[vse.index(i)+1][:]
            temp.reverse()
            a = len(temp) - temp.index(max(vse[vse.index(i)+1][indexVecje:indexVecje+a]))
        else:
            a = 2
print(sestevek)