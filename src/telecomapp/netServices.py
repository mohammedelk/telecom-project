import json

from src.telecomapp.model import Model
import numpy as np


class NetServices:
    def __init__(self, model):
        self.model = model
        self.subtree = {}

    # return the root tree of a node
    def get_root_node(self, node):
        if len(self.model.graph.nodes) == 0:
            return None
        # n = self.model.get_a_node()
        if self.model.has_parent(node):
            return self.get_root_node(self.model.get_parent(node)[0])
        else:
            return node

    """ recursive fun return a tree as a dict with a root node and a max deep"""
    def get_subtree(self, n_root, tree, deep, max_deep):
        # root : root node; tree : dict accumulative tree, firstly = {}, deep firstly = 0, max_deep : max deep of tree
        tree['id'] = n_root['netLabel']
        tree['name'] = n_root['netLabel']
        tree['Vendor'] = n_root['Vendor']
        tree['NE_Type'] = n_root['NE_Type']
        tree['Dependency'] = n_root['Dependency']
        tree['children'] = []
        if max_deep > deep:
            l_child = self.model.get_children(n_root)
            for it in np.arange(0, len(l_child)):
                n_chi = l_child[it]
                conn = self.model.get_relationship(n_root, n_chi)
                if not np.array_equal(conn, []):
                    tree['Protection'] = conn[0]['Protection']
                    tree['Modulation'] = conn[0]['Modulation']
                    tree['Freq_min'] = conn[0]['Freq_min']
                    tree['Freq_max'] = conn[0]['Freq_max']
                    tree['Channels'] = conn[0]['Channels']
                    tree['Capacity'] = conn[0]['Capacity']
                    tree['Bandwidth'] = conn[0]['Bandwidth']
                    tree['Band'] = conn[0]['Band']
                tree['children'].append({})
                self.get_subtree(n_chi, tree['children'][it], deep + 1, max_deep)
        return tree

    """ return a tree as a DICT of all nodes with specific city having father as parent """
    def get_subtree_city(self, father, city, max_deep):
        # father : node; city like "NADOR"
        subtree_city = {'id': father['netLabel'], 'name': father['netLabel'], 'children': []}
        list_subtree = self.model.get_list_subtree(father, city)
        for node in list_subtree:
            subtree_city['children'].append(self.get_subtree(node, {}, 0, max_deep))
        return subtree_city




# just for testing
if __name__ == "__main__":
    m = Model("azeaze")
    nets = NetServices(m)

    n = nets.model.get_node("FO")
    res = nets.get_subtree_city(n, "TAZA", 12)
    # root = nets.get_root_node(n['netLabel'])
    # tree = nets.get_subtree(n, {}, 0,1)
    #tree2 = nets.get_subtree_city(n, "AGADIR", 2)
    # print(nets.get_root_node(nets.model.get_node("AGA001")))
    #print(json.dumps(tree2))
    print(json.dumps(res))
