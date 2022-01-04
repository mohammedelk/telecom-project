import pandas as pd

df = pd.read_csv('../../data/BD Routage 30 10 2021.csv')
print(df.to_string())


class Node:
    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.parent = None

    def set_parent(self, parent):
        if not self.child_became_parent(parent):
            self.parent = parent

    def get_parent(self):
        return self.parent

    def has_parent(self):
        if self.parent is None:
            return False
        else:
            return True

    def child_became_parent(self, parent):
        if parent.id == self.id:
            return True
        else:
            return self.child_became_parent(parent.getparent())

        return False
