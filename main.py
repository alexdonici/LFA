###########################
##########TEMA 1###########
###########################
def run_dfa(dfa, input_string):
    
    stare_curenta = dfa['stare_initiala'] #### seteaza starea curenta la starea initiala a DFA-ului ###
     
 
    for simbol in input_string:
        
        if simbol not in dfa['alfabet']:   ### verifica daca simbolul nu se afla in alfabetul DFA-ului ###
            return False
        
        
        stare_curenta = dfa['tranzitii'].get((stare_curenta, simbol), None)     ### obtine urmatoarea stare pe baza starii curente i a simbolului ###
        
        ### Verifică dacă nu există o tranziție definită pentru perechea (stare_curenta, simbol)###
        if stare_curenta is None:
            return False
    
    ### Verifică dacă starea curentă se află în mulțimea stărilor finale ###
    return stare_curenta in dfa['stari_finale']


def read_file(nume_fisier):
    dfa = {}
    with open(nume_fisier, 'r') as f:
        tranzitii = {}
        stari_finale = set()
        linii = f.readlines()
        
        ### Parcurge fiecare linie din fișier ###
        for linie in linii:
            parti = linie.strip().split()
            
            ### Verifică dacă linia are 3 componente (stare, simbol, stare_urmatoare) - reprezentând o tranziție ###
            if len(parti) == 3:
                stare, simbol, stare_urmatoare = parti
                
                ### Adaugă tranziția în dicționarul de tranzitii ###
                tranzitii[(stare, simbol)] = stare_urmatoare
            
            ### Verifică dacă linia este ultima - reprezentând stările finale ###
            elif linie == linii[-1]:
                for parte in parti:
                    # Adaugă fiecare parte în mulțimea de stări finale
                    stari_finale.add(parte)
            
            ### Altfel, afișează linia ca fiind ignorată ###
            else:
                print(f"Linii ignorate: {linie.strip()}")
        
        alfabet = set()
        stari = set()
        
        ### Extrage alfabetul și mulțimea de stări din dicționarul de tranzitii ###
        for (stare, simbol) in tranzitii:
            alfabet.add(simbol)
            stari.add(stare)
            stari.add(tranzitii[(stare, simbol)])
        
        ### Setează starea inițială ca fiind "q" + cel mai mic element din mulțimea de stări ###
        stare_initiala = "q" + min([x[1] for x in stari])
        
        ### Construiește DFA-ul folosind informațiile extrase ###
        dfa['alfabet'] = alfabet
        dfa['stari'] = stari
        dfa['stare_initiala'] = stare_initiala
        dfa['stari_finale'] = stari_finale
        dfa['tranzitii'] = tranzitii
        
    return dfa


###############################
######## MAIN PROGRAM #########
###############################


dfa = read_file('input.txt')
input_string = input("Input: ")

### Verifică dacă șirul de intrare este acceptat de DFA și afișează rezultatul corespunzător ###
if run_dfa(dfa, input_string):
    print("Acceptat")
else:
    print("Respins")
