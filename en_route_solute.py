def solution(s):
    right_direction_counter = 0
    salutes = 0
    
    for i in range(len(s)):
        if s[i] == '-':
            pass
        elif s[i] == '>':
            right_direction_counter += 1
        elif s[i] == '<':
            salutes += right_direction_counter
    
    salutes *= 2

    return salutes

print(solution('--->-><-><-->-'))
print(solution('>----<'))
print(solution('<<>><'))