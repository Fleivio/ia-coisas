from Problem import Problem
from Searches import a_star, breadth_first, depth_first, greedy_bf

class Runner():
    def run_a_star(a : Problem):
        print("--------Running A*--------")
        path = a_star(a.initial, a.next_states, a.check_goal, a.h, a.g)
        Runner.print_result(a, path)

    def run_breadth_first(a : Problem):
        print("--------Running Breadth First--------")
        path = breadth_first(a.initial, a.next_states, a.check_goal)
        Runner.print_result(a, path)

    def run_depth_first(a : Problem):
        print("--------Running Depth First--------")
        path = depth_first(a.initial, a.next_states, a.check_goal)
        Runner.print_result(a, path)

    def run_greedy_bf(a : Problem):
        print("--------Running Greedy Best First--------")
        path = greedy_bf(a.initial, a.next_states, a.check_goal, a.h)
        Runner.print_result(a, path)

    def print_result(a : Problem, result):
        print("----------------")
        print("Solution: ")
        a.show_transitions_and_cost(result)