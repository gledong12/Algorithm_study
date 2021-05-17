def solution(s):
    answer = ""
    s_list = s.split(" ")
    answer_list = []
    
    for str in s_list:
        for n, i in enumerate(str):
            if n % 2 == 0 or n == 0:
                answer += i.upper()
            else:
                answer += i.lower()
        answer_list.append(answer)
        answer =" "
    return "".join(answer_list)
    
s="try hello world"
print(solution(s))