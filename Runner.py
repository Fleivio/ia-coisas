from Problem import Problem
from Searches import a_star, breadth_first, depth_first, greedy_bf, greedy_acc

class Runner():
    def run_a_star(a : Problem):
        print("-------------------------------------")
        print("-------------Running A*--------------")
        print("-------------------------------------")
        path = a_star(a.initial, a.next_states, a.check_goal, a.heuristic, a.transition_cost)
        Runner.print_result(a, path)

    def run_breadth_first(a : Problem):
        print("-------------------------------------")
        print("--------Running Breadth First--------")
        print("-------------------------------------")
        path = breadth_first(a.initial, a.next_states, a.check_goal)
        Runner.print_result(a, path)

    def run_greedy_acc(a : Problem):
        print("-------------------------------------")
        print("-----Running Greddy Acc Heuristic-----")
        print("-------------------------------------")
        path = greedy_acc(a.initial, a.next_states, a.check_goal, a.heuristic)
        Runner.print_result(a, path)

    def run_depth_first(a : Problem):
        print("-------------------------------------")
        print("---------Running Depth First---------")
        print("-------------------------------------")
        path = depth_first(a.initial, a.next_states, a.check_goal)
        Runner.print_result(a, path)

    def run_greedy_bf(a : Problem):
        print("-------------------------------------")
        print("------Running Greedy Best First------")
        print("-------------------------------------")
        path = greedy_bf(a.initial, a.next_states, a.check_goal, a.heuristic)
        Runner.print_result(a, path)

    def print_result(a : Problem, result):
        print("-----------")
        print("Solution: ")
        a.show_transitions_and_cost(result)