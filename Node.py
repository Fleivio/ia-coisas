
class Node():
    def __init__ (self, state, path=[], path_cost=0, heuristic=0):
        self.state = state
        self.path = path
        self.path_cost = path_cost
        self.heuristic = heuristic
        self.f = path_cost + heuristic

    def __str__(self):
        return str(self.state) + " " + str(self.f)

    def print_node(self):
        print("State: ", self.state)
        print("F: ", self.f)