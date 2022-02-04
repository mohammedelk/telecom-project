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

    """ return list of relationship of two nodes supposed one """
    def get_relationship(self,parent, child):
        par = parent['netLabel']
        chil = child['netLabel']
        results = self.graph.run("MATCH (node1:NetNode {netLabel: \"" + str(chil) + "\"})-[r:CHILD_OF]->(node2:NetNode {netLabel: \"" + str(par) + "\"}) RETURN r")
        if results is None:
            return np.array([])
        res = np.array([r['r'] for r in results.data()])
        return res

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

    """return list of parents of node, nodes : accumulative, firstly = []"""
    def get_parents(self, node, nodes):
        if self.has_parent(node):
            parent = self.get_parent(node)[0]
            nodes.append(parent)
            return self.get_parents(parent, nodes)
        return nodes

    def set_dependency(self):
        for n in np.arange(0, len(self.graph.nodes)):
            node=self.graph.nodes.get(n)
            node['Dependency'] = len(self.get_parents(node, []))
            self.graph.push(node)

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


# just for testing
if __name__ == "__main__":
    m = Model("azeaze")
    n = m.get_node("FO")
    ag = m.get_node("AGA001")
    #nn = m.graph.nodes
    #print(m.graph.nodes.get(0))
    #print(m.get_list_subtree("FO","RABAT"))
    #print(m.get_children(m.get_net_node("FO")))
    #print(m.get_parent(m.get_node("AGA001")))
    #print(m.get_node("AGA001"))
    #print(m.get_parents(n, []))
    #m.set_dependency()
    #n['Dependency'] = 1
    #m.graph.push(m.graph.)
    #print(n['Dependency'])
    print(m.get_relationship(n, ag))
"""
py2neo :  https://py2neo.org/v4/data.html#py2neo.data.walk

url = os.getenv("NEO4J_URI", "bolt://localhost:7687")
username = os.getenv("NEO4J_USER", "neo4j")
password = os.getenv("NEO4J_PASSWORD", "azeaze")
neo4j_version = os.getenv("NEO4J_VERSION", "4")
database = os.getenv("NEO4J_DATABASE", "neo4j")

from py2neo import Graph, Node, Relationship

uri = "bolt://localhost:7687"
user = "neo4j"
password = "..."

g = Graph(uri=uri, user=user, password=password)

# optionally clear the graph
# g.delete_all()

print(len(g.nodes))
print(len(g.relationships))

# begin a transaction
tx = g.begin()

# define some nodes and relationships
a = Node("Person", name="Alice")
b = Node("Person", name="Bob")
ab = Relationship(a, "KNOWS", b)

# create the nodes and relationships
tx.create(a)
tx.create(b)
tx.create(ab)

# commit the transaction
tx.commit()

print(g.exists(ab))
print(len(g.nodes))
print(len(g.relationships))
"""
