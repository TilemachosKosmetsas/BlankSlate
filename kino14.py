import random


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


ret = {  # apodoseis opap
    '7b1': 2,
    '7b2': 3,
    '7b3': 8,
    '7b4': 13,
    '7b5': 80,
    '7b6': 400,
    '7b7': 15000,
    '7no3': 1,
    '7no4': 3,
    '7no5': 20,
    '7no6': 100,
    '7no7': 5000,
    '6b1': 2,
    '6b2': 3,
    '6b3': 9,
    '6b4': 27,
    '6b5': 300,
    '6b6': 4100,
    '6no3': 1,
    '6no4': 7,
    '6no5': 50,
    '6no6': 1600,
    '5b1': 3,
    '5b2': 5,
    '5b3': 17,
    '5b4': 90,
    '5b5': 1350,
    '5no3': 2,
    '5no4': 20,
    '5no5': 450,
    '4no2': 1,
    '4no3': 4,
    '4no4': 100,
    '4b1': 5,
    '4b2': 8,
    '4b3': 24,
    '4b4': 600,
    '3no2': 2.5,
    '3no3': 25,
    '3b1': 8,
    '3b2': 18,
    '3b3': 175,
    '2no1': 1,
    '2no2': 5,
    '2b1': 16,
    '2b2': 70,
    '1no1': 2.5,
    '1b1': 52.5

}

print('     Kino!!! \n ')
while True:
    try:
        inp = int(input("posa noumera thes na paikseis (apo ena ews 12) : "))
        if 0 < inp < 13:
            break
        else:
            print("Edwses mh apodekto arithmo paixnidiwn \n")
            continue
    except ValueError:
        print("Mallon den edwses noumero, prospathise ksana \n")
        continue
while True:
    try:
        rep = int(input("Posa paixnidia theleis na paikseis (repetitions) : "))
        break
    except ValueError:
        print("Mallon den edwses arithmo epanalhspewn, prospathise ksana \n ")
        continue

print()
flag_1e = 0  # flags gia tis epityxies pou plirwnoun , tha me voithisei na metrisw katallhla tis epityxies
flag_1eb = 0
flag_2e = 0
flag_2eb = 0
flag_3e = 0
flag_3eb = 0
flag_4e = 0
flag_4eb = 0
flag_5e = 0
flag_5eb = 0
flag_6e = 0
flag_6eb = 0
flag_7e = 0
flag_7eb = 0
flag_8e = 0
flag_8eb = 0
flag_9e = 0
flag_9eb = 0
flag_10e = 0
flag_10eb = 0
flag_11e = 0
flag_11eb = 0
flag_12e = 0
flag_12eb = 0
flag_0e = 0

gamelist = []  # ta noumera tis mhxanhs
playerlist = []  # ta noumera tou paikth
epityxies = []
list80a = list(range(1, 81))  # h lista tis mhxanhs
list80b = list(range(1, 81))  # h lista tou paikth
bonus = 0


def run20(a):
    while a < 21:  # edw travame eikosi tyxaia noymera apo ta 80 xwris epanathesh
        global bonus

        x = (random.choice(list80a))
        gamelist.append(x)
        y = x
        list80a.remove(y)
        a += 1
    if a == 21:
        bonus = gamelist[-1]
        return bonus


def mygamble(b, c):
    while b < c + 1:  # edw travame c tyxaia noymera apo ta 80 xwris epanathesh
        x = (random.choice(list80b))
        playerlist.append(x)
        y = x
        list80b.remove(y)
        b += 1


