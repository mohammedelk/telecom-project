from py2neo import Graph
import json
from py2neo import Node, Relationship


class Model:
    def __init__(self, password):
        self.graph = Graph(password=password)

    def get_graph(self):
        return self.graph

    def get_net_node(self, net_label):
        return self.graph.nodes.match("NetNode", netLabel=net_label).first()

    def get_children(self, parent):
        results = self.graph.run("MATCH (n)-[:CHILD_OF]->(node:NetNode {netLabel: \"" + str(parent) + "\"}) RETURN n")
        if results is None:
            return []
        return results.data()

    def get_parent(self, child):
        results = self.graph.run("MATCH (node:NetNode {netLabel: \"" + str(child) + "\"})-[:CHILD_OF]->(n) RETURN n")
        return results.data()

    def has_parent(self, node):
        if len(self.get_parent(node)) == 0:
            return False
        else:
            return True


    def has_children(self, node):
        if len(self.get_parent(node)) == 0:
            return False
        else:
            return True


    def get_a_node(self):
        l = self.graph.run("MATCH (n) RETURN n limit 1").data()
        return l[0]['n']





if __name__ == "__main__":
    m = Model("azeaze")
    print(len(m.get_children("FO")))

"""
url = os.getenv("NEO4J_URI", "bolt://localhost:7687")
username = os.getenv("NEO4J_USER", "neo4j")
password = os.getenv("NEO4J_PASSWORD", "azeaze")
neo4j_version = os.getenv("NEO4J_VERSION", "4")
database = os.getenv("NEO4J_DATABASE", "neo4j")
"""
