import pandas as pd
import numpy as np
# from .node import Node

from node import Node


class Net:
    def __init__(self, arr_tree):
        self.arr_tree = arr_tree
        self.nodes = {}
        self.str_tree = ""

    # create nodes by batch array
    def get_nodes(self):
        if self.nodes == {}:
            for s, f in self.arr_tree:
                if not (s in self.nodes.keys()):
                    s_node = Node(s)
                    self.nodes[s] = s_node
                if not (f in self.nodes.keys()):
                    f_node = Node(f)
                    self.nodes[f] = f_node
                self.nodes[s].set_parent(self.nodes[f])
        return self.nodes

    # add node to net
    def connect_net(self):
        pass

    def gen_json(self, tree_src):
        self.str_tree += "{ " + " id:" + "\"" + tree_src.get_label() + "\"" + ", name:" + "\"" + tree_src.get_label() + "\"" + ", data:" + str(
            tree_src.data) + ", children: [ \n"
        for i in np.arange(0, len(tree_src.child)):
            self.gen_json(tree_src.child[i])
            if i < len(tree_src.child) - 1:
                self.str_tree += ", \n"

        self.str_tree += " ] }"


def csv_to_arr(csv_path, columns):
    df = pd.read_csv(csv_path, sep=';')
    #arr_tree = df[['Site', 'Farend']].to_numpy()
    arr_tree = df[columns].to_numpy()
    return np.array(arr_tree)


def arr_to_tree(arr):
    pass
