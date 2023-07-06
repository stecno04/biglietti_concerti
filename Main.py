from pymongo import MongoClient
from pymongo.collation import Collation
from geopy.geocoders import Nominatim


#gestione concerti
concerti_selezionati = []

client = MongoClient('mongodb+srv://user2:ciao@cluster0.7l0lshi.mongodb.net/')
db = client['Concerti']
collection = db['Eventi']
biglietti = db['Biglietti']



collection.create_index([("coordinate", "2dsphere")])

def login():
    
    return username

def scelta(risultati):
    # Lista per i dati dei concerti
    concerti = []
    counter = 1
    # Stampa i risultati
    for concerto in risultati:
        disponibilita = concerto['disponibilita']
        if disponibilita == '0':
            disponibilita = 'sold-out'
        else:
            disponibilita = f"disp:{disponibilita}"

        nome = concerto['nome']
        data = concerto['data']
        costo = concerto['costo']
        artista = concerto['artista']
        
        # Aggiungi i dati del concerto alla lista
        concerto_data = [nome, data, disponibilita, costo, artista]
        concerti.append(concerto_data)

        print(f"{counter}: {concerto_data}")
        counter += 1

    if len(concerti) == 0:
        print("Nessun concerto trovato.")
        return None
    # Chiedi all'utente di scegliere un concerto
    scelta = int(input("Inserisci il numero del concerto che vuoi selezionare: "))
    # Restituisci il concerto scelto
    

    # l'utente può decidere di non selezionare nessun concerto
    if scelta == 0:
        print("Nessun concerto selezionato.")
        return None
    else:
        scelta = concerti[scelta - 1]
    
    return scelta

def ricerca_artista():
    concerto_scelto = scelta(risultati)
    
    return concerto_scelto

def ricerca_data():
    
   concerto_scelto = scelta(risultati)
    
    return concerto_scelto

def ricerca_nome():
    
    concerto_scelto = scelta(risultati)
    
    return concerto_scelto

def ricerca_vicinanza():

    concerto_scelto = scelta(risultati)
    return concerto_scelto

def acquisto(concerti, username):
    print('Vuoi procedere con l\'acquisto?')
    acquisto = input('s/n ')
    if acquisto == 's':
        
        #l'utente può decidere quanti posti acquistare per ogni concerto
        for concerto in concerti:
            print(f'Quanti posti vuoi acquistare per {concerto[0]}?')
            posti = int(input('Inserisci il numero di posti: '))
            concerto.append(posti)
            
        print('Il costo totale è: ')
        costo_totale = 0
        for concerto in concerti:
            costo_totale += concerto[3] * concerto[5]
        print(costo_totale)
        print('Acquisto effettuato e disponibilità aggiornata')
        # Update the document
        biglietti.update_one(
            {"username": username},
            {"$set": {"concerti": concerti}},
            upsert=True
        )
        for concerto in concerti:
            # modifica della disponibilità dei posti                
            collection.update_one({'nome': concerto[0]}, {'$inc': {'disponibilita': - concerto[5]}})
    else:
        print('acquisto annullato')
        

def main():
    
    username = login()
    while True:
        print("Gestione concerti")
        print("Inserisci 1 per cercare per artista")
        print("Inserisci 2 per cercare per data")
        print("Inserisci 3 per cercare per vicinanza")
        print("Inserisci 4 per cercare per nome del concerto")
        print("Inserisci 5 per vedere i concerti già precedentemente acquistati")
        selezione = input("Inserisci la tua scelta: ")
        # ognuna di queste funzioni restituisce al massimo un concerto
        if selezione == '1':
            result = ricerca_artista()
            if result is not None:
                concerti_selezionati.append(result)
        elif selezione == '2':
            result = ricerca_data()
            if result is not None:
                concerti_selezionati.append(result)
        elif selezione == '3':
            result = ricerca_vicinanza()
            if result is not None:
                concerti_selezionati.append(result)
        elif selezione == '5':
            print("I concerti che hai già acquistato sono:")
            for biglietto in biglietti.find({'username': username}, {'_id': 0, 'concerti': 1}):
                print(biglietto)
        elif selezione == '4':
            result = ricerca_nome()
            if result is not None:
                concerti_selezionati.append(result)
        
        if len(concerti_selezionati) > 0:
            print("I concerti selezionati sono:")
            for concerto in concerti_selezionati:
                print(concerto)
            altri_o_no = input("Vuoi aggiungere altri concerti? (s/n) ")
            if altri_o_no == "n":
                acquisto(concerti_selezionati, username)
                break
            elif altri_o_no == "s": 
                continue


main()