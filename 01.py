from Runner import Runner
from Problem import Problem

class Cannibals(Problem):
    
    def __init__(self, size=3, boat_size=2):
        self.initial = (size, size, 1)
        self.goal = (0,0,0)
        self.size = size
        self.boat_size = boat_size

    def check_goal(self, possible_goal):
        return possible_goal == self.goal

    def check_valid_transition(self, _, state):
        (m, c, _) = state

        size = self.size

        if c < 0 or m < 0 or c > size or m > size:
            return False
        if m > 0 and c > m:
            return False
        if size - m > 0 and size - c > size - m:
            return False
        return True

    def operators(self):

        def check_valid_boat(i,j):
            return i+j <= self.boat_size and i+j>0

        def shift_state(i,j,s):
            (m, c, b) = s
            delta = -1 if b == 1 else 1

            return (m + i*delta, c + j*delta, 0 if b == 1 else 1)

        operators = []

        for i in range(0, self.boat_size + 1):
            for j in range(0, self.boat_size + 1):
                if check_valid_boat(i,j):
                    operators.append(lambda s, i=i, j=j: shift_state(i,j,s))
        return operators

    def show_transition(self, state, new_state):
        (m, c, b) = state
        (m2, c2, _) = new_state

        return (str(state) + "--> Levou " + str(abs(m - m2)) +
                " missionarios e " + str(abs(c - c2)) + " canibais para a " +
                ("esquerda" if b == 1 else "direita") + " ->> " + str(new_state))

    def run_canibais(self):
        return searches.breadth_first(self.initial, self.next_states, lambda x: x == self.goal)

if __name__ == '__main__':
    problem = Cannibals()
    Runner.run_breadth_first(problem)
