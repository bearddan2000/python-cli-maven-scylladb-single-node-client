from cassandra.cluster import Cluster

cluster = Cluster(
    contact_points=[
        "db",
    ]
)

session = cluster.connect()

results = session.execute('SELECT * FROM system.clients LIMIT 10')

for item in results:
    print(item)
    print(item.address)