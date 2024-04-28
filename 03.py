import searches

class Farm():

    def __init__(self, initial=[0,0,0,0], goal=[1,1,1,1], restrictions=[(1,2),(2,3)], names=['_', 'Lobo', 'Ovelha', 'Repolho']):
        self.initial = initial
        self.goal = goal
        self.restrictions = restrictions
        self.names = names
        self.size = len(initial)

    def is_valid(self, state):
        for (r,s) in self.restrictions:
            if state[r] == state[s] and state[0] != state[r]:
                return False
        return True

    def show_transition(self, state, new_state):
        if state[1:] == new_state[1:]:
            return str(state) + ' ->> Fazendeiro atravessa sozinho ->> ' + str(new_state)

        diff = 0

        for i in range(1, self.size):
            if state[i] != new_state[i]:
                diff = i
                break

        return (str(state) + " ->> Fazendeiro atravessa com " + self.names[diff] + " ->> " + str(new_state))

    def next_states(self, state):

        def farmer_cross(s):
            return cross_at(0, s)

        def cross_at(i, s):
            s[i] = 1 if s[i] == 0 else 0
            return s

        operators = []
        
        if self.is_valid(farmer_cross(state.copy())):
            operators.append(farmer_cross(state.copy()))

        for i in range(1,self.size):
            new_state = cross_at(i, farmer_cross(state.copy()))
            if state[0] == state[i] and self.is_valid(new_state):
                operators.append(new_state)
        return operators

    def run_farm(self):
        return searches.breadth_first(self.initial, self.next_states, lambda x: x==self.goal)


if __name__ == '__main__':
    a = Farm()
    
    path = a.run_farm()
    path = zip(path, path[1:])
    for s in path:
        print(a.show_transition(s[0], s[1]))