def success():  # metraei tis epityxies , opws kai h parakatw successprintout apla h 2h ektypwnei kiolas

    global flag_1e
    global flag_1eb
    global flag_2e
    global flag_2eb
    global flag_3e
    global flag_3eb
    global flag_4e
    global flag_4eb
    global flag_5e
    global flag_5eb
    global flag_6e
    global flag_6eb
    global flag_7e
    global flag_7eb
    global flag_8e
    global flag_8eb
    global flag_9e
    global flag_9eb
    global flag_10e
    global flag_10eb
    global flag_11e
    global flag_11eb
    global flag_12e
    global flag_12eb
    global flag_0e

    for num in list(sorted(playerlist)):
        if num in list(sorted(gamelist)):
            epityxies.append(num)

    if len(epityxies) == 1:
        if bonus in epityxies:
            flag_1eb += 1
            return flag_1eb
        else:
            flag_1e += 1
            return flag_1e
    elif len(epityxies) == 2:
        if bonus in epityxies:
            flag_2eb += 1
            return flag_2eb
        else:
            flag_2e += 1
            return flag_2e

    elif len(epityxies) == 3:
        if bonus in epityxies:
            flag_3eb += 1
            return flag_3eb
        else:
            flag_3e += 1
            return flag_3e

    elif len(epityxies) == 4:
        if bonus in epityxies:
            flag_4eb += 1
            return flag_4eb
        else:
            flag_4e += 1
            return flag_4e

    elif len(epityxies) == 5:
        if bonus in epityxies:
            flag_5eb += 1
            return flag_5eb
        else:
            flag_5e += 1
            return flag_5e

    elif len(epityxies) == 6:
        if bonus in epityxies:
            flag_6eb += 1
            return flag_6eb
        else:
            flag_6e += 1
            return flag_6e

    elif len(epityxies) == 7:
        if bonus in epityxies:
            flag_7eb += 1
            return flag_7eb
        else:
            flag_7e += 1
            return flag_7e

    elif len(epityxies) == 8:
        if bonus in epityxies:
            flag_8eb += 1
            return flag_8eb
        else:
            flag_8e += 1
            return flag_8e

    elif len(epityxies) == 9:
        if bonus in epityxies:
            flag_9eb += 1
            return flag_9eb
        else:
            flag_9e += 1
            return flag_9e

    elif len(epityxies) == 10:
        if bonus in epityxies:
            flag_10eb += 1
            return flag_10eb
        else:
            flag_10e += 1
            return flag_10e

    elif len(epityxies) == 11:
        if bonus in epityxies:
            flag_11eb += 1
            return flag_11eb
        else:
            flag_11e += 1
            return flag_11e

    elif len(epityxies) == 12:
        if bonus in epityxies:
            flag_12eb += 1
            return flag_12eb
        else:
            flag_12e += 1
            return flag_12e

    else:
        flag_0e += 1
        return flag_0e


