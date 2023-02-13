from collections import deque

def pair_compare(target,word):
    count = 0
    target = list(target)
    word = list(word)
    word2 = list(word)
    for i in range(len(target)):
        if target[i] == word[i]:
            word2.remove(word[i])
    if len(word2) == 1:
        print(target,word)
        return True
    else:
        return False
    

def solution(begin, target, words):
    answer = 0
    Q = deque()
    Q.append((begin,answer))
    word = begin
    if target not in words:
        answer = 0
        return answer
    else:
        while Q:
            Q.popleft()
            for w in words:
                if pair_compare(target,word):
                    answer+=1
                    return answer
                if pair_compare(w,word):
                    word = w
                    answer+=1
                    Q.append((word,answer))   
    
    return answer
