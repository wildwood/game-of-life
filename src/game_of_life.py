from collections import Counter

class GridTick:
    def __init__(self, width, height, live_cell_coordinates):
        self.live_cells = frozenset(live_cell_coordinates)
        self.width = width
        self.height = height
        self.grid = tuple(tuple((x,y) in self.live_cells for y in range(self.height)) for x in range(self.width))
        # TODO - needs more validation - (what if there are no live cells? cells out of bounds?)

    # TODO - how much work to allow an infinite board?
        
    # TODO - would be nice to have a smaller presentation mode that removes empty space    
    # get the grid for this tick, trimmed of all empty outside rows and columns
    def trim(self):
        first_column = min([i[0] for i in self.live_cells])
        last_column = max([i[0] for i in self.live_cells]) + 1
        first_row = min([i[1] for i in self.live_cells])
        last_row = min([i[1] for i in self.live_cells]) + 1

        return tuple(tuple((x,y) in self.live_cells for y in range(first_row, last_row)) for x in range(first_column, last_column))

    # enumerate all the neighbors for a given point
    def neighbors(self, point):
        return [(point[0]-1,point[1]-1),
                (point[0]-1,point[1]),
                (point[0]-1,point[1]+1),
                (point[0],point[1]-1),
                (point[0],point[1]+1),
                (point[0]+1,point[1]-1),
                (point[0]+1,point[1]),
                (point[0]+1,point[1]+1)]

    # make sure that the point is in the grid's bounds
    def in_bounds(self, point):
        return point[0] >= 0 and point[0] < self.width and point[1] >= 0 and point[1] < self.height
    
    def bounded_neighbors(self, point):
        return [item for item in self.neighbors(point) if self.in_bounds(item)]
    
    # calculate the next tick, based on this one, and return a new GridTick object with that next tick
    def tick(self):
        live_neighbor_lists = [self.bounded_neighbors(x) for x in self.live_cells]
        live_neighbor_counts = Counter([item for sublist in live_neighbor_lists for item in sublist])
        still_alive_neighbors = [x for x in live_neighbor_counts.keys() if x in self.live_cells and live_neighbor_counts[x] > 1 and live_neighbor_counts[x] < 4]
        newly_alive_neighbors = [x for x in live_neighbor_counts.keys() if x not in self.live_cells and live_neighbor_counts[x] == 3]
        return GridTick(self.width, self.height, still_alive_neighbors + newly_alive_neighbors)

    def print(self):
        output = ''
        for row in range(self.height):
            for column in range(self.width):
                if (column, row) in self.live_cells:
                    output = output + '*'
                else:
                    output = output + '.'
            output = output + '\n'
        print(output)
        
def main():
    grid = GridTick(25, 25, [(12,11), (13,12), (11,13), (12,13), (13,13)])
    grid.print()
    for i in range(1,5):
        grid = grid.tick()
        print('\n\n\nIteration ')
        print(i)
        print(':')
        grid.print()


if __name__ == '__main__':
    main()
