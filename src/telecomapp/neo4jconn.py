# from https://towardsdatascience.com/neo4j-cypher-python-7a919a372be7
from neo4j import GraphDatabase


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


if __name__ == "__main__":
    conn = Neo4jConnection("bolt://localhost:7687", "neo4j", "azeaze")
    #query = '''match (n) where n.nLabel='PY001' return id(n)'''
    query = '''match (n) where n.nLabel="AGA001" create (a:Node{nLabel:"PY003"})-[:CHILD_OF]->(n)'''
    print(conn.query(query, db='neo4j'))
