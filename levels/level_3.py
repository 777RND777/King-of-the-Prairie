from consts import *


walls = [
    Wall(map_scaling(11), map_scaling(11)),
    Wall(map_scaling(13), map_scaling(11)),
    Wall(map_scaling(15), map_scaling(11)),
    Wall(map_scaling(11), map_scaling(13)),
    Wall(map_scaling(11), map_scaling(15)),

    Wall(map_scaling(19), map_scaling(11)),
    Wall(map_scaling(21), map_scaling(11)),
    Wall(map_scaling(23), map_scaling(11)),
    Wall(map_scaling(23), map_scaling(13)),
    Wall(map_scaling(23), map_scaling(15)),

    Wall(map_scaling(11), map_scaling(19)),
    Wall(map_scaling(11), map_scaling(21)),
    Wall(map_scaling(11), map_scaling(23)),
    Wall(map_scaling(13), map_scaling(23)),
    Wall(map_scaling(15), map_scaling(23)),

    Wall(map_scaling(23), map_scaling(19)),
    Wall(map_scaling(23), map_scaling(21)),
    Wall(map_scaling(19), map_scaling(23)),
    Wall(map_scaling(21), map_scaling(23)),
    Wall(map_scaling(23), map_scaling(23)),
]
