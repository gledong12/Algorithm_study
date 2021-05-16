def solution(n):
    answer=set(range(2, n+1))
    print(answer)
    
    for i in range(2, n+1):
        if i in answer:
            print('i',i,'1111',set(range(2*i, n+1, i)))
            answer -= set(range(2*i, n+1, i))
    return len(answer)
    
    count = 0
    for num in n:
        for i in num:
            if num % i == 0:
                break
            count += 1
    return count
                



print(solution(10))
