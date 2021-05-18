def solution(n):
    answer=set(range(2, n+1))
    print(answer)
    
    for i in range(2, n+1):
        if i in answer:
            print('i',i,'1111',set(range(2*i, n+1, i)))
            answer -= set(range(2*i, n+1, i))
    return len(answer)
    



print(solution(10))
