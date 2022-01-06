import pandas as pd
import numpy as np
from node import Node


class Net:
    def __init__(self, arr_tree):
        self.arr_tree = arr_tree
        self.nodes = {}

    # create nodes by batch array
    def get_nodes(self):
        if self.nodes is None:
            for s, f in self.arr_tree:

                if not (s in self.nodes.keys()):
                    s_node = Node(s)
                    self.nodes[s] = s_node
                if not (f in self.nodes.keys()):
                    f_node = Node(s)
                    self.nodes[f] = f_node
                s_node.set_parent(f_node)
        return self.nodes

    # add node to net
    def connect_net(self):
        pass


def csv_to_arr(csv_path):
    csv_path = '../../data/BD Routage 30 10 2021.csv'
    df = pd.read_csv(csv_path)
    arr_tree = df[['Site', 'Farend']][0:200].to_numpy()
    return arr_tree


def arr_to_tree(arr):
    pass
