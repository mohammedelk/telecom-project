
class NetServices:
    def __init__(self,model):
        self.model = model

    def get_top_node(self):
        if len(self.model.graph.nodes) == 0:
            return None
        n = self.model.get_a_node()
        if self.model.has_parent(n):
            return

