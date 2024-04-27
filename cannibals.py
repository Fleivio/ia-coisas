import breadth_first


class Cannibals():
    
    def __init__(self, size=3, boat_size=2):
        self.initial = (size, size, 1)
        self.goal = (0,0,0)
        self.size = size
        self.boat_size = boat_size

    def is_valid(self, state):
        (miss, can, boat) = state
        size = self.size

        if can < 0 or miss < 0 or can > size or miss > size:
            return False
        if miss > 0 and can > miss:
            return False
        if size - miss > 0 and size - can > size - miss:
            return False
        return True

    def gen_operators(self):

        def check_valid_boat(k):
            (i,j) = k
            return i+j <= self.boat_size and i+j>0

        return filter (check_valid_boat,
                [(j,i)  
                    for j in range(0, self.boat_size + 1) 
                    for i in range(0, self.boat_size + 1)]
                )

    def gen_action(self, state):
        (miss, can, boat) = state
        delta = -1 if boat == 1 else 1


        def show_state(new_state):
            return (new_state, 
                    str(state) + "--> Levou " + str(miss - new_state[0]*delta) +
                    " missionarios e " + str(can - new_state[1]*delta) + " canibais para a " +
                    ("esquerda" if boat == 1 else "direita") + " ->> " + str(new_state)) 

        def shift_state(k):
            (i,j) = k

            new_state = (miss + i*delta, can + j*delta, 0 if boat == 1 else 1)

            return (new_state,
                    str(state) + " --> Levou " + str(i) + " missionarios e " + str(j) + 
                    " canibais para a " + ("esquerda" if boat == 1 else "direita") + " --> " + str(new_state))
        
        possible_next = list(map (shift_state, self.gen_operators()))
        filtered_next = list(filter(lambda k: self.is_valid(k[0]), possible_next))

        return filtered_next

    def run_canibais(self):
        return breadth_first.breadth_first(self.initial, self.gen_action, lambda x: x == self.goal)

def canibal_10_4():
    cn = Cannibals(10, 4)

    for i in cn.run_canibais():
        print(i)

if __name__ == '__main__':
    classical = Cannibals()

    for i in classical.run_canibais():
        print(i)
