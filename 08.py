import searches

class Puzzle:
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    def show_state(st):
        for i in st:
            print(i)
        print()

    def gen_operators(self, state):
        def swap(ls, ms, state):
            (i,j) = ls
            (k,l) = ms
            state[i][j], state[k][l] = state[k][l], state[i][j]
            return state

        operators = []
        for l in range(len(self.initial)):
            for c in range(len(self.initial[0])):
                if l > 0 and state[l-1][c] == ' ':
                    #can move up
                    operators.append(lambda s, l=l, c=c: swap((l,c), (l-1,c), [row[:] for row in s]))
                if l < len(self.initial) - 1 and state[l+1][c] == ' ':
                    #can move down
                    operators.append(lambda s, l=l, c=c: swap((l,c), (l+1,c), [row[:] for row in s]))
                if c > 0 and state[l][c-1] == ' ':
                    #can move left
                    operators.append(lambda s, l=l, c=c: swap((l,c), (l,c-1), [row[:] for row in s]))
                if c < len(self.initial[l]) - 1 and state[l][c+1] == ' ':
                    #can move right
                    operators.append(lambda s, l=l, c=c: swap((l,c), (l,c+1), [row[:] for row in s]))

        return operators

    def get_sum_distances(self, state):
        
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

    def next_states(self, state):
        return list(map(lambda op: op(state), self.gen_operators(state)))

    def run_puzzle_a_star(self):
        return searches.a_star(self.initial, 
                                self.next_states, 
                                lambda x: x==self.goal,
                                lambda s,x: self.get_sum_distances(x),
                                lambda s,x: 1)

    def run_puzzle_greedy(self):
        return searches.greedy_bf(self.initial, 
                                self.next_states, 
                                lambda x: x == self.goal,
                                lambda s,x: 1)

a = Puzzle([[1,2,3],
            [4,5,8],
            [7,' ',6]], [[1,2,3],[4,5,6],[7,8,' ']])

'''
for i in a.next_states([[1,2,3],[' ',6,4],[8,7,5]]):
    Puzzle.show_state(i)
'''

b = a.run_puzzle_a_star()
print("Intermediary states:")
for i in b:
    Puzzle.show_state(i)