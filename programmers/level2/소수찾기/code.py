from itertools import permutations
import math

def check(n):
    k = math.sqrt(n)
    # print(k)
    if n < 2:
        return False

    for i in range(2, int(k)+1):
        if n % i ==0:
            return False
    return True

def solution(numbers):
    answer = []
    for i in range(1, len(numbers)+1):
        print()
        tmp = list(map(''.join, permutations(numbers,i)))
        for i in list(set(tmp)):
            if check(int(i)):
                answer.append(int(i))
    answer = len(set(answer))

    return answer
    



print(solution("17"))
print(solution("011"))	