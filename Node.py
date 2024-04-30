
class Node():
    def __init__ (self, state, parent=None, path_cost=0, heuristic=0, childs=[]):
        self.state = state
        self.parent = parent
        self.path_cost = path_cost
        self.heuristic = heuristic
        self.f = path_cost + heuristic
        self.childs = childs

    def __str__(self):
        return str(self.state) + " " + str(self.f)

    def get_path(self):
        path = []
        node = self
        while node:
            path.append(node.state)
            node = node.parent
        return list(reversed(path))