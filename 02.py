from Runner import Runner
from Problem import Problem

class Jars(Problem):
        
    def __init__(self, sizes=[3,4], goal_check=lambda x: x[1] == 2):
        self.initial = [0] * len(sizes)
        self.goal = goal_check
        self.sizes = sizes

    def check_goal(self, possible_goal):
        return self.goal(possible_goal)

    def show_transition(self, state, new_state):
        diffs = []

        for i in range(len(state)):
            if state[i] != new_state[i]:
                diffs.append(i)

        if len(diffs) == 1:
            if state[diffs[0]] == 0:
                return "Encher jarra " + str(diffs[0]) + " ->> " + str(new_state)
            else:
                return "Esvaziar jarra " + str(diffs[0]) + " ->> " + str(new_state)
        else:
            if state[diffs[1]] > new_state[diffs[1]]:
                return "Transferir de " + str(diffs[1]) + " para " + str(diffs[0]) + " ->> " + str(new_state)
            else:
                return "Transferir de " + str(diffs[0]) + " para " + str(diffs[1]) + " ->> " + str(new_state)

    def operators(self):

        def fill_jar(index, states):
            states[index] = self.sizes[index]
            return states

        def empty_jar(index, states):
            states[index] = 0
            return states

        def transfer(i, j, states):
            ia = states[i]
            ja = states[j]

            states[j] = min(self.sizes[j], ia + ja)
            states[i] = max(0, ia - (self.sizes[j] - ja))

            return states

        operators = []
        for i in range(0, len(self.sizes)):
            operators.append(lambda s, i=i: fill_jar(i, s.copy()))
            operators.append(lambda s, i=i: empty_jar(i, s.copy()))
            for j in range(len(self.sizes)):
                if i != j:
                    operators.append(lambda s, i=i, j=j: transfer(i, j, s.copy()))
        return operators

    def check_valid_transition(self, _, state):
        return True


if __name__ == '__main__':
    jars = Jars()
    
    Runner.run_breadth_first(jars)