from Runner import Runner
from Problem import Problem

routes = {
    1: ('A','B'),
    2: ('A','B'),
    3: ('A','D'),
    4: ('B','E'), 
    5: ('B','F'), 
    6: ('C','G'),
    7: ('C','H'),
    8: ('C','I'),
    9: ('D','J'),
    10: ('E','K'),
    11: ('E','L'),
    12: ('G','M'),
    13: ('J','N'),
    14: ('J','O'),
    15: ('K','F'),
    16: ('L','H'),
    17: ('M','D'),
    18: ('O','A'),
    19: ('N','B')
}

class Flights(Problem):
    def __init__(self, initial, destination, routes):
        self.initial = initial
        self.destination = destination
        self.routes = routes

    def show_transition(self, state, new_state):
        return f"De {state} para {new_state}"

    def check_goal(self, state):
        return state == self.destination

    def next_states(self, state):
        return [self.routes[r][1] for r in self.routes if self.routes[r][0] == state]

    def run_flights(self, runner):
        return runner(self.initial, self.next_states, lambda x: x == self.destination)

if __name__ == '__main__':
    print("QUESTÃO 4: VOOS\n")
    a = Flights('A','J', routes)

    Runner.run_depth_first(a)

    Runner.run_breadth_first(a)


    