# Implement A star Algorithm for any game search problem.
import heapq

class Node:
    def __init__(self, state, parent=None, action=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = heuristic
        
    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def astar(initial_state, goal_test, actions, successor, heuristic):
    frontier = []
    heapq.heappush(frontier, Node(initial_state, None, None, 0, heuristic(initial_state)))
    explored = set()

    while frontier:
        node = heapq.heappop(frontier)
        if goal_test(node.state):
            return node

        explored.add(node.state)

        for action in actions(node.state):
            child_state = successor(node.state, action)
            if child_state not in explored:
                child_node = Node(child_state, node, action, node.cost + 1, heuristic(child_state))
                heapq.heappush(frontier, child_node)

    return None

# Example heuristic function (Manhattan distance)
def manhattan_distance(state):
    goal_state = (3, 3)  # Example goal state
    return abs(state[0] - goal_state[0]) + abs(state[1] - goal_state[1])

# Example usage
def goal_test(state):
    return state == (3, 3)  # Example goal state

def actions(state):
    return [(1, 0), (0, 1)]  # Example actions (right and down)

def successor(state, action):
    return (state[0] + action[0], state[1] + action[1])

initial_state = (1, 1)  # Example initial state

result_node = astar(initial_state, goal_test, actions, successor, manhattan_distance)

if result_node:
    path = []
    while result_node.parent:
        path.append(result_node.action)
        result_node = result_node.parent
    path.reverse()
    print("Solution Path:", path)
else:
    print("No solution found.")
