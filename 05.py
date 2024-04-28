
routes = {
    1: ('A','B',1),
    2: ('A','C',9),
    3: ('D','A',4),
    4: ('B','C',7),
    5: ('B','E',6),
    6: ('B','F',1),
    7: ('C','F',7),
    8: ('D','F',4),
    9: ('D','G',5),
    10: ('E','H',9),
    11: ('F','H',4),
    12: ('G','H',1)
}

class Flights2():

    def __init__(self, initial, destination, routes):
        self.initial = initial
        self.destitination = destination
        self.routes = routes

    def get_routes(self, state):
        return ([(self.routes[r][1], r) for r in self.routes if self.routes[r][0] == state]
                + [(self.routes[r][0], r) for r in self.routes if self.routes[r][1] == state])

    def get_routes_cost(self, state):
        return ([(self.routes[r][1], r, self.routes[r][2]) for r in self.routes if self.routes[r][0] == state]
                + [(self.routes[r][0], r, self.routes[r][2]) for r in self.routes if self.routes[r][1] == state])

a = Flights2('A','H', routes)
print(a.get_routes('H'))
print("---------")
print(a.get_routes_cost('H'))