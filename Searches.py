from typing import TypeVar, Callable, List, Tuple
from Queue import Queue
from Node import Node

T = TypeVar('T')

def breadth_first(initial: T, transitions: Callable[T, List[T]], checkGoal: Callable[T, bool]) -> List[T]:
    queue = Queue(elements=[Node(initial, [initial])],
                 idKey=lambda x: x.state,
                 sortingKey=lambda x: 1)
    visited = []

    while queue.elements:
        node = queue.get()
        nodepath = node.path
        node = node.state

        visited.append(node)

        print("------------", node)

        print("Expanding", node)
        print("Queue")
        queue.print_queue()
        print("Visited", visited)
        
        if checkGoal(node):
            print("Goal reached")
            return nodepath

        for derivated_state in transitions(node):
            if derivated_state not in visited:
                queue.put(Node(derivated_state, nodepath + [derivated_state]))

    return []

def depth_first(initial: T, transitions: Callable[T, List[T]], checkGoal: Callable[[T], bool]) -> List[T]:
    visited = []

    def search(state):
        if checkGoal(state):
            return []

        visited.append(state)

        for derivated_state in transitions(state):
            if derivated_state not in visited:
                if checkGoal(derivated_state):
                    return [state, derivated_state]
                else:
                    result = search(derivated_state)
                    if result:
                        return [state] + result

        return []

    return search(initial)

def greedy_bf(initial: T, 
                    transitions: Callable[T, List[T]],
                    checkGoal: Callable[T, bool],
                    heuristic: Callable[[T, T], float],
                    ) -> List[T]:
    visited = []
    queue = Queue([Node(state=initial, path=[initial], heuristic=0)],
                  sortingKey=lambda x: x.f,
                  idKey=lambda x: x.state)

    while queue.elements:
        nd = queue.get()
        state = nd.state
        path = nd.path

        if checkGoal(state):
            print("Expanding", state, "Goal reached")
            return path

        visited.append(state)

        new_states_ = list(filter(lambda x: x not in visited, transitions(state)))
        new_states = list(map(lambda s: Node(s, path=path+[s], heuristic=heuristic(state, s)), new_states_))

        queue.put_s(new_states)
        
        print("----------------")
        print("Expanding", state, new_states_)
        queue.print_queue()
        

    return []

def a_star(initial: T,
           transitions: Callable[[T], List[T]],
           check_goal: Callable[[T], bool],
           h: Callable[[T, T], float],
           g: Callable[[T, T], float]) -> List[T]:

    queue = Queue([Node(initial, path=[initial], heuristic=h(initial,initial), path_cost=0)],
                    sortingKey=lambda x: x.f)

    while queue.elements:
        nd = queue.get()
        state = nd.state
        path = nd.path

        path_cost = nd.path_cost

        if check_goal(state):
            print("Expanding", state, "Goal reached")
            return path


        new_states_ = list(transitions(state))
        new_states = list(map(lambda s: Node(s, path=path+[s],
                            heuristic=h(state, s), 
                            path_cost=path_cost+g(state, s)), new_states_))

        queue.put_s(new_states)

        print("----------------")
        print("Expanding", state, new_states_)
        queue.print_queue()


if __name__ == '__main__':
    def tr(a, b):
        match (a,b):
            case ("a","b"):
                return 6
            case ("c","b"):
                return 3
            case ("a","c"):
                return 2
            case ("c","g"):
                return 15
            case ("b","g"):
                return 7
            case _:
                return tr(b,a)
    
    def h(a):
        match a:
            case "a":
                return 10
            case "b":
                return 2
            case "c":
                return 7
            case "g":
                return 0

    def trs(a):
        match a:
            case "a":
                return ["b","c"]
            case "b":
                return ["g","c","a"]
            case "c":
                return ["g","b","a"]
            case "g":
                return ["b","c"]

    a = a_star("a", trs, lambda x: x == "g", lambda s,x: h(x), tr)
    print(a)