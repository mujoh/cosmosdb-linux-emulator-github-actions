import time
from azure.cosmos import CosmosClient, PartitionKey

URL = "https://localhost:8081/"
KEY = "C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw=="

client = CosmosClient(URL, credential=KEY, connection_verify=False)

db = client.create_database_if_not_exists("TestDB")
container = db.create_container_if_not_exists(
    id="Items",
    partition_key=PartitionKey(path="/pk")
)

item = { "id": "1", "pk": "test", "name": "hello world" }
container.upsert_item(item)

print("Inserted OK")
