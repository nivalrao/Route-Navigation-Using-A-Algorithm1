# Coordinates of each location
coordinates = {
    "A": (0, 0),
    "B": (2, 3),
    "C": (4, 1),
    "D": (5, 4),
    "E": (7, 2),
    "F": (9, 5),
    "G": (6, 7),
    "H": (10, 8)
}


# Weighted map
# Edge weights represent travel distance/cost.
# Each weight is greater than or equal to the
# straight-line distance between the connected locations.

graph = {
    "A": {
        "B": 4.0,
        "C": 4.5
    },

    "B": {
        "A": 4.0,
        "C": 3.0,
        "D": 3.5
    },

    "C": {
        "A": 4.5,
        "B": 3.0,
        "D": 3.5,
        "E": 3.5
    },

    "D": {
        "B": 3.5,
        "C": 3.5,
        "E": 3.0,
        "G": 3.5
    },

    "E": {
        "C": 3.5,
        "D": 3.0,
        "F": 4.0,
        "H": 7.0
    },

    "F": {
        "E": 4.0,
        "G": 4.0,
        "H": 3.5
    },

    "G": {
        "D": 3.5,
        "F": 4.0,
        "H": 4.5
    },

    "H": {
        "E": 7.0,
        "F": 3.5,
        "G": 4.5
    }
}