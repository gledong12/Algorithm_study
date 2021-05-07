# stack을 사용해서 문제풀이

def isvalid(s):
    stack = []
    table = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

    # 스택 이용 예외 처리 및 일치 여부 판별
    for i in s:
        if i not in table:
            stack.append(i)
        elif not stack or table[i] != stack.pop():
            return False
    return len(stack) ==0
