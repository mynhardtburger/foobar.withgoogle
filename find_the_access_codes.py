def solution(l):
    triples_count = 0
    pairs = [0] * len(l)

    for i in range(len(l) - 2):
        for j in range(i + 1, len(l) - 1):
            if l[j] % l[i] == 0:
                pairs[j] += 1

    for j in range(1, len(l) - 1):
        for k in range(j + 1, len(l)):
            if l[k] % l[j] == 0:
                triples_count += pairs[j]

    return triples_count

print(solution([1,1,1]) == 1)
print(solution([1,2,3,4,5,6]) == 3)
print(solution([1,2,4,8]) == 4)
print(solution([1,2,4,6,12]) == 7)
print(solution([1,2]) == 0)
print(solution([2,3,7,11]) == 0)
print(solution([1,1,1,1]) == 4)
