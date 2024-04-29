import searches
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
    def __init__(self, origin, destination, routes):
        self.origin = origin
        self.destination = destination
        self.routes = routes

    def operators(self):
        pass
    
    def check_valid_transition(self, state, new_state):
        pass
    
    def check_goal(self, state):
        return state == self.destination

    def show_transition(self, state, new_state):
        for r in self.routes:
            if self.routes[r][0] == state and self.routes[r][1] == new_state:
                return str(r) + ": " + str(state) + ' ->> ' + str(new_state)

    def next_states(self, state):
        return [self.routes[r][1] for r in self.routes if self.routes[r][0] == state]

    def run_flights(self, runner):
        return runner(self.origin, self.next_states, lambda x: x == self.destination)

if __name__ == '__main__':
    a = Flights('A','J', routes)

    print("Busca em Profundidade:")
    print("----------------------")

    path = a.run_flights(searches.depth_first)
    path = zip(path, path[1:])
    for (i,j) in path:
        print(a.show_transition(i,j))
    
    print("Busca em Largura:")
    print("----------------------")

    path = a.run_flights(searches.breadth_first)
    path = zip(path, path[1:])
    for (i,j) in path:
        print(a.show_transition(i,j))


    