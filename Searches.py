from Queue import Queue
from Node import Node


def breadth_first(initial, transitions, checkGoal):
    queue = Queue(elements=[Node(initial)],
                 idKey=lambda x: x.state,
                 sortingKey=lambda x: 1)
    visited = [initial]

    if checkGoal(initial):
        return [initial]

    while queue.elements:
        node = queue.get()
        state = node.state

        #visited.append(state)

        print("------------")

        print("Expanding", state)

        for child in transitions(state):
            
            if checkGoal(child):
                print("Goal reached", child)
                return node.get_path() + [child]
            if child not in visited:
                visited.append(child)
                queue.put(Node(child, node))

        print("Queue")
        queue.print_queue()
        print("Visited", visited)
    return []

def depth_first(initial, transitions, checkGoal):
    visited = []

    def search(state):
        if state in visited:
            return []
        visited.append(state)

        print("------------")
        print('Expanding', state)
        trs = list(filter(lambda x: x not in visited, transitions(state)))
        print(trs)
        for derivated_state in trs:
            if checkGoal(derivated_state):
                return [state, derivated_state]
            else:
                result = search(derivated_state)
                if result:
                    return [state] + result

        return []

    return search(initial)

def a_star(initial,
           transitions,
           check_goal,
           h,
           g):

    queue = Queue([Node(initial, heuristic=0, path_cost=0)],
                    sortingKey=lambda x: x.f,
                    idKey=lambda x: x.state)

    visited = Queue([], sortingKey=lambda x: x.f, idKey=lambda x: x.state)

    while queue.elements:
        node = queue.get()
        state = node.state

        path_cost = node.path_cost

        if check_goal(state):
            print("Expanding", state, "Goal reached")
            return node.get_path()

        visited.put(node)
        new_states_ = transitions(state)

        for s in new_states_:
            s_node = Node(s, parent=node, heuristic=h(state, s), path_cost=path_cost+g(state, s))
            if visited.has(s):
                if visited.has_better_eq(s_node):
                    continue
                else:
                    _ = visited.get_by_key(s)
                    queue.put(s_node)
            else:
                queue.put(s_node)

        print("----------------")
        print("Expanding", state, new_states_)
        queue.print_queue()

def greedy_bf(initial, transitions, check_goal, h):
    queue = Queue([Node(initial, heuristic=0, path_cost=0)],
                    sortingKey=lambda x: x.f,
                    idKey=lambda x: x.state)

    visited = Queue([], sortingKey=lambda x: x.f, idKey=lambda x: x.state)

    while queue.elements:
        node = queue.get()
        state = node.state


        if check_goal(state):
            print("Expanding", state, "Goal reached")
            return node.get_path()

        visited.put(node)
        new_states_ = transitions(state)

        for s in new_states_:
            s_node = Node(s, parent=node, heuristic=h(state, s))
            if visited.has(s):
                if visited.has_better_eq(s_node):
                    continue
                else:
                    _ = visited.get_by_key(s)
                    queue.put(s_node)
            else:
                queue.put(s_node)

        print("----------------")
        print("Expanding", state, new_states_)
        queue.print_queue()

def test1():
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

if __name__ == '__main__':
    test1()