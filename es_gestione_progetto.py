prenota=int(input("Digitare 1 per effettuare una prenotazione: "))
print("------------------------------------------------------------------------------------------")
carne = 20
pesce = 30
if prenota == 1:
    persone = int(input("Inserire in cifre il numero di posti per la prenotazione: "))
    print()
    fumatori = int(input("Inserire i fumatori per la suddivisione dei tavoli: "))
    print()
    portate_carne = int(input("Inserire quante persone desiderano il menu di carne (ad esclusione il resto usufruirà delle portate a base di pesce): "))
    print("--------------------------------------------------------------------------------------")
    portate_pesce = persone-portate_carne
    tavoli_non_fumatori = (persone-fumatori)
    if tavoli_non_fumatori > 6:
        tavoli_non_fumatori = tavoli_non_fumatori/6
        tavoli_non_fumatori = round(tavoli_non_fumatori,0)
    elif tavoli_non_fumatori < 1:
        tavoli_non_fumatori = 0
    else:
        tavoli_non_fumatori = 1
    if fumatori > 6:
        tavoli_fumatori = fumatori/6
        tavoli_fumatori = round(tavoli_fumatori,0)
    elif fumatori < 1:
        tavoli_fumatori = 0
    else:
        tavoli_fumatori = 1
        
    camerieri = 2*(tavoli_fumatori + tavoli_non_fumatori)
    print("il numero di camerieri per questa prenotazione è: ", camerieri)
    totale = (portate_carne*carne) + (portate_pesce*pesce) 
    lista_camerieri = []
    for i in range (camerieri):
        nome = input("Inserisci nome cameriere: ")
        anni_di_servizio = input("inserisci anni di esperienza cameriere: ")
        lista_camerieri.append(nome)
        lista_camerieri.append(anni_di_servizio)
        i+=1
    print("-------------------------------------------------------------------------------------")
    print("La prenotazione sta per essere conclusa con successo ora si inseriscano i dati dei clienti: ")
    lista_clienti = []
    for x in range (persone):
        nome = input("Inserisci nome cliente: ")
        numero_telefono = int(input("inserisci numero di telefono: "))
        lista_clienti.append(nome)
        lista_clienti.append(numero_telefono)
        x+=1
print()
print()
print()
print("RIEPILOGO PRENOTAZIONE")
print("si tenga conto che i tavoli sono composti da 6 posti ed ogni tavolo viene servito da 2 camerieri")
print("************************************************************************************************************************************")
print("Numero Clienti: ", persone)
print()
print("Lista dei clienti: ", lista_clienti)
print()
print("Portate di carne: ",portate_carne)
print()
print("Portate di pesce: ", portate_pesce)
print()
print("Tavoli per non fumatori: ", tavoli_non_fumatori)
print()
print("Tavoli per i fumatori: ", tavoli_fumatori)
print()
print("Numero camerieri: ", camerieri)
print()
print("lista dei camerieri: ", lista_camerieri)
print()
print()
print()
print()
print("Spesa totale della prenotazione: ", totale)
        
        

        
        
        
   
        
        
    
    
    
    
    
    
    
