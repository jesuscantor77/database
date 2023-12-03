import pymongo

def connect_to_db(port, replica_set):
    return pymongo.MongoClient(f"mongodb://localhost:{port}/replicaSet={replica_set}")

def insert_and_query(client, db, collection, document, port):
    doc_id = client[db][collection].insert_one(document).inserted_id
    for d in client[db][collection].find(document):
        print (f'find documents: DB{port}', d)

def main():
    ports = [27017, 27018, 27019]
    replica_set = 'rs0'
    db = 'torneo_deportivo'
    collection = 'testColl'
    document = dict(DEMO="Python for demo", MESG="Hello ApsaraDB For MongoDB")

    for port in ports:
        client = connect_to_db(port, replica_set)
        insert_and_query(client, db, collection, document, port)
        client.close()

if __name__ == "__main__":
    main()