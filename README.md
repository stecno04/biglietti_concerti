# Gestore di Concerti
Questo è un programma Python che consente agli utenti di cercare e acquistare biglietti per concerti. Utilizza il modulo pymongo per interagire con un database MongoDB che contiene informazioni sugli eventi e i biglietti disponibili.

## Requisiti
* Python 3.x
* pymongo package
* geopy package
## Installazione
1. Assicurarsi di avere Python 3 installato correttamente sul proprio sistema.

2. Installare le dipendenze necessarie eseguendo il seguente comando:

    pip install pymongo geopy

3. Clonare o scaricare il repository su un'unità locale.

## Configurazione del database
1. Creare un account su MongoDB Atlas (https://www.mongodb.com/cloud/atlas) o utilizzare un'istanza MongoDB esistente.
2. Creare un nuovo database chiamato "Concerti" e una nuova collezione chiamata "Eventi".
3. Inserire i dati degli eventi nel database utilizzando un client MongoDB o uno script Python per l'importazione dei dati.
## Utilizzo
1. Aprire il file concerti.py in un editor di testo o in un ambiente di sviluppo Python.

2. Modificare la riga di connessione del client MongoDB con le proprie credenziali:
client = MongoClient('mongodb+srv://<username>:<password>@<cluster-url>/')
Sostituire <username>, <password> e <cluster-url> con le proprie informazioni di accesso.

3. Seguire le istruzioni visualizzate nel terminale per registrarsi o accedere come utente.

4. Utilizzare il menu per cercare concerti per artista, data, vicinanza o nome.

5. Selezionare i concerti desiderati e procedere con l'acquisto.

6. I concerti acquistati e le relative disponibilità verranno aggiornati nel database.  