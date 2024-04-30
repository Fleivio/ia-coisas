from Runner import Runner
from Problem import Problem

routes = {
    'A': {'B':1, 'C':9, 'D':4},
    'B': {'A':1, 'C':7, 'E':6, 'F':1},
    'C': {'A':9, 'B':7, 'F':7},
    'D': {'A':4, 'F':4, 'G':5},
    'E': {'B':6, 'H':9},
    'F': {'B':1, 'C':7, 'D':4, 'H':4},
    'G': {'D':5, 'H':1},
    'H': {'E':9, 'F':4, 'G':1}
}

class Flights2(Problem):

    def __init__(self, initial, destination, routes):
        self.initial = initial
        self.destination = destination
        self.routes = routes
    
    def check_goal(self, state):
        return state == self.destination

    def show_transition(self, state, new_state):
        return f"De {state} para {new_state}"    

    def heuristic(self, fromSt, toSt):
        return self.routes[fromSt][toSt]
        
    def transition_cost(self, fromSt, toSt):
        return self.heuristic(fromSt, toSt)

    def next_states(self, state):
        return list(self.routes[state].keys())

if __name__ == '__main__':
    print("QUESTÃO 5: VOOS\n")
    a = Flights2('A','H', routes)
    Runner.run_greedy_acc(a)
    


