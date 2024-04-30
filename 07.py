from Runner import Runner
from Problem import Problem

routes = {
    'A': {'B':7, 'C':9, 'D':3},
    'B': {'A':7, 'F':3, 'I':4},
    'C': {'A':9, 'J':5},
    'D': {'A':3, 'E':1},
    'F': {'B':3, 'G':2},
    'G': {'F':2, 'H':3},
    'H': {'G':3},
    'I': {'B':4, 'K':5},
    'J': {'C':5, 'L':6},
    'K': {'L':4, 'I':5},
    'L': {'K':4, 'J':6},
}

heuristic = {
    'A': 15,
    'B': 7,
    'C': 6,
    'D': 14,
    'E': 15,
    'F': 7,
    'G': 8,
    'H': 5,
    'I': 5,
    'J': 3,
    'K': 0,
    'L': 4
}

class Flights2(Problem):

    def __init__(self, initial, destination, routes, heuristic):
        self.initial = initial
        self.destination = destination
        self.routes = routes
        self.h = heuristic

    def check_goal(self, possible_goal):
        return possible_goal == self.destination

    def show_transition(self, state, new_state):
        return f"De {state} para {new_state}"

    def next_states(self, state):
        if state not in self.routes.keys():
            return [k for k in self.routes.keys() if state in self.routes[k]]
        return list(self.routes[state].keys()) + [k for k in self.routes.keys() if state in self.routes[k]]

    def transition_cost(self, fromSt, toSt):
        return self.routes[fromSt][toSt]

    def heuristic(self, _, state):
        return self.h[state]


if __name__ == '__main__':
    a = Flights2('A','K', routes, heuristic)
    Runner.run_greedy_bf(a)
    Runner.run_a_star(a)