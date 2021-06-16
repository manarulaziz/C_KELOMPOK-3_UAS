import csv

data_kelas = []
nilai_quiz1 = []
nilai_quiz2 = []
nilai_quiz3 = []
header_kelas = []
def kelas():
    with open('kelasc.csv', 'r', encoding = 'utf-8-sig') as csvfile:
        csvreader = csv.reader(csvfile)
        print("")
        print("Siswa Kelas C".center(36))
        print('-'*36)
        headers = next(csvreader)
        header_kelas.append(headers)
        for i in headers:
            print(i, end="\t\t")
        for siswa_c in csvreader:
            data_kelas.append(siswa_c)   
        print("")
        for siswa in data_kelas[0]:
            print(siswa, end="|")
        print("")
        for siswa in data_kelas[1]:
            print(siswa, end="|")
        print("")
        for siswa in data_kelas[2]:
            print(siswa, end="|")
        print("")
        for siswa in data_kelas[-2]:
            print(siswa, end="|")
        print("")
        for siswa in data_kelas[-1]:
            print(siswa, end="|")
        print("")

def quiz1():
    with open('quiz1.csv', 'r', encoding = 'utf-8-sig') as csvfile:
        csvreader = csv.reader(csvfile)
        
        print("")
        print("Nilai Quiz 1".center(36))
        print('-'*36)
        
        headers = next(csvreader)
        for a in headers:
            print(a, end="\t")
        
        for quiz1 in csvreader:
            nilai_quiz1.append(quiz1)   
        print("")

        for quiz1 in nilai_quiz1[0]:
            print(quiz1, end="\t|")
        print("")
        for quiz1 in nilai_quiz1[1]:
            print(quiz1, end="\t|")
        print("")
        for quiz1 in nilai_quiz1[2]:
            print(quiz1, end="\t|")
        print("")
        for quiz1 in nilai_quiz1[-2]:
            print(quiz1, end="\t|")
        print("")
        for siswa in nilai_quiz1[-1]:
            print(siswa, end="\t|")
        print("")

def quiz2():
    with open('quiz2.csv', 'r', encoding = 'utf-8-sig') as csvfile:
        csvreader = csv.reader(csvfile)
        
        print("")
        print("Nilai Quiz 2".center(36))
        print('-'*36)
        
        headers = next(csvreader)
        for a in headers:
            print(a, end="\t\t")
        
        for quiz2 in csvreader:
            nilai_quiz2.append(quiz2)   
        print("")

        for quiz2 in nilai_quiz2[0]:
            print(quiz2, end="\t|")
        print("")
        for quiz2 in nilai_quiz2[1]:
            print(quiz2, end="\t|")
        print("")
        for quiz2 in nilai_quiz2[2]:
            print(quiz2, end="\t|")
        print("")
        for quiz2 in nilai_quiz2[-2]:
            print(quiz2, end="\t|")
        print("")
        for quiz2 in nilai_quiz2[-1]:
            print(quiz2, end="\t|")
        print("")

def quiz3():
    with open('quiz3.csv', 'r', encoding = 'utf-8-sig') as csvfile:
        csvreader = csv.reader(csvfile)
        
        print("")
        print("Nilai Quiz 3".center(36))
        print('-'*36)
        
        headers = next(csvreader)
        for a in headers:
            print(a, end="\t\t")
        
        for quiz3 in csvreader:
            nilai_quiz3.append(quiz3)   
        print("")

        for quiz3 in nilai_quiz3[0]:
            print(quiz3, end="\t|")
        print("")
        for quiz3 in nilai_quiz3[1]:
            print(quiz3, end="\t|")
        print("")
        for quiz3 in nilai_quiz3[2]:
            print(quiz3, end="\t|")
        print("")
        for quiz3 in nilai_quiz3[-2]:
            print(quiz3, end="\t|")
        print("")
        for quiz3 in nilai_quiz3[-1]:
            print(quiz3, end="\t|")
        print("")

kelas()
quiz1()
quiz2()
quiz3() 

