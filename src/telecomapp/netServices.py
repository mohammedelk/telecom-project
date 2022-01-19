from src.telecomapp.model import Model
import numpy as np


class NetServices:
    def __init__(self, model):
        self.model = model
        self.subtree = {}

    def get_root_node(self, n):
        if len(self.model.graph.nodes) == 0:
            return None
        # n = self.model.get_a_node()
        if self.model.has_parent(n):
            return self.get_root_node(self.model.get_parent(n))
        else:
            return n[0]

    def get_subtree(self, n_root, tree, deep, max_deep):
        # root : root node; tree : dict accumulative tree, deep firstly = 0, max_deep : maxx deep of tree
        tree['id'] = n_root['netLabel']
        tree['children'] = []
        if max_deep > deep:
            l_child = self.model.get_children(n_root['netLabel'])
            for chi in np.arange(0, len(l_child)):
                n_chi = l_child[chi]['n']
                tree['children'].append({})
                self.get_subtree(n_chi, tree['children'][chi], deep + 1, max_deep)
        return tree


if __name__ == "__main__":
    m = Model("azeaze")
    nets = NetServices(m)
    n = nets.model.get_net_node("FO")
    root = nets.get_root_node(n['netLabel'])
    tree = nets.get_subtree(n,{},0,1)


    print(tree)
