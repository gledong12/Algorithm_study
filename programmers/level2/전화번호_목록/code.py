def solution(phone_book):    
    for i in phone_book:
        num_data = i
        phone_book.remove(i)
        while True:
            for j in phone_book:
                if num_data[0] in j:
                    return False
    return True




# 런타임 에러 발생, 몇 개의 다른 테스트 케이스에서 제대로 발생하지 않았다.
