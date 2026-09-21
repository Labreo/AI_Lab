def create_graph():
    graph = {}
    while True:
        node = input("Enter node (or 'done' to finish): ")
        if node == 'done':
            break
        sub_nodes = {}
        while True:
            sub_node = input(f"Enter connection from node {node} (or 'done' to finish): ")
            if sub_node == 'done':
                break
            hValue = int(input(f"Enter the Heuristic value for connection for {sub_node}: "))
            sub_nodes[sub_node] = hValue
        graph[node] = sub_nodes
    return graph


start_node = input("Enter the start node: ")
start_heuristic = int(input("Enter the heuristic value for the start node: "))
goal = input("Enter the goal node: ").split()
start = {start_node: start_heuristic}
graph = create_graph()


OPEN = {}
CLOSED = {}
# goal = 'L'

def move_gen(graph, current):
    for key, val in graph.items():
        if key == current:
            return val

def goal_test(current,goal):
    return goal and current in goal

def best_first_search(graph, current, OPEN, CLOSED,goal):
    candidates = {}
    for key, val in graph.items():
        if key == current:
            candidates = val
            break

    OPEN.update(candidates)
    CLOSED[current] = True
    del OPEN[current]

    if not OPEN:
        print("Goal not found, No more nodes to expand.")
        return "failure"

    current = min(OPEN.keys(), key=(lambda k: OPEN[k]))

    if goal_test(current,goal):
        print('GOAL NODE IS:', current, '\n')
        print('TRAVERSAL ORDER IS:')
        for v in CLOSED:
            print('-', v, '-')
        print('-', current)
        return "success"
    else:
        best_first_search(graph, current, OPEN, CLOSED,goal)

# start = {'S': 10}
for k, v in start.items():
    current = k
    if goal_test(current,goal):
        print('Goal found at Start state')
        print(current)
    else:
        CLOSED[current] = True
        candidates = move_gen(graph, current)
        OPEN.update(candidates)
        current = min(OPEN.keys(), key=(lambda k: OPEN[k]))
        best_first_search(graph, current, OPEN, CLOSED,goal)
