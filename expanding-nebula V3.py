from timeit import default_timer as timer
start = timer()

from collections import defaultdict

prestates_4 = {
    1: (
        ((1, 0), (0, 0)),
        ((0, 1), (0, 0)),
        ((0, 0), (1, 0)),
        ((0, 0), (0, 1))
    ),
    0: (
        ((0, 0), (0, 0)),
        ((1, 1), (0, 0)),
        ((1, 0), (1, 0)),
        ((1, 0), (0, 1)),
        ((0, 1), (1, 0)),
        ((0, 1), (0, 1)),
        ((0, 0), (1, 1)),
        ((0, 1), (1, 1)),
        ((1, 0), (1, 1)),
        ((1, 1), (0, 1)),
        ((1, 1), (1, 0)),
        ((1, 1), (1, 1))
    )
}

true_prestates = {
    (0, 0): ((1, 0), (0, 1)),
    (1, 0): ((0, 0),),
    (0, 1): ((0, 0),),
}

false_prestates = {
    (0, 0): ((0, 0), (1, 1)),
    (0, 1): ((1, 0), (0, 1), (1, 1)),
    (1, 0): ((1, 0), (0, 1), (1, 1)),
    (1, 1): ((0, 0), (1, 0), (0, 1), (1, 1))
}

def solution(g):
    """Return a possible previous nebula state."""

    optimized_g = tuple(zip(*g)) # Limit input to shortest row/column to prevent breaking on malformed input.

    prev_column_count = defaultdict(int)

    for possible_column in shared_possible_columns(optimized_g[0]):
        prev_column_count[possible_column[1]] += 1

    for column in xrange(1, len(optimized_g)):
        next_column_count = defaultdict(int)
        for possible_column in shared_possible_columns(optimized_g[column]):
            if possible_column[0] in prev_column_count:
                next_column_count[possible_column[1]] = prev_column_count[possible_column[0]] + (next_column_count[possible_column[1]] if possible_column[1] in next_column_count else 0)

        prev_column_count = next_column_count

    return sum(prev_column_count.values())

def shared_possible_columns(column):
    next_row = list()

    prev_row = prestates_4[column[0]]

    # Subsequent rows
    for row in xrange(1, len(column)):
        possible_prestates = true_prestates if column[row] else false_prestates

        for prev_row_item in prev_row:
            for prestate_key in possible_prestates:
                if prev_row_item[-1] == prestate_key:
                    for value in possible_prestates[prestate_key]:
                        next_row.append(prev_row_item + (value,))

        prev_row = next_row
        next_row = list()

    # Rotate row tuples into columns
    prev_columns = tuple([zip(*i) for i in prev_row])

    return prev_columns

# print(solution([[1, 1], [1, 1]]))
# print(solution([[1, 1], [1]]))
# print(solution([[1, 1]]))
# print(solution([[1, 1, 1], [1, 1, 1]]))
print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))
# print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))
# print(solution([[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]))
# print(solution([[1,1,1,1,1], [1,1,1,1,1], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]))
# print(solution([[True, True, False, True, False, True, False, True, True, False], [True, True, False, False, False, False, True, True, True, False], [True, True, False, False, False, False, False, False, False, True], [False, True, False, False, False, False, True, True, False, False]]))
# print(solution([[True, False, True], [False, True, False], [True, False, True]]))
# print(solution([[True, False, True, False, False, True, True, True], [True, False, True, False, False, False, True, False], [True, True, True, False, False, False, True, False], [True, False, True, False, False, False, True, False], [True, False, True, False, False, True, True, True]]))

end = timer()
print(end - start)
