import math

def solution(dimensions, your_position, trainer_position, distance):
    shots_detailed = []
    shot_directions = set()
    own_shot_directions = {}

    # Perimeter loop:
    # Evaluate from top left to bottom right.
    # If in the first or last row, then evaluate all columns, else only first and last column
    loop_reachable_shots = 1
    loop_counter = 0
    while loop_reachable_shots:
        loop_reachable_shots = 0
        for loop_x in range(-loop_counter, loop_counter + 1):
            for loop_y in range(-loop_counter, loop_counter + 1):
                if (loop_x not in [-loop_counter, loop_counter] and
                        loop_y not in [-loop_counter, loop_counter]):
                    pass
                else:
                    # Determine vector which will hit yourself
                    own_target = mirror_coordinates(dimensions, your_position, [loop_x, loop_y])
                    own_shot_result = evaluate_shot(your_position, own_target, distance)

                    if (own_shot_result["reachable"] and
                            own_shot_result["distance"] > 0 and
                            own_shot_result["simplified vector"] not in own_shot_directions):
                        own_shot_directions[own_shot_result["simplified vector"]] = own_shot_result["distance"]

                    # Determine vector which will hit target
                    target = mirror_coordinates(dimensions, trainer_position, [loop_x, loop_y])
                    shot_result = evaluate_shot(your_position, target, distance)

                    # Test if beam will hit yourself before the target
                    if (shot_result["simplified vector"] in own_shot_directions and
                            own_shot_directions[shot_result["simplified vector"]] <= shot_result["distance"]):
                        continue

                    if (shot_result["reachable"] and
                            shot_result["simplified vector"] not in shot_directions):
                        shot_directions.add(shot_result["simplified vector"])
                        shots_detailed.append(shot_result)
                        loop_reachable_shots += 1
        loop_counter += 1
    return len(shot_directions)

def mirror_coordinates(dimensions, position, direction):
    dimensions_x, dimensions_y = dimensions[0], dimensions[1]
    starting_x, starting_y = position[0], position[1]
    direction_x, direction_y = direction[0], direction[1]

    inverted_x = dimensions_x - starting_x
    inverted_y = dimensions_y - starting_y

    if direction_x == 0:
        ending_x = starting_x
    elif direction_x % 2 == 0:
        ending_x = dimensions_x * direction_x + starting_x
    elif direction_x % 2 != 0:
        ending_x = dimensions_x * direction_x + inverted_x

    if direction_y == 0:
        ending_y = starting_y
    elif direction_y % 2 == 0:
        ending_y = dimensions_y * direction_y + starting_y
    elif direction_y % 2 != 0:
        ending_y = dimensions_y * direction_y + inverted_y

    return [ending_x, ending_y]

def evaluate_shot(your_position, target_position, shot_distance):
    px, py = float(your_position[0]), float(your_position[1])
    tx, ty = float(target_position[0]), float(target_position[1])

    direction_vector = (tx - px, ty - py)
    target_distance = math.hypot(*direction_vector)
    reachable = target_distance <= shot_distance

    simplified_vector = math.atan2(*direction_vector)

    shot_result = {
        "target position": target_position,
        "vector": direction_vector,
        "simplified vector": simplified_vector,
        "distance": target_distance,
        "reachable": reachable
    }

    return shot_result

# def evaluate_corner_shot(dimensions, target):
#     dx, dy = dimensions[0], dimensions[1]
#     tx, ty = target[0], target[1]

#     return tx % dx == 0 and ty % dy == 0

print(solution([3, 2], [1, 1], [2, 1], 4))
print(solution([300, 275], [150, 150], [185, 100], 500))
print(solution([2, 5], [1, 2], [1, 4], 11))
