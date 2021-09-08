def solution_old(x, y):
    mach = int(x)
    facula = int(y)
    generation = 0

    while mach > 0 and facula > 0:
        generation +=1
        if mach > facula:
            mach -= facula
        else:
            facula -= mach
        
        if mach == 1 and facula == 1:
            return str(generation)

    return "impossible"

def solution(x, y):
    mach = int(x)
    facula = int(y)
    generation = 0

    while mach != facula:
        if mach > facula:
            repeats = (mach - facula) // facula + ((mach - facula) % facula > 0)
            mach -= facula * repeats
            generation += repeats
        else:
            repeats = (facula - mach) // mach  + ((facula - mach) % mach  > 0)
            generation += repeats
            facula -= mach * repeats
        
        if mach == 1 and facula == 1:
            return str(generation)

    return "impossible"
    
    
print(solution('2', '1')) # 1
print(solution('4', '7')) # 4
print(solution('2', '4')) # impossible
print(solution('200', '400')) # impossible
print(solution('22973719', '54715817')) # 42
print(solution('11', '2')) # 6
