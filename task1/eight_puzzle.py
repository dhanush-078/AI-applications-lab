import heapq
goal_state = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8)
)
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def is_valid_move(x, y):
    return 0 <= x < 3 and 0 <= y < 3
def calculate_heuristic(state):
    total_distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                target_row, target_col = divmod(state[i][j] - 1, 3)
                total_distance += abs(i - target_row) + abs(j - target_col)
    return total_distance
def get_initial_state():
    initial_state = []
    print("Enter the initial state of the 8-puzzle (3x3 grid, use 0 to represent the empty space):")
    for i in range(3):
        row = input(f"Enter row {i + 1} (3 numbers separated by spaces): ").split()
        row = [int(x) for x in row]
        initial_state.append(tuple(row))
    return tuple(initial_state)
def solve_8_puzzle(initial_state):
    open_set = [(0, initial_state)]
    closed_set = set()
    parent_map = {}
    while open_set:
        priority, current_state = heapq.heappop(open_set)

        if current_state == goal_state:
            path = []
            while current_state != initial_state:
                path.append(current_state)
                current_state = parent_map[current_state]
            path.append(initial_state)
            path.reverse()
            for step, state in enumerate(path):
                print(f"Step {step}:")
                for row in state:
                    print(row)
                print()
            return
        closed_set.add(current_state)
        for dx, dy in moves:
            i, j = None, None
            for x in range(3):
                for y in range(3):
                    if current_state[x][y] == 0:
                        i, j = x, y
                        break
                if i is not None:
                    break
            new_i, new_j = i + dx, j + dy
            if is_valid_move(new_i, new_j):
                new_state = [list(row) for row in current_state]
                new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
                new_state = tuple(tuple(row) for row in new_state)
                if new_state not in closed_set:
                    g_cost = priority + 1
                    h_cost = calculate_heuristic(new_state)
                    f_cost = g_cost + h_cost
                    heapq.heappush(open_set, (f_cost, new_state))
                    parent_map[new_state] = current_state
    print("No solution found.")
initial_state = get_initial_state()
solve_8_puzzle(initial_state)
