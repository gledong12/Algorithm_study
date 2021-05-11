def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for com, k in zip(participant, completion):
        if com != k:
            return com 
    return participant[-1]

