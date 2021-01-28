
import types
"""
    Stack의 사용법 1번
"""
def solution(s:str)->bool:

    stack=[]
    table={
        ')':'(',
        ']':'[',
        '}':'{'
    }
    for char in s:
        if char not in table:
            stack.append(char)
        elif table[char]!=stack.pop():
            return False
    return len(stack)==0


if __name__ == '__main__':
    s='()[]{}'
    print(solution(s))