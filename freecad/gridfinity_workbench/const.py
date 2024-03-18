#Gridfinity Standard Dimensions are placed here, changing theses values will alter the dimensions of the bins and baseplates generated which may result in non compatable bins. Alternativly you can make a custom grid size to your liking.

GRID_SIZE = 42
HEIGHT_UNIT = 7

BIN_BASE_BOTTOM_CHAMFER = 0.8
BIN_BASE_VERTICAL_SECTION = 1.8
BIN_BASE_TOP_CHAMFER = 2.15

BIN_OUTER_RADIUS = 3.75
BIN_BASE_VERTICAL_RADIUS = 1.6
BIN_BASE_BOTTOM_RADIUS = 0.8

BASEPLATE_BOTTOM_CHAMFER = 0.7
BASEPLATE_VERTICAL_SECTION = 1.8
BASEPLATE_TOP_CHAMFER = 1.75
BASEPLATE_TOP_LEDGE_WIDTH = 0.4

BASEPLATE_OUTER_RADIUS = 4.0
BASEPLATE_VERTICAL_RADIUS = 1.85
BASEPLATE_BOTTOM_RADIUS = 1.15

TOLERANCE = 0.25

BIN_UNIT = GRID_SIZE - TOLERANCE*2

MAGNET_HOLE_DIAMETER = 6.5
MAGNET_HOLE_DEPTH = 2.4

SCREW_HOLE_DIAMETER = 3
SCREW_HOLE_DEPTH = 6

MAGNET_HOLE_DISTANCE_FROM_EDGE = 8

#Starting values that are used to create the initial shape and can be edited by the Gridfinity Properties.