# Problem 3 : Tiles required to covering floor of room 144 sq.m.

floor_area = 144              # floor area in sq.m
tile_size = 12 * 12           # tile size in sq.cm

floor = 144 * 10000           # 1 sq.m into 10000 sq.cm

tiles_required = floor/tile_size
print(tiles_required,"tiles are required to covering flooring of room.")