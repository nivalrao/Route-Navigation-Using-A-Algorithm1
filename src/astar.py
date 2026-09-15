import heapq
import math
import sys
import os

# Allow Python to find the dataset folder
sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from dataset.map_data import graph, coordinates


# Calculate straight-line distance
def heuristic(node, goal):
    x1, y1 = coordinates[node]
    x2, y2 = coordinates[goal]

    return math.sqrt(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2
    )


# A* Search Algorithm
def a_star(start, goal):

    # Priority queue
    open_list = []

    # g(n) = actual cost from start
    g_cost = {
        node: float("inf")
        for node in graph
    }

    g_cost[start] = 0

    # Store previous node
    parent = {}

    # Add starting node
    h = heuristic(start, goal)
    f = g_cost[start] + h

    heapq.heappush(open_list, (f, start))

    visited = set()

    print("\nA* SEARCH PROCESS")
    print("-" * 55)
    print(f"{'Node':<10}{'g(n)':<12}{'h(n)':<12}{'f(n)':<12}")
    print("-" * 55)

    while open_list:

        # Select node with smallest f(n)
        current_f, current = heapq.heappop(open_list)

        if current in visited:
            continue

        visited.add(current)

        # Calculate g, h and f
        g = g_cost[current]
        h = heuristic(current, goal)
        f = g + h

        print(
            f"{current:<10}"
            f"{g:<12.2f}"
            f"{h:<12.2f}"
            f"{f:<12.2f}"
        )

        # Destination reached
        if current == goal:
            break

        # Check all neighbours
        for neighbour, weight in graph[current].items():

            new_g = g_cost[current] + weight

            # Found a better route
            if new_g < g_cost[neighbour]:

                g_cost[neighbour] = new_g
                parent[neighbour] = current

                h = heuristic(neighbour, goal)
                f = new_g + h

                heapq.heappush(
                    open_list,
                    (f, neighbour)
                )

    # Check whether destination was reached
    if goal not in parent and goal != start:
        print("\nNo route found.")
        return

    # Reconstruct path
    path = []
    current = goal

    while current != start:
        path.append(current)
        current = parent[current]

    path.append(start)
    path.reverse()

    # Display result
    print("-" * 55)
    print("\nRESULT")
    print("-" * 55)

    print("Optimal Path:")
    print(" -> ".join(path))

    print(f"\nTotal Cost: {g_cost[goal]:.2f}")

    print("\nHeuristic Used:")
    print("Straight-line distance")

    print("\nFormula:")
    print("f(n) = g(n) + h(n)")

    print("\nWhy is the heuristic admissible?")
    print(
        "Straight-line distance never overestimates "
        "the actual shortest travel distance."
    )


# Main program
if __name__ == "__main__":

    print("=" * 55)
    print("       ROUTE NAVIGATION USING A* ALGORITHM")
    print("=" * 55)

    start = "A"
    goal = "H"

    print(f"\nStart Location : {start}")
    print(f"Destination    : {goal}")

    a_star(start, goal)