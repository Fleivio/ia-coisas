from typing import TypeVar, Callable, List, Tuple

T = TypeVar('T')
S = TypeVar('S')

def breadth_first(initial: T, transitions: Callable[[T], List[Tuple[T, S]]], checkGoal: Callable[[T], bool]) -> List[S]:
    queue = [(initial, [])]
    visited = []

    while queue:
        (node, nodepath) = queue.pop(0)
            
        visited.append(node)
        
        if checkGoal(node):
            return nodepath

        for derivated_state, action in transitions(node):
            if derivated_state not in visited:
                queue.append((derivated_state, nodepath + [action]))

    return queue

if __name__ == '__main__':
    tr = lambda x: [(x+1, "add 1"), (x-1, "sub 1")]
    init = 2
    final = -10

    print (breadth_first(init, tr, lambda x: x == final))