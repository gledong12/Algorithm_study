def solution(n):
    num_list = ['1','2','4']
    if n <= 3:
        return num_list[n-1]
    else:
        q, r = divmod(n-1, 3)
        return solution(q)+num_list[r]
    
    

print(solution(10))