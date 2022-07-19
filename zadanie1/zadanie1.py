
import sys
import os

pocet_argumentov = len(sys.argv)
list_argumentov = str(sys.argv)

pomlcka_counter = velkost_hesla = sifra = desifra = parameter = vstupny_subor = vystupny_subor = counter = 0
ASCII_hodnoty_nove_znaky = ord_posun_hodnot = []
desifrovane_znaky = nove_znaky = []
data_vstupneho_suboru = heslo = nazov_vstupneho_suboru = chr

if(len(sys.argv) != 8): sys.exit('Chyba')

while len(list_argumentov) > counter:

    if list_argumentov[counter] == '-':
        pomlcka_counter += 1
        counter += 1

        if list_argumentov[counter] == 's':
            sifra = 1
        elif list_argumentov[counter] == 'd':
            desifra = 1
        elif list_argumentov[counter] == 'p':
            parameter = 1
            counter += 5
            pomocny_counter = counter

            if(len(list_argumentov) < counter):
                sys.exit("Chyba")

            while list_argumentov[counter] != ',' and list_argumentov[counter] != list_argumentov[-1]:
                counter += 1

            heslo = list_argumentov[pomocny_counter:counter - 1]

            x = 0
            while len(heslo) - 1 >= x:
                velkost_hesla = velkost_hesla + ord(heslo[x])
                x += 1

            while velkost_hesla // 2 > 5:
                velkost_hesla = velkost_hesla // 2

        elif(list_argumentov[counter] == 'i'):
            vstupny_subor = 1
            counter += 5
            pomocny_counter = counter

            if(len(list_argumentov) < counter):
                sys.exit("Chyba")

            while list_argumentov[counter] != ',' and list_argumentov[counter] != list_argumentov[-1]:
                counter += 1

            nazov_vstupneho_suboru = list_argumentov[pomocny_counter:counter - 1]

            if os.path.isfile(nazov_vstupneho_suboru) == False:
                sys.exit("Chyba")

            input_file = open(nazov_vstupneho_suboru, "r", encoding='utf-8')
            data_vstupneho_suboru = input_file.read()
           

        elif(list_argumentov[counter] == 'o'):
            vystupny_subor = 1
            counter += 5
            pomocny_counter = counter

            if(len(list_argumentov) < counter):
                sys.exit("Chyba")

            while list_argumentov[counter] != ',' and list_argumentov[counter] != list_argumentov[-1]:
                counter += 1

            nazov_vystupneho_suboru = list_argumentov[pomocny_counter:counter - 1]

            output_file = open(nazov_vystupneho_suboru, "w", encoding='utf-8')

        elif ord(list_argumentov[counter + 1]) != 39 or list_argumentov[counter] != 's' or list_argumentov[counter] != 'd' or list_argumentov[counter] != 'p' or list_argumentov[counter] != 'i' or list_argumentov[counter] != 'o':
            sys.exit("Chyba")

    elif len(list_argumentov) - 1 == counter and pomlcka_counter == 0:
        sys.exit("Chyba")

    counter += 1

if (sifra == 1 and desifra == 1) or (sifra == 0 and desifra == 0):
    sys.exit("Chyba")

if vystupny_subor == 0 or vstupny_subor == 0 or parameter == 0:
    sys.exit("Chyba")

if(sifra == 1):
    x = 0

    while len(data_vstupneho_suboru) - 1 >= x:

        if (ord(data_vstupneho_suboru[x]) + velkost_hesla) > 1114111:
            posun = ord(data_vstupneho_suboru[x]) + velkost_hesla - 1114111
            ord_posun_hodnot.append(posun)
            
        else: ord_posun_hodnot.append(ord(data_vstupneho_suboru[x]) + velkost_hesla)

        nove_znaky.append(chr(ord_posun_hodnot[x]))
        output_file.write(nove_znaky[x])
        x += 1

if(desifra == 1):
    x = 0
    while len(data_vstupneho_suboru) - 1 >= x:
        if (ord(data_vstupneho_suboru[x]) - velkost_hesla) < 0: 
            posun = velkost_hesla - ord(data_vstupneho_suboru[x])
            ord_posun_hodnot.append(1114111 - posun)

        else: ord_posun_hodnot.append(ord(data_vstupneho_suboru[x]) - velkost_hesla)
        
        nove_znaky.append(chr(ord_posun_hodnot[x]))
        output_file.write(nove_znaky[x])
        x += 1

input_file.close()
output_file.close()