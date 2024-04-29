from Runner import Runner
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
    'K': {'L':4},
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

    def check_goal(self, possible_goal):
        return possible_goal == self.destination

    def show_transition(self, state, new_state):
        return f"De {state} para {new_state}"

    def next_states(self, state):
        if state not in self.routes.keys():
            return [k for k in self.routes.keys() if state in self.routes[k]]
        return list(self.routes[state].keys()) + [k for k in self.routes.keys() if state in self.routes[k]]

    def g(self, fromSt, toSt):
        if fromSt in self.routes.keys() and toSt in self.routes[fromSt]:
            return self.routes[fromSt][toSt]
        else:
            return self.routes[toSt][fromSt]

    def h(self, _, state):
        return self.heuristic[state]

    def run_flights(self):
        return searches.a_star(self.initial, #inicial
                                self.next_states, #gerador de novos nós
                                self.check_goal, #verificador de objetivo
                                self.h,  #heuristica
                                self.g) #custo da rota

if __name__ == '__main__':
    a = Flights2('A','K', routes, heuristic)
    Runner.run_a_star(a)