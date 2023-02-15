import collections
def solution(participant, completion):
    answer = ''
    #all_list = sum(participant)
    #print(collections.Counter(participant))
    answer = collections.Counter(participant) - collections.Counter(completion)
    #print(list(answer.keys())[0])
    answer = list(answer.keys())[0]
    #answer = answer[answer.keys()[0]]
    """
    for i in range(len(participant)):
        if participant[i] not in completion: #and not participant.count(participant[i]) > 1:
            return participant[i]
        else:
            if participant.count(participant[i]) != completion.count(participant[i]):
                return participant[i]
                """
    
    return answer
