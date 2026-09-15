import sys
import os
import matplotlib

# Use a non-GUI backend
matplotlib.use("Agg")

import matplotlib.pyplot as plt

# Add the project folder to Python's path
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

sys.path.append(PROJECT_ROOT)

from dataset.map_data import graph, coordinates


# Optimal path obtained from A* algorithm
optimal_path = ["A", "C", "E", "H"]


# Create the figure
plt.figure(figsize=(10, 7))


# ---------------------------------------------------------
# Draw all roads and edge weights
# ---------------------------------------------------------

drawn_edges = set()

for node in graph:

    x1, y1 = coordinates[node]

    for neighbour, weight in graph[node].items():

        x2, y2 = coordinates[neighbour]

        # Avoid drawing the same road twice
        edge = tuple(sorted([node, neighbour]))

        if edge in drawn_edges:
            continue

        drawn_edges.add(edge)

        # Draw road
        plt.plot(
            [x1, x2],
            [y1, y2],
            linewidth=1.5
        )

        # Display edge weight
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2

        plt.text(
            mid_x,
            mid_y,
            str(weight),
            fontsize=10
        )


# ---------------------------------------------------------
# Draw locations
# ---------------------------------------------------------

for node, (x, y) in coordinates.items():

    plt.scatter(
        x,
        y,
        s=500,
        zorder=3
    )

    plt.text(
        x,
        y,
        node,
        ha="center",
        va="center",
        fontsize=12,
        fontweight="bold"
    )


# ---------------------------------------------------------
# Highlight the optimal path
# ---------------------------------------------------------

path_x = [
    coordinates[node][0]
    for node in optimal_path
]

path_y = [
    coordinates[node][1]
    for node in optimal_path
]

plt.plot(
    path_x,
    path_y,
    linewidth=4,
    marker="o",
    markersize=8,
    label="Optimal Route"
)


# ---------------------------------------------------------
# Labels and title
# ---------------------------------------------------------

plt.title(
    "Route Navigation Using A* Algorithm",
    fontsize=16
)

plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")

plt.grid(True)

plt.legend()

plt.tight_layout()


# Save the map
plt.savefig(
    "results/route_map.png",
    dpi=300
)

print("\nRoute map saved successfully!")
print("Location: results/route_map.png")

