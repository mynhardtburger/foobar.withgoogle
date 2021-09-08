grid1 = [
    [0, 1, 1, 0],
    [0, 0, 0, 1],
    [1, 1, 0, 0],
    [1, 1, 1, 0]
]

grid2 = [
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0]
]

grid3 = [
    [0,0],
    [1,0]
]

grid4 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]

grid5 = [
    [0,0,1],
    [0,1,1],
    [1,1,0],
]

def solution(map):
    map_rows = len(map)
    map_columns = len(map[0])
    move_counter = 0
    total_walls_available = 1

    queue = [(0, 0, total_walls_available)] # row, column, breakable walls remaining
    explored = set()
    
    explored.add((0, 0, total_walls_available)) # row, column, breakable walls remaining

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # up, down, left, right

    while queue:
        move_counter += 1

        for i in range(len(queue)):
            row, column, walls_available = queue.pop(0)
            #print("movecount:", move_counter, "cell:", f"({row},{column},{walls_available})", " queue:", queue, " explored:", explored)

            if row == (map_rows - 1) and column == (map_columns - 1):
                return move_counter
            
            for d in directions:
                new_row = row + d[0]
                new_column = column + d[1]

                if 0 <= new_row < map_rows and 0 <= new_column < map_columns:
                    if walls_available > 0 and map[new_row][new_column] == 1 and (new_row, new_column, walls_available - 1) not in explored:
                        queue.append((new_row, new_column, walls_available - 1))
                        explored.add((new_row, new_column, walls_available - 1))
                    elif map[new_row][new_column] == 0 and (new_row, new_column, walls_available) not in explored:
                        queue.append((new_row, new_column, walls_available))
                        explored.add((new_row, new_column, walls_available))


print(solution(grid1)) # Output: 7
print(solution(grid2)) # Output: 11
print(solution(grid3)) # Output: 3
print(solution(grid4)) # Output: -1
print(solution(grid5)) # Output: -1
