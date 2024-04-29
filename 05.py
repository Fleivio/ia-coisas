import searches
from Problem import Problem

routes = {
    'A': {'B':1, 'C':9, 'D':4},
    'B': {'C':7, 'E':6},
    'C': {'F':7},
    'D': {'F':4, 'G':5},
    'E': {'H':9},
    'F': {'H':4},
    'G': {'H':1}
}

class Flights2(Problem):

    def __init__(self, initial, destination, routes):
        self.initial = initial
        self.destination = destination
        self.routes = routes

    def operators(self):
        pass
    
    def check_valid_transition(self, state, new_state):
        pass
    
    def check_goal(self, state):
        return state == self.destination

    def show_transition(self, state, new_state):
        for r in self.routes[state]:
            if r == new_state:
                return str(state) + ' ->> ' + str(new_state)

    def h(self, fromSt, toSt):
        if fromSt in self.routes.keys() and toSt in self.routes[fromSt]:
            return self.routes[fromSt][toSt]
        else:
            return self.routes[toSt][fromSt]    
            
    def next_states(self, state):
        return list(self.routes[state].keys()) + [k for k in self.routes.keys() if state in self.routes[k]]

    def run_flights(self):
        return searches.greedy_bf(self.initial, self.next_states, self.check_goal, self.h)

a = Flights2('A','H', routes)
print(a.run_flights())