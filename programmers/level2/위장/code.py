# 내가 푼 풀이 -> 테스트 케이스는 만족 시켰지만, 제출하기를 누르면 난리가 났다
from itertools import product

def solution(clothes):
    # clothe_dict = {}
    # for clothe in clothes:
    #     if clothe[1] not in clothe_dict:
    #         clothe_dict[clothe[1]] = [clothe[0]]
    #     else:
    #         clothe_dict[clothe[1]].append(clothe[0])
    
    # clothe_values = list(clothe_dict.values())
    
    # if len(clothe_values) == 1:
    #     return len(clothes)
    # else:
    #     return len(list(product(*clothe_values))) + len(clothes)
    
    # 가상 해시 함수를 잘 사용해서 푼 문제
    clothes_type = {}
    
    for c, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2
        else:
            clothes_type[t] += 1
    
    print(clothes_type)  
    cnt =1
    for num in clothes_type.values():
        cnt *= num
    
    return cnt -1
            
