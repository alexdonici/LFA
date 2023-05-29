############################
####### MINIMAL DFA ########
############################
import random


def afisare(dictionar):
    for linie in dictionar:
        print(linie, dictionar[linie])
    print()


def afisare_partitie(partitii):
    for partitie in partitii:
        print(partitii.index(partitie))
        for stare in partitie:
            print(stare, partitie[stare])
    print()


def stari_aproape_egale(st1, st2):
    ok = 1
    for litera in alfabet:
        if st1[litera][1] != st2[litera][1]:
            ok = 0
    return ok

#####################################
######## PARTITIE AUXILIARA #########
#####################################
def partitionare(lista_partitii):
    partitie_noua = []
    for partitie in lista_partitii:
        for stare in partitie:
            if len(partitie_noua) == 0 or len(partitie) == 1:  # dacă partitia e goală sau are o sg stare
                partitie_noua.append({stare: partitie[stare]})
            else:
                for x in partitie_noua:
                    if stari_aproape_egale(partitie[stare], x[random.choice(list(x.keys()))]):
                        x[stare] = partitie[stare]
                        break
                else:
                    partitie_noua.append({stare: partitie[stare]})
    return partitie_noua

#################################
### RECONSTRUIREA PARTITIILOR ### -impartim starile DFA-ului in functie de echivalenta lor
#################################
def reconstruct(partitii):
    for partitie in partitii:
        for stare in partitie:
            for litera in partitie[stare]:
                for partitie2 in partitii:
                    if partitie[stare][litera][0] in partitie2:
                        partitie[stare][litera][1] = partitii.index(partitie2)


#################################
########## RANDOM.TXT ###########
#################################
with open("random.txt") as f:
    alfabet = f.readline().strip().split()  # Citirea alfabetului
    finale = f.readline().strip().split()  # Citirea starilor finale
    tranzitii = f.readline().strip().split()  # Citirea tranzitiilor
    dictionar_tranzitii = {}
    for stare in tranzitii:
        dictionar_tranzitii[stare] = {}
    for linie in f:
        tranz = linie.strip().split()
        dictionar_tranzitii[tranz[0]][tranz[1]] = [tranz[2], None]




partitii = []
A = {}
B = {}
for stare in dictionar_tranzitii:
    if stare in finale:
        B[stare] = dictionar_tranzitii[stare]
    else:
        A[stare] = dictionar_tranzitii[stare]
partitii.append(A)  # Adăugarea primei partiții A
partitii.append(B)  # Adăugarea celei de-a doua partiții B
reconstruct(partitii)




partitie_aux = partitionare(partitii)  # Crearea primei partiții auxiliare
reconstruct(partitie_aux)




while partitie_aux != partitii:
    partitii = partitionare(partitii)  # Actualizarea partițiilor
    reconstruct(partitii)

    partitie_aux = partitionare(partitie_aux)  # Crearea unei noi partiții auxiliare
    reconstruct(partitie_aux)


#######################
####### AFISARE #######
#######################


print("Partitii finale după minimizare:")
afisare_partitie(partitii)  # Afișarea partițiilor finale
