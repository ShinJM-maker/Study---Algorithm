from collections import defaultdict
def solution(genres, plays):
    answer = []
    genreses = list(set(genres))
    #print(genreses)
    genres_dict = defaultdict(list)
    genres_dict_sum = defaultdict(int)
    #genres_dict[]
    plays2=plays.copy()
    plays2.sort(reverse=True)
    #print(plays)
    #print(plays2)
    visited = []
    for i in range(len(plays2)):
        index = plays.index(plays2[i])
        #plays.remove(plays2[i])
        #print(index)
        if (plays2[i],index) in visited:
            index = plays[index+1:].index(plays2[i])+(index+1)
        #if plays.count(plays2[i]) >1:
        #    index_list = [j for j, value in enumerate(plays2) if value == plays2[i]]
        #    print(plays2[i])
        genres_dict[genres[index]].append((plays2[i],index))
        #genres_dict[genres[index]].append(index)
        genres_dict_sum[genres[index]]+=plays2[i]
        visited.append((plays2[i],index))
    #for g in genenres:
        
    #print(plays)
    #print(genres_dict)
    #genres_dict_sum = list(genres_dict_sum)
    
    
    sorted_dict = sorted(genres_dict_sum.items(), key = lambda item: item[1], reverse = True)
    #print(genres_dict_sum) #.sort(reverse=False))
    #print(sorted_dict[0][0])
    for i in range(len(genreses)):
        key = sorted_dict[i][0]
        if len(genres_dict[key])>1:
            answer.append(genres_dict[key][0][1])
            answer.append(genres_dict[key][1][1])
        elif len(genres_dict[key])==1:
            answer.append(genres_dict[key][0][1])
            #answer.append(genres_dict[key][1])
    #print(sorted_dict)
    #print(answer)
    return answer
   