def successprintout():  # auth h funtion einai idia me tin prohgoumenh , alla kanei kai prints
    global flag_1e
    global flag_1eb
    global flag_2e
    global flag_2eb
    global flag_3e
    global flag_3eb
    global flag_4e
    global flag_4eb
    global flag_5e
    global flag_5eb
    global flag_6e
    global flag_6eb
    global flag_7e
    global flag_7eb
    global flag_8e
    global flag_8eb
    global flag_9e
    global flag_9eb
    global flag_10e
    global flag_10eb
    global flag_11e
    global flag_11eb
    global flag_12e
    global flag_12eb
    global flag_0e

    for num in list(sorted(playerlist)):
        if num in list(sorted(gamelist)):
            epityxies.append(num)

    if len(epityxies) == 1:
        print("eixes mia epityxia, ton arithmo " + str(epityxies[0]))
        if bonus in epityxies:
            print("kai einai o arithmos bonus ")
            print()
            flag_1eb += 1
            return flag_1eb
        else:
            print()
            flag_1e += 1
            return flag_1e

    elif len(epityxies) == 2:
        print("eixes 2 epityxies, tous arithmous " + str(epityxies[0:]))
        if bonus in epityxies:
            print("pou perilamvanoyn ton arithmo bonus " + str(bonus))
            print()
            flag_2eb += 1
            return flag_2eb
        else:
            print()
            flag_2e += 1
            return flag_2e

    elif len(epityxies) == 3:
        print("eixes 3 epityxies, tous arithmous " + str(epityxies[0:]))
        if bonus in epityxies:
            print("pou perilamvanoyn ton arithmo bonus " + str(bonus))
            print()
            flag_3eb += 1
            return flag_3eb
        else:
            print()
            flag_3e += 1
            return flag_3e

    elif len(epityxies) == 4:
        print("eixes 4 epityxies, tous arithmous " + str(epityxies[0:]))
        if bonus in epityxies:
            print("pou perilamvanoyn ton arithmo bonus " + str(bonus))
            print()
            flag_4eb += 1
            return flag_4eb
        else:
            print()
            flag_4e += 1
            return flag_4e

    elif len(epityxies) == 5:
        print("eixes 5 epityxies, tous arithmous " + str(epityxies[0:]))
        if bonus in epityxies:
            print("pou perilamvanoyn ton arithmo bonus " + str(bonus))
            print()
            flag_5eb += 1
            return flag_5eb
        else:
            print()
            flag_5e += 1
            return flag_5e

    elif len(epityxies) == 6:
        print("eixes 6 epityxies, tous arithmous " + str(epityxies[0:]))
        if bonus in epityxies:
            print("pou perilamvanoyn ton arithmo bonus " + str(bonus))
            print()
            flag_6eb += 1
            return flag_6eb
        else:
            print()
            flag_6e += 1
            return flag_6e

    elif len(epityxies) == 7:
        print("eixes 7 epityxies, tous arithmous " + str(epityxies[0:]))
        if bonus in epityxies:
            print("pou perilamvanoyn ton arithmo bonus " + str(bonus))
            print()
            flag_7eb += 1
            return flag_7eb
        else:
            print()
            flag_7e += 1
            return flag_7e

    elif len(epityxies) == 8:
        print("eixes 8 epityxies, tous arithmous " + str(epityxies[0:]))
        if bonus in epityxies:
            print("pou perilamvanoyn ton arithmo bonus " + str(bonus))
            print()
            flag_8eb += 1
            return flag_8eb
        else:
            print()
            flag_8e += 1
            return flag_8e

    elif len(epityxies) == 9:
        print("eixes 9 epityxies, tous arithmous " + str(epityxies[0:]))
        if bonus in epityxies:
            print("pou perilamvanoyn ton arithmo bonus " + str(bonus))
            print()
            flag_9eb += 1
            return flag_9eb
        else:
            print()
            flag_9e += 1
            return flag_9e

    elif len(epityxies) == 10:
        print("eixes 10 epityxies, tous arithmous " + str(epityxies[0:]))
        if bonus in epityxies:
            print("pou perilamvanoyn ton arithmo bonus " + str(bonus))
            print()
            flag_10eb += 1
            return flag_10eb
        else:
            print()
            flag_10e += 1
            return flag_10e

    elif len(epityxies) == 11:
        print("eixes 11 epityxies, tous arithmous " + str(epityxies[0:]))
        if bonus in epityxies:
            print("pou perilamvanoyn ton arithmo bonus " + str(bonus))
            print()
            flag_11eb += 1
            return flag_11eb
        else:
            print()
            flag_11e += 1
            return flag_11e

    elif len(epityxies) == 12:
        print("eixes 12 epityxies, tous arithmous " + str(epityxies[0:]))
        if bonus in epityxies:
            print("pou perilamvanoyn ton arithmo bonus " + str(bonus))
            print()
            flag_12eb += 1
            return flag_12eb
        else:
            print()
            flag_12e += 1
            return flag_12e

    else:
        print("Den epiases kanena noumero")
        print()
        flag_0e += 1
        return flag_0e

        # teleiwsan oi functions , ksekinaei to paixnidi

while True:
    result = (input("An theleis na deis poies itan i epityxies sou akrivws se kathe paixnidi, pata to 1 \n"
                    "An theleis na deis tin kathe klirwsh ksexwrista, kai tis epityxies pata to 2\n"
                    "An Theleis na deis mono ta pososta (faster method) sto telos pata 3 \n"
                    ": "))
    try:
        if int(result) == 1:
            counter = 0
            if counter == 0:
                print()
                print()
            while counter < int(rep):
                gamelist = []  # ta ksana evala auta edw mesa wste na ksekinaei i loopa me kathe fora adeies tis listes
                playerlist = []
                epityxies = []
                list80a = list(range(1, 81))
                list80b = list(range(1, 81))
                print("Game " + str(int(counter + 1)) + ": ")
                run20(1)  # ena simainei ksekina apo thn prwth loopa apo to 1 (tha traviksei 20 noumera outws h allws)
                mygamble(1, int(inp))  # <--------o deuteros arithmos simainei trava tosa noumera apo ta 80
                successprintout()
                counter += 1
            if counter == int(rep):
                print()
                print()
                print("Akolouthoun ta pososta: ")
            break

        if int(result) == 2:
            counter = 0
            if counter == 0:
                print()
                print()
            while counter < int(rep):
                gamelist = []  # ta ksana evala auta edw mesa wste na ksekinaei i loopa me kathe fora adeies tis listes
                playerlist = []
                epityxies = []
                list80a = list(range(1, 81))
                list80b = list(range(1, 81))
                print("Game " + str(int(counter + 1)) + ": ")
                run20(1)
                mygamble(1, int(inp))
                print("to mixanima klirwse ta noumera : ")
                print(Color.BOLD + str(sorted(gamelist)) + Color.END)  # sortarismenh
                print("kai o arithmos bonus einai to " + str(bonus))
                print("ta noumera to paikti itan :")
                print(Color.BOLD + str(sorted(playerlist)) + Color.END)
                print()
                successprintout()
                counter += 1
            if counter == int(rep):
                print()
                print()
                print("Akolouthoun ta pososta: ")
            break

        if int(result) == 3:
            counter = 0
            if counter == 0:
                print()
            while counter < int(rep):
                gamelist = []  # ta ksana evala auta edw mesa wste na ksekinaei i loopa me kathe fora adeies tis listes
                playerlist = []
                epityxies = []
                list80a = list(range(1, 81))
                list80b = list(range(1, 81))
                run20(1)
                mygamble(1, int(inp))  # <--------o deuteros arithmos simainei trava tosa noumera apo ta 80
                success()
                counter += 1
            if counter == int(rep):
                print()
                print()
                print("Akolouthoun ta pososta: ")
            break

    except ValueError:
        continue

