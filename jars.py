import breadth_first

class Jars():
        
    def __init__(self, sizes=[3,4], goal_check=lambda x: x[1] == 2):
        self.initial = [0] * len(sizes)
        self.goal = goal_check
        self.sizes = sizes

    def fill_jar(self, index, states):
        states[index] = self.sizes[index]
        return (states, "Encher jarra " + str(index) + " ->> " + str(states))

    def empty_jar(self, index, states):
        states[index] = 0
        return (states, "Esvaziar jarra " + str(index) + " ->> " + str(states))

    def transfer(self, i, j, states):
        ia = states[i]
        ja = states[j]

        states[j] = min(self.sizes[j], ia + ja)
        states[i] = max(0, ia - (self.sizes[j] - ja))

        return (states, "Transferir de " + str(i) + " para " + str(j) + " ->> " + str(states))

    def is_valid(self, state):
        for jar, limit in zip(state, self.sizes):
            if jar < 0 or jar > limit:
                return False
        return True
    
    def gen_operators(self):
        operators = []
        for i in range(0, len(self.sizes)):
            operators.append(lambda s, i=i: self.fill_jar(i, s.copy()))
            operators.append(lambda s, i=i: self.empty_jar(i, s.copy()))
            for j in range(len(self.sizes)):
                if i != j:
                    operators.append(lambda s, i=i, j=j: self.transfer(i, j, s.copy()))
        return operators

    def gen_actions(self, state):
        
        def show_state(state):
            return (state, str(state))
        
        ops = self.gen_operators()

        possible_next = list(map(lambda f: f(state.copy()), ops))
        filtered_next = list(filter(lambda k: self.is_valid(k[0]), possible_next))
        return filtered_next

    def run_jars(self):
        return breadth_first.breadth_first(self.initial, self.gen_actions, self.goal)

if __name__ == '__main__':
    j = Jars()
    
    for i in j.run_jars():
        print(i)