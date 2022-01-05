import numpy as np


class Node:
    def __init__(self, label):
        self.label = label
        self.data = {}
        self.parent = None
        self.child = np.array([])

    def set_parent(self, parent):
        if not self.child_became_parent(parent):
            self.parent = parent
            parent.add_child(self)

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

    def add_child(self, child):
        np.append(self.child, child)
