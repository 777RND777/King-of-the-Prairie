from consts import *


walls = [
    Wall(map_scaling(9), map_scaling(9)),
    Wall(map_scaling(11), map_scaling(9)),
    Wall(map_scaling(9), map_scaling(11)),

    Wall(map_scaling(23), map_scaling(9)),
    Wall(map_scaling(25), map_scaling(9)),
    Wall(map_scaling(25), map_scaling(11)),

    Wall(map_scaling(9), map_scaling(23)),
    Wall(map_scaling(9), map_scaling(25)),
    Wall(map_scaling(11), map_scaling(25)),

    Wall(map_scaling(25), map_scaling(23)),
    Wall(map_scaling(23), map_scaling(25)),
    Wall(map_scaling(25), map_scaling(25)),
]
