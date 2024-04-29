
class Problem():

    def operators(self):
        pass
    
    def check_goal(self, possible_goal):
        pass

    def check_valid_transition(self, prev_state, next_state):
        pass

    def show_state(self, state):
        str(state)

    def show_transition(self, prev_state, next_state):
        pass

    def sum_costs(self, state_list):
        ziped = map (lambda x: self.g(x[0], x[1]), list(zip(state_list, state_list[1:])))
        return sum(list(ziped))

    def show_transitions_and_cost(self, path):
        path_ = zip(path, path[1:])
        for (i,j) in path_:
            print(self.show_transition(i,j))
        print("Total Cost:", self.sum_costs(path))

    def h(self, prev_state, next_state):
        return 1

    def g(self, prev_state, next_state):
        return 1

    def next_states(self, state):
        possibles = list(map(lambda op: op(state), self.operators()))
        return list( filter(lambda x: self.check_valid_transition(state, x), possibles) )