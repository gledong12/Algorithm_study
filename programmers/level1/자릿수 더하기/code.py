def solution(N):
    answer = 0
    for i in str(N):
        answer += int(i)
    return answer


print(solution(987))