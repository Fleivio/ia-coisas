from Runner import Runner
from Problem import Problem

class Puzzle(Problem):
    def __init__(self, initial, goal=[[1,2,3], [8,' ',4], [7,6,5]]):
        self.initial = initial
        self.goal = goal

    def show_state(self, st):
        s = ""
        for i in st:
            s += str(i) + "\n"
        return s

    def show_transition(self, state, new_state):
        return f"Moved from \n{self.show_state(state)} to\n{self.show_state(new_state)}"

    def next_states(self, state):
        def swap(ls, ms, state):
            (i,j) = ls
            (k,l) = ms
            state[i][j], state[k][l] = state[k][l], state[i][j]
            return state

        nexts = []
        for l in range(len(self.initial)):
            for c in range(len(self.initial[0])):
                if l > 0 and state[l-1][c] == ' ':
                    #can move up
                    nexts.append(swap((l,c), (l-1,c), [row[:] for row in state.copy()]))
                if l < len(self.initial) - 1 and state[l+1][c] == ' ':
                    #can move down
                    nexts.append(swap((l,c), (l+1,c), [row[:] for row in state.copy()]))
                if c > 0 and state[l][c-1] == ' ':
                    #can move left
                    nexts.append(swap((l,c), (l,c-1), [row[:] for row in state.copy()]))
                if c < len(self.initial[l]) - 1 and state[l][c+1] == ' ':
                    #can move right
                    nexts.append(swap((l,c), (l,c+1), [row[:] for row in state.copy()]))

        return nexts

    def heuristic(self, _, state):
        
        def find_value_position(v):
            for l in range(len(self.goal)):
                for c in range(len(self.goal[l])):
                    if self.goal[l][c] == v:
                        return (l,c)
            return (0,0)

        distances = []
        for l in range(len(self.goal)):
            for c in range(len(self.goal[l])):
                (i,j) = find_value_position(state[l][c])
                distances.append(abs(i-l) + abs(j-c))
        return sum(distances)

    def check_goal(self, state):
        return state == self.goal

if __name__ == "__main__":
        
    a = Puzzle([[1,2,3],
                [' ',6,4],
                [8,7,5]])
    
    #Runner.run_breadth_first(a)
    Runner.run_a_star(a)
