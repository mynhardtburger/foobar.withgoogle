def solution(x, y):
    # https://en.wikipedia.org/wiki/Triangular_number
    # Sum of sequence = number of items * (value of fist item + value of last item) / 2

    row_one_sum_of_sequence = x * (1 + x) / 2
    height_sum_of_sequence = (y - 1) * (x + (x + y - 2)) / 2
    bunny_id = int(row_one_sum_of_sequence + height_sum_of_sequence)
  
    return str(bunny_id)

print(solution(3,2))
print(solution(5,10))