# apo dw kai katw akolouthei apologismos , efoson einai aparaithtos , to if simainei oti efoson
# to flag exei anevei panw
# apo to mhden , tote kai mono tote na mou vgalei apotelesmata/statistika, an einai miden
# na mi mou leei px 0& xwris logo

if (flag_1e or flag_1eb) > 0:
    print("Toses fores eixes apo mia epityxia : " + str(flag_1e) + " me pososto " + str(
        float(flag_1e / int(rep)) * 100) + " %")
    print("Mia epityxia me Bonus:  " + str(flag_1eb) + " me pososto " + str(float(flag_1eb / int(rep)) * 100) + " %")
    print()
if (flag_2e or flag_2eb) > 0:
    print("Toses fores eixes apo dyo epityxies :" + str(flag_2e) + " me pososto " + str(
        float(flag_2e / int(rep)) * 100) + " %")
    print("Dyo epityxies me Bonus:  " + str(flag_2eb) + " me pososto " + str(float(flag_2eb / int(rep)) * 100) + " %")
    print()
if (flag_3e or flag_3eb) > 0:
    print("Toses fores eixes apo treis epityxies : " + str(flag_3e) + " me pososto " + str(
        float(flag_3e / int(rep)) * 100) + " %")
    print(
        "Treis epityxies me bonus:  " + str(flag_3eb) + " me pososto " + str(float(flag_3eb / int(rep)) * 100) + " %")
    print()
if (flag_4e or flag_4eb) > 0:
    print("Toses fores eixes apo tessereis epityxies : " + str(flag_4e) + " me pososto " + str(
        float(flag_4e / int(rep)) * 100) + " %")
    print("Tessereis epityxies me bonus:   " + str(flag_4eb) + " me pososto " + str(
        float(flag_4eb / int(rep)) * 100) + " %")
    print()
if (flag_5e or flag_5eb) > 0:
    print("Toses fores eixes apo pente epityxies : " + str(flag_5e) + " me pososto " + str(
        float(flag_5e / int(rep)) * 100) + " %")
    print(
        "Pente epityxies me bonus:  " + str(flag_5eb) + " me pososto " + str(float(flag_5eb / int(rep)) * 100) + " %")
    print()
if (flag_6e or flag_6eb) > 0:
    print("Toses fores eixes apo eksi epityxies : " + str(flag_6e) + " me pososto " + str(
        float(flag_6e / int(rep)) * 100) + " %")
    print(
        "Eksi epityxies me bonus:  " + str(flag_6eb) + " me pososto " + str(float(flag_6eb / int(rep)) * 100) + " %")
    print()
if (flag_7e or flag_7eb) > 0:
    print("Toses fores eixes apo epta epityxies : " + str(flag_7e) + " me pososto " + str(
        float(flag_7e / int(rep)) * 100) + " %")
    print(
        "Epta epityxies me bonus:  " + str(flag_7eb) + " me pososto " + str(float(flag_7eb / int(rep)) * 100) + " %")
    print()
if (flag_8e or flag_8eb) > 0:
    print("Toses fores eixes apo oxto epityxies : " + str(flag_8e) + " me pososto " + str(
        float(flag_8e / int(rep)) * 100) + " %")
    print(
        "Oxto epityxies me bonus:  " + str(flag_8eb) + " me pososto " + str(float(flag_8eb / int(rep)) * 100) + " %")
    print()
