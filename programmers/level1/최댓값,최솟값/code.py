def solution(s):
    num_list2 = list(map(int, s.split(' ')))
    max_num = max(num_list2)
    min_num = min(num_list2)

    return str(min_num) + " " + str(max_num)
