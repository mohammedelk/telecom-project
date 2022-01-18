from src.telecomapp.model import Model


class NetServices:
    def __init__(self, model):
        self.model = model

    def get_top_node(self, n):
        if len(self.model.graph.nodes) == 0:
            return None
        # n = self.model.get_a_node()
        if self.model.has_parent(n):
            return self.get_top_node(self.model.get_parent(n))
        else:
            return n


if __name__ == "__main__":
    m = Model("azeaze")
    nets = NetServices(m)
    n = nets.model.get_net_node('NAD071')
    root = nets.get_top_node(n['netLabel'])
    print(root)