if (flag_9e or flag_9eb) > 0:
    print("Toses fores eixes apo ennia epityxies : " + str(flag_9e) + " me pososto " + str(
        float(flag_9e / int(rep)) * 100) + " %")
    print(
        "Ennia epityxies me bonus:  " + str(flag_9eb) + " me pososto " + str(float(flag_9eb / int(rep)) * 100) + " %")
    print()
if (flag_10e or flag_10eb) > 0:
    print("Toses fores eixes apo deka epityxies : " + str(flag_10e) + " me pososto " + str(
        float(flag_10e / int(rep)) * 100) + " %")
    print("Deka epityxies me bonus:  " + str(flag_10eb) + " me pososto " + str(
        float(flag_10eb / int(rep)) * 100) + " %")
    print()
if (flag_11e or flag_11eb) > 0:
    print("Toses fores eixes apo enteka epityxies : " + str(flag_11e) + " me pososto " + str(
        float(flag_11e / int(rep)) * 100) + " %")
    print("Enteka epityxies me bonus:  " + str(flag_11eb) + " me pososto " + str(
        float(flag_11eb / int(rep)) * 100) + " %")
    print()
if (flag_12e or flag_12eb) > 0:
    print("Toses fores eixes apo dwdeka epityxies : " + str(flag_12e) + " me pososto " + str(
        float(flag_12e / int(rep)) * 100) + " %")
    print("Dwdeka epityxies me bonus:  " + str(flag_12eb) + " me pososto " + str(
        float(flag_12eb / int(rep)) * 100) + " %")
    print()
if flag_0e > 0:
    print("Toses fores den yphrkse kammia epityxia:  " + str(flag_0e) + " me pososto " + str(
        float(flag_0e / int(rep)) * 100) + " %")
    print()

roi_1ib = (flag_1eb * ret['1b1'] + flag_1e * ret['1no1'])
roi_2ib = (flag_1eb * ret['2b1'] + flag_1e * ret['2no1'] + flag_2e * ret['2no2'] + flag_2eb * ret['2b2'])
roi_3ib = (flag_1eb * ret['3b1'] + flag_2e * ret['3no2'] + flag_2eb * ret['3b2'] +
           flag_3e * ret['3no3'] + flag_3eb * ret['3b3'])
roi_4ib = (flag_1eb * ret['4b1'] + flag_2e * ret['4no2'] + flag_2eb * ret['4b2'] +
           flag_3e * ret['4no3'] + flag_3eb * ret['4b3'] + flag_4e * ret['4no4'] + flag_4eb * ret['4b4'])
roi_5ib = (flag_1eb * ret['5b1'] + flag_2eb * ret['5b2'] + flag_3eb * ret['5b3'] +
           flag_4eb * ret['5b4'] + flag_5eb * ret['5b5'] + flag_3e * ret['5no3'] +
           flag_4e * ret['5no4'] + flag_5e * ret['5no5'])
roi_6ib = (flag_1eb * ret['6b1'] + flag_2eb * ret['6b2'] + flag_3eb * ret['6b3'] +
           flag_4eb * ret['6b4'] + flag_5eb * ret['6b5'] + flag_6eb * ret['6b6'] +
           flag_3e * ret['6no3'] + flag_4e * ret['6no4'] + flag_5e * ret['6no5'] +
           flag_6e * ret['6no6'])
roi_7ib = (flag_1eb * ret['7b1'] + flag_2eb * ret['7b2'] + flag_3eb * ret['7b3'] +
           flag_4eb * ret['7b4'] + flag_5eb * ret['7b5'] + flag_6eb * ret['7b6'] +
           flag_7eb * ret['7b7'] + flag_3e * ret['7no3'] + flag_4e * ret['7no4'] +
           flag_5e * ret['7no5'] + flag_6e * ret['7no6'] + flag_7e * ret['7no7'])

if inp == 1:
    print("Roi1 with b")
    print(roi_1ib / (2 * rep))
if inp == 2:
    print("Roi2 with b")
    print(roi_2ib / (2 * rep))
if inp == 3:
    print("Roi3 with b")
    print(roi_3ib / (2 * rep))
if inp == 4:
    print("Roi4 with b")
    print(roi_4ib / (2 * rep))
if inp == 5:
    print("Roi5 with b")
    print(roi_5ib / (2 * rep))
if inp == 6:
    print("Roi6 with b")
    print(roi_6ib / (2 * rep))
if inp == 7:
    print("Roi7 with b")
    print(roi_7ib / (2 * rep))
if 2 == 2:
    input("Press Enter to Exit : ")
