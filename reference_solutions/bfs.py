def goal_test(S, goal_states):
    return S in goal_states


def move_gen(node):
    return graph[node]


def breadth_first_search(start_state, goal_states, graph):
    open_list = [start_state]
    close_list = [[start_state, None]]
    goal_nodes = []
    while open_list:
        head_node = open_list.pop(0)
        child_list = move_gen(head_node)
        for child in child_list:
            if child not in open_list and child not in (item[0] for item in close_list):
                open_list.append(child)
                close_list.append([child, head_node])
                if goal_test(child, goal_states):
                    goal_nodes.append(child)
                    return close_list, goal_nodes
    return close_list, goal_nodes


num_nodes = int(input("Enter the number of nodes: "))
graph = {}
for i in range(num_nodes):
    node = input(f"Enter node {i + 1}: ")
    children = input(f"Enter children of node {node}: ").split()
    graph[node] = children

start_state = input("Enter the start state: ")
goal_states = input("Enter the goal state(s) separated by space: ").split()

if start_state in goal_states:
    print("Start node is the same as the goal node.")
    print("Path:", start_state)
    exit()

result, goal_nodes = breadth_first_search(start_state, goal_states, graph)

print("BFS Traversal:")
for item in result:
    print(item[0], end=" ")
print("\nPath:")
if goal_nodes:
    for goal_node in goal_nodes:
        current_node = goal_node
        path = []
        while current_node != start_state:
            for item in result:
                if item[0] == current_node:
                    path.append(current_node)
                    current_node = item[1]
                    break
            path.append(start_state)
            path.reverse()
            print("-->".join(path))

else:
    print("No path found from start to any of the goal nodes.")



