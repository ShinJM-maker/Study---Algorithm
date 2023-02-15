def solution(nums):
    answer = 0
    
    poket_dict = dict()
    N = int(len(nums)/2)
    for i in nums:
        poket_dict[str(i)] = nums.count(i)
    key_list = poket_dict.keys() 
    choose_list = []
    visited = []
    if len(key_list) > N:
        return N
    elif len(key_list) <= N:
        return len(key_list)
    return answer
