
default_map = [
    [6, 7, 5, 5, 3, 6, 7, 3],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
]


class Node:

    def __init__(self, coordinate, combination):
        #(x, y)
        self.coordinate = coordinate
        self.combination = combination

    def get_paths(self):
        # Top - Right - Bottom - Left
        match self.combination:
            case 1:
                comb = [0, 0, 0, 1]
            case 2:
                comb = [0, 0, 1, 0]
            case 3:
                comb = [0, 0, 1, 1]
            case 4:
                comb = [0, 1, 0, 0]
            case 5:
                comb = [0, 1, 0, 1]
            case 6:
                comb = [0, 1, 1, 0]
            case 7:
                comb = [0, 1, 1, 1]
            case 8:
                comb = [1, 0, 0, 0]
            case 9:
                comb = [1, 0, 0, 1]
            case 10:
                comb = [1, 0, 1, 0]
            case 11:
                comb = [1, 0, 1, 1]
            case 12:
                comb = [1, 1, 0, 0]
            case 13:
                comb = [1, 1, 0, 1]
            case 14:
                comb = [1, 1, 1, 0]
            case 15:
                comb = [1, 1, 1, 1]
            case _:
                comb = [0, 0, 0, 0]
        return comb


class Map:

    def __init__(self):
        self.game_map = []

    def generate_map(self, map_data):
        data = []
        _y = 0
        for row in map_data:
            data.append([])
            _x = 0
            for _ in row:
                coordinate = [_x, _y]
                combination = map_data[_y][_x]
                data[_y].append(Node(coordinate, combination))
                _x += 1
            _y += 1

        self.game_map = data

    def get_node_at(self, coordinate):
        try:
            return self.game_map[coordinate[1]][coordinate[0]]
        except IndexError:
            return None


if __name__ == "__main__":
    test = Map()
    test.generate_map(default_map)

    for y in test.game_map:
        for x in y:
            print(x.get_paths())

    print(test.get_node_at([0, 2]))
    print(test.get_node_at([9, 2]))
