import pandas as pd
import numpy as np


class Net:
    def __init__(self, arr_tree):
        self.arr_tree = arr_tree
        self.nodes = {}
    def get_nodes(self):
        for s,f in self.arr_tree:
            pass
def csv_to_arr(csv_path):
    csv_path = '../../data/BD Routage 30 10 2021.csv'
    df = pd.read_csv(csv_path)
    arr_tree = df[['Site', 'Farend']][0:200].to_numpy()
    return arr_tree


def arr_to_tree(arr):
    pass
