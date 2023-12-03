import pymongo

# Conectarse al nodo maestro
client = pymongo.MongoClient("mongodb://localhost:27017/replicaSet=rs0")

Db = 'torneo_deportivo'
testColl = 'testColl'

# Insertar un registro
doc = dict(DEMO="Python for demo", MESG="Hello ApsaraDB For MongoDB")
doc_id = client[Db][testColl].insert_one(doc).inserted_id

# Consultar el registro
for d in client[Db][testColl].find(dict(DEMO="Python for demo")):
    print ('find documents: DB1', d)

client.close()

# Repetimos el proceso en el segundo nodo
client2 = pymongo.MongoClient("mongodb://localhost:27018/replicaSet=rs0")
Db = 'torneo_deportivo'
testColl = 'testColl'
doc = dict(DEMO="Python for demo", MESG="Hello ApsaraDB For MongoDB")
doc_id = client2[Db][testColl].insert_one(doc).inserted_id
for d in client2[Db][testColl].find(dict(DEMO="Python for demo")):
    print ('find documents: DB2', d)
client2.close()

# Repetimos el proceso en el tercer nodo
client3 = pymongo.MongoClient("mongodb://localhost:27019/replicaSet=rs0")
Db = 'torneo_deportivo'
testColl = 'testColl'
doc = dict(DEMO="Python for demo", MESG="Hello ApsaraDB For MongoDB")
doc_id = client3[Db][testColl].insert_one(doc).inserted_id
for d in client3[Db][testColl].find(dict(DEMO="Python for demo")):
    print ('find documents DB3:', d)
client3.close()
