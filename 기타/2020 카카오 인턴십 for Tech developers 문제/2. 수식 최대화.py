# https://velog.io/@tjdud0123/%EC%88%98%EC%8B%9D-%EC%B5%9C%EB%8C%80%ED%99%94-2020-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EC%9D%B8%ED%84%B4%EC%8B%AD-%EB%AC%B8%EC%A0%9C
from itertools import permutations
import re

def solution(expression):
    expressions = set(re.findall("\D", expression))
    prior = permutations(expressions)
    cand = []

    for op_cand in prior:
        temp = re.compile("(\D)").split('' + expression)
        for exp in op_cand:
            while exp in temp:
                idx = temp.index(exp)
                temp = temp[:idx-1] + [str(eval(''.join(temp[idx-1:idx+2])))] + temp[idx+2:]
        cand.append(abs(int(temp[0])))
    return max(cand)

print(solution("100-200*300-500+20"),60420)
print(solution("50*6-3*2"),300)