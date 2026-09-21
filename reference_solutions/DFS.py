def movegen(node, graph):
    return graph[node]

def goal_test(child, goal_state):
    return child in goal_state

def depth_first_search(graph, start_state, goal_state, num_states):
    open_list = [start_state]
    close_list = [[start_state, None]]
    goal_nodes = []
    while open_list:
        head_node = open_list.pop()  # Change pop(0) to pop() for DFS
        child_list = movegen(head_node, graph)
        for child in child_list:
            if child not in open_list and child not in (item[0] for item in close_list):
                open_list.append(child)
                close_list.append([child, head_node])
                if goal_test(child, goal_state):
                    goal_nodes.append(child)
                    return close_list, goal_nodes

    return close_list, goal_nodes

num_states = int(input("Enter the number of states: "))
graph = {}
for _ in range(num_states):
    node = input("Enter the node: ")
    children = input(f"Enter the children for {node}: ").split()
    graph[node] = children

start_state = input("Enter the start state: ")
goal_state = input("Enter goal state(s): ").split()

if start_state in goal_state:
    print("start state is goal state")
    print(f"Path : {start_state}")

results, goal_nodes = depth_first_search(graph, start_state, goal_state, num_states)
print("DFS Traversal")
for item in results:
    print(item[0], end=" ")
print("\nPath")

if goal_nodes:
    for goal in goal_nodes:
        path = []
        current_state = goal
        while current_state is not None:
            path.append(current_state)
            for item in results:
                if item[0] == current_state:
                    current_state = item[1]
                    break
        path.reverse()
        print('-->'.join(path))
