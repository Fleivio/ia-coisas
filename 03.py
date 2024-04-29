from Runner import Runner
from Problem import Problem

class Farm(Problem):

    def __init__(self, initial=[0,0,0,0], goal=[1,1,1,1], restrictions=[(1,2),(2,3)], names=['_', 'Lobo', 'Ovelha', 'Repolho']):
        self.initial = initial
        self.goal = goal
        self.restrictions = restrictions
        self.names = names
        self.size = len(initial)
    
    def check_goal(self, state):
        return state == self.goal

    def check_restrictions(self, state):
        for (r,s) in self.restrictions:
            if state[r] == state[s] and state[0] != state[r]:
                return False
        return True

    def get_diff(self, state, new_state):
        for i in range(self.size):
            if state[i] != new_state[i]:
                return i

    def show_transition(self, state, new_state):
        if state[1:] == new_state[1:]:
            return str(state) + ' ->> Fazendeiro atravessa sozinho ->> ' + str(new_state)

        diff = self.get_diff(state[1:], new_state[1:]) + 1

        return (str(state) + " ->> Fazendeiro atravessa com " + self.names[diff] + " ->> " + str(new_state))

    def operators(self):
        def farmer_cross(s):
            return cross_at(0, s.copy())

        def cross_at(i, s):
            s[i] = 1 if s[i] == 0 else 0
            return s

        return [farmer_cross] + [lambda s, i=i: farmer_cross(cross_at(i, s.copy())) for i in range(1,self.size)]

    def check_valid_transition(self, state, new_state):
        # Se o lobo pode comer a ovelha
        if not self.check_restrictions(new_state):
            return False

        # Se o fazendeiro se moveu sozinho
        if state[1:] == new_state[1:]:
            return True

            
        diff = self.get_diff(state[1:], new_state[1:]) + 1
        # Se o fazendeiro moveu o animal do lado certo
        if state[0] == state[diff]:
            return True
        return False

if __name__ == '__main__':
    a = Farm()
    Runner.run_breadth_first(a)