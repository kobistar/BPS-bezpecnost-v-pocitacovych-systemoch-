#!/bin/bash python3
import getpass
from posixpath import split
import os

path_to_dir = os.getcwd()
list_suborov = []
list_priecinkov = []
list_prav_suborov = [] 
list_prav_priecinkov = []
list_vlastnikov_suborov = []
list_vlastnikov_priecinkov = []

list_suborov2_0 = []
list_priecinkov2_0 = []
list_prav_suborov2_0 = [] 
list_prav_priecinkov2_0 = []
list_vlastnikov_suborov2_0 = []
list_vlastnikov_priecinkov2_0 = []

medzi_list_suborov = []
medzi_list_priecinkov = []
medzi_list_prav_suborov = [] 
medzi_list_prav_priecinkov = []
medzi_list_vlastnikov_suborov = []
medzi_list_vlastnikov_priecinkov = []

counter_suborov_priecinkov = 0

sken = input('# ')
koniec = 0
podpriecinok = 0
plnenie = 0
pomocny_list = sken.split()
meno_podpriecinka = chr

while koniec != 1:
    run_counter = 0
    if len(pomocny_list) == 0:
        sken = input('# ')
        pomocny_list = sken.split()
    
    else:
        if pomocny_list[0] == "ls":
            if (counter_suborov_priecinkov == 0) and (run_counter == 0) and (len(pomocny_list) == 1): print("Ziaden subor")
            elif (counter_suborov_priecinkov > 0) and (run_counter == 0) and (len(pomocny_list) == 1):

                z = 0
                while z < len(list_suborov): 
                    print(list_suborov[z],list_vlastnikov_suborov[z], list_prav_suborov[z])
                    z += 1
                z = 0
                while z < len(list_priecinkov): 
                    print(list_priecinkov[z],list_vlastnikov_priecinkov[z], list_prav_priecinkov[z])
                    z += 1
                
            elif (len(pomocny_list) == 2) and (run_counter == 0) and (pomocny_list[1] in list_priecinkov):
                index = list_priecinkov.index(pomocny_list[1])

                if (list_prav_priecinkov[index] == "-wx") or (list_prav_priecinkov[index] == "-w-") or (list_prav_priecinkov[index] == "--x") or (list_prav_priecinkov[index] == "---"): print("chyba prav")
                else: print(list_priecinkov[index],list_vlastnikov_priecinkov[index], list_prav_priecinkov[index])
                
            elif (len(pomocny_list) == 2) and (run_counter == 0) and (pomocny_list[1] in list_suborov):
                index = list_suborov.index(pomocny_list[1])
    
                if (list_prav_suborov[index] == "-wx") or (list_prav_suborov[index] == "-w-") or (list_prav_suborov[index] == "--x") or (list_prav_suborov[index] == "---"): print("chyba prav")
                else: print(list_suborov[index],list_vlastnikov_suborov[index], list_prav_suborov[index])
                        
            elif (run_counter == 0) and (len(pomocny_list) == 2) and (pomocny_list[1] not in list_priecinkov): print("chyba")
            elif (run_counter == 0) and (len(pomocny_list) == 2) and (pomocny_list[1] not in list_suborov): print("chyba")

            run_counter += 1

        elif pomocny_list[0] == "touch":
            if len(pomocny_list) != 2:
                print("chyba")
            if (run_counter == 0) and (pomocny_list[1] not in list_suborov) and (pomocny_list[1] not in list_priecinkov):
                if podpriecinok == 1 : plnenie += 1
                list_suborov.append(pomocny_list[1])
                list_prav_suborov.append("rwx")
                list_vlastnikov_suborov.append(getpass.getuser())
                counter_suborov_priecinkov += 1
            else: print("chyba")
            run_counter += 1

        elif pomocny_list[0] == "mkdir":
            if len(pomocny_list) != 2:
                print("chyba")

            elif (run_counter == 0) and (pomocny_list[1] not in list_priecinkov) and (pomocny_list[1] not in list_suborov):
                if podpriecinok == 1 : plnenie += 1
                list_priecinkov.append(pomocny_list[1])
                list_prav_priecinkov.append("rwx")
                list_vlastnikov_priecinkov.append(getpass.getuser())
                counter_suborov_priecinkov += 1

            else: print("chyba")    
            run_counter += 1

        elif pomocny_list[0] == "rm":
            chyba = 0
            
            if len(pomocny_list) != 2:
                print("chyba")
            
            if (len(pomocny_list) == 2) and (run_counter == 0) and (pomocny_list[1] in list_priecinkov): 

                index = list_priecinkov.index(pomocny_list[1])
                if (list_prav_priecinkov[index] == "r-x") or (list_prav_priecinkov[index] == "r--") or (list_prav_priecinkov[index] == "--x") or (list_prav_priecinkov[index] == "---"): 
                    chyba = 1
                    print("chyba prav")

            if (len(pomocny_list) == 2) and (run_counter == 0) and (pomocny_list[1] in list_suborov):
    
                index = list_suborov.index(pomocny_list[1])
                if (list_prav_suborov[index] == "r-x") or (list_prav_suborov[index] == "r--") or (list_prav_suborov[index] == "--x") or (list_prav_suborov[index] == "---"): 
                    chyba = 1
                    print("chyba prav")
                
            if (chyba == 0) and (run_counter == 0) and (pomocny_list[1] in list_priecinkov2_0) and (plnenie > 0) and (podpriecinok == 1):

                plnenie -= 1 
                list_suborov.clear()
                list_priecinkov.clear()
                list_prav_suborov.clear() 
                list_prav_priecinkov.clear()
                list_vlastnikov_suborov.clear()
                list_vlastnikov_priecinkov.clear()

                x = 0
                while x < len(list_priecinkov2_0):
                    list_vlastnikov_priecinkov.append(list_vlastnikov_priecinkov2_0[x])
                    list_priecinkov.append(list_priecinkov2_0[x])
                    list_prav_priecinkov.append(list_prav_priecinkov2_0[x])
                    x += 1

                x = 0
                while x < len(list_suborov2_0):
                    list_suborov.append(list_suborov2_0[x])
                    list_prav_suborov.append(list_prav_suborov2_0[x])
                    list_vlastnikov_suborov.append(list_vlastnikov_suborov2_0[x])
                    x += 1
                
                list_suborov2_0.clear()
                list_priecinkov2_0.clear()
                list_prav_suborov2_0.clear() 
                list_prav_priecinkov2_0.clear()
                list_vlastnikov_suborov2_0.clear()
                list_vlastnikov_priecinkov2_0.clear()

                index = list_priecinkov.index(pomocny_list[1])
                list_priecinkov.pop(index)
                list_prav_priecinkov.pop(index)
                list_vlastnikov_priecinkov.pop(index)        
                counter_suborov_priecinkov -= 1

            elif (chyba == 0) and (run_counter == 0) and (pomocny_list[1] in list_priecinkov) and (plnenie > 0) and (podpriecinok == 0):
                
                plnenie -= 1
                index = list_priecinkov.index(pomocny_list[1])
                
                list_suborov2_0.clear()
                list_priecinkov2_0.clear()
                list_prav_suborov2_0.clear() 
                list_prav_priecinkov2_0.clear()
                list_vlastnikov_suborov2_0.clear()
                list_vlastnikov_priecinkov2_0.clear()

                list_priecinkov.pop(index)
                list_prav_priecinkov.pop(index)
                list_vlastnikov_priecinkov.pop(index)        
                counter_suborov_priecinkov -= 1
                
            elif (chyba == 0) and (run_counter == 0) and (pomocny_list[1] in list_priecinkov):

                index = list_priecinkov.index(pomocny_list[1])
                list_priecinkov.pop(index)
                list_prav_priecinkov.pop(index)
                list_vlastnikov_priecinkov.pop(index)        
                counter_suborov_priecinkov -= 1

            elif (chyba == 0) and (run_counter == 0) and (pomocny_list[1] in list_suborov):
                
                if(plnenie > 0) and (podpriecinok == 1): plnenie -= 1
                index = list_suborov.index(pomocny_list[1])
                list_suborov.pop(index)
                list_prav_suborov.pop(index)
                list_vlastnikov_suborov.pop(index)
                counter_suborov_priecinkov -= 1

            else: print("chyba")

            run_counter += 1

        elif pomocny_list[0] == "vypis":
            if len(pomocny_list) != 2:
                print("chyba")

            elif (run_counter == 0 and pomocny_list[1] in list_suborov):
                index = list_suborov.index(pomocny_list[1])
                if (list_prav_suborov[index] == "r--") or (list_prav_suborov[index] == "rw-") or (list_prav_suborov[index] == "rwx") or (list_prav_suborov[index] == "r-x"): print("ok")
                else: print("chyba prav")

            elif (run_counter == 0 and pomocny_list[1] in list_priecinkov):
                index = list_priecinkov.index(pomocny_list[1])
                if (list_prav_priecinkov[index] == "r--") or (list_prav_priecinkov[index] == "rw-") or (list_prav_priecinkov[index] == "rwx") or (list_prav_priecinkov[index] == "r-x"): print("ok")
                else: print("chyba prav")

            else: print("chyba")
            run_counter += 1

        elif pomocny_list[0] == "quit": exit()

        elif pomocny_list[0] == "spusti":
            if len(pomocny_list) != 2:
                print("chyba")
            
            elif (run_counter == 0 and pomocny_list[1] in list_suborov):
                index = list_suborov.index(pomocny_list[1])
                if (list_prav_suborov[index] == "--x") or (list_prav_suborov[index] == "-wx") or (list_prav_suborov[index] == "rwx") or (list_prav_suborov[index] == "r-x"): print("ok")
                else: print("chyba prav")
            
            elif (run_counter == 0 and pomocny_list[1] in list_priecinkov):
                index = list_priecinkov.index(pomocny_list[1])
                if (list_prav_priecinkov[index] == "--x") or (list_prav_priecinkov[index] == "-wx") or (list_prav_priecinkov[index] == "rwx") or (list_prav_priecinkov[index] == "r-x"): print("ok")
                else: print("chyba prav")
                
            else: print("chyba")
            run_counter += 1

        elif pomocny_list[0] == "zapis":
            if len(pomocny_list) != 2:
                print("chyba")

            elif (run_counter == 0 and pomocny_list[1] in list_suborov):
                index = list_suborov.index(pomocny_list[1])
                if (list_prav_suborov[index] == "-w-") or (list_prav_suborov[index] == "-wx") or (list_prav_suborov[index] == "rwx") or (list_prav_suborov[index] == "rw-"): print("ok")
                else: print("chyba prav")

            elif (run_counter == 0 and pomocny_list[1] in list_priecinkov):
                index = list_priecinkov.index(pomocny_list[1])
                if (list_prav_priecinkov[index] == "-w-") or (list_prav_priecinkov[index] == "-wx") or (list_prav_priecinkov[index] == "rwx") or (list_prav_priecinkov[index] == "rw-"): print("ok")    
                else: print("chyba prav")

            else: print("chyba")
            run_counter += 1

        elif pomocny_list[0] == "chmod":
            if len(pomocny_list) != 3:
                print("chyba") 
            elif (run_counter == 0) and (pomocny_list[2] in list_suborov) and (len(pomocny_list) == 3):
                index = list_suborov.index(pomocny_list[2])

                if pomocny_list[1] == "1": list_prav_suborov[index] = "--x"
                elif pomocny_list[1] == "0": list_prav_suborov[index] = "---"
                elif pomocny_list[1] == "2": list_prav_suborov[index] = "-w-"
                elif pomocny_list[1] == "4": list_prav_suborov[index] = "r--"
                elif pomocny_list[1] == "3": list_prav_suborov[index] = "-wx"
                elif pomocny_list[1] == "5": list_prav_suborov[index] = "r-x"
                elif pomocny_list[1] == "6": list_prav_suborov[index] = "rw-"
                elif pomocny_list[1] == "7": list_prav_suborov[index] = "rwx"
                else: print("chyba")

            elif (run_counter == 0) and (pomocny_list[2] in list_priecinkov) and (len(pomocny_list) == 3):
                index = list_priecinkov.index(pomocny_list[2])

                if pomocny_list[1] == "1": list_prav_priecinkov[index] = "--x"
                elif pomocny_list[1] == "0": list_prav_priecinkov[index] = "---"
                elif pomocny_list[1] == "2": list_prav_priecinkov[index] = "-w-"
                elif pomocny_list[1] == "4": list_prav_priecinkov[index] = "r--"
                elif pomocny_list[1] == "3": list_prav_priecinkov[index] = "-wx"
                elif pomocny_list[1] == "5": list_prav_priecinkov[index] = "r-x"
                elif pomocny_list[1] == "6": list_prav_priecinkov[index] = "rw-"
                elif pomocny_list[1] == "7": list_prav_priecinkov[index] = "rwx"
                else: print("chyba")
        
            else: print("chyba")
            run_counter += 1

        elif pomocny_list[0] == "chown":
            if len(pomocny_list) != 3:
                print("chyba") 
            elif (run_counter == 0) and (pomocny_list[2] in list_suborov) and (len(pomocny_list) == 3):
                    index = list_suborov.index(pomocny_list[2])
                    list_vlastnikov_suborov[index] = pomocny_list[1]
            elif (run_counter == 0) and (pomocny_list[2] in list_priecinkov) and (len(pomocny_list) == 3):
                    index = list_priecinkov.index(pomocny_list[2])
                    list_vlastnikov_priecinkov[index] = pomocny_list[1]

            else: print("chyba")

            run_counter += 1

        elif pomocny_list[0] == "cd":
            if (len(pomocny_list) != 2):
                print("chyba") 
            elif (run_counter == 0) and (pomocny_list[1] in list_priecinkov):
                index = list_priecinkov.index(pomocny_list[1])
                meno_podpriecinka = pomocny_list[1]
                if (list_prav_priecinkov[index] == "r--") or (list_prav_priecinkov[index] == "rw-") or (list_prav_priecinkov[index] == "-w-") or (list_prav_priecinkov[index] == "---"): print("chyba prav")
                
                else:
                    if (run_counter == 0) and (pomocny_list[1] in list_priecinkov) and (len(pomocny_list) == 2) and (len(list_prav_priecinkov2_0) == 0):
                        podpriecinok = 1
                        x = 0
                        while x < len(list_suborov):
                            list_suborov2_0.append(list_suborov[x])
                            list_prav_suborov2_0.append(list_prav_suborov[x]) 
                            list_vlastnikov_suborov2_0.append(list_vlastnikov_suborov[x])
                            x += 1
                        x = 0
                        while x < len(list_priecinkov):
                            list_priecinkov2_0.append(list_priecinkov[x])
                            list_prav_priecinkov2_0.append(list_prav_priecinkov[x])
                            list_vlastnikov_priecinkov2_0.append(list_vlastnikov_priecinkov[x])
                            x += 1

                        list_suborov.clear()
                        list_priecinkov.clear()
                        list_prav_suborov.clear() 
                        list_prav_priecinkov.clear()
                        list_vlastnikov_suborov.clear()
                        list_vlastnikov_priecinkov.clear()

                    elif (run_counter == 0) and (pomocny_list[1] in list_priecinkov) and (len(pomocny_list) == 2) and (len(list_prav_priecinkov2_0) != 0):
                        podpriecinok = 1
                        x = 0
                        while x < len(list_priecinkov):
                            medzi_list_vlastnikov_priecinkov.append(list_vlastnikov_priecinkov[x])
                            medzi_list_priecinkov.append(list_priecinkov[x])
                            medzi_list_prav_priecinkov.append(list_prav_priecinkov[x])
                            x += 1

                        x = 0
                        while x < len(list_suborov):
                            medzi_list_suborov.append(list_suborov[x])
                            medzi_list_prav_suborov.append(list_prav_suborov[x])
                            medzi_list_vlastnikov_suborov.append(list_vlastnikov_suborov[x])
                            x += 1

                        list_suborov.clear()
                        list_priecinkov.clear()
                        list_prav_suborov.clear() 
                        list_prav_priecinkov.clear()
                        list_vlastnikov_suborov.clear()
                        list_vlastnikov_priecinkov.clear()
                        
                        x = 0
                        while x < len(list_suborov2_0):
                            list_suborov.append(list_suborov2_0[x])
                            list_prav_suborov.append(list_prav_suborov2_0[x]) 
                            list_vlastnikov_suborov.append(list_vlastnikov_suborov2_0[x])
                            x += 1
                        x = 0
                        while x < len(list_priecinkov2_0):
                            list_priecinkov.append(list_priecinkov2_0[x])
                            list_prav_priecinkov.append(list_prav_priecinkov2_0[x])
                            list_vlastnikov_priecinkov.append(list_vlastnikov_priecinkov2_0[x])
                            x += 1

                        list_suborov2_0.clear()
                        list_priecinkov2_0.clear()
                        list_prav_suborov2_0.clear() 
                        list_prav_priecinkov2_0.clear()
                        list_vlastnikov_suborov2_0.clear()
                        list_vlastnikov_priecinkov2_0.clear()

                        x = 0
                        while x < len(medzi_list_suborov):
                            list_suborov2_0.append(medzi_list_suborov[x])
                            list_prav_suborov2_0.append(medzi_list_prav_suborov[x]) 
                            list_vlastnikov_suborov2_0.append(medzi_list_vlastnikov_suborov[x])
                            x += 1

                        x = 0
                        while x < len(medzi_list_priecinkov):
                            list_priecinkov2_0.append(medzi_list_priecinkov[x])
                            list_prav_priecinkov2_0.append(medzi_list_prav_priecinkov[x])
                            list_vlastnikov_priecinkov2_0.append(medzi_list_vlastnikov_priecinkov[x])
                            x += 1

                        medzi_list_suborov.clear()
                        medzi_list_priecinkov.clear()
                        medzi_list_prav_suborov.clear() 
                        medzi_list_prav_priecinkov.clear()
                        medzi_list_vlastnikov_suborov.clear()
                        medzi_list_vlastnikov_priecinkov.clear()            

            elif (run_counter == 0) and (pomocny_list[1] == "..") and (len(pomocny_list) == 2):
                podpriecinok = 0
                x = 0
                while x < len(list_priecinkov):
                    medzi_list_vlastnikov_priecinkov.append(list_vlastnikov_priecinkov[x])
                    medzi_list_priecinkov.append(list_priecinkov[x])
                    medzi_list_prav_priecinkov.append(list_prav_priecinkov[x])
                    x += 1
                x = 0
                while x < len(list_suborov):
                    medzi_list_suborov.append(list_suborov[x])
                    medzi_list_prav_suborov.append(list_prav_suborov[x])
                    medzi_list_vlastnikov_suborov.append(list_vlastnikov_suborov[x])
                    x += 1

                list_suborov.clear()
                list_priecinkov.clear()
                list_prav_suborov.clear() 
                list_prav_priecinkov.clear()
                list_vlastnikov_suborov.clear()
                list_vlastnikov_priecinkov.clear()
                
                x = 0
                while x < len(list_suborov2_0):
                    list_suborov.append(list_suborov2_0[x])
                    list_prav_suborov.append(list_prav_suborov2_0[x]) 
                    list_vlastnikov_suborov.append(list_vlastnikov_suborov2_0[x])
                    x += 1
                x = 0
                while x < len(list_priecinkov2_0):
                    list_priecinkov.append(list_priecinkov2_0[x])
                    list_prav_priecinkov.append(list_prav_priecinkov2_0[x])
                    list_vlastnikov_priecinkov.append(list_vlastnikov_priecinkov2_0[x])
                    x += 1

                list_suborov2_0.clear()
                list_priecinkov2_0.clear()
                list_prav_suborov2_0.clear() 
                list_prav_priecinkov2_0.clear()
                list_vlastnikov_suborov2_0.clear()
                list_vlastnikov_priecinkov2_0.clear()

                x = 0
                while x < len(medzi_list_suborov):
                    list_suborov2_0.append(medzi_list_suborov[x])
                    list_prav_suborov2_0.append(medzi_list_prav_suborov[x]) 
                    list_vlastnikov_suborov2_0.append(medzi_list_vlastnikov_suborov[x])
                    x += 1

                x = 0
                while x < len(medzi_list_priecinkov):
                    list_priecinkov2_0.append(medzi_list_priecinkov[x])
                    list_prav_priecinkov2_0.append(medzi_list_prav_priecinkov[x])
                    list_vlastnikov_priecinkov2_0.append(medzi_list_vlastnikov_priecinkov[x])
                    x += 1

                medzi_list_suborov.clear()
                medzi_list_priecinkov.clear()
                medzi_list_prav_suborov.clear() 
                medzi_list_prav_priecinkov.clear()
                medzi_list_vlastnikov_suborov.clear()
                medzi_list_vlastnikov_priecinkov.clear()

            else: print("chyba")    
            run_counter += 1
        else: print("chyba")

        sken = input('# ')
        pomocny_list = sken.split()