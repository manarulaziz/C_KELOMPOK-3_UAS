import sort
from modul import *
header_kelas.extend(["Quiz 1, Quiz 2, Quiz 3"])


for i in nilai_quiz1:
    i[0] = int(i[0])
    i[1] = float(i[1])

sort.selection(nilai_quiz1,0)

i = 39
n = 0
while i <= len(nilai_quiz1):
    if n >= len(data_kelas):
        break
    if nilai_quiz1[i][0] == int(data_kelas[n][0][5:]):
        data_kelas[n].append(nilai_quiz1[i][1])
        n += 1
        i += 1
    else:
        for j in range(i,len(nilai_quiz1)):
            if nilai_quiz1[j][0] == int(data_kelas[n][0][5:]):
                data_kelas[n].append(nilai_quiz1[j][1])
                break
        data_kelas[n].append(0)
        if len(data_kelas[n]) == 4:
            data_kelas[n].pop(-1)
        n += 1

### Quiz 2
for i in nilai_quiz2:
    i[0] = int(i[0][5:])
    i[1] = float(i[1])

sort.selection(nilai_quiz2,0)

i = 37
n = 0
while i <= len(nilai_quiz2):
    if n >= len(data_kelas):
        break
    if nilai_quiz2[i][0] == int(data_kelas[n][0][5:]):
        data_kelas[n].append(nilai_quiz2[i][1])
        n += 1
        i += 1
    else:
        for j in range(i,len(nilai_quiz2)):
            if nilai_quiz2[j][0] == int(data_kelas[n][0][5:]):
                data_kelas[n].append(nilai_quiz2[j][1])
                break
        data_kelas[n].append(0)
        if len(data_kelas[n]) == 5:
            data_kelas[n].pop(-1)
        n += 1

### Quiz 3
for i in nilai_quiz3:
    i[0] = float(i[0])
    i[1] = int(i[1][5:])

sort.selection(nilai_quiz3,1)

i = 37
n = 0
while i <= len(nilai_quiz3):
    if n >= len(data_kelas):
        break
    if nilai_quiz3[i][1] == int(data_kelas[n][0][5:]):
        data_kelas[n].append(nilai_quiz3[i][0])
        n += 1
        i += 1
    else:
        for j in range(i,len(nilai_quiz3)):
            if nilai_quiz3[j][1] == int(data_kelas[n][0][5:]):
                data_kelas[n].append(nilai_quiz3[j][0])
                break
        data_kelas[n].append(0)
        if len(data_kelas[n]) == 6:
            data_kelas[n].pop(-1)
        n += 1

print("="*75)
print("Data Nilai (No. 7)".center(75))
print("="*75)

header_kelas.extend(["Quiz 1","Quiz 2","Quiz 3"])

for i in header_kelas:
    print(i, end="\t")
print("")

data_Quiz = []
for i in data_kelas:
    data_Quiz.append(i)

for i in data_Quiz[0]:
    print(i, end="\t")
print("")
for i in data_Quiz[1]:
    print(i, end="\t")
print("")
for i in data_Quiz[2]:
    print(i, end="\t")
print("")
for i in data_Quiz[-2]:
    print(i, end="\t")
print("")
for i in data_Quiz[-1]:
    print(i, end="\t")
print("")
print("-"*75)
print("")
