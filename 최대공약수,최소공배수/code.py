def solution(n, m):
    answer = []
    a = n
    b = m
    while b:
        a, b = b, a % b
        print(b)
    answer.append(a)
    lcm = a
    answer.append(n*m // lcm )
    return answer

