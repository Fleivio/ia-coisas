import searches
from Problem import Problem

routes = {
    'A': {'B':7, 'C':9, 'D':3},
    'B': {'F':3, 'I':4},
    'C': {'J':5},
    'D': {'E':1},
    'F': {'G':2},
    'G': {'H':3},
    'I': {'K':5},
    'J': {'L':6},
    'K': {'I':5, 'L':4},
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
        self.heuristic = heuristic

    def operators(self):
        pass
    
    def check_valid_transition(self, state, new_state):
        pass

    def check_goal(self, state):
        return state == self.destination

    def next_states(self, state):
        if state not in self.routes.keys():
            return [k for k in self.routes.keys() if state in self.routes[k]]
        return list(self.routes[state].keys()) + [k for k in self.routes.keys() if state in self.routes[k]]

    def show_transition(self, state, new_state):
        for r in self.routes[state]:
            if r == new_state:
                return str(state) + ' ->> ' + str(new_state)

    def g(self, fromSt, toSt):
        if fromSt in self.routes.keys() and toSt in self.routes[fromSt]:
            return self.routes[fromSt][toSt]
        else:
            return self.routes[toSt][fromSt]

    def h(self, state):
        return self.heuristic[state]

    def run_flights(self):
        return searches.greedy_bf(self.initial, self.next_states, self.check_goal, lambda s,x: self.h(x))

a = Flights2('A','K', routes, heuristic)
print(a.run_flights())