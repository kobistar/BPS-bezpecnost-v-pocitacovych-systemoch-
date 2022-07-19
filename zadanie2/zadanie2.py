import hashlib
import sys
import os

mena = []
hes = []
kluce = []

if os.path.isfile('./hesla.csv') == False: 
    print("chyba")
    exit()
    
file = open('hesla.csv', 'r+', encoding = 'utf-8')
line = file.readlines()

x = 0
while len(line) - 1 >= x:
    one_line = line[x]
    list_one_line = one_line.split(':')
    
    mena.append(list_one_line[0])
    hes.append(list_one_line[1])
    
    string_kluce = list_one_line[2]
    kluce_one_line = string_kluce.split(',')
    last_key =  kluce_one_line[-1]
    
    list_last_key = last_key.split()
    kluce_one_line.pop(-1)
    if len(list_last_key) != 0: kluce_one_line.append(list_last_key[0])

    kluce.append(kluce_one_line)
    x += 1

meno = input("meno: ")
input_heslo = input("heslo: ")
overovaci_kluc = input("overovaci kluc: ")

if meno not in mena: 
    print("chyba")
    exit()

x = 0
while len(mena) > x:
    if meno == mena[x]: index_mena = x
    x += 1

input_hes = hashlib.sha256(input_heslo.encode()).hexdigest()
if input_hes != hes[index_mena]: 
    print("chyba")
    exit()

if overovaci_kluc not in kluce[index_mena]: 
    print("chyba")
    exit()

for i in range (len(kluce[index_mena])): 
    if overovaci_kluc == kluce[index_mena][i]: index_kluca = i

kluce[index_mena].pop(index_kluca)

file.close()
file = open('hesla.csv', 'w')

for i in range (len(mena)):
    meno = mena[i]
    file.write(meno)
    file.write(":")
    has = hes[i]
    file.write(has)
    file.write(":")
    x = 0
    for x in range(len(kluce[i])):
        kluc = kluce[i][x]
        file.write(kluc)
        if x < len(kluce[i]) - 1: file.write(",") 

    file.write('\n')

file.close()
print("ok")