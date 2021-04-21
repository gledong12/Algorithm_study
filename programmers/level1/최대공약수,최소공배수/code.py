def solution(n, m):
    # 최대공약수
    answer = []
    a = n
    b = m
    while b:
        a, b = b, a % b
        print(b)
    answer.append(a)
    lcm = a
    
    # 최소공배수
    answer.append(n*m // lcm )
    return answer

