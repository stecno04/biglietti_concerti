from pymongo import MongoClient

# Gestione concerti
concerti_selezionati = []

client = MongoClient('mongodb+srv://user2:ciao@cluster0.7l0lshi.mongodb.net/')
db = client['Concerti']
collection = db['Eventi']
biglietti = db['Biglietti']



def scelta(risultati):
    # funzione che restituisce il concerto scelto dall'utente
    return concerto_scelto

def ricerca_artista():
    # ricerca per artista restituire il concerto scelto
    return concerto_scelto

def ricerca_data():
    # ricerca per data restituire il concerto scelto
    return concerto_scelto

def ricerca_vicinanza():
    # ricerca per vicinanza restituire il concerto scelto
    return concerto_scelto

def acquisto(concerti):
    # acquisto dei biglietti e insert del biglietto nella collection Biglietti
    return


def main():
    while True:
        print("Gestione concerti")
        print("1. Inserisci uno per cercare per artista")
        print("2. Inserisci due per cercare per data")
        print("3. Inserisci tre per cercare per vicinanza")
        print("4. Inserisci quattro per uscire")
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
        elif selezione == '4':
            break
        else:
            print("Scelta non valida")
        
        if len(concerti_selezionati) > 0:
            print("I concerti selezionati sono:")
            for concerto in concerti_selezionati:
                print(concerto)
            altri_o_no = input("Vuoi aggiungere altri concerti? (s/n) ")
            if altri_o_no == "n":
                acquisto(concerti_selezionati)
                break
            elif altri_o_no == "s": 
                continue

main()
