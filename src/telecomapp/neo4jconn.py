# from https://towardsdatascience.com/neo4j-cypher-python-7a919a372be7
from neo4j import GraphDatabase
from net import csv_to_arr


class Neo4jConnection:

    def __init__(self, uri, user, pwd):
        self.__uri = uri
        self.__user = user
        self.__pwd = pwd
        self.__driver = None
        try:
            self.__driver = GraphDatabase.driver(self.__uri, auth=(self.__user, self.__pwd))
        except Exception as e:
            print("Failed to create the driver:", e)

    def close(self):
        if self.__driver is not None:
            self.__driver.close()

    def query(self, query, db=None):
        assert self.__driver is not None, "Driver not initialized!"
        session = None
        response = None
        try:
            session = self.__driver.session(database=db) if db is not None else self.__driver.session()
            response = list(session.run(query))
        except Exception as e:
            print("Query failed:", e)
        finally:
            if session is not None:
                session.close()
        return response


def create_db_from_csv(csv_path, conn):
    data_arr = csv_to_arr(csv_path, ['Site', 'Farend'])
    for n_destination, n_source, in data_arr:
        conn.query("merge (n1: NetNode{ netLabel :\"" + n_destination + "\" })"
        "merge (n2: NetNode{ netLabel :\"" + n_source + "\" })"
        "merge (n1)-[:CHILD_OF]->(n2)")

def create_db_conn_csv(csv_path, conn):
    data_arr = csv_to_arr(csv_path,['Name1','Name2','Supplier', 'NE_Type1', 'NE_Type2','Capa', 'Modulation', 'Protection', 'Channels', 'Freq_min', 'Freq_max', 'Band', 'LB' ])
    for node1, node2, supplier, ne_type1, ne_type2, capacity, modulation, protection, channels, freq_min, freq_max, band, lb in   data_arr:
        conn.query("merge (n1: NetNode{ netLabel :\"" + node1 + "\" })"
        "set n1.Vendor = \"" + supplier + "\", n1.NE_Type = \"" + ne_type1 + "\"  "
        "merge (n2: NetNode{ netLabel :\"" + node2 + "\"})"
        "set  n2.NE_Type = \"" + ne_type2 + "\"  "
        "with n1,n2 match (n1)-[r1:CHILD_OF]->(n2)"
                   "set r1.Capacity = \"" + str(capacity) + "\", r1.Modulation = \"" + str(modulation) + "\", r1.Protection = \"" + str(protection) + "\",r1.Channels = \"" + str(channels) + "\", r1.Freq_min = \"" + str(freq_min) + "\",r1.Freq_max = \"" + str(freq_max) + "\",r1.Band = \"" + str(band) + "\",r1.Bandwidth = \"" + str(lb) + "\""
        "with n1,n2 match (n2)-[r2:CHILD_OF]->(n1)"
                   "set r2.Capacity = \"" + str(capacity) + "\", r2.Modulation = \"" + str(modulation) + "\", r2.Protection = \"" + str(protection) + "\",r2.Channels = \"" + str(channels) + "\", r2.Freq_min = \"" + str(freq_min) + "\",r2.Freq_max = \"" + str(freq_max) + "\",r2.Band = \"" + str(band) + "\",r2.Bandwidth = \"" + str(lb) + "\"")





if __name__ == "__main__":
    conn = Neo4jConnection("bolt://localhost:7687", "neo4j", "azeaze")
    create_db_from_csv('H:/workspace/python/telecom-project/data/BD Routage 30 10 2021.csv', conn)
    print("db created")
    create_db_conn_csv('H:/workspace/python/telecom-project/data/dataDashboard.csv', conn)
    print("db connextion created")
    #query = '''match (n) where n.nLabel='PY001' return id(n)'''
    #data_arr = csv_to_arr('H:/workspace/python/telecom-project/data/BD Routage 30 10 2021.csv', ['Site', 'Farend'])
    """
    for destination ,source, in data_arr:
        conn.query("merge (n1: NetNode{ netLabel :\""+destination+"\" })"
        "merge (n2: NetNode{ netLabel :\""+source+"\" })"
        "merge (n1)-[:CHILD_OF]->(n2)")"""

    #query = "match (n) where n.nLabel= \"" + source + "\" create (a:Node{nLabel:\"" +destination+"\" })-[:CHILD_OF]->(n)"
    #print(conn.query(query, db='neo4j'))
