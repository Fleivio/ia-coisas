from abc import ABC, abstractmethod

class Problem(ABC):

    @abstractmethod
    def operators(self):
        pass
    
    @abstractmethod
    def check_goal(self, possible_goal):
        pass

    @abstractmethod
    def check_valid_transition(self, prev_state, next_state):
        pass

    @abstractmethod
    def show_transition(self, prev_state, next_state):
        pass

    def h(self, prev_state, next_state):
        return 0

    def g(self, prev_state, next_state):
        return 0

    def next_states(self, state):
        possibles = list(map(lambda op: op(state), self.operators()))
        return list( filter(lambda x: self.check_valid_transition(state, x), possibles) )