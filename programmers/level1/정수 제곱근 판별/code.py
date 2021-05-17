def solution(n):
    char = n**(1/2)
    if int(char) == char:
        return (char+1)**2
    else:
        return -1




print(solution(121))
print(solution(225))
print(solution(33))