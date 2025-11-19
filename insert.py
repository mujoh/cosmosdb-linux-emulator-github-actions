from azure.cosmos import CosmosClient, PartitionKey

URL = "https://localhost:8081/"
KEY = "C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw=="

client = CosmosClient(URL, credential=KEY, connection_verify=False)

print("Connected to Cosmos Emulator")

# -----------------------------------------------------------------------------
# Create database + container
# -----------------------------------------------------------------------------
db = client.create_database_if_not_exists("TestDB")
print("Database ready:", db.id)

container = db.create_container_if_not_exists(
    id="Items",
    partition_key=PartitionKey(path="/pk")
)
print("Container ready:", container.id)

# -----------------------------------------------------------------------------
# Insert test item
# -----------------------------------------------------------------------------
item = {
    "id": "1",
    "pk": "test",
    "msg": "hello cosmos"
}

container.upsert_item(item)
print("Inserted item:", item)

# -----------------------------------------------------------------------------
# List all databases
# -----------------------------------------------------------------------------
print("\n=== DATABASES ===")
for d in client.list_databases():
    print(" -", d["id"])

# -----------------------------------------------------------------------------
# List all containers in TestDB
# -----------------------------------------------------------------------------
print("\n=== CONTAINERS IN TestDB ===")
for c in db.list_containers():
    print(" -", c["id"])

# -----------------------------------------------------------------------------
# Fetch all items from container
# -----------------------------------------------------------------------------
print("\n=== ITEMS IN CONTAINER ===")
for it in container.read_all_items():
    print(" -", it)

print("\nDone!")
