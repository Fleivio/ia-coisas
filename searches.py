from typing import TypeVar, Callable, List, Tuple

T = TypeVar('T')

def breadth_first(initial: T, transitions: Callable[T, List[Tuple[T]]], checkGoal: Callable[T, bool]) -> List[T]:
    queue = [(initial, [initial])]
    visited = []

    while queue:
        (node, nodepath) = queue.pop(0)
            
        visited.append(node)
        
        if checkGoal(node):
            return nodepath

        for derivated_state in transitions(node):
            if derivated_state not in visited:
                queue.append((derivated_state, nodepath + [derivated_state]))

    return queue


def depth_first(initial: T, transitions: Callable[T, List[Tuple[T]]], checkGoal: Callable[[T], bool]) -> List[T]:
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
'''
def greedy_search(initial: T, 
                    transitions: Callable[T, List[Tuple[T, S]]],
                    checkGoal: Callable[T, bool],
                    heuristic: Callable[T, int]
                    ) -> List[S]:
    visited = []

if __name__ == '__main__':

    def tr(s):
        match s:
            case "o":
                return ["h","v","m"]
            case "h":
                return ["e","l"]
            case "v":
                return ["t","x"]
            case "h":
                return ["h","i"]
            case "v":
                return ["u","w"]
            case "e":
                return ["d","f"]
            case "l":
                return ["k","m"]
            case _:
                return []

    init = "o"
    final = "m"

    print (breadth_first(init, lambda x: list(map(lambda y: (y,y), tr(x))), lambda x: x == final))
    print (depth_first(init, lambda x: list(map(lambda y: (y,y), tr(x))), lambda x: x == final))
'''