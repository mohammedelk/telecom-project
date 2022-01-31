from py2neo import Graph
import numpy as np
import json
from py2neo import Node, Relationship


class Model:
    def __init__(self, password):
        self.graph = Graph(password=password)

    def get_graph(self):
        return self.graph

    """return a node by netLabel = id"""
    def get_node(self, net_label):
        return self.graph.nodes.match("NetNode", netLabel=net_label).first()

    """return an np array of childrens of a node"""
    def get_children(self, parent):
        # parent : node
        par = parent['netLabel']
        results = self.graph.run("MATCH (n)-[:CHILD_OF]->(node:NetNode {netLabel: \"" + str(par) + "\"}) RETURN n")
        if results is None:
            return np.array([])
        res = np.array([r['n'] for r in results.data()])
        return res

    """ return list of parent of a node supposed one """
    def get_parent(self, child):
        chil = child['netLabel']
        results = self.graph.run("MATCH (node:NetNode {netLabel: \"" + str(chil) + "\"})-[:CHILD_OF]->(n) RETURN n")
        if results is None:
            return np.array([])
        res = np.array([r['n'] for r in results.data()])
        return res

    # **not general function specific to "FO"
    def has_parent(self, node):
        if node['netLabel'] == "FO":
            return False
        else:
            return True


    def has_children(self, node):
        if len(self.get_parent(node)) == 0:
            return False
        else:
            return True

    """return random node"""
    def get_a_node(self):
        l = self.graph.run("MATCH (n) RETURN n limit 1").data()
        return l[0]['n']

    """return a list of nodes haven father as parent and city like city; exp agadir 
    [AGA001,AGA002...]"""
    def get_list_subtree(self, father, city):
        str_father = father['netLabel']
        ci = city[0:3]
        results = self.graph.run("MATCH (node1)-[:CHILD_OF]->(node2:NetNode {netLabel: \"" + str(str_father) + "\"}) where node1.netLabel STARTS WITH \"" + str(ci) + "\"  RETURN node1")
        res = [node['node1'] for node in results.data()]
        return res



if __name__ == "__main__":
    m = Model("azeaze")
    #print(m.get_list_subtree("FO","RABAT"))
    #print(m.get_children(m.get_net_node("FO")))
    print(m.get_parent(m.get_node("AGA001")))
    print(m.get_node("AGA001"))
"""
url = os.getenv("NEO4J_URI", "bolt://localhost:7687")
username = os.getenv("NEO4J_USER", "neo4j")
password = os.getenv("NEO4J_PASSWORD", "azeaze")
neo4j_version = os.getenv("NEO4J_VERSION", "4")
database = os.getenv("NEO4J_DATABASE", "neo4j")
"""
