#Esto tan solo es un ejemplo de como se puede conectar a una base de datos de mongoDB.


import pymongo

# Conectarse al nodo maestro
client = pymongo.MongoClient("mongodb://localhost:27017")

# Configurar la replicación
config = {
    "_id": "eventos_deportivos",
    "members": [
        {"_id": 0, "host": "localhost:27017"},
        {"_id": 1, "host": "localhost:27018"},
        {"_id": 2, "host": "localhost:27019"}
    ]
}

try:
    client.admin.command("replSetInitiate", config)
except pymongo.errors.OperationFailure as e:
    print(f"Error al iniciar el conjunto de réplicas: {e}")

# Conectarse al nodo maestro
client = pymongo.MongoClient("mongodb://localhost:27017")

# Obtener el estado de la replicación
status = client.admin.command("replSetGetStatus")

# Imprimir el estado de la replicación
print(status)