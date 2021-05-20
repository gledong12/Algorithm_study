import collections

# 내 코드
# def solution(progresss ,speeds):
#     answer = []
        
#     answer_list = [0] * len(progresss)
#     print(answer_list)
    
#     for i in range(len(progresss)):
#         during_days = (100-progresss[i]) // speeds[i]
        
#         if (100-progresss[i]) % speeds[i]:
#             during_days += 1
        
#         answer_list.append(during_days)
        
#     k = 1
#     for j in range(len(answer_list)):
#         while answer_list[j] >= answer_list[j+1]:
#             k += 1
#             answer_list.pop(answer_list[j+1])  
#         answer.append(k)
#     return answer


def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    
    while len(progresses) > 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer
            
    

print(solution([93, 30, 55],[1, 30, 5]))   