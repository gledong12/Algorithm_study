def solution(n):
    answer=''
    
    for i in range(1, n+1):
        if i % 2 == 0:
            print(i)
            answer +='박'
        else:
            answer += '수'
    
    return answer

print(solution(4))